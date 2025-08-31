# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from parallel import Parallel, AsyncParallel
from tests.utils import assert_matches_type
from parallel.types.beta import (
    TaskGroup,
    TaskGroupRunResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTaskGroup:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Parallel) -> None:
        task_group = client.beta.task_group.create()
        assert_matches_type(TaskGroup, task_group, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Parallel) -> None:
        task_group = client.beta.task_group.create(
            metadata={"foo": "string"},
        )
        assert_matches_type(TaskGroup, task_group, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Parallel) -> None:
        response = client.beta.task_group.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task_group = response.parse()
        assert_matches_type(TaskGroup, task_group, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Parallel) -> None:
        with client.beta.task_group.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task_group = response.parse()
            assert_matches_type(TaskGroup, task_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Parallel) -> None:
        task_group = client.beta.task_group.retrieve(
            "taskgroup_id",
        )
        assert_matches_type(TaskGroup, task_group, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Parallel) -> None:
        response = client.beta.task_group.with_raw_response.retrieve(
            "taskgroup_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task_group = response.parse()
        assert_matches_type(TaskGroup, task_group, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Parallel) -> None:
        with client.beta.task_group.with_streaming_response.retrieve(
            "taskgroup_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task_group = response.parse()
            assert_matches_type(TaskGroup, task_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Parallel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `task_group_id` but received ''"):
            client.beta.task_group.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_add_runs(self, client: Parallel) -> None:
        task_group = client.beta.task_group.add_runs(
            task_group_id="taskgroup_id",
            inputs=[
                {
                    "input": "What was the GDP of France in 2023?",
                    "processor": "base",
                }
            ],
        )
        assert_matches_type(TaskGroupRunResponse, task_group, path=["response"])

    @parametrize
    def test_method_add_runs_with_all_params(self, client: Parallel) -> None:
        task_group = client.beta.task_group.add_runs(
            task_group_id="taskgroup_id",
            inputs=[
                {
                    "input": "What was the GDP of France in 2023?",
                    "processor": "base",
                    "enable_events": True,
                    "mcp_servers": [
                        {
                            "name": "name",
                            "url": "url",
                            "allowed_tools": ["string"],
                            "headers": {"foo": "string"},
                            "type": "url",
                        }
                    ],
                    "metadata": {"foo": "string"},
                    "source_policy": {
                        "exclude_domains": ["string"],
                        "include_domains": ["string"],
                    },
                    "task_spec": {
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
                    "webhook": {
                        "url": "url",
                        "event_types": ["task_run.status"],
                    },
                }
            ],
            default_task_spec={
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
            betas=["mcp-server-2025-07-17"],
        )
        assert_matches_type(TaskGroupRunResponse, task_group, path=["response"])

    @parametrize
    def test_raw_response_add_runs(self, client: Parallel) -> None:
        response = client.beta.task_group.with_raw_response.add_runs(
            task_group_id="taskgroup_id",
            inputs=[
                {
                    "input": "What was the GDP of France in 2023?",
                    "processor": "base",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task_group = response.parse()
        assert_matches_type(TaskGroupRunResponse, task_group, path=["response"])

    @parametrize
    def test_streaming_response_add_runs(self, client: Parallel) -> None:
        with client.beta.task_group.with_streaming_response.add_runs(
            task_group_id="taskgroup_id",
            inputs=[
                {
                    "input": "What was the GDP of France in 2023?",
                    "processor": "base",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task_group = response.parse()
            assert_matches_type(TaskGroupRunResponse, task_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_add_runs(self, client: Parallel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `task_group_id` but received ''"):
            client.beta.task_group.with_raw_response.add_runs(
                task_group_id="",
                inputs=[
                    {
                        "input": "What was the GDP of France in 2023?",
                        "processor": "base",
                    }
                ],
            )

    @pytest.mark.skip(reason="Prism doesn't support text/event-stream responses")
    @parametrize
    def test_method_events(self, client: Parallel) -> None:
        task_group_stream = client.beta.task_group.events(
            task_group_id="taskgroup_id",
        )
        task_group_stream.response.close()

    @pytest.mark.skip(reason="Prism doesn't support text/event-stream responses")
    @parametrize
    def test_method_events_with_all_params(self, client: Parallel) -> None:
        task_group_stream = client.beta.task_group.events(
            task_group_id="taskgroup_id",
            last_event_id="last_event_id",
            api_timeout=0,
        )
        task_group_stream.response.close()

    @pytest.mark.skip(reason="Prism doesn't support text/event-stream responses")
    @parametrize
    def test_raw_response_events(self, client: Parallel) -> None:
        response = client.beta.task_group.with_raw_response.events(
            task_group_id="taskgroup_id",
        )

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = response.parse()
        stream.close()

    @pytest.mark.skip(reason="Prism doesn't support text/event-stream responses")
    @parametrize
    def test_streaming_response_events(self, client: Parallel) -> None:
        with client.beta.task_group.with_streaming_response.events(
            task_group_id="taskgroup_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = response.parse()
            stream.close()

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism doesn't support text/event-stream responses")
    @parametrize
    def test_path_params_events(self, client: Parallel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `task_group_id` but received ''"):
            client.beta.task_group.with_raw_response.events(
                task_group_id="",
            )

    @pytest.mark.skip(reason="Prism doesn't support text/event-stream responses")
    @parametrize
    def test_method_get_runs(self, client: Parallel) -> None:
        task_group_stream = client.beta.task_group.get_runs(
            task_group_id="taskgroup_id",
        )
        task_group_stream.response.close()

    @pytest.mark.skip(reason="Prism doesn't support text/event-stream responses")
    @parametrize
    def test_method_get_runs_with_all_params(self, client: Parallel) -> None:
        task_group_stream = client.beta.task_group.get_runs(
            task_group_id="taskgroup_id",
            include_input=True,
            include_output=True,
            last_event_id="last_event_id",
            status="queued",
        )
        task_group_stream.response.close()

    @pytest.mark.skip(reason="Prism doesn't support text/event-stream responses")
    @parametrize
    def test_raw_response_get_runs(self, client: Parallel) -> None:
        response = client.beta.task_group.with_raw_response.get_runs(
            task_group_id="taskgroup_id",
        )

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = response.parse()
        stream.close()

    @pytest.mark.skip(reason="Prism doesn't support text/event-stream responses")
    @parametrize
    def test_streaming_response_get_runs(self, client: Parallel) -> None:
        with client.beta.task_group.with_streaming_response.get_runs(
            task_group_id="taskgroup_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = response.parse()
            stream.close()

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism doesn't support text/event-stream responses")
    @parametrize
    def test_path_params_get_runs(self, client: Parallel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `task_group_id` but received ''"):
            client.beta.task_group.with_raw_response.get_runs(
                task_group_id="",
            )


class TestAsyncTaskGroup:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncParallel) -> None:
        task_group = await async_client.beta.task_group.create()
        assert_matches_type(TaskGroup, task_group, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncParallel) -> None:
        task_group = await async_client.beta.task_group.create(
            metadata={"foo": "string"},
        )
        assert_matches_type(TaskGroup, task_group, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncParallel) -> None:
        response = await async_client.beta.task_group.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task_group = await response.parse()
        assert_matches_type(TaskGroup, task_group, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncParallel) -> None:
        async with async_client.beta.task_group.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task_group = await response.parse()
            assert_matches_type(TaskGroup, task_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncParallel) -> None:
        task_group = await async_client.beta.task_group.retrieve(
            "taskgroup_id",
        )
        assert_matches_type(TaskGroup, task_group, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncParallel) -> None:
        response = await async_client.beta.task_group.with_raw_response.retrieve(
            "taskgroup_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task_group = await response.parse()
        assert_matches_type(TaskGroup, task_group, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncParallel) -> None:
        async with async_client.beta.task_group.with_streaming_response.retrieve(
            "taskgroup_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task_group = await response.parse()
            assert_matches_type(TaskGroup, task_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncParallel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `task_group_id` but received ''"):
            await async_client.beta.task_group.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_add_runs(self, async_client: AsyncParallel) -> None:
        task_group = await async_client.beta.task_group.add_runs(
            task_group_id="taskgroup_id",
            inputs=[
                {
                    "input": "What was the GDP of France in 2023?",
                    "processor": "base",
                }
            ],
        )
        assert_matches_type(TaskGroupRunResponse, task_group, path=["response"])

    @parametrize
    async def test_method_add_runs_with_all_params(self, async_client: AsyncParallel) -> None:
        task_group = await async_client.beta.task_group.add_runs(
            task_group_id="taskgroup_id",
            inputs=[
                {
                    "input": "What was the GDP of France in 2023?",
                    "processor": "base",
                    "enable_events": True,
                    "mcp_servers": [
                        {
                            "name": "name",
                            "url": "url",
                            "allowed_tools": ["string"],
                            "headers": {"foo": "string"},
                            "type": "url",
                        }
                    ],
                    "metadata": {"foo": "string"},
                    "source_policy": {
                        "exclude_domains": ["string"],
                        "include_domains": ["string"],
                    },
                    "task_spec": {
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
                    "webhook": {
                        "url": "url",
                        "event_types": ["task_run.status"],
                    },
                }
            ],
            default_task_spec={
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
            betas=["mcp-server-2025-07-17"],
        )
        assert_matches_type(TaskGroupRunResponse, task_group, path=["response"])

    @parametrize
    async def test_raw_response_add_runs(self, async_client: AsyncParallel) -> None:
        response = await async_client.beta.task_group.with_raw_response.add_runs(
            task_group_id="taskgroup_id",
            inputs=[
                {
                    "input": "What was the GDP of France in 2023?",
                    "processor": "base",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task_group = await response.parse()
        assert_matches_type(TaskGroupRunResponse, task_group, path=["response"])

    @parametrize
    async def test_streaming_response_add_runs(self, async_client: AsyncParallel) -> None:
        async with async_client.beta.task_group.with_streaming_response.add_runs(
            task_group_id="taskgroup_id",
            inputs=[
                {
                    "input": "What was the GDP of France in 2023?",
                    "processor": "base",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task_group = await response.parse()
            assert_matches_type(TaskGroupRunResponse, task_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_add_runs(self, async_client: AsyncParallel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `task_group_id` but received ''"):
            await async_client.beta.task_group.with_raw_response.add_runs(
                task_group_id="",
                inputs=[
                    {
                        "input": "What was the GDP of France in 2023?",
                        "processor": "base",
                    }
                ],
            )

    @pytest.mark.skip(reason="Prism doesn't support text/event-stream responses")
    @parametrize
    async def test_method_events(self, async_client: AsyncParallel) -> None:
        task_group_stream = await async_client.beta.task_group.events(
            task_group_id="taskgroup_id",
        )
        await task_group_stream.response.aclose()

    @pytest.mark.skip(reason="Prism doesn't support text/event-stream responses")
    @parametrize
    async def test_method_events_with_all_params(self, async_client: AsyncParallel) -> None:
        task_group_stream = await async_client.beta.task_group.events(
            task_group_id="taskgroup_id",
            last_event_id="last_event_id",
            api_timeout=0,
        )
        await task_group_stream.response.aclose()

    @pytest.mark.skip(reason="Prism doesn't support text/event-stream responses")
    @parametrize
    async def test_raw_response_events(self, async_client: AsyncParallel) -> None:
        response = await async_client.beta.task_group.with_raw_response.events(
            task_group_id="taskgroup_id",
        )

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = await response.parse()
        await stream.close()

    @pytest.mark.skip(reason="Prism doesn't support text/event-stream responses")
    @parametrize
    async def test_streaming_response_events(self, async_client: AsyncParallel) -> None:
        async with async_client.beta.task_group.with_streaming_response.events(
            task_group_id="taskgroup_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = await response.parse()
            await stream.close()

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism doesn't support text/event-stream responses")
    @parametrize
    async def test_path_params_events(self, async_client: AsyncParallel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `task_group_id` but received ''"):
            await async_client.beta.task_group.with_raw_response.events(
                task_group_id="",
            )

    @pytest.mark.skip(reason="Prism doesn't support text/event-stream responses")
    @parametrize
    async def test_method_get_runs(self, async_client: AsyncParallel) -> None:
        task_group_stream = await async_client.beta.task_group.get_runs(
            task_group_id="taskgroup_id",
        )
        await task_group_stream.response.aclose()

    @pytest.mark.skip(reason="Prism doesn't support text/event-stream responses")
    @parametrize
    async def test_method_get_runs_with_all_params(self, async_client: AsyncParallel) -> None:
        task_group_stream = await async_client.beta.task_group.get_runs(
            task_group_id="taskgroup_id",
            include_input=True,
            include_output=True,
            last_event_id="last_event_id",
            status="queued",
        )
        await task_group_stream.response.aclose()

    @pytest.mark.skip(reason="Prism doesn't support text/event-stream responses")
    @parametrize
    async def test_raw_response_get_runs(self, async_client: AsyncParallel) -> None:
        response = await async_client.beta.task_group.with_raw_response.get_runs(
            task_group_id="taskgroup_id",
        )

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = await response.parse()
        await stream.close()

    @pytest.mark.skip(reason="Prism doesn't support text/event-stream responses")
    @parametrize
    async def test_streaming_response_get_runs(self, async_client: AsyncParallel) -> None:
        async with async_client.beta.task_group.with_streaming_response.get_runs(
            task_group_id="taskgroup_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = await response.parse()
            await stream.close()

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism doesn't support text/event-stream responses")
    @parametrize
    async def test_path_params_get_runs(self, async_client: AsyncParallel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `task_group_id` but received ''"):
            await async_client.beta.task_group.with_raw_response.get_runs(
                task_group_id="",
            )
