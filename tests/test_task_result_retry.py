from __future__ import annotations

import time
from unittest.mock import Mock

import httpx
import pytest

from parallel import Parallel, AsyncParallel, APIStatusError


@pytest.mark.parametrize("asynchronous", [False, True])
@pytest.mark.parametrize("failure", [408, 503, 504, "timeout"])
async def test_result_retries_after_transient_failure(asynchronous: bool, failure: int | str) -> None:
    calls = 0

    def handler(request: httpx.Request) -> httpx.Response:
        nonlocal calls
        if request.method == "POST":
            return httpx.Response(200, json={"run_id": "run_test"})
        calls += 1
        if calls == 1:
            if failure == "timeout":
                raise httpx.ReadTimeout("temporary", request=request)
            return httpx.Response(int(failure), json={"error": "temporary"})
        return httpx.Response(200, json={"run_id": "run_test", "output": {"type": "text", "content": "done"}})

    if asynchronous:
        async with AsyncParallel(
            api_key="test", max_retries=0, http_client=httpx.AsyncClient(transport=httpx.MockTransport(handler))
        ) as client:
            result = await client.task_run.execute(input="test", processor="lite", timeout=10)
    else:
        with Parallel(
            api_key="test", max_retries=0, http_client=httpx.Client(transport=httpx.MockTransport(handler))
        ) as client:
            result = client.task_run.execute(input="test", processor="lite", timeout=10)
    assert result.output.content == "done"
    assert calls == 2


@pytest.mark.parametrize("asynchronous", [False, True])
async def test_non_retryable_error_propagates(asynchronous: bool) -> None:
    handler = Mock(return_value=httpx.Response(429, json={"error": "rate limited"}))
    with pytest.raises(APIStatusError) as exc:
        if asynchronous:
            async with AsyncParallel(
                api_key="test", max_retries=0, http_client=httpx.AsyncClient(transport=httpx.MockTransport(handler))
            ) as client:
                await client.task_run._wait_for_result(run_id="run_test", deadline=time.monotonic() + 10)
        else:
            with Parallel(
                api_key="test", max_retries=0, http_client=httpx.Client(transport=httpx.MockTransport(handler))
            ) as client:
                client.task_run._wait_for_result(run_id="run_test", deadline=time.monotonic() + 10)
    assert exc.value.status_code == 429
    assert handler.call_count == 1


@pytest.mark.parametrize("asynchronous", [False, True])
@pytest.mark.parametrize("expired", [False, True])
async def test_deadline_and_last_error(monkeypatch: pytest.MonkeyPatch, asynchronous: bool, expired: bool) -> None:
    from types import SimpleNamespace

    from parallel.lib._parsing import _task_run_result

    clock = Mock(side_effect=[2] if expired else [0, 2])
    monkeypatch.setattr(_task_run_result, "time", SimpleNamespace(monotonic=clock))
    handler = Mock(return_value=httpx.Response(503, json={"error": "temporary"}))
    with pytest.raises(TimeoutError, match="run_test") as exc:
        if asynchronous:
            async with AsyncParallel(
                api_key="test", max_retries=0, http_client=httpx.AsyncClient(transport=httpx.MockTransport(handler))
            ) as client:
                await client.task_run._wait_for_result(run_id="run_test", deadline=1)
        else:
            with Parallel(
                api_key="test", max_retries=0, http_client=httpx.Client(transport=httpx.MockTransport(handler))
            ) as client:
                client.task_run._wait_for_result(run_id="run_test", deadline=1)
    assert handler.call_count == (0 if expired else 1)
    if expired:
        assert exc.value.__cause__ is None
    else:
        assert isinstance(exc.value.__cause__, APIStatusError)
        assert exc.value.__cause__.status_code == 503
