# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from parallel import Parallel, AsyncParallel
from tests.utils import assert_matches_type
from parallel.types.beta import SearchResult

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBeta:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_search(self, client: Parallel) -> None:
        beta = client.beta.search()
        assert_matches_type(SearchResult, beta, path=["response"])

    @parametrize
    def test_method_search_with_all_params(self, client: Parallel) -> None:
        beta = client.beta.search(
            max_chars_per_result=0,
            max_results=0,
            objective="objective",
            processor="base",
            search_queries=["string"],
            source_policy={
                "exclude_domains": ["string"],
                "include_domains": ["string"],
            },
        )
        assert_matches_type(SearchResult, beta, path=["response"])

    @parametrize
    def test_raw_response_search(self, client: Parallel) -> None:
        response = client.beta.with_raw_response.search()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        beta = response.parse()
        assert_matches_type(SearchResult, beta, path=["response"])

    @parametrize
    def test_streaming_response_search(self, client: Parallel) -> None:
        with client.beta.with_streaming_response.search() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            beta = response.parse()
            assert_matches_type(SearchResult, beta, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncBeta:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_search(self, async_client: AsyncParallel) -> None:
        beta = await async_client.beta.search()
        assert_matches_type(SearchResult, beta, path=["response"])

    @parametrize
    async def test_method_search_with_all_params(self, async_client: AsyncParallel) -> None:
        beta = await async_client.beta.search(
            max_chars_per_result=0,
            max_results=0,
            objective="objective",
            processor="base",
            search_queries=["string"],
            source_policy={
                "exclude_domains": ["string"],
                "include_domains": ["string"],
            },
        )
        assert_matches_type(SearchResult, beta, path=["response"])

    @parametrize
    async def test_raw_response_search(self, async_client: AsyncParallel) -> None:
        response = await async_client.beta.with_raw_response.search()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        beta = await response.parse()
        assert_matches_type(SearchResult, beta, path=["response"])

    @parametrize
    async def test_streaming_response_search(self, async_client: AsyncParallel) -> None:
        async with async_client.beta.with_streaming_response.search() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            beta = await response.parse()
            assert_matches_type(SearchResult, beta, path=["response"])

        assert cast(Any, response.is_closed) is True
