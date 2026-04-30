# Shared Types

```python
from parallel.types import ErrorObject, ErrorResponse, SourcePolicy, Warning
```

# Parallel

Types:

```python
from parallel.types import (
    AdvancedExtractSettings,
    AdvancedSearchSettings,
    ExcerptSettings,
    ExtractError,
    ExtractResponse,
    ExtractResult,
    FetchPolicy,
    SearchResult,
    UsageItem,
    WebSearchResult,
)
```

Methods:

- <code title="post /v1/extract">client.<a href="./src/parallel/_client.py">extract</a>(\*\*<a href="src/parallel/types/client_extract_params.py">params</a>) -> <a href="./src/parallel/types/extract_response.py">ExtractResponse</a></code>
- <code title="post /v1/search">client.<a href="./src/parallel/_client.py">search</a>(\*\*<a href="src/parallel/types/client_search_params.py">params</a>) -> <a href="./src/parallel/types/search_result.py">SearchResult</a></code>

# TaskRun

Types:

```python
from parallel.types import (
    AutoSchema,
    Citation,
    FieldBasis,
    JsonSchema,
    ParsedTaskRunResult,
    RunInput,
    TaskRun,
    TaskRunJsonOutput,
    TaskRunResult,
    TaskRunTextOutput,
    TaskSpec,
    TextSchema,
)
```

Methods:

- <code title="post /v1/tasks/runs">client.task_run.<a href="./src/parallel/resources/task_run.py">create</a>(\*\*<a href="src/parallel/types/task_run_create_params.py">params</a>) -> <a href="./src/parallel/types/task_run.py">TaskRun</a></code>
- <code title="get /v1/tasks/runs/{run_id}">client.task_run.<a href="./src/parallel/resources/task_run.py">retrieve</a>(run_id) -> <a href="./src/parallel/types/task_run.py">TaskRun</a></code>
- <code title="get /v1/tasks/runs/{run_id}/result">client.task_run.<a href="./src/parallel/resources/task_run.py">result</a>(run_id, \*\*<a href="src/parallel/types/task_run_result_params.py">params</a>) -> <a href="./src/parallel/types/task_run_result.py">TaskRunResult</a></code>

Convenience methods:

- <code title="post /v1/tasks/runs">client.task_run.<a href="./src/parallel/resources/task_run.py">execute</a>(input, processor, output: <a href="./src/parallel/types/task_spec_param.py">OutputSchema</a>) -> <a href="./src/parallel/types/task_run_result.py">TaskRunResult</a></code>
- <code title="post /v1/tasks/runs">client.task_run.<a href="./src/parallel/resources/task_run.py">execute</a>(input, processor, output: Type[OutputT]) -> <a href="./src/parallel/types/parsed_task_run_result.py">ParsedTaskRunResult[OutputT]</a></code>
# TaskGroup

Types:

```python
from parallel.types import (
    TaskGroup,
    TaskGroupRunResponse,
    TaskGroupStatus,
    TaskGroupEventsResponse,
    TaskGroupGetRunsResponse,
)
```

Methods:

- <code title="post /v1/tasks/groups">client.task_group.<a href="./src/parallel/resources/task_group.py">create</a>(\*\*<a href="src/parallel/types/task_group_create_params.py">params</a>) -> <a href="./src/parallel/types/task_group.py">TaskGroup</a></code>
- <code title="get /v1/tasks/groups/{taskgroup_id}">client.task_group.<a href="./src/parallel/resources/task_group.py">retrieve</a>(task_group_id) -> <a href="./src/parallel/types/task_group.py">TaskGroup</a></code>
- <code title="post /v1/tasks/groups/{taskgroup_id}/runs">client.task_group.<a href="./src/parallel/resources/task_group.py">add_runs</a>(task_group_id, \*\*<a href="src/parallel/types/task_group_add_runs_params.py">params</a>) -> <a href="./src/parallel/types/task_group_run_response.py">TaskGroupRunResponse</a></code>
- <code title="get /v1/tasks/groups/{taskgroup_id}/events">client.task_group.<a href="./src/parallel/resources/task_group.py">events</a>(task_group_id, \*\*<a href="src/parallel/types/task_group_events_params.py">params</a>) -> <a href="./src/parallel/types/task_group_events_response.py">TaskGroupEventsResponse</a></code>
- <code title="get /v1/tasks/groups/{taskgroup_id}/runs">client.task_group.<a href="./src/parallel/resources/task_group.py">get_runs</a>(task_group_id, \*\*<a href="src/parallel/types/task_group_get_runs_params.py">params</a>) -> <a href="./src/parallel/types/task_group_get_runs_response.py">TaskGroupGetRunsResponse</a></code>

# [Beta](src/parallel/resources/beta/api.md)
