# Parallel Python API library

[![PyPI version](https://img.shields.io/pypi/v/parallel-web.svg)](https://pypi.org/project/parallel-web/)

The Parallel Python library provides convenient access to the Parallel REST API from any Python 3.8+
application. The library includes type definitions for all request params and response fields,
and offers both synchronous and asynchronous clients powered by [httpx](https://github.com/encode/httpx).
It is strongly encouraged to use the asynchronous client for best performance.

It is generated with [Stainless](https://www.stainless.com/).

## Documentation

The REST API documentation can be found on our [docs](https://docs.parallel.ai).
The full API of this Python library can be found in [api.md](api.md).

## Installation

```sh
# install from PyPI
pip install parallel-web
```

## Usage

The full API of this library can be found in [api.md](api.md).

```python
import os
from parallel import Parallel

client = Parallel(
    api_key=os.environ.get("PARALLEL_API_KEY"),  # This is the default and can be omitted
)

run_result = client.task_run.execute(
    input="France (2023)",
    processor="core",
    output="GDP"
)
print(run_result.output)
```

While you can provide an `api_key` keyword argument,
we recommend using [python-dotenv](https://pypi.org/project/python-dotenv/)
to add `PARALLEL_API_KEY="My API Key"` to your `.env` file
so that your API Key is not stored in source control.

## Async usage

Simply import `AsyncParallel` instead of `Parallel` and use `await` with each API call:

```python
import os
import asyncio
from parallel import AsyncParallel

client = AsyncParallel(
    api_key=os.environ.get("PARALLEL_API_KEY"),  # This is the default and can be omitted
)


async def main() -> None:
    run_result = await client.task_run.execute(
        input="France (2023)",
        processor="core",
        output="GDP"
    )
    print(run_result.output)


if __name__ == "__main__":
    asyncio.run(main())
```

To get the best performance out of Parallel's API, we recommend
using the asynchronous client, especially for executing multiple Task Runs concurrently.
Functionality between the synchronous and asynchronous clients is identical.

## Convenience methods

### Execute

The `execute` method provides a single call which combines creating a task run,
polling until it is completed, and parsing structured outputs (if specified).

If an output type which inherits from `BaseModel` is
specified in the call to `.execute()`, the response content will be parsed into an
instance of the provided output type. The parsed output can be accessed via the
`parsed` property on the output field of the response.

```python
import os
import asyncio
from parallel import AsyncParallel
from pydantic import BaseModel

client = AsyncParallel()

class SampleOutputStructure(BaseModel):
    output: str

async def main() -> None:
    # with pydantic
    run_result = await client.task_run.execute(
        input="France (2023)",
        processor="core",
        output=SampleOutputStructure,
    )
    # parsed output of type SampleOutputStructure
    print(run_result.output.parsed)
    # without pydantic
    run_result = await client.task_run.execute(
        input="France (2023)",
        processor="core",
        output="GDP"
    )
    print(run_result.output)


if __name__ == "__main__":
    asyncio.run(main())
```

The async client allows creating several task runs without blocking.
To create multiple task runs in one go, call execute and then gather the results at the end.

```python
import asyncio
import os

from parallel import AsyncParallel
from pydantic import BaseModel, Field
from typing import List

class CountryInput(BaseModel):
    country: str = Field(
        description="Name of the country to research. Must be a recognized "
        "sovereign nation (e.g., 'France', 'Japan')."
    )
    year: int = Field(
        description="Year for which to retrieve data. Must be 2000 or later. "
                    "Use most recent full-year estimates if year is current."
    )

class CountryOutput(BaseModel):
    gdp: str = Field(
        description="GDP in USD for the year, formatted like '$3.1 trillion (2023)'."
    )
    top_exports: List[str] = Field(
        description="Top 3 exported goods/services by value. Use credible sources."
    )
    top_imports: List[str] = Field(
        description="Top 3 imported goods/services by value. Use credible sources."
    )

async def main():
    # Initialize the Parallel client
    client = AsyncParallel(api_key=os.environ.get("PARALLEL_API_KEY"))

    # Prepare structured input
    input_data = [
        CountryInput(country="France", year=2023),
        CountryInput(country="Germany", year=2023),
        CountryInput(country="Italy", year=2023)
    ]

    run_results = await asyncio.gather(*[
        client.task_run.execute(
            input=datum,
            output=CountryOutput,
            processor="core"
        )
        for datum in input_data
    ])

    for run_input, run_result in zip(input_data, run_results):
        print(f"Task run output for {run_input}: {run_result.output.parsed}")

if __name__ == "__main__":
    asyncio.run(main())
```

## Low level API Access

The library also provides access to the low level API for accessing the Parallel API.

```python
from parallel import Parallel
from parallel.types import TaskSpecParam

client = Parallel()

task_run = client.task_run.create(
    input="France (2023)",
    processor="processor",
    task_spec={
        "output_schema": {
            "json_schema": {
                "additionalProperties": False,
                "properties": {
                    "gdp": {
                        "description": "GDP in USD for the year, formatted like '$3.1 trillion (2023)'",
                        "type": "string",
                    }
                },
                "required": ["gdp"],
                "type": "object",
            },
            "type": "json",
        },
        "input_schema": {
            "json_schema": {
                "additionalProperties": False,
                "properties": {
                    "gdp": {
                        "description": "GDP in USD for the year, formatted like '$3.1 trillion (2023)'",
                        "type": "string",
                    }
                },
                "required": ["gdp"],
                "type": "object",
            },
            "type": "json",
        },
    },
)

run_result = client.task_run.result(task_run.id)
print(run_result.output)
```

For more information, please check out the relevant section in our docs:

- [Task Spec](https://docs.parallel.ai/core-concepts/task-spec)
- [Task Runs](https://docs.parallel.ai/core-concepts/task-runs)

## Handling errors

When the library is unable to connect to the API (for example, due to network connection problems or a timeout), a subclass of `parallel.APIConnectionError` is raised.

When the API returns a non-success status code (that is, 4xx or 5xx
response), a subclass of `parallel.APIStatusError` is raised, containing `status_code` and `response` properties.

All errors inherit from `parallel.APIError`.

```python
import parallel
from parallel import Parallel

client = Parallel()

try:
    client.task_run.execute(
        input="France (2023)",
        processor="core",
        output="GDP"
    )
except parallel.APIConnectionError as e:
    print("The server could not be reached")
    print(e.__cause__)  # an underlying Exception, likely raised within httpx.
except parallel.RateLimitError as e:
    print("A 429 status code was received; we should back off a bit.")
except parallel.APIStatusError as e:
    print("Another non-200-range status code was received")
    print(e.status_code)
    print(e.response)
```

Error codes are as follows:

| Status Code | Error Type                 |
| ----------- | -------------------------- |
| 400         | `BadRequestError`          |
| 401         | `AuthenticationError`      |
| 403         | `PermissionDeniedError`    |
| 404         | `NotFoundError`            |
| 422         | `UnprocessableEntityError` |
| 429         | `RateLimitError`           |
| >=500       | `InternalServerError`      |
| N/A         | `APIConnectionError`       |

### Retries

Certain errors are automatically retried 2 times by default, with a short exponential backoff.
Connection errors (for example, due to a network connectivity problem), 408 Request Timeout, 409 Conflict,
429 Rate Limit, and >=500 Internal errors are all retried by default.

You can use the `max_retries` option to configure or disable retry settings:

```python
from parallel import Parallel

# Configure the default for all requests:
client = Parallel(
    # default is 2
    max_retries=0,
)

# Or, configure per-request:
client.with_options(max_retries=5).task_run.execute(
    input="France (2023)",
    processor="core",
    output="GDP"
)
```

### Timeouts

By default requests time out after 1 minute. You can configure this with a `timeout` option,
which accepts a float or an [`httpx.Timeout`](https://www.python-httpx.org/advanced/#fine-tuning-the-configuration) object:

```python
from parallel import Parallel

# Configure the default for all requests:
client = Parallel(
    # 20 seconds (default is 1 minute)
    timeout=20.0,
)

# More granular control:
client = Parallel(
    timeout=httpx.Timeout(60.0, read=5.0, write=10.0, connect=2.0),
)

# Override per-request:
client.with_options(timeout=5.0).task_run.execute(
    input="France (2023)",
    processor="core",
    output="GDP"
)
```

On timeout, an `APITimeoutError` is thrown.

Note that requests that time out are [retried twice by default](#retries).

## Advanced

### Logging

We use the standard library [`logging`](https://docs.python.org/3/library/logging.html) module.

You can enable logging by setting the environment variable `PARALLEL_LOG` to `info`.

```shell
$ export PARALLEL_LOG=info
```

Or to `debug` for more verbose logging.

### How to tell whether `None` means `null` or missing

In an API response, a field may be explicitly `null`, or missing entirely; in either case, its value is `None` in this library. You can differentiate the two cases with `.model_fields_set`:

```py
if response.my_field is None:
  if 'my_field' not in response.model_fields_set:
    print('Got json like {}, without a "my_field" key present at all.')
  else:
    print('Got json like {"my_field": null}.')
```

### Accessing raw response data (e.g. headers)

The "raw" Response object can be accessed by prefixing `.with_raw_response.` to any HTTP method call, e.g.,

```py
from parallel import Parallel

client = Parallel()
response = client.task_run.with_raw_response.execute(
    input="France (2023)",
    processor="core",
    output="GDP"
)
print(response.headers.get('X-My-Header'))

task_run = response.parse()  # get the object that `task_run.execute()` would have returned
print(task_run.output)
```

These methods return an [`APIResponse`](https://github.com/shapleyai/parallel-sdk-python/tree/main/src/parallel/_response.py) object.

The async client returns an [`AsyncAPIResponse`](https://github.com/shapleyai/parallel-sdk-python/tree/main/src/parallel/_response.py) with the same structure, the only difference being `await`able methods for reading the response content.

#### `.with_streaming_response`

The above interface eagerly reads the full response body when you make the request, which may not always be what you want.

To stream the response body, use `.with_streaming_response` instead, which requires a context manager and only reads the response body once you call `.read()`, `.text()`, `.json()`, `.iter_bytes()`, `.iter_text()`, `.iter_lines()` or `.parse()`. In the async client, these are async methods.

```python
with client.task_run.with_streaming_response.execute(
    input="France (2023)",
    processor="core",
    output="GDP"
) as response:
    print(response.headers.get("X-My-Header"))

    for line in response.iter_lines():
        print(line)
```

The context manager is required so that the response will reliably be closed.

### Making custom/undocumented requests

This library is typed for convenient access to the documented API.

If you need to access undocumented endpoints, params, or response properties, the library can still be used.

#### Undocumented endpoints

To make requests to undocumented endpoints, you can make requests using `client.get`, `client.post`, and other
http verbs. Options on the client will be respected (such as retries) when making this request.

```py
import httpx

response = client.post(
    "/foo",
    cast_to=httpx.Response,
    body={"my_param": True},
)

print(response.headers.get("x-foo"))
```

#### Undocumented request params

If you want to explicitly send an extra param, you can do so with the `extra_query`, `extra_body`, and `extra_headers` request
options.

#### Undocumented response properties

To access undocumented response properties, you can access the extra fields like `response.unknown_prop`. You
can also get all the extra fields on the Pydantic model as a dict with
[`response.model_extra`](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel.model_extra).

### Configuring the HTTP client

You can directly override the [httpx client](https://www.python-httpx.org/api/#client) to customize it for your use case, including:

- Support for [proxies](https://www.python-httpx.org/advanced/proxies/)
- Custom [transports](https://www.python-httpx.org/advanced/transports/)
- Additional [advanced](https://www.python-httpx.org/advanced/clients/) functionality

```python
import httpx
from parallel import Parallel, DefaultHttpxClient

client = Parallel(
    # Or use the `PARALLEL_BASE_URL` env var
    base_url="http://my.test.server.example.com:8083",
    http_client=DefaultHttpxClient(
        proxy="http://my.test.proxy.example.com",
        transport=httpx.HTTPTransport(local_address="0.0.0.0"),
    ),
)
```

You can also customize the client on a per-request basis by using `with_options()`:

```python
client.with_options(http_client=DefaultHttpxClient(...))
```

### Managing HTTP resources

By default the library closes underlying HTTP connections whenever the client is [garbage collected](https://docs.python.org/3/reference/datamodel.html#object.__del__). You can manually close the client using the `.close()` method if desired, or with a context manager that closes when exiting.

```py
from parallel import Parallel

with Parallel() as client:
  # make requests here
  ...

# HTTP client is now closed
```

## Versioning

This package generally follows [SemVer](https://semver.org/spec/v2.0.0.html) conventions, though certain backwards-incompatible changes may be released as minor versions:

1. Changes that only affect static types, without breaking runtime behavior.
2. Changes to library internals which are technically public but not intended or documented for external use. _(Please open a GitHub issue to let us know if you are relying on such internals.)_
3. Changes that we do not expect to impact the vast majority of users in practice.

We take backwards-compatibility seriously and work hard to ensure you can rely on a smooth upgrade experience.

We are keen for your feedback; please open an [issue](https://www.github.com/shapleyai/parallel-sdk-python/issues) with questions, bugs, or suggestions.

### Determining the installed version

If you've upgraded to the latest version but aren't seeing any new features you were expecting then your python environment is likely still using an older version.

You can determine the version that is being used at runtime with:

```py
import parallel
print(parallel.__version__)
```

## Requirements

Python 3.8 or higher.

## Contributing

See [the contributing documentation](./CONTRIBUTING.md).
