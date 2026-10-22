from __future__ import annotations

import time
from typing import Any, Type, Union, Callable, NoReturn, Coroutine, cast

from ...types import TaskRunResult, ParsedTaskRunResult
from ..._types import Omit
from ..._utils import is_str, is_given
from ..._compat import model_parse, model_parse_json
from ..._models import construct_type_unchecked
from .._pydantic import is_basemodel_type
from ._task_spec import is_output_schema_param
from ..._exceptions import APIStatusError, APITimeoutError
from ...types.task_spec_param import OutputT, OutputSchema


def wait_for_result(
    *,
    run_id: str,
    deadline: float,
    callable: Callable[[str, float], TaskRunResult | ParsedTaskRunResult[OutputT]],
) -> TaskRunResult | ParsedTaskRunResult[OutputT]:
    """Wait for a task run to complete within the given timeout."""
    exc: Exception | None = None
    while time.monotonic() < deadline:
        try:
            return callable(run_id, deadline)
        except APITimeoutError as error:
            exc = error
        except APIStatusError as error:
            if not _is_retryable_error(error.status_code):
                raise
            exc = error
    _raise_timeout(run_id, exc)


async def wait_for_result_async(
    *,
    run_id: str,
    deadline: float,
    callable: Callable[[str, float], Coroutine[Any, Any, TaskRunResult | ParsedTaskRunResult[OutputT]]],
) -> TaskRunResult | ParsedTaskRunResult[OutputT]:
    """Wait for a task run to complete within the given timeout."""
    exc: Exception | None = None
    while time.monotonic() < deadline:
        try:
            return await callable(run_id, deadline)
        except APITimeoutError as error:
            exc = error
        except APIStatusError as error:
            if not _is_retryable_error(error.status_code):
                raise
            exc = error
    _raise_timeout(run_id, exc)


def task_run_result_parser(
    run_result: TaskRunResult, output_format: Union[OutputSchema, Type[OutputT]] | Omit | None
) -> TaskRunResult | ParsedTaskRunResult[OutputT]:
    """Parse a TaskRunResult object into a ParsedTaskRunResult based on output_format."""
    if not is_given(output_format) or output_format is None or is_output_schema_param(output_format):
        return run_result

    if is_basemodel_type(output_format):
        return _create_parsed_task_run_result(
            task_run_result=run_result,
            response_format=output_format,
        )

    raise TypeError(f"Invalid output_format. Expected pydantic.BaseModel, found: {type(output_format)}")


def _create_parsed_task_run_result(
    *,
    response_format: Type[OutputT],
    task_run_result: TaskRunResult,
) -> ParsedTaskRunResult[OutputT]:
    """Convert a TaskRunResult object into a ParsedTaskRunResult."""
    run_result_output = task_run_result.output
    return cast(
        ParsedTaskRunResult[OutputT],
        construct_type_unchecked(
            type_=cast(Any, ParsedTaskRunResult)[response_format],
            value={
                **task_run_result.to_dict(),
                "output": {
                    **task_run_result.output.to_dict(),
                    "parsed": maybe_parse_content(
                        response_format=response_format,
                        message=run_result_output.content,
                    ),
                },
            },
        ),
    )


def maybe_parse_content(
    *,
    response_format: type[OutputT],
    message: str | object,
) -> OutputT | None:
    """Parse message content based on the response format."""
    return _parse_content(response_format, message)


def _parse_content(response_format: type[OutputT], content: str | object) -> OutputT:
    """Parse content based on the response format.

    Only pydantic basemodels are currently supported.
    """
    if is_basemodel_type(response_format):
        if is_str(content):
            return cast(OutputT, model_parse_json(response_format, content))
        else:
            return cast(OutputT, model_parse(response_format, content))

    raise TypeError(f"Unable to automatically parse response format type {response_format}")


def _raise_timeout(run_id: str, exc: Union[Exception, None]) -> NoReturn:
    raise TimeoutError(f"Fetching task run result for run id {run_id} timed out.") from exc


def _is_retryable_error(status_code: int) -> bool:
    """Determine if an error is retryable.

    We retry the following HTTP status codes within the SDK:
    - 408 (Request Timeout): The server timed out waiting for the request
    - 503 (Service Unavailable): The server is temporarily unable to handle the request
    - 504 (Gateway Timeout): The gateway server timed out

    These errors typically indicate temporary issues with the server or network
    that may resolve upon retry. We don't include 429 (Too Many Requests) as this
    indicates rate limiting, which requires backing off rather than immediate retries.

    Note: This is a low-level retry mechanism within the SDK. Customers may want to
    implement their own retry logic at the application level for other error types.
    """
    return status_code in (408, 503, 504)
