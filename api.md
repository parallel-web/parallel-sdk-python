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
    FullContentSettings,
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
    TaskAdvancedSettings,
    TaskRun,
    TaskRunJsonOutput,
    TaskRunProgressMessageEvent,
    TaskRunProgressStatsEvent,
    TaskRunResult,
    TaskRunSourceStats,
    TaskRunTextOutput,
    TaskSpec,
    TextSchema,
)
```

Methods:

- <code title="post /v1/tasks/runs">client.task_run.<a href="./src/parallel/resources/task_run.py">create</a>(\*\*<a href="src/parallel/types/task_run_create_params.py">params</a>) -> <a href="./src/parallel/types/task_run.py">TaskRun</a></code>
- <code title="get /v1/tasks/runs/{run_id}">client.task_run.<a href="./src/parallel/resources/task_run.py">retrieve</a>(run_id) -> <a href="./src/parallel/types/task_run.py">TaskRun</a></code>
- <code title="get /v1/tasks/runs/{run_id}/result">client.task_run.<a href="./src/parallel/resources/task_run.py">result</a>(run_id, \*\*<a href="src/parallel/types/task_run_result_params.py">params</a>) -> <a href="./src/parallel/types/task_run_result.py">TaskRunResult</a></code>
- <code title="get /v1/tasks/runs/{run_id}/input">client.task_run.<a href="./src/parallel/resources/task_run.py">retrieve_input</a>(run_id) -> <a href="./src/parallel/types/run_input.py">RunInput</a></code>

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
    TaskGroupStatusEvent,
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
- <code title="get /v1/tasks/groups/{taskgroup_id}/runs/{run_id}">client.task_group.<a href="./src/parallel/resources/task_group.py">retrieve_run</a>(run_id, \*, task_group_id) -> <a href="./src/parallel/types/task_run.py">TaskRun</a></code>

# Monitor

Types:

```python
from parallel.types import (
    AdvancedMonitorSettings,
    CreateMonitorRequest,
    Monitor,
    MonitorCompletionEvent,
    MonitorErrorEvent,
    MonitorEventStreamEvent,
    MonitorEventStreamResponseSettings,
    MonitorEventStreamSettings,
    MonitorSnapshotEvent,
    MonitorSnapshotOutput,
    MonitorSnapshotResponseSettings,
    MonitorSnapshotSettings,
    MonitorWebhook,
    PaginatedMonitorEvents,
    PaginatedMonitorResponse,
    UpdateMonitorEventStreamSettings,
    UpdateMonitorRequest,
)
```

Methods:

- <code title="post /v1/monitors">client.monitor.<a href="./src/parallel/resources/monitor.py">create</a>(\*\*<a href="src/parallel/types/monitor_create_params.py">params</a>) -> <a href="./src/parallel/types/monitor.py">Monitor</a></code>
- <code title="get /v1/monitors/{monitor_id}">client.monitor.<a href="./src/parallel/resources/monitor.py">retrieve</a>(monitor_id) -> <a href="./src/parallel/types/monitor.py">Monitor</a></code>
- <code title="post /v1/monitors/{monitor_id}/update">client.monitor.<a href="./src/parallel/resources/monitor.py">update</a>(monitor_id, \*\*<a href="src/parallel/types/monitor_update_params.py">params</a>) -> <a href="./src/parallel/types/monitor.py">Monitor</a></code>
- <code title="get /v1/monitors">client.monitor.<a href="./src/parallel/resources/monitor.py">list</a>(\*\*<a href="src/parallel/types/monitor_list_params.py">params</a>) -> <a href="./src/parallel/types/paginated_monitor_response.py">PaginatedMonitorResponse</a></code>
- <code title="post /v1/monitors/{monitor_id}/cancel">client.monitor.<a href="./src/parallel/resources/monitor.py">cancel</a>(monitor_id) -> <a href="./src/parallel/types/monitor.py">Monitor</a></code>
- <code title="get /v1/monitors/{monitor_id}/events">client.monitor.<a href="./src/parallel/resources/monitor.py">events</a>(monitor_id, \*\*<a href="src/parallel/types/monitor_events_params.py">params</a>) -> <a href="./src/parallel/types/paginated_monitor_events.py">PaginatedMonitorEvents</a></code>
- <code title="post /v1/monitors/{monitor_id}/trigger">client.monitor.<a href="./src/parallel/resources/monitor.py">trigger</a>(monitor_id) -> None</code>

# [Beta](src/parallel/resources/beta/api.md)
