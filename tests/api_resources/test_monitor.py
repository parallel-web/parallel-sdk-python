# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from parallel import Parallel, AsyncParallel
from tests.utils import assert_matches_type
from parallel.types import (
    Monitor,
    PaginatedMonitorEvents,
    PaginatedMonitorResponse,
)
from parallel._utils import parse_date

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMonitor:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Parallel) -> None:
        monitor = client.monitor.create(
            frequency="1h",
            settings={"query": "Extract recent news about AI"},
            type="event_stream",
        )
        assert_matches_type(Monitor, monitor, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Parallel) -> None:
        monitor = client.monitor.create(
            frequency="1h",
            settings={
                "query": "Extract recent news about AI",
                "advanced_settings": {
                    "location": "us",
                    "source_policy": {
                        "after_date": parse_date("2024-01-01"),
                        "exclude_domains": ["reddit.com", "x.com", ".ai"],
                        "include_domains": ["wikipedia.org", "usa.gov", ".edu"],
                    },
                },
                "include_backfill": True,
                "output_schema": {
                    "json_schema": {
                        "additionalProperties": "bar",
                        "properties": "bar",
                        "required": "bar",
                        "type": "bar",
                    },
                    "type": "json",
                },
            },
            type="event_stream",
            metadata={
                "slack_thread_id": "1234567890.123456",
                "user_id": "U123ABC",
            },
            processor="lite",
            webhook={
                "url": "https://example.com/webhook",
                "event_types": ["monitor.event.detected"],
            },
        )
        assert_matches_type(Monitor, monitor, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Parallel) -> None:
        response = client.monitor.with_raw_response.create(
            frequency="1h",
            settings={"query": "Extract recent news about AI"},
            type="event_stream",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        monitor = response.parse()
        assert_matches_type(Monitor, monitor, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Parallel) -> None:
        with client.monitor.with_streaming_response.create(
            frequency="1h",
            settings={"query": "Extract recent news about AI"},
            type="event_stream",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            monitor = response.parse()
            assert_matches_type(Monitor, monitor, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Parallel) -> None:
        monitor = client.monitor.retrieve(
            "monitor_id",
        )
        assert_matches_type(Monitor, monitor, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Parallel) -> None:
        response = client.monitor.with_raw_response.retrieve(
            "monitor_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        monitor = response.parse()
        assert_matches_type(Monitor, monitor, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Parallel) -> None:
        with client.monitor.with_streaming_response.retrieve(
            "monitor_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            monitor = response.parse()
            assert_matches_type(Monitor, monitor, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Parallel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `monitor_id` but received ''"):
            client.monitor.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: Parallel) -> None:
        monitor = client.monitor.update(
            monitor_id="monitor_id",
        )
        assert_matches_type(Monitor, monitor, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Parallel) -> None:
        monitor = client.monitor.update(
            monitor_id="monitor_id",
            frequency="1h",
            metadata={
                "slack_thread_id": "1234567890.123456",
                "user_id": "U123ABC",
            },
            settings={
                "advanced_settings": {
                    "location": "us",
                    "source_policy": {
                        "after_date": parse_date("2024-01-01"),
                        "exclude_domains": ["reddit.com", "x.com", ".ai"],
                        "include_domains": ["wikipedia.org", "usa.gov", ".edu"],
                    },
                }
            },
            type="event_stream",
            webhook={
                "url": "https://example.com/webhook",
                "event_types": ["monitor.event.detected"],
            },
        )
        assert_matches_type(Monitor, monitor, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Parallel) -> None:
        response = client.monitor.with_raw_response.update(
            monitor_id="monitor_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        monitor = response.parse()
        assert_matches_type(Monitor, monitor, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Parallel) -> None:
        with client.monitor.with_streaming_response.update(
            monitor_id="monitor_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            monitor = response.parse()
            assert_matches_type(Monitor, monitor, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Parallel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `monitor_id` but received ''"):
            client.monitor.with_raw_response.update(
                monitor_id="",
            )

    @parametrize
    def test_method_list(self, client: Parallel) -> None:
        monitor = client.monitor.list()
        assert_matches_type(PaginatedMonitorResponse, monitor, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Parallel) -> None:
        monitor = client.monitor.list(
            cursor="cursor",
            limit=1,
            status=["active"],
            type=["event_stream"],
        )
        assert_matches_type(PaginatedMonitorResponse, monitor, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Parallel) -> None:
        response = client.monitor.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        monitor = response.parse()
        assert_matches_type(PaginatedMonitorResponse, monitor, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Parallel) -> None:
        with client.monitor.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            monitor = response.parse()
            assert_matches_type(PaginatedMonitorResponse, monitor, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_cancel(self, client: Parallel) -> None:
        monitor = client.monitor.cancel(
            "monitor_id",
        )
        assert_matches_type(Monitor, monitor, path=["response"])

    @parametrize
    def test_raw_response_cancel(self, client: Parallel) -> None:
        response = client.monitor.with_raw_response.cancel(
            "monitor_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        monitor = response.parse()
        assert_matches_type(Monitor, monitor, path=["response"])

    @parametrize
    def test_streaming_response_cancel(self, client: Parallel) -> None:
        with client.monitor.with_streaming_response.cancel(
            "monitor_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            monitor = response.parse()
            assert_matches_type(Monitor, monitor, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_cancel(self, client: Parallel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `monitor_id` but received ''"):
            client.monitor.with_raw_response.cancel(
                "",
            )

    @parametrize
    def test_method_events(self, client: Parallel) -> None:
        monitor = client.monitor.events(
            monitor_id="monitor_id",
        )
        assert_matches_type(PaginatedMonitorEvents, monitor, path=["response"])

    @parametrize
    def test_method_events_with_all_params(self, client: Parallel) -> None:
        monitor = client.monitor.events(
            monitor_id="monitor_id",
            cursor="cursor",
            event_group_id="event_group_id",
            include_completions=True,
            limit=1,
        )
        assert_matches_type(PaginatedMonitorEvents, monitor, path=["response"])

    @parametrize
    def test_raw_response_events(self, client: Parallel) -> None:
        response = client.monitor.with_raw_response.events(
            monitor_id="monitor_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        monitor = response.parse()
        assert_matches_type(PaginatedMonitorEvents, monitor, path=["response"])

    @parametrize
    def test_streaming_response_events(self, client: Parallel) -> None:
        with client.monitor.with_streaming_response.events(
            monitor_id="monitor_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            monitor = response.parse()
            assert_matches_type(PaginatedMonitorEvents, monitor, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_events(self, client: Parallel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `monitor_id` but received ''"):
            client.monitor.with_raw_response.events(
                monitor_id="",
            )

    @parametrize
    def test_method_trigger(self, client: Parallel) -> None:
        monitor = client.monitor.trigger(
            "monitor_id",
        )
        assert monitor is None

    @parametrize
    def test_raw_response_trigger(self, client: Parallel) -> None:
        response = client.monitor.with_raw_response.trigger(
            "monitor_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        monitor = response.parse()
        assert monitor is None

    @parametrize
    def test_streaming_response_trigger(self, client: Parallel) -> None:
        with client.monitor.with_streaming_response.trigger(
            "monitor_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            monitor = response.parse()
            assert monitor is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_trigger(self, client: Parallel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `monitor_id` but received ''"):
            client.monitor.with_raw_response.trigger(
                "",
            )


class TestAsyncMonitor:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncParallel) -> None:
        monitor = await async_client.monitor.create(
            frequency="1h",
            settings={"query": "Extract recent news about AI"},
            type="event_stream",
        )
        assert_matches_type(Monitor, monitor, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncParallel) -> None:
        monitor = await async_client.monitor.create(
            frequency="1h",
            settings={
                "query": "Extract recent news about AI",
                "advanced_settings": {
                    "location": "us",
                    "source_policy": {
                        "after_date": parse_date("2024-01-01"),
                        "exclude_domains": ["reddit.com", "x.com", ".ai"],
                        "include_domains": ["wikipedia.org", "usa.gov", ".edu"],
                    },
                },
                "include_backfill": True,
                "output_schema": {
                    "json_schema": {
                        "additionalProperties": "bar",
                        "properties": "bar",
                        "required": "bar",
                        "type": "bar",
                    },
                    "type": "json",
                },
            },
            type="event_stream",
            metadata={
                "slack_thread_id": "1234567890.123456",
                "user_id": "U123ABC",
            },
            processor="lite",
            webhook={
                "url": "https://example.com/webhook",
                "event_types": ["monitor.event.detected"],
            },
        )
        assert_matches_type(Monitor, monitor, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncParallel) -> None:
        response = await async_client.monitor.with_raw_response.create(
            frequency="1h",
            settings={"query": "Extract recent news about AI"},
            type="event_stream",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        monitor = await response.parse()
        assert_matches_type(Monitor, monitor, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncParallel) -> None:
        async with async_client.monitor.with_streaming_response.create(
            frequency="1h",
            settings={"query": "Extract recent news about AI"},
            type="event_stream",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            monitor = await response.parse()
            assert_matches_type(Monitor, monitor, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncParallel) -> None:
        monitor = await async_client.monitor.retrieve(
            "monitor_id",
        )
        assert_matches_type(Monitor, monitor, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncParallel) -> None:
        response = await async_client.monitor.with_raw_response.retrieve(
            "monitor_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        monitor = await response.parse()
        assert_matches_type(Monitor, monitor, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncParallel) -> None:
        async with async_client.monitor.with_streaming_response.retrieve(
            "monitor_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            monitor = await response.parse()
            assert_matches_type(Monitor, monitor, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncParallel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `monitor_id` but received ''"):
            await async_client.monitor.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncParallel) -> None:
        monitor = await async_client.monitor.update(
            monitor_id="monitor_id",
        )
        assert_matches_type(Monitor, monitor, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncParallel) -> None:
        monitor = await async_client.monitor.update(
            monitor_id="monitor_id",
            frequency="1h",
            metadata={
                "slack_thread_id": "1234567890.123456",
                "user_id": "U123ABC",
            },
            settings={
                "advanced_settings": {
                    "location": "us",
                    "source_policy": {
                        "after_date": parse_date("2024-01-01"),
                        "exclude_domains": ["reddit.com", "x.com", ".ai"],
                        "include_domains": ["wikipedia.org", "usa.gov", ".edu"],
                    },
                }
            },
            type="event_stream",
            webhook={
                "url": "https://example.com/webhook",
                "event_types": ["monitor.event.detected"],
            },
        )
        assert_matches_type(Monitor, monitor, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncParallel) -> None:
        response = await async_client.monitor.with_raw_response.update(
            monitor_id="monitor_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        monitor = await response.parse()
        assert_matches_type(Monitor, monitor, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncParallel) -> None:
        async with async_client.monitor.with_streaming_response.update(
            monitor_id="monitor_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            monitor = await response.parse()
            assert_matches_type(Monitor, monitor, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncParallel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `monitor_id` but received ''"):
            await async_client.monitor.with_raw_response.update(
                monitor_id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncParallel) -> None:
        monitor = await async_client.monitor.list()
        assert_matches_type(PaginatedMonitorResponse, monitor, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncParallel) -> None:
        monitor = await async_client.monitor.list(
            cursor="cursor",
            limit=1,
            status=["active"],
            type=["event_stream"],
        )
        assert_matches_type(PaginatedMonitorResponse, monitor, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncParallel) -> None:
        response = await async_client.monitor.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        monitor = await response.parse()
        assert_matches_type(PaginatedMonitorResponse, monitor, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncParallel) -> None:
        async with async_client.monitor.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            monitor = await response.parse()
            assert_matches_type(PaginatedMonitorResponse, monitor, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_cancel(self, async_client: AsyncParallel) -> None:
        monitor = await async_client.monitor.cancel(
            "monitor_id",
        )
        assert_matches_type(Monitor, monitor, path=["response"])

    @parametrize
    async def test_raw_response_cancel(self, async_client: AsyncParallel) -> None:
        response = await async_client.monitor.with_raw_response.cancel(
            "monitor_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        monitor = await response.parse()
        assert_matches_type(Monitor, monitor, path=["response"])

    @parametrize
    async def test_streaming_response_cancel(self, async_client: AsyncParallel) -> None:
        async with async_client.monitor.with_streaming_response.cancel(
            "monitor_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            monitor = await response.parse()
            assert_matches_type(Monitor, monitor, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_cancel(self, async_client: AsyncParallel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `monitor_id` but received ''"):
            await async_client.monitor.with_raw_response.cancel(
                "",
            )

    @parametrize
    async def test_method_events(self, async_client: AsyncParallel) -> None:
        monitor = await async_client.monitor.events(
            monitor_id="monitor_id",
        )
        assert_matches_type(PaginatedMonitorEvents, monitor, path=["response"])

    @parametrize
    async def test_method_events_with_all_params(self, async_client: AsyncParallel) -> None:
        monitor = await async_client.monitor.events(
            monitor_id="monitor_id",
            cursor="cursor",
            event_group_id="event_group_id",
            include_completions=True,
            limit=1,
        )
        assert_matches_type(PaginatedMonitorEvents, monitor, path=["response"])

    @parametrize
    async def test_raw_response_events(self, async_client: AsyncParallel) -> None:
        response = await async_client.monitor.with_raw_response.events(
            monitor_id="monitor_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        monitor = await response.parse()
        assert_matches_type(PaginatedMonitorEvents, monitor, path=["response"])

    @parametrize
    async def test_streaming_response_events(self, async_client: AsyncParallel) -> None:
        async with async_client.monitor.with_streaming_response.events(
            monitor_id="monitor_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            monitor = await response.parse()
            assert_matches_type(PaginatedMonitorEvents, monitor, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_events(self, async_client: AsyncParallel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `monitor_id` but received ''"):
            await async_client.monitor.with_raw_response.events(
                monitor_id="",
            )

    @parametrize
    async def test_method_trigger(self, async_client: AsyncParallel) -> None:
        monitor = await async_client.monitor.trigger(
            "monitor_id",
        )
        assert monitor is None

    @parametrize
    async def test_raw_response_trigger(self, async_client: AsyncParallel) -> None:
        response = await async_client.monitor.with_raw_response.trigger(
            "monitor_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        monitor = await response.parse()
        assert monitor is None

    @parametrize
    async def test_streaming_response_trigger(self, async_client: AsyncParallel) -> None:
        async with async_client.monitor.with_streaming_response.trigger(
            "monitor_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            monitor = await response.parse()
            assert monitor is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_trigger(self, async_client: AsyncParallel) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `monitor_id` but received ''"):
            await async_client.monitor.with_raw_response.trigger(
                "",
            )
