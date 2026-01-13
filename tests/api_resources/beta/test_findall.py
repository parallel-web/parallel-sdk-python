# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from parallel import Parallel, AsyncParallel
from tests.utils import assert_matches_type
from parallel.types.beta import (
    FindAllRun,
    FindAllSchema,
    FindAllRunResult,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFindAll:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Parallel) -> None:
        findall = client.beta.findall.create(
            entity_type="entity_type",
            generator="base",
            match_conditions=[
                {
                    "description": "Company must have SOC2 Type II certification (not Type I). Look for evidence in: trust centers, security/compliance pages, audit reports, or press releases specifically mentioning 'SOC2 Type II'. If no explicit SOC2 Type II mention is found, consider requirement not satisfied.",
                    "name": "name",
                }
            ],
            match_limit=0,
            objective="objective",
        )
        assert_matches_type(FindAllRun, findall, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Parallel) -> None:
        findall = client.beta.findall.create(
            entity_type="entity_type",
            generator="base",
            match_conditions=[
                {
                    "description": "Company must have SOC2 Type II certification (not Type I). Look for evidence in: trust centers, security/compliance pages, audit reports, or press releases specifically mentioning 'SOC2 Type II'. If no explicit SOC2 Type II mention is found, consider requirement not satisfied.",
                    "name": "name",
                }
            ],
            match_limit=0,
            objective="objective",
            exclude_list=[
                {
                    "name": "name",
                    "url": "url",
                }
            ],
            metadata={"foo": "string"},
            webhook={
                "url": "url",
                "event_types": ["task_run.status"],
            },
            betas=["mcp-server-2025-07-17"],
        )
        assert_matches_type(FindAllRun, findall, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Parallel) -> None:
        response = client.beta.findall.with_raw_response.create(
            entity_type="entity_type",
            generator="base",
            match_conditions=[
                {
                    "description": "Company must have SOC2 Type II certification (not Type I). Look for evidence in: trust centers, security/compliance pages, audit reports, or press releases specifically mentioning 'SOC2 Type II'. If no explicit SOC2 Type II mention is found, consider requirement not satisfied.",
                    "name": "name",
                }
            ],
            match_limit=0,
            objective="objective",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        findall = response.parse()
        assert_matches_type(FindAllRun, findall, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Parallel) -> None:
        with client.beta.findall.with_streaming_response.create(
            entity_type="entity_type",
            generator="base",
            match_conditions=[
                {
                    "description": "Company must have SOC2 Type II certification (not Type I). Look for evidence in: trust centers, security/compliance pages, audit reports, or press releases specifically mentioning 'SOC2 Type II'. If no explicit SOC2 Type II mention is found, consider requirement not satisfied.",
                    "name": "name",
                }
            ],
            match_limit=0,
            objective="objective",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            findall = response.parse()
            assert_matches_type(FindAllRun, findall, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Parallel) -> None:
        findall = client.beta.findall.retrieve(
            findall_id="findall_id",
        )
        assert_matches_type(FindAllRun, findall, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Parallel) -> None:
        findall = client.beta.findall.retrieve(
            findall_id="findall_id",
            betas=["mcp-server-2025-07-17"],
        )
        assert_matches_type(FindAllRun, findall, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Parallel) -> None:
        response = client.beta.findall.with_raw_response.retrieve(
            findall_id="findall_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        findall = response.parse()
        assert_matches_type(FindAllRun, findall, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Parallel) -> None:
        with client.beta.findall.with_streaming_response.retrieve(
            findall_id="findall_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            findall = response.parse()
            assert_matches_type(FindAllRun, findall, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Parallel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `findall_id` but received ''"):
            client.beta.findall.with_raw_response.retrieve(
                findall_id="",
            )

    @parametrize
    def test_method_cancel(self, client: Parallel) -> None:
        findall = client.beta.findall.cancel(
            findall_id="findall_id",
        )
        assert_matches_type(object, findall, path=["response"])

    @parametrize
    def test_method_cancel_with_all_params(self, client: Parallel) -> None:
        findall = client.beta.findall.cancel(
            findall_id="findall_id",
            betas=["mcp-server-2025-07-17"],
        )
        assert_matches_type(object, findall, path=["response"])

    @parametrize
    def test_raw_response_cancel(self, client: Parallel) -> None:
        response = client.beta.findall.with_raw_response.cancel(
            findall_id="findall_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        findall = response.parse()
        assert_matches_type(object, findall, path=["response"])

    @parametrize
    def test_streaming_response_cancel(self, client: Parallel) -> None:
        with client.beta.findall.with_streaming_response.cancel(
            findall_id="findall_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            findall = response.parse()
            assert_matches_type(object, findall, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_cancel(self, client: Parallel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `findall_id` but received ''"):
            client.beta.findall.with_raw_response.cancel(
                findall_id="",
            )

    @parametrize
    def test_method_enrich(self, client: Parallel) -> None:
        findall = client.beta.findall.enrich(
            findall_id="findall_id",
            output_schema={
                "json_schema": {
                    "additionalProperties": "bar",
                    "properties": "bar",
                    "required": "bar",
                    "type": "bar",
                }
            },
        )
        assert_matches_type(FindAllSchema, findall, path=["response"])

    @parametrize
    def test_method_enrich_with_all_params(self, client: Parallel) -> None:
        findall = client.beta.findall.enrich(
            findall_id="findall_id",
            output_schema={
                "json_schema": {
                    "additionalProperties": "bar",
                    "properties": "bar",
                    "required": "bar",
                    "type": "bar",
                },
                "type": "json",
            },
            mcp_servers=[
                {
                    "name": "name",
                    "url": "url",
                    "allowed_tools": ["string"],
                    "headers": {"foo": "string"},
                    "type": "url",
                }
            ],
            processor="processor",
            betas=["mcp-server-2025-07-17"],
        )
        assert_matches_type(FindAllSchema, findall, path=["response"])

    @parametrize
    def test_raw_response_enrich(self, client: Parallel) -> None:
        response = client.beta.findall.with_raw_response.enrich(
            findall_id="findall_id",
            output_schema={
                "json_schema": {
                    "additionalProperties": "bar",
                    "properties": "bar",
                    "required": "bar",
                    "type": "bar",
                }
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        findall = response.parse()
        assert_matches_type(FindAllSchema, findall, path=["response"])

    @parametrize
    def test_streaming_response_enrich(self, client: Parallel) -> None:
        with client.beta.findall.with_streaming_response.enrich(
            findall_id="findall_id",
            output_schema={
                "json_schema": {
                    "additionalProperties": "bar",
                    "properties": "bar",
                    "required": "bar",
                    "type": "bar",
                }
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            findall = response.parse()
            assert_matches_type(FindAllSchema, findall, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_enrich(self, client: Parallel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `findall_id` but received ''"):
            client.beta.findall.with_raw_response.enrich(
                findall_id="",
                output_schema={
                    "json_schema": {
                        "additionalProperties": "bar",
                        "properties": "bar",
                        "required": "bar",
                        "type": "bar",
                    }
                },
            )

    @pytest.mark.skip(reason="Prism doesn't support text/event-stream responses")
    @parametrize
    def test_method_events(self, client: Parallel) -> None:
        findall_stream = client.beta.findall.events(
            findall_id="findall_id",
        )
        findall_stream.response.close()

    @pytest.mark.skip(reason="Prism doesn't support text/event-stream responses")
    @parametrize
    def test_method_events_with_all_params(self, client: Parallel) -> None:
        findall_stream = client.beta.findall.events(
            findall_id="findall_id",
            last_event_id="last_event_id",
            api_timeout=0,
            betas=["mcp-server-2025-07-17"],
        )
        findall_stream.response.close()

    @pytest.mark.skip(reason="Prism doesn't support text/event-stream responses")
    @parametrize
    def test_raw_response_events(self, client: Parallel) -> None:
        response = client.beta.findall.with_raw_response.events(
            findall_id="findall_id",
        )

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = response.parse()
        stream.close()

    @pytest.mark.skip(reason="Prism doesn't support text/event-stream responses")
    @parametrize
    def test_streaming_response_events(self, client: Parallel) -> None:
        with client.beta.findall.with_streaming_response.events(
            findall_id="findall_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = response.parse()
            stream.close()

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism doesn't support text/event-stream responses")
    @parametrize
    def test_path_params_events(self, client: Parallel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `findall_id` but received ''"):
            client.beta.findall.with_raw_response.events(
                findall_id="",
            )

    @parametrize
    def test_method_extend(self, client: Parallel) -> None:
        findall = client.beta.findall.extend(
            findall_id="findall_id",
            additional_match_limit=0,
        )
        assert_matches_type(FindAllSchema, findall, path=["response"])

    @parametrize
    def test_method_extend_with_all_params(self, client: Parallel) -> None:
        findall = client.beta.findall.extend(
            findall_id="findall_id",
            additional_match_limit=0,
            betas=["mcp-server-2025-07-17"],
        )
        assert_matches_type(FindAllSchema, findall, path=["response"])

    @parametrize
    def test_raw_response_extend(self, client: Parallel) -> None:
        response = client.beta.findall.with_raw_response.extend(
            findall_id="findall_id",
            additional_match_limit=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        findall = response.parse()
        assert_matches_type(FindAllSchema, findall, path=["response"])

    @parametrize
    def test_streaming_response_extend(self, client: Parallel) -> None:
        with client.beta.findall.with_streaming_response.extend(
            findall_id="findall_id",
            additional_match_limit=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            findall = response.parse()
            assert_matches_type(FindAllSchema, findall, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_extend(self, client: Parallel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `findall_id` but received ''"):
            client.beta.findall.with_raw_response.extend(
                findall_id="",
                additional_match_limit=0,
            )

    @parametrize
    def test_method_ingest(self, client: Parallel) -> None:
        findall = client.beta.findall.ingest(
            objective="Find all AI companies that raised Series A funding in 2024",
        )
        assert_matches_type(FindAllSchema, findall, path=["response"])

    @parametrize
    def test_method_ingest_with_all_params(self, client: Parallel) -> None:
        findall = client.beta.findall.ingest(
            objective="Find all AI companies that raised Series A funding in 2024",
            betas=["mcp-server-2025-07-17"],
        )
        assert_matches_type(FindAllSchema, findall, path=["response"])

    @parametrize
    def test_raw_response_ingest(self, client: Parallel) -> None:
        response = client.beta.findall.with_raw_response.ingest(
            objective="Find all AI companies that raised Series A funding in 2024",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        findall = response.parse()
        assert_matches_type(FindAllSchema, findall, path=["response"])

    @parametrize
    def test_streaming_response_ingest(self, client: Parallel) -> None:
        with client.beta.findall.with_streaming_response.ingest(
            objective="Find all AI companies that raised Series A funding in 2024",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            findall = response.parse()
            assert_matches_type(FindAllSchema, findall, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_result(self, client: Parallel) -> None:
        findall = client.beta.findall.result(
            findall_id="findall_id",
        )
        assert_matches_type(FindAllRunResult, findall, path=["response"])

    @parametrize
    def test_method_result_with_all_params(self, client: Parallel) -> None:
        findall = client.beta.findall.result(
            findall_id="findall_id",
            betas=["mcp-server-2025-07-17"],
        )
        assert_matches_type(FindAllRunResult, findall, path=["response"])

    @parametrize
    def test_raw_response_result(self, client: Parallel) -> None:
        response = client.beta.findall.with_raw_response.result(
            findall_id="findall_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        findall = response.parse()
        assert_matches_type(FindAllRunResult, findall, path=["response"])

    @parametrize
    def test_streaming_response_result(self, client: Parallel) -> None:
        with client.beta.findall.with_streaming_response.result(
            findall_id="findall_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            findall = response.parse()
            assert_matches_type(FindAllRunResult, findall, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_result(self, client: Parallel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `findall_id` but received ''"):
            client.beta.findall.with_raw_response.result(
                findall_id="",
            )

    @parametrize
    def test_method_schema(self, client: Parallel) -> None:
        findall = client.beta.findall.schema(
            findall_id="findall_id",
        )
        assert_matches_type(FindAllSchema, findall, path=["response"])

    @parametrize
    def test_method_schema_with_all_params(self, client: Parallel) -> None:
        findall = client.beta.findall.schema(
            findall_id="findall_id",
            betas=["mcp-server-2025-07-17"],
        )
        assert_matches_type(FindAllSchema, findall, path=["response"])

    @parametrize
    def test_raw_response_schema(self, client: Parallel) -> None:
        response = client.beta.findall.with_raw_response.schema(
            findall_id="findall_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        findall = response.parse()
        assert_matches_type(FindAllSchema, findall, path=["response"])

    @parametrize
    def test_streaming_response_schema(self, client: Parallel) -> None:
        with client.beta.findall.with_streaming_response.schema(
            findall_id="findall_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            findall = response.parse()
            assert_matches_type(FindAllSchema, findall, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_schema(self, client: Parallel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `findall_id` but received ''"):
            client.beta.findall.with_raw_response.schema(
                findall_id="",
            )


class TestAsyncFindAll:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncParallel) -> None:
        findall = await async_client.beta.findall.create(
            entity_type="entity_type",
            generator="base",
            match_conditions=[
                {
                    "description": "Company must have SOC2 Type II certification (not Type I). Look for evidence in: trust centers, security/compliance pages, audit reports, or press releases specifically mentioning 'SOC2 Type II'. If no explicit SOC2 Type II mention is found, consider requirement not satisfied.",
                    "name": "name",
                }
            ],
            match_limit=0,
            objective="objective",
        )
        assert_matches_type(FindAllRun, findall, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncParallel) -> None:
        findall = await async_client.beta.findall.create(
            entity_type="entity_type",
            generator="base",
            match_conditions=[
                {
                    "description": "Company must have SOC2 Type II certification (not Type I). Look for evidence in: trust centers, security/compliance pages, audit reports, or press releases specifically mentioning 'SOC2 Type II'. If no explicit SOC2 Type II mention is found, consider requirement not satisfied.",
                    "name": "name",
                }
            ],
            match_limit=0,
            objective="objective",
            exclude_list=[
                {
                    "name": "name",
                    "url": "url",
                }
            ],
            metadata={"foo": "string"},
            webhook={
                "url": "url",
                "event_types": ["task_run.status"],
            },
            betas=["mcp-server-2025-07-17"],
        )
        assert_matches_type(FindAllRun, findall, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncParallel) -> None:
        response = await async_client.beta.findall.with_raw_response.create(
            entity_type="entity_type",
            generator="base",
            match_conditions=[
                {
                    "description": "Company must have SOC2 Type II certification (not Type I). Look for evidence in: trust centers, security/compliance pages, audit reports, or press releases specifically mentioning 'SOC2 Type II'. If no explicit SOC2 Type II mention is found, consider requirement not satisfied.",
                    "name": "name",
                }
            ],
            match_limit=0,
            objective="objective",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        findall = await response.parse()
        assert_matches_type(FindAllRun, findall, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncParallel) -> None:
        async with async_client.beta.findall.with_streaming_response.create(
            entity_type="entity_type",
            generator="base",
            match_conditions=[
                {
                    "description": "Company must have SOC2 Type II certification (not Type I). Look for evidence in: trust centers, security/compliance pages, audit reports, or press releases specifically mentioning 'SOC2 Type II'. If no explicit SOC2 Type II mention is found, consider requirement not satisfied.",
                    "name": "name",
                }
            ],
            match_limit=0,
            objective="objective",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            findall = await response.parse()
            assert_matches_type(FindAllRun, findall, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncParallel) -> None:
        findall = await async_client.beta.findall.retrieve(
            findall_id="findall_id",
        )
        assert_matches_type(FindAllRun, findall, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncParallel) -> None:
        findall = await async_client.beta.findall.retrieve(
            findall_id="findall_id",
            betas=["mcp-server-2025-07-17"],
        )
        assert_matches_type(FindAllRun, findall, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncParallel) -> None:
        response = await async_client.beta.findall.with_raw_response.retrieve(
            findall_id="findall_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        findall = await response.parse()
        assert_matches_type(FindAllRun, findall, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncParallel) -> None:
        async with async_client.beta.findall.with_streaming_response.retrieve(
            findall_id="findall_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            findall = await response.parse()
            assert_matches_type(FindAllRun, findall, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncParallel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `findall_id` but received ''"):
            await async_client.beta.findall.with_raw_response.retrieve(
                findall_id="",
            )

    @parametrize
    async def test_method_cancel(self, async_client: AsyncParallel) -> None:
        findall = await async_client.beta.findall.cancel(
            findall_id="findall_id",
        )
        assert_matches_type(object, findall, path=["response"])

    @parametrize
    async def test_method_cancel_with_all_params(self, async_client: AsyncParallel) -> None:
        findall = await async_client.beta.findall.cancel(
            findall_id="findall_id",
            betas=["mcp-server-2025-07-17"],
        )
        assert_matches_type(object, findall, path=["response"])

    @parametrize
    async def test_raw_response_cancel(self, async_client: AsyncParallel) -> None:
        response = await async_client.beta.findall.with_raw_response.cancel(
            findall_id="findall_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        findall = await response.parse()
        assert_matches_type(object, findall, path=["response"])

    @parametrize
    async def test_streaming_response_cancel(self, async_client: AsyncParallel) -> None:
        async with async_client.beta.findall.with_streaming_response.cancel(
            findall_id="findall_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            findall = await response.parse()
            assert_matches_type(object, findall, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_cancel(self, async_client: AsyncParallel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `findall_id` but received ''"):
            await async_client.beta.findall.with_raw_response.cancel(
                findall_id="",
            )

    @parametrize
    async def test_method_enrich(self, async_client: AsyncParallel) -> None:
        findall = await async_client.beta.findall.enrich(
            findall_id="findall_id",
            output_schema={
                "json_schema": {
                    "additionalProperties": "bar",
                    "properties": "bar",
                    "required": "bar",
                    "type": "bar",
                }
            },
        )
        assert_matches_type(FindAllSchema, findall, path=["response"])

    @parametrize
    async def test_method_enrich_with_all_params(self, async_client: AsyncParallel) -> None:
        findall = await async_client.beta.findall.enrich(
            findall_id="findall_id",
            output_schema={
                "json_schema": {
                    "additionalProperties": "bar",
                    "properties": "bar",
                    "required": "bar",
                    "type": "bar",
                },
                "type": "json",
            },
            mcp_servers=[
                {
                    "name": "name",
                    "url": "url",
                    "allowed_tools": ["string"],
                    "headers": {"foo": "string"},
                    "type": "url",
                }
            ],
            processor="processor",
            betas=["mcp-server-2025-07-17"],
        )
        assert_matches_type(FindAllSchema, findall, path=["response"])

    @parametrize
    async def test_raw_response_enrich(self, async_client: AsyncParallel) -> None:
        response = await async_client.beta.findall.with_raw_response.enrich(
            findall_id="findall_id",
            output_schema={
                "json_schema": {
                    "additionalProperties": "bar",
                    "properties": "bar",
                    "required": "bar",
                    "type": "bar",
                }
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        findall = await response.parse()
        assert_matches_type(FindAllSchema, findall, path=["response"])

    @parametrize
    async def test_streaming_response_enrich(self, async_client: AsyncParallel) -> None:
        async with async_client.beta.findall.with_streaming_response.enrich(
            findall_id="findall_id",
            output_schema={
                "json_schema": {
                    "additionalProperties": "bar",
                    "properties": "bar",
                    "required": "bar",
                    "type": "bar",
                }
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            findall = await response.parse()
            assert_matches_type(FindAllSchema, findall, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_enrich(self, async_client: AsyncParallel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `findall_id` but received ''"):
            await async_client.beta.findall.with_raw_response.enrich(
                findall_id="",
                output_schema={
                    "json_schema": {
                        "additionalProperties": "bar",
                        "properties": "bar",
                        "required": "bar",
                        "type": "bar",
                    }
                },
            )

    @pytest.mark.skip(reason="Prism doesn't support text/event-stream responses")
    @parametrize
    async def test_method_events(self, async_client: AsyncParallel) -> None:
        findall_stream = await async_client.beta.findall.events(
            findall_id="findall_id",
        )
        await findall_stream.response.aclose()

    @pytest.mark.skip(reason="Prism doesn't support text/event-stream responses")
    @parametrize
    async def test_method_events_with_all_params(self, async_client: AsyncParallel) -> None:
        findall_stream = await async_client.beta.findall.events(
            findall_id="findall_id",
            last_event_id="last_event_id",
            api_timeout=0,
            betas=["mcp-server-2025-07-17"],
        )
        await findall_stream.response.aclose()

    @pytest.mark.skip(reason="Prism doesn't support text/event-stream responses")
    @parametrize
    async def test_raw_response_events(self, async_client: AsyncParallel) -> None:
        response = await async_client.beta.findall.with_raw_response.events(
            findall_id="findall_id",
        )

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = await response.parse()
        await stream.close()

    @pytest.mark.skip(reason="Prism doesn't support text/event-stream responses")
    @parametrize
    async def test_streaming_response_events(self, async_client: AsyncParallel) -> None:
        async with async_client.beta.findall.with_streaming_response.events(
            findall_id="findall_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = await response.parse()
            await stream.close()

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism doesn't support text/event-stream responses")
    @parametrize
    async def test_path_params_events(self, async_client: AsyncParallel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `findall_id` but received ''"):
            await async_client.beta.findall.with_raw_response.events(
                findall_id="",
            )

    @parametrize
    async def test_method_extend(self, async_client: AsyncParallel) -> None:
        findall = await async_client.beta.findall.extend(
            findall_id="findall_id",
            additional_match_limit=0,
        )
        assert_matches_type(FindAllSchema, findall, path=["response"])

    @parametrize
    async def test_method_extend_with_all_params(self, async_client: AsyncParallel) -> None:
        findall = await async_client.beta.findall.extend(
            findall_id="findall_id",
            additional_match_limit=0,
            betas=["mcp-server-2025-07-17"],
        )
        assert_matches_type(FindAllSchema, findall, path=["response"])

    @parametrize
    async def test_raw_response_extend(self, async_client: AsyncParallel) -> None:
        response = await async_client.beta.findall.with_raw_response.extend(
            findall_id="findall_id",
            additional_match_limit=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        findall = await response.parse()
        assert_matches_type(FindAllSchema, findall, path=["response"])

    @parametrize
    async def test_streaming_response_extend(self, async_client: AsyncParallel) -> None:
        async with async_client.beta.findall.with_streaming_response.extend(
            findall_id="findall_id",
            additional_match_limit=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            findall = await response.parse()
            assert_matches_type(FindAllSchema, findall, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_extend(self, async_client: AsyncParallel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `findall_id` but received ''"):
            await async_client.beta.findall.with_raw_response.extend(
                findall_id="",
                additional_match_limit=0,
            )

    @parametrize
    async def test_method_ingest(self, async_client: AsyncParallel) -> None:
        findall = await async_client.beta.findall.ingest(
            objective="Find all AI companies that raised Series A funding in 2024",
        )
        assert_matches_type(FindAllSchema, findall, path=["response"])

    @parametrize
    async def test_method_ingest_with_all_params(self, async_client: AsyncParallel) -> None:
        findall = await async_client.beta.findall.ingest(
            objective="Find all AI companies that raised Series A funding in 2024",
            betas=["mcp-server-2025-07-17"],
        )
        assert_matches_type(FindAllSchema, findall, path=["response"])

    @parametrize
    async def test_raw_response_ingest(self, async_client: AsyncParallel) -> None:
        response = await async_client.beta.findall.with_raw_response.ingest(
            objective="Find all AI companies that raised Series A funding in 2024",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        findall = await response.parse()
        assert_matches_type(FindAllSchema, findall, path=["response"])

    @parametrize
    async def test_streaming_response_ingest(self, async_client: AsyncParallel) -> None:
        async with async_client.beta.findall.with_streaming_response.ingest(
            objective="Find all AI companies that raised Series A funding in 2024",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            findall = await response.parse()
            assert_matches_type(FindAllSchema, findall, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_result(self, async_client: AsyncParallel) -> None:
        findall = await async_client.beta.findall.result(
            findall_id="findall_id",
        )
        assert_matches_type(FindAllRunResult, findall, path=["response"])

    @parametrize
    async def test_method_result_with_all_params(self, async_client: AsyncParallel) -> None:
        findall = await async_client.beta.findall.result(
            findall_id="findall_id",
            betas=["mcp-server-2025-07-17"],
        )
        assert_matches_type(FindAllRunResult, findall, path=["response"])

    @parametrize
    async def test_raw_response_result(self, async_client: AsyncParallel) -> None:
        response = await async_client.beta.findall.with_raw_response.result(
            findall_id="findall_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        findall = await response.parse()
        assert_matches_type(FindAllRunResult, findall, path=["response"])

    @parametrize
    async def test_streaming_response_result(self, async_client: AsyncParallel) -> None:
        async with async_client.beta.findall.with_streaming_response.result(
            findall_id="findall_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            findall = await response.parse()
            assert_matches_type(FindAllRunResult, findall, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_result(self, async_client: AsyncParallel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `findall_id` but received ''"):
            await async_client.beta.findall.with_raw_response.result(
                findall_id="",
            )

    @parametrize
    async def test_method_schema(self, async_client: AsyncParallel) -> None:
        findall = await async_client.beta.findall.schema(
            findall_id="findall_id",
        )
        assert_matches_type(FindAllSchema, findall, path=["response"])

    @parametrize
    async def test_method_schema_with_all_params(self, async_client: AsyncParallel) -> None:
        findall = await async_client.beta.findall.schema(
            findall_id="findall_id",
            betas=["mcp-server-2025-07-17"],
        )
        assert_matches_type(FindAllSchema, findall, path=["response"])

    @parametrize
    async def test_raw_response_schema(self, async_client: AsyncParallel) -> None:
        response = await async_client.beta.findall.with_raw_response.schema(
            findall_id="findall_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        findall = await response.parse()
        assert_matches_type(FindAllSchema, findall, path=["response"])

    @parametrize
    async def test_streaming_response_schema(self, async_client: AsyncParallel) -> None:
        async with async_client.beta.findall.with_streaming_response.schema(
            findall_id="findall_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            findall = await response.parse()
            assert_matches_type(FindAllSchema, findall, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_schema(self, async_client: AsyncParallel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `findall_id` but received ''"):
            await async_client.beta.findall.with_raw_response.schema(
                findall_id="",
            )
