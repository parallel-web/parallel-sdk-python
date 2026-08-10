# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from parallel import Parallel, AsyncParallel
from tests.utils import assert_matches_type
from parallel._utils import parse_datetime
from parallel.types.beta import MemoryRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMemory:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Parallel) -> None:
        memory = client.beta.memory.retrieve()
        assert_matches_type(MemoryRetrieveResponse, memory, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Parallel) -> None:
        memory = client.beta.memory.retrieve(
            kind="task",
            limit=1,
            memory_scope_key="memory_scope_key",
            query="query",
            since=parse_datetime("2026-07-15T17:30:00Z"),
        )
        assert_matches_type(MemoryRetrieveResponse, memory, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Parallel) -> None:
        response = client.beta.memory.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory = response.parse()
        assert_matches_type(MemoryRetrieveResponse, memory, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Parallel) -> None:
        with client.beta.memory.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory = response.parse()
            assert_matches_type(MemoryRetrieveResponse, memory, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_clear(self, client: Parallel) -> None:
        memory = client.beta.memory.clear()
        assert memory is None

    @parametrize
    def test_method_clear_with_all_params(self, client: Parallel) -> None:
        memory = client.beta.memory.clear(
            memory_scope_key="memory_scope_key",
        )
        assert memory is None

    @parametrize
    def test_raw_response_clear(self, client: Parallel) -> None:
        response = client.beta.memory.with_raw_response.clear()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory = response.parse()
        assert memory is None

    @parametrize
    def test_streaming_response_clear(self, client: Parallel) -> None:
        with client.beta.memory.with_streaming_response.clear() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory = response.parse()
            assert memory is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_evict(self, client: Parallel) -> None:
        memory = client.beta.memory.evict(
            id="id",
            kind="task",
        )
        assert memory is None

    @parametrize
    def test_method_evict_with_all_params(self, client: Parallel) -> None:
        memory = client.beta.memory.evict(
            id="id",
            kind="task",
            memory_scope_key="memory_scope_key",
        )
        assert memory is None

    @parametrize
    def test_raw_response_evict(self, client: Parallel) -> None:
        response = client.beta.memory.with_raw_response.evict(
            id="id",
            kind="task",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory = response.parse()
        assert memory is None

    @parametrize
    def test_streaming_response_evict(self, client: Parallel) -> None:
        with client.beta.memory.with_streaming_response.evict(
            id="id",
            kind="task",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory = response.parse()
            assert memory is None

        assert cast(Any, response.is_closed) is True


class TestAsyncMemory:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncParallel) -> None:
        memory = await async_client.beta.memory.retrieve()
        assert_matches_type(MemoryRetrieveResponse, memory, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncParallel) -> None:
        memory = await async_client.beta.memory.retrieve(
            kind="task",
            limit=1,
            memory_scope_key="memory_scope_key",
            query="query",
            since=parse_datetime("2026-07-15T17:30:00Z"),
        )
        assert_matches_type(MemoryRetrieveResponse, memory, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncParallel) -> None:
        response = await async_client.beta.memory.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory = await response.parse()
        assert_matches_type(MemoryRetrieveResponse, memory, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncParallel) -> None:
        async with async_client.beta.memory.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory = await response.parse()
            assert_matches_type(MemoryRetrieveResponse, memory, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_clear(self, async_client: AsyncParallel) -> None:
        memory = await async_client.beta.memory.clear()
        assert memory is None

    @parametrize
    async def test_method_clear_with_all_params(self, async_client: AsyncParallel) -> None:
        memory = await async_client.beta.memory.clear(
            memory_scope_key="memory_scope_key",
        )
        assert memory is None

    @parametrize
    async def test_raw_response_clear(self, async_client: AsyncParallel) -> None:
        response = await async_client.beta.memory.with_raw_response.clear()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory = await response.parse()
        assert memory is None

    @parametrize
    async def test_streaming_response_clear(self, async_client: AsyncParallel) -> None:
        async with async_client.beta.memory.with_streaming_response.clear() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory = await response.parse()
            assert memory is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_evict(self, async_client: AsyncParallel) -> None:
        memory = await async_client.beta.memory.evict(
            id="id",
            kind="task",
        )
        assert memory is None

    @parametrize
    async def test_method_evict_with_all_params(self, async_client: AsyncParallel) -> None:
        memory = await async_client.beta.memory.evict(
            id="id",
            kind="task",
            memory_scope_key="memory_scope_key",
        )
        assert memory is None

    @parametrize
    async def test_raw_response_evict(self, async_client: AsyncParallel) -> None:
        response = await async_client.beta.memory.with_raw_response.evict(
            id="id",
            kind="task",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory = await response.parse()
        assert memory is None

    @parametrize
    async def test_streaming_response_evict(self, async_client: AsyncParallel) -> None:
        async with async_client.beta.memory.with_streaming_response.evict(
            id="id",
            kind="task",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory = await response.parse()
            assert memory is None

        assert cast(Any, response.is_closed) is True
