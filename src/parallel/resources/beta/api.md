# Beta

## FindAll

Types:

```python
from parallel.types.beta import (
    FindAllCandidate,
    FindAllCandidateMatchStatusEvent,
    FindAllCandidateMetrics,
    FindAllEnrichInput,
    FindAllEntitySearchRequest,
    FindAllEntitySearchResponse,
    FindAllExtendInput,
    FindAllRun,
    FindAllRunInput,
    FindAllRunResult,
    FindAllRunStatus,
    FindAllRunStatusEvent,
    FindAllSchema,
    FindAllSchemaUpdatedEvent,
    IngestInput,
    MatchCondition,
    ParallelBeta,
    FindAllEventsResponse,
)
```

Methods:

- <code title="post /v1beta/findall/runs">client.beta.findall.<a href="./src/parallel/resources/beta/findall.py">create</a>(\*\*<a href="src/parallel/types/beta/findall_create_params.py">params</a>) -> <a href="./src/parallel/types/beta/findall_run.py">FindAllRun</a></code>
- <code title="get /v1beta/findall/runs/{findall_id}">client.beta.findall.<a href="./src/parallel/resources/beta/findall.py">retrieve</a>(findall_id) -> <a href="./src/parallel/types/beta/findall_run.py">FindAllRun</a></code>
- <code title="post /v1beta/findall/runs/{findall_id}/cancel">client.beta.findall.<a href="./src/parallel/resources/beta/findall.py">cancel</a>(findall_id) -> None</code>
- <code title="post /v1beta/findall/runs/{findall_id}/enrich">client.beta.findall.<a href="./src/parallel/resources/beta/findall.py">enrich</a>(findall_id, \*\*<a href="src/parallel/types/beta/findall_enrich_params.py">params</a>) -> <a href="./src/parallel/types/beta/findall_schema.py">FindAllSchema</a></code>
- <code title="post /v1beta/findall/entity-search">client.beta.findall.<a href="./src/parallel/resources/beta/findall.py">entity_search</a>(\*\*<a href="src/parallel/types/beta/findall_entity_search_params.py">params</a>) -> <a href="./src/parallel/types/beta/findall_entity_search_response.py">FindAllEntitySearchResponse</a></code>
- <code title="get /v1beta/findall/runs/{findall_id}/events">client.beta.findall.<a href="./src/parallel/resources/beta/findall.py">events</a>(findall_id, \*\*<a href="src/parallel/types/beta/findall_events_params.py">params</a>) -> <a href="./src/parallel/types/beta/findall_events_response.py">FindAllEventsResponse</a></code>
- <code title="post /v1beta/findall/runs/{findall_id}/extend">client.beta.findall.<a href="./src/parallel/resources/beta/findall.py">extend</a>(findall_id, \*\*<a href="src/parallel/types/beta/findall_extend_params.py">params</a>) -> <a href="./src/parallel/types/beta/findall_schema.py">FindAllSchema</a></code>
- <code title="post /v1beta/findall/ingest">client.beta.findall.<a href="./src/parallel/resources/beta/findall.py">ingest</a>(\*\*<a href="src/parallel/types/beta/findall_ingest_params.py">params</a>) -> <a href="./src/parallel/types/beta/findall_schema.py">FindAllSchema</a></code>
- <code title="get /v1beta/findall/runs/{findall_id}/result">client.beta.findall.<a href="./src/parallel/resources/beta/findall.py">result</a>(findall_id) -> <a href="./src/parallel/types/beta/findall_run_result.py">FindAllRunResult</a></code>
- <code title="get /v1beta/findall/runs/{findall_id}/schema">client.beta.findall.<a href="./src/parallel/resources/beta/findall.py">schema</a>(findall_id) -> <a href="./src/parallel/types/beta/findall_schema.py">FindAllSchema</a></code>
