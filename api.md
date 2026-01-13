# Shared Types

```python
from parallel.types import ErrorObject, ErrorResponse, SourcePolicy, Warning
```

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
# Beta

Types:

```python
from parallel.types.beta import (
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

- <code title="post /v1beta/extract">client.beta.<a href="./src/parallel/resources/beta/beta.py">extract</a>(\*\*<a href="src/parallel/types/beta/beta_extract_params.py">params</a>) -> <a href="./src/parallel/types/beta/extract_response.py">ExtractResponse</a></code>
- <code title="post /v1beta/search">client.beta.<a href="./src/parallel/resources/beta/beta.py">search</a>(\*\*<a href="src/parallel/types/beta/beta_search_params.py">params</a>) -> <a href="./src/parallel/types/beta/search_result.py">SearchResult</a></code>

## TaskRun

Types:

```python
from parallel.types.beta import (
    BetaRunInput,
    BetaTaskRunResult,
    ErrorEvent,
    McpServer,
    McpToolCall,
    ParallelBeta,
    TaskRunEvent,
    Webhook,
    TaskRunEventsResponse,
)
```

Methods:

- <code title="post /v1/tasks/runs?beta=true">client.beta.task_run.<a href="./src/parallel/resources/beta/task_run.py">create</a>(\*\*<a href="src/parallel/types/beta/task_run_create_params.py">params</a>) -> <a href="./src/parallel/types/task_run.py">TaskRun</a></code>
- <code title="get /v1beta/tasks/runs/{run_id}/events">client.beta.task_run.<a href="./src/parallel/resources/beta/task_run.py">events</a>(run_id) -> <a href="./src/parallel/types/beta/task_run_events_response.py">TaskRunEventsResponse</a></code>
- <code title="get /v1/tasks/runs/{run_id}/result?beta=true">client.beta.task_run.<a href="./src/parallel/resources/beta/task_run.py">result</a>(run_id, \*\*<a href="src/parallel/types/beta/task_run_result_params.py">params</a>) -> <a href="./src/parallel/types/beta/beta_task_run_result.py">BetaTaskRunResult</a></code>

## TaskGroup

Types:

```python
from parallel.types.beta import (
    TaskGroup,
    TaskGroupRunResponse,
    TaskGroupStatus,
    TaskGroupEventsResponse,
    TaskGroupGetRunsResponse,
)
```

Methods:

- <code title="post /v1beta/tasks/groups">client.beta.task_group.<a href="./src/parallel/resources/beta/task_group.py">create</a>(\*\*<a href="src/parallel/types/beta/task_group_create_params.py">params</a>) -> <a href="./src/parallel/types/beta/task_group.py">TaskGroup</a></code>
- <code title="get /v1beta/tasks/groups/{taskgroup_id}">client.beta.task_group.<a href="./src/parallel/resources/beta/task_group.py">retrieve</a>(task_group_id) -> <a href="./src/parallel/types/beta/task_group.py">TaskGroup</a></code>
- <code title="post /v1beta/tasks/groups/{taskgroup_id}/runs">client.beta.task_group.<a href="./src/parallel/resources/beta/task_group.py">add_runs</a>(task_group_id, \*\*<a href="src/parallel/types/beta/task_group_add_runs_params.py">params</a>) -> <a href="./src/parallel/types/beta/task_group_run_response.py">TaskGroupRunResponse</a></code>
- <code title="get /v1beta/tasks/groups/{taskgroup_id}/events">client.beta.task_group.<a href="./src/parallel/resources/beta/task_group.py">events</a>(task_group_id, \*\*<a href="src/parallel/types/beta/task_group_events_params.py">params</a>) -> <a href="./src/parallel/types/beta/task_group_events_response.py">TaskGroupEventsResponse</a></code>
- <code title="get /v1beta/tasks/groups/{taskgroup_id}/runs">client.beta.task_group.<a href="./src/parallel/resources/beta/task_group.py">get_runs</a>(task_group_id, \*\*<a href="src/parallel/types/beta/task_group_get_runs_params.py">params</a>) -> <a href="./src/parallel/types/beta/task_group_get_runs_response.py">TaskGroupGetRunsResponse</a></code>

## FindAll

Types:

```python
from parallel.types.beta import (
    FindAllCandidateMatchStatusEvent,
    FindAllEnrichInput,
    FindAllExtendInput,
    FindAllRun,
    FindAllRunInput,
    FindAllRunResult,
    FindAllRunStatusEvent,
    FindAllSchema,
    FindAllSchemaUpdatedEvent,
    IngestInput,
    FindAllEventsResponse,
)
```

Methods:

- <code title="post /v1beta/findall/runs">client.beta.findall.<a href="./src/parallel/resources/beta/findall.py">create</a>(\*\*<a href="src/parallel/types/beta/findall_create_params.py">params</a>) -> <a href="./src/parallel/types/beta/findall_run.py">FindAllRun</a></code>
- <code title="get /v1beta/findall/runs/{findall_id}">client.beta.findall.<a href="./src/parallel/resources/beta/findall.py">retrieve</a>(findall_id) -> <a href="./src/parallel/types/beta/findall_run.py">FindAllRun</a></code>
- <code title="post /v1beta/findall/runs/{findall_id}/cancel">client.beta.findall.<a href="./src/parallel/resources/beta/findall.py">cancel</a>(findall_id) -> object</code>
- <code title="post /v1beta/findall/runs/{findall_id}/enrich">client.beta.findall.<a href="./src/parallel/resources/beta/findall.py">enrich</a>(findall_id, \*\*<a href="src/parallel/types/beta/findall_enrich_params.py">params</a>) -> <a href="./src/parallel/types/beta/findall_schema.py">FindAllSchema</a></code>
- <code title="get /v1beta/findall/runs/{findall_id}/events">client.beta.findall.<a href="./src/parallel/resources/beta/findall.py">events</a>(findall_id, \*\*<a href="src/parallel/types/beta/findall_events_params.py">params</a>) -> <a href="./src/parallel/types/beta/findall_events_response.py">FindAllEventsResponse</a></code>
- <code title="post /v1beta/findall/runs/{findall_id}/extend">client.beta.findall.<a href="./src/parallel/resources/beta/findall.py">extend</a>(findall_id, \*\*<a href="src/parallel/types/beta/findall_extend_params.py">params</a>) -> <a href="./src/parallel/types/beta/findall_schema.py">FindAllSchema</a></code>
- <code title="post /v1beta/findall/ingest">client.beta.findall.<a href="./src/parallel/resources/beta/findall.py">ingest</a>(\*\*<a href="src/parallel/types/beta/findall_ingest_params.py">params</a>) -> <a href="./src/parallel/types/beta/findall_schema.py">FindAllSchema</a></code>
- <code title="get /v1beta/findall/runs/{findall_id}/result">client.beta.findall.<a href="./src/parallel/resources/beta/findall.py">result</a>(findall_id) -> <a href="./src/parallel/types/beta/findall_run_result.py">FindAllRunResult</a></code>
- <code title="get /v1beta/findall/runs/{findall_id}/schema">client.beta.findall.<a href="./src/parallel/resources/beta/findall.py">schema</a>(findall_id) -> <a href="./src/parallel/types/beta/findall_schema.py">FindAllSchema</a></code>
