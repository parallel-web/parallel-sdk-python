# TaskRun

Types:

```python
from parallel.types import Input, JsonSchema, TaskRun, TaskRunResult, TaskSpec, TextSchema
```

Methods:

- <code title="post /v1/tasks/runs">client.task_run.<a href="./src/parallel/resources/task_run.py">create</a>(\*\*<a href="src/parallel/types/task_run_create_params.py">params</a>) -> <a href="./src/parallel/types/task_run.py">TaskRun</a></code>
- <code title="get /v1/tasks/runs/{run_id}">client.task_run.<a href="./src/parallel/resources/task_run.py">retrieve</a>(run_id) -> <a href="./src/parallel/types/task_run.py">TaskRun</a></code>
- <code title="get /v1/tasks/runs/{run_id}/result">client.task_run.<a href="./src/parallel/resources/task_run.py">result</a>(run_id, \*\*<a href="src/parallel/types/task_run_result_params.py">params</a>) -> <a href="./src/parallel/types/task_run_result.py">TaskRunResult</a></code>
