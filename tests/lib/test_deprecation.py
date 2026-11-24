from __future__ import annotations

import os
import warnings
from typing import Any, Dict, Iterator

import httpx
import pytest
from respx import MockRouter

from parallel import Parallel, AsyncParallel
from parallel.lib import _deprecation
from parallel.lib._deprecation import ParallelDeprecationWarning

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")

SEARCH_RESULT: Dict[str, Any] = {"search_id": "s1", "results": []}
DEPRECATION_HEADERS = {
    "Deprecation": "@1767225600",
    "Link": '<https://docs.parallel.ai/search/search-migration-guide>; rel="deprecation", '
    '<https://api.parallel.ai/v1/search>; rel="successor-version"',
}


@pytest.fixture(autouse=True)
def reset_seen() -> Iterator[None]:
    _deprecation._seen.clear()
    yield
    _deprecation._seen.clear()


@pytest.mark.respx(base_url=base_url)
def test_deprecation_header_warns_once(respx_mock: MockRouter) -> None:
    respx_mock.post("/v1/search").mock(
        return_value=httpx.Response(200, json=SEARCH_RESULT, headers=DEPRECATION_HEADERS)
    )
    client = Parallel(base_url=base_url, api_key="k", max_retries=0)

    with pytest.warns(ParallelDeprecationWarning) as record:
        client.search(search_queries=["q"])
        client.search(search_queries=["q"])

    assert len(record) == 1
    assert record[0].filename == __file__
    assert str(record[0].message) == (
        "Parallel API: POST /v1/search is deprecated. Use https://api.parallel.ai/v1/search instead. "
        "See https://docs.parallel.ai/search/search-migration-guide"
    )


@pytest.mark.respx(base_url=base_url)
def test_sunset_header_is_shown(respx_mock: MockRouter) -> None:
    respx_mock.post("/v1/search").mock(
        return_value=httpx.Response(
            200,
            json=SEARCH_RESULT,
            headers={"Deprecation": "@1767225600", "Sunset": "Wed, 01 Jul 2026 00:00:00 GMT"},
        )
    )
    client = Parallel(base_url=base_url, api_key="k", max_retries=0)

    with pytest.warns(ParallelDeprecationWarning, match=r"removed after Wed, 01 Jul 2026 00:00:00 GMT\.$"):
        client.search(search_queries=["q"])


@pytest.mark.respx(base_url=base_url)
def test_body_deprecation_warning(respx_mock: MockRouter) -> None:
    body = {
        **SEARCH_RESULT,
        "warnings": [
            {"type": "input_validation_warning", "message": "ignored"},
            {
                "type": "deprecation_warning",
                "message": "This endpoint is deprecated. Use /v1/search instead.",
                "detail": {
                    "replacement_endpoint": "/v1/search",
                    "documentation": "https://docs.parallel.ai/search/search-migration-guide",
                },
            },
        ],
    }
    respx_mock.post("/v1/search").mock(return_value=httpx.Response(200, json=body))
    client = Parallel(base_url=base_url, api_key="k", max_retries=0)

    with pytest.warns(ParallelDeprecationWarning) as record:
        client.search(search_queries=["q"])

    assert [str(r.message) for r in record] == [
        "Parallel API: This endpoint is deprecated. Use /v1/search instead. "
        "See https://docs.parallel.ai/search/search-migration-guide"
    ]


@pytest.mark.respx(base_url=base_url)
def test_header_and_body_warn_only_once(respx_mock: MockRouter) -> None:
    body = {**SEARCH_RESULT, "warnings": [{"type": "deprecation_warning", "message": "deprecated"}]}
    respx_mock.post("/v1/search").mock(return_value=httpx.Response(200, json=body, headers=DEPRECATION_HEADERS))
    client = Parallel(base_url=base_url, api_key="k", max_retries=0)

    with pytest.warns(ParallelDeprecationWarning) as record:
        client.search(search_queries=["q"])

    assert len(record) == 1
    assert "POST /v1/search is deprecated" in str(record[0].message)


@pytest.mark.respx(base_url=base_url)
def test_no_warning_without_deprecation_signal(respx_mock: MockRouter) -> None:
    respx_mock.post("/v1/search").mock(return_value=httpx.Response(200, json=SEARCH_RESULT))
    client = Parallel(base_url=base_url, api_key="k", max_retries=0)

    with warnings.catch_warnings():
        warnings.simplefilter("error")
        client.search(search_queries=["q"])


@pytest.mark.respx(base_url=base_url)
async def test_async_deprecation_header_warns(respx_mock: MockRouter) -> None:
    respx_mock.post("/v1/search").mock(
        return_value=httpx.Response(200, json=SEARCH_RESULT, headers=DEPRECATION_HEADERS)
    )
    client = AsyncParallel(base_url=base_url, api_key="k", max_retries=0)

    with pytest.warns(ParallelDeprecationWarning, match="POST /v1/search is deprecated") as record:
        await client.search(search_queries=["q"])

    assert record[0].filename == __file__
