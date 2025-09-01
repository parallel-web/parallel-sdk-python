# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from parallel import Parallel, AsyncParallel
from tests.utils import assert_matches_type
from parallel.types import TaskRun, TaskRunResult

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTaskRun:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Parallel) -> None:
        task_run = client.task_run.create(
            input="What was the GDP of France in 2023?",
            processor="base",
        )
        assert_matches_type(TaskRun, task_run, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Parallel) -> None:
        task_run = client.task_run.create(
            input="What was the GDP of France in 2023?",
            processor="base",
            metadata={"foo": "string"},
            source_policy={
                "exclude_domains": ["string"],
                "include_domains": ["string"],
            },
            task_spec={
                "output_schema": {
                    "json_schema": {
                        "additionalProperties": "bar",
                        "properties": "bar",
                        "required": "bar",
                        "type": "bar",
                    },
                    "type": "json",
                },
                "input_schema": "string",
            },
        )
        assert_matches_type(TaskRun, task_run, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Parallel) -> None:
        response = client.task_run.with_raw_response.create(
            input="What was the GDP of France in 2023?",
            processor="base",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task_run = response.parse()
        assert_matches_type(TaskRun, task_run, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Parallel) -> None:
        with client.task_run.with_streaming_response.create(
            input="What was the GDP of France in 2023?",
            processor="base",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task_run = response.parse()
            assert_matches_type(TaskRun, task_run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Parallel) -> None:
        task_run = client.task_run.retrieve(
            "run_id",
        )
        assert_matches_type(TaskRun, task_run, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Parallel) -> None:
        response = client.task_run.with_raw_response.retrieve(
            "run_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task_run = response.parse()
        assert_matches_type(TaskRun, task_run, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Parallel) -> None:
        with client.task_run.with_streaming_response.retrieve(
            "run_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task_run = response.parse()
            assert_matches_type(TaskRun, task_run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Parallel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            client.task_run.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_result(self, client: Parallel) -> None:
        task_run = client.task_run.result(
            run_id="run_id",
        )
        assert_matches_type(TaskRunResult, task_run, path=["response"])

    @parametrize
    def test_method_result_with_all_params(self, client: Parallel) -> None:
        task_run = client.task_run.result(
            run_id="run_id",
            api_timeout=0,
        )
        assert_matches_type(TaskRunResult, task_run, path=["response"])

    @parametrize
    def test_raw_response_result(self, client: Parallel) -> None:
        response = client.task_run.with_raw_response.result(
            run_id="run_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task_run = response.parse()
        assert_matches_type(TaskRunResult, task_run, path=["response"])

    @parametrize
    def test_streaming_response_result(self, client: Parallel) -> None:
        with client.task_run.with_streaming_response.result(
            run_id="run_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task_run = response.parse()
            assert_matches_type(TaskRunResult, task_run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_result(self, client: Parallel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            client.task_run.with_raw_response.result(
                run_id="",
            )


class TestAsyncTaskRun:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncParallel) -> None:
        task_run = await async_client.task_run.create(
            input="What was the GDP of France in 2023?",
            processor="base",
        )
        assert_matches_type(TaskRun, task_run, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncParallel) -> None:
        task_run = await async_client.task_run.create(
            input="What was the GDP of France in 2023?",
            processor="base",
            metadata={"foo": "string"},
            source_policy={
                "exclude_domains": ["string"],
                "include_domains": ["string"],
            },
            task_spec={
                "output_schema": {
                    "json_schema": {
                        "additionalProperties": "bar",
                        "properties": "bar",
                        "required": "bar",
                        "type": "bar",
                    },
                    "type": "json",
                },
                "input_schema": "string",
            },
        )
        assert_matches_type(TaskRun, task_run, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncParallel) -> None:
        response = await async_client.task_run.with_raw_response.create(
            input="What was the GDP of France in 2023?",
            processor="base",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task_run = await response.parse()
        assert_matches_type(TaskRun, task_run, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncParallel) -> None:
        async with async_client.task_run.with_streaming_response.create(
            input="What was the GDP of France in 2023?",
            processor="base",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task_run = await response.parse()
            assert_matches_type(TaskRun, task_run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncParallel) -> None:
        task_run = await async_client.task_run.retrieve(
            "run_id",
        )
        assert_matches_type(TaskRun, task_run, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncParallel) -> None:
        response = await async_client.task_run.with_raw_response.retrieve(
            "run_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task_run = await response.parse()
        assert_matches_type(TaskRun, task_run, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncParallel) -> None:
        async with async_client.task_run.with_streaming_response.retrieve(
            "run_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task_run = await response.parse()
            assert_matches_type(TaskRun, task_run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncParallel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            await async_client.task_run.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_result(self, async_client: AsyncParallel) -> None:
        task_run = await async_client.task_run.result(
            run_id="run_id",
        )
        assert_matches_type(TaskRunResult, task_run, path=["response"])

    @parametrize
    async def test_method_result_with_all_params(self, async_client: AsyncParallel) -> None:
        task_run = await async_client.task_run.result(
            run_id="run_id",
            api_timeout=0,
        )
        assert_matches_type(TaskRunResult, task_run, path=["response"])

    @parametrize
    async def test_raw_response_result(self, async_client: AsyncParallel) -> None:
        response = await async_client.task_run.with_raw_response.result(
            run_id="run_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task_run = await response.parse()
        assert_matches_type(TaskRunResult, task_run, path=["response"])

    @parametrize
    async def test_streaming_response_result(self, async_client: AsyncParallel) -> None:
        async with async_client.task_run.with_streaming_response.result(
            run_id="run_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task_run = await response.parse()
            assert_matches_type(TaskRunResult, task_run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_result(self, async_client: AsyncParallel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            await async_client.task_run.with_raw_response.result(
                run_id="",
            )
