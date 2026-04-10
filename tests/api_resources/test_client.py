# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from parallel import Parallel, AsyncParallel
from tests.utils import assert_matches_type
from parallel.types import SearchResult, ExtractResponse
from parallel._utils import parse_date

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestClient:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_extract(self, client: Parallel) -> None:
        client_ = client.extract(
            urls=["string"],
        )
        assert_matches_type(ExtractResponse, client_, path=["response"])

    @parametrize
    def test_method_extract_with_all_params(self, client: Parallel) -> None:
        client_ = client.extract(
            urls=["string"],
            advanced={
                "excerpt_settings": {"max_chars_per_result": 0},
                "fetch_policy": {
                    "disable_cache_fallback": True,
                    "max_age_seconds": 86400,
                    "timeout_seconds": 60,
                },
                "full_content": {"max_chars_per_result": 0},
            },
            client_model="claude-sonnet-4-6-20260401",
            max_chars_total=0,
            objective="objective",
            search_queries=["string"],
        )
        assert_matches_type(ExtractResponse, client_, path=["response"])

    @parametrize
    def test_raw_response_extract(self, client: Parallel) -> None:
        response = client.with_raw_response.extract(
            urls=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client_ = response.parse()
        assert_matches_type(ExtractResponse, client_, path=["response"])

    @parametrize
    def test_streaming_response_extract(self, client: Parallel) -> None:
        with client.with_streaming_response.extract(
            urls=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client_ = response.parse()
            assert_matches_type(ExtractResponse, client_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_search(self, client: Parallel) -> None:
        client_ = client.search(
            search_queries=["string"],
        )
        assert_matches_type(SearchResult, client_, path=["response"])

    @parametrize
    def test_method_search_with_all_params(self, client: Parallel) -> None:
        client_ = client.search(
            search_queries=["string"],
            advanced={
                "excerpt_settings": {"max_chars_per_result": 0},
                "fetch_policy": {
                    "disable_cache_fallback": True,
                    "max_age_seconds": 86400,
                    "timeout_seconds": 60,
                },
                "location": "us",
                "source_policy": {
                    "after_date": parse_date("2024-01-01"),
                    "exclude_domains": ["reddit.com", "x.com", ".ai"],
                    "include_domains": ["wikipedia.org", "usa.gov", ".edu"],
                },
            },
            client_model="claude-sonnet-4-6-20260401",
            max_chars_total=0,
            mode="basic",
            objective="objective",
        )
        assert_matches_type(SearchResult, client_, path=["response"])

    @parametrize
    def test_raw_response_search(self, client: Parallel) -> None:
        response = client.with_raw_response.search(
            search_queries=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client_ = response.parse()
        assert_matches_type(SearchResult, client_, path=["response"])

    @parametrize
    def test_streaming_response_search(self, client: Parallel) -> None:
        with client.with_streaming_response.search(
            search_queries=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client_ = response.parse()
            assert_matches_type(SearchResult, client_, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncClient:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_extract(self, async_client: AsyncParallel) -> None:
        client = await async_client.extract(
            urls=["string"],
        )
        assert_matches_type(ExtractResponse, client, path=["response"])

    @parametrize
    async def test_method_extract_with_all_params(self, async_client: AsyncParallel) -> None:
        client = await async_client.extract(
            urls=["string"],
            advanced={
                "excerpt_settings": {"max_chars_per_result": 0},
                "fetch_policy": {
                    "disable_cache_fallback": True,
                    "max_age_seconds": 86400,
                    "timeout_seconds": 60,
                },
                "full_content": {"max_chars_per_result": 0},
            },
            client_model="claude-sonnet-4-6-20260401",
            max_chars_total=0,
            objective="objective",
            search_queries=["string"],
        )
        assert_matches_type(ExtractResponse, client, path=["response"])

    @parametrize
    async def test_raw_response_extract(self, async_client: AsyncParallel) -> None:
        response = await async_client.with_raw_response.extract(
            urls=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client = await response.parse()
        assert_matches_type(ExtractResponse, client, path=["response"])

    @parametrize
    async def test_streaming_response_extract(self, async_client: AsyncParallel) -> None:
        async with async_client.with_streaming_response.extract(
            urls=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client = await response.parse()
            assert_matches_type(ExtractResponse, client, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_search(self, async_client: AsyncParallel) -> None:
        client = await async_client.search(
            search_queries=["string"],
        )
        assert_matches_type(SearchResult, client, path=["response"])

    @parametrize
    async def test_method_search_with_all_params(self, async_client: AsyncParallel) -> None:
        client = await async_client.search(
            search_queries=["string"],
            advanced={
                "excerpt_settings": {"max_chars_per_result": 0},
                "fetch_policy": {
                    "disable_cache_fallback": True,
                    "max_age_seconds": 86400,
                    "timeout_seconds": 60,
                },
                "location": "us",
                "source_policy": {
                    "after_date": parse_date("2024-01-01"),
                    "exclude_domains": ["reddit.com", "x.com", ".ai"],
                    "include_domains": ["wikipedia.org", "usa.gov", ".edu"],
                },
            },
            client_model="claude-sonnet-4-6-20260401",
            max_chars_total=0,
            mode="basic",
            objective="objective",
        )
        assert_matches_type(SearchResult, client, path=["response"])

    @parametrize
    async def test_raw_response_search(self, async_client: AsyncParallel) -> None:
        response = await async_client.with_raw_response.search(
            search_queries=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client = await response.parse()
        assert_matches_type(SearchResult, client, path=["response"])

    @parametrize
    async def test_streaming_response_search(self, async_client: AsyncParallel) -> None:
        async with async_client.with_streaming_response.search(
            search_queries=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client = await response.parse()
            assert_matches_type(SearchResult, client, path=["response"])

        assert cast(Any, response.is_closed) is True
