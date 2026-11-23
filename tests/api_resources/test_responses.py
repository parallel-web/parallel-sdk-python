# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from parallel import Parallel, AsyncParallel
from tests.utils import assert_matches_type
from parallel.types.responses import ResponseResult

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestResponses:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create_overload_1(self, client: Parallel) -> None:
        response = client.responses.create(
            input="What are the latest developments in fusion energy?",
            model="parallel",
        )
        assert_matches_type(ResponseResult, response, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_1(self, client: Parallel) -> None:
        response = client.responses.create(
            input="What are the latest developments in fusion energy?",
            model="parallel",
            background=True,
            data_sources={
                "excluded": ["string"],
                "free": ["string"],
                "pay_per_use": ["string"],
            },
            instructions="instructions",
            metadata={"foo": "string"},
            previous_response_id="previous_response_id",
            reasoning={"effort": "high"},
            stream=False,
            text={
                "format": {"type": "text"},
                "verbosity": "low",
            },
            tools=[
                {
                    "type": "web_search",
                    "filters": {
                        "allowed_domains": ["string"],
                        "blocked_domains": ["string"],
                    },
                    "search_context_size": "low",
                    "user_location": {
                        "city": "city",
                        "country": "country",
                        "region": "region",
                        "timezone": "timezone",
                        "type": "approximate",
                    },
                }
            ],
        )
        assert_matches_type(ResponseResult, response, path=["response"])

    @parametrize
    def test_raw_response_create_overload_1(self, client: Parallel) -> None:
        http_response = client.responses.with_raw_response.create(
            input="What are the latest developments in fusion energy?",
            model="parallel",
        )

        assert http_response.is_closed is True
        assert http_response.http_request.headers.get("X-Stainless-Lang") == "python"
        response = http_response.parse()
        assert_matches_type(ResponseResult, response, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_1(self, client: Parallel) -> None:
        with client.responses.with_streaming_response.create(
            input="What are the latest developments in fusion energy?",
            model="parallel",
        ) as http_response:
            assert not http_response.is_closed
            assert http_response.http_request.headers.get("X-Stainless-Lang") == "python"

            response = http_response.parse()
            assert_matches_type(ResponseResult, response, path=["response"])

        assert cast(Any, http_response.is_closed) is True

    @parametrize
    def test_method_create_overload_2(self, client: Parallel) -> None:
        response_stream = client.responses.create(
            input="What are the latest developments in fusion energy?",
            model="parallel",
            stream=True,
        )
        response_stream.response.close()

    @parametrize
    def test_method_create_with_all_params_overload_2(self, client: Parallel) -> None:
        response_stream = client.responses.create(
            input="What are the latest developments in fusion energy?",
            model="parallel",
            stream=True,
            background=True,
            data_sources={
                "excluded": ["string"],
                "free": ["string"],
                "pay_per_use": ["string"],
            },
            instructions="instructions",
            metadata={"foo": "string"},
            previous_response_id="previous_response_id",
            reasoning={"effort": "high"},
            text={
                "format": {"type": "text"},
                "verbosity": "low",
            },
            tools=[
                {
                    "type": "web_search",
                    "filters": {
                        "allowed_domains": ["string"],
                        "blocked_domains": ["string"],
                    },
                    "search_context_size": "low",
                    "user_location": {
                        "city": "city",
                        "country": "country",
                        "region": "region",
                        "timezone": "timezone",
                        "type": "approximate",
                    },
                }
            ],
        )
        response_stream.response.close()

    @parametrize
    def test_raw_response_create_overload_2(self, client: Parallel) -> None:
        response = client.responses.with_raw_response.create(
            input="What are the latest developments in fusion energy?",
            model="parallel",
            stream=True,
        )

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = response.parse()
        stream.close()

    @parametrize
    def test_streaming_response_create_overload_2(self, client: Parallel) -> None:
        with client.responses.with_streaming_response.create(
            input="What are the latest developments in fusion energy?",
            model="parallel",
            stream=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = response.parse()
            stream.close()

        assert cast(Any, response.is_closed) is True


class TestAsyncResponses:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create_overload_1(self, async_client: AsyncParallel) -> None:
        response = await async_client.responses.create(
            input="What are the latest developments in fusion energy?",
            model="parallel",
        )
        assert_matches_type(ResponseResult, response, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_1(self, async_client: AsyncParallel) -> None:
        response = await async_client.responses.create(
            input="What are the latest developments in fusion energy?",
            model="parallel",
            background=True,
            data_sources={
                "excluded": ["string"],
                "free": ["string"],
                "pay_per_use": ["string"],
            },
            instructions="instructions",
            metadata={"foo": "string"},
            previous_response_id="previous_response_id",
            reasoning={"effort": "high"},
            stream=False,
            text={
                "format": {"type": "text"},
                "verbosity": "low",
            },
            tools=[
                {
                    "type": "web_search",
                    "filters": {
                        "allowed_domains": ["string"],
                        "blocked_domains": ["string"],
                    },
                    "search_context_size": "low",
                    "user_location": {
                        "city": "city",
                        "country": "country",
                        "region": "region",
                        "timezone": "timezone",
                        "type": "approximate",
                    },
                }
            ],
        )
        assert_matches_type(ResponseResult, response, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_1(self, async_client: AsyncParallel) -> None:
        http_response = await async_client.responses.with_raw_response.create(
            input="What are the latest developments in fusion energy?",
            model="parallel",
        )

        assert http_response.is_closed is True
        assert http_response.http_request.headers.get("X-Stainless-Lang") == "python"
        response = await http_response.parse()
        assert_matches_type(ResponseResult, response, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_1(self, async_client: AsyncParallel) -> None:
        async with async_client.responses.with_streaming_response.create(
            input="What are the latest developments in fusion energy?",
            model="parallel",
        ) as http_response:
            assert not http_response.is_closed
            assert http_response.http_request.headers.get("X-Stainless-Lang") == "python"

            response = await http_response.parse()
            assert_matches_type(ResponseResult, response, path=["response"])

        assert cast(Any, http_response.is_closed) is True

    @parametrize
    async def test_method_create_overload_2(self, async_client: AsyncParallel) -> None:
        response_stream = await async_client.responses.create(
            input="What are the latest developments in fusion energy?",
            model="parallel",
            stream=True,
        )
        await response_stream.response.aclose()

    @parametrize
    async def test_method_create_with_all_params_overload_2(self, async_client: AsyncParallel) -> None:
        response_stream = await async_client.responses.create(
            input="What are the latest developments in fusion energy?",
            model="parallel",
            stream=True,
            background=True,
            data_sources={
                "excluded": ["string"],
                "free": ["string"],
                "pay_per_use": ["string"],
            },
            instructions="instructions",
            metadata={"foo": "string"},
            previous_response_id="previous_response_id",
            reasoning={"effort": "high"},
            text={
                "format": {"type": "text"},
                "verbosity": "low",
            },
            tools=[
                {
                    "type": "web_search",
                    "filters": {
                        "allowed_domains": ["string"],
                        "blocked_domains": ["string"],
                    },
                    "search_context_size": "low",
                    "user_location": {
                        "city": "city",
                        "country": "country",
                        "region": "region",
                        "timezone": "timezone",
                        "type": "approximate",
                    },
                }
            ],
        )
        await response_stream.response.aclose()

    @parametrize
    async def test_raw_response_create_overload_2(self, async_client: AsyncParallel) -> None:
        response = await async_client.responses.with_raw_response.create(
            input="What are the latest developments in fusion energy?",
            model="parallel",
            stream=True,
        )

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = await response.parse()
        await stream.close()

    @parametrize
    async def test_streaming_response_create_overload_2(self, async_client: AsyncParallel) -> None:
        async with async_client.responses.with_streaming_response.create(
            input="What are the latest developments in fusion energy?",
            model="parallel",
            stream=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = await response.parse()
            await stream.close()

        assert cast(Any, response.is_closed) is True
