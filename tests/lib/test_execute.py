from __future__ import annotations

import os
from typing import Any, Dict, List

import httpx
import pytest
from respx import MockRouter

from parallel import Parallel, AsyncParallel

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")

RUN: Dict[str, Any] = {
    "run_id": "trun_1",
    "interaction_id": "i1",
    "processor": "core",
    "status": "running",
    "is_active": True,
}
DONE: Dict[str, Any] = {
    "run": {**RUN, "status": "completed", "is_active": False},
    "output": {"type": "text", "content": "done", "basis": []},
}


def unfinished_then_done(first_wait: str) -> List[Any]:
    """Result responses: the first wait ends with the run still active, the second
    returns its result."""
    if first_wait == "408":
        return [httpx.Response(408, json={"error": {"message": "still active"}}), httpx.Response(200, json=DONE)]
    return [httpx.ReadTimeout("read timed out"), httpx.Response(200, json=DONE)]


@pytest.mark.parametrize("first_wait", ["408", "client timeout"])
@pytest.mark.respx(base_url=base_url)
def test_execute_waits_again_when_a_result_wait_ends_unfinished(respx_mock: MockRouter, first_wait: str) -> None:
    respx_mock.post("/v1/tasks/runs").mock(return_value=httpx.Response(202, json=RUN))
    respx_mock.get("/v1/tasks/runs/trun_1/result").mock(side_effect=unfinished_then_done(first_wait))
    client = Parallel(base_url=base_url, api_key="k", max_retries=0)

    result = client.task_run.execute(input="q", processor="core", timeout=60)

    assert result.output.content == "done"


@pytest.mark.parametrize("first_wait", ["408", "client timeout"])
@pytest.mark.respx(base_url=base_url)
async def test_async_execute_waits_again_when_a_result_wait_ends_unfinished(
    respx_mock: MockRouter, first_wait: str
) -> None:
    respx_mock.post("/v1/tasks/runs").mock(return_value=httpx.Response(202, json=RUN))
    respx_mock.get("/v1/tasks/runs/trun_1/result").mock(side_effect=unfinished_then_done(first_wait))
    client = AsyncParallel(base_url=base_url, api_key="k", max_retries=0)

    result = await client.task_run.execute(input="q", processor="core", timeout=60)

    assert result.output.content == "done"
