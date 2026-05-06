# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Optional
from typing_extensions import Literal

import httpx

from ..types import (
    monitor_list_params,
    monitor_create_params,
    monitor_events_params,
    monitor_update_params,
)
from .._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.monitor import Monitor
from ..types.monitor_webhook_param import MonitorWebhookParam
from ..types.paginated_monitor_events import PaginatedMonitorEvents
from ..types.paginated_monitor_response import PaginatedMonitorResponse
from ..types.update_monitor_event_stream_settings_param import UpdateMonitorEventStreamSettingsParam

__all__ = ["MonitorResource", "AsyncMonitorResource"]


class MonitorResource(SyncAPIResource):
    """The Monitor API watches the web for material changes on a fixed frequency.

    Each monitor runs once on creation and then on its configured schedule, emitting events when meaningful changes are detected.
    - `event_stream` monitors track a search query and emit an event for each new material change.
    - `snapshot` monitors track a specific task run's output and emit an event when the output changes.

    Results can be polled via the events endpoint or delivered via webhooks.
    """

    @cached_property
    def with_raw_response(self) -> MonitorResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/parallel-web/parallel-sdk-python#accessing-raw-response-data-eg-headers
        """
        return MonitorResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MonitorResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/parallel-web/parallel-sdk-python#with_streaming_response
        """
        return MonitorResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        frequency: str,
        settings: monitor_create_params.Settings,
        type: Literal["event_stream", "snapshot"],
        metadata: Optional[Dict[str, str]] | Omit = omit,
        processor: Literal["lite", "base"] | Omit = omit,
        webhook: Optional[MonitorWebhookParam] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Monitor:
        """
        Create a monitor.

        Monitors run on a fixed frequency to detect material changes in web content. Set
        `type=event_stream` to monitor a search query, or `type=snapshot` to monitor a
        specific task run's output. The monitor runs once immediately at creation, then
        continues on the configured schedule.

        Args:
          frequency: Frequency of the monitor. Format: '<number><unit>' where unit is 'h' (hours),
              'd' (days), or 'w' (weeks). Must be between 1h and 30d (inclusive).

          settings: Type-specific settings for the monitor. The expected shape is determined by the
              root `type` field: pass `MonitorEventStreamSettings` when `type` is
              `event_stream`, and `MonitorSnapshotSettings` when `type` is `snapshot`.

          type: Type of monitor to create. `event_stream` monitors a search query for material
              changes; `snapshot` monitors a specific task run's output. Determines the
              expected shape of `settings`.

          metadata: User-provided metadata stored with the monitor and echoed back in webhook
              notifications and GET responses, so you can map events to objects in your
              application. Keys: max 16 chars; values: max 512 chars.

          processor: Processor to use for the monitor. `lite` is faster and cheaper; `base` performs
              more thorough analysis at higher cost and latency. Defaults to `lite`.

          webhook: Webhook configuration for a monitor.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/monitors",
            body=maybe_transform(
                {
                    "frequency": frequency,
                    "settings": settings,
                    "type": type,
                    "metadata": metadata,
                    "processor": processor,
                    "webhook": webhook,
                },
                monitor_create_params.MonitorCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Monitor,
        )

    def retrieve(
        self,
        monitor_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Monitor:
        """Retrieve a monitor.

        Retrieves a specific monitor by `monitor_id`.

        Returns the monitor configuration
        including status, frequency, query, and webhook settings.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not monitor_id:
            raise ValueError(f"Expected a non-empty value for `monitor_id` but received {monitor_id!r}")
        return self._get(
            path_template("/v1/monitors/{monitor_id}", monitor_id=monitor_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Monitor,
        )

    def update(
        self,
        monitor_id: str,
        *,
        frequency: Optional[str] | Omit = omit,
        metadata: Optional[Dict[str, str]] | Omit = omit,
        settings: Optional[UpdateMonitorEventStreamSettingsParam] | Omit = omit,
        type: Optional[Literal["event_stream", "snapshot"]] | Omit = omit,
        webhook: Optional[MonitorWebhookParam] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Monitor:
        """
        Update a monitor.

        Only fields explicitly included in the request body are changed. Pass `null` for
        `webhook` or `metadata` to clear those fields. Pass `type` and `settings` to
        update type-specific settings on an `event_stream` monitor. At least one field
        must be provided. Cancelled monitors cannot be updated.

        Args:
          frequency: Frequency of the monitor. Format: '<number><unit>' where unit is 'h' (hours),
              'd' (days), or 'w' (weeks). Must be between 1h and 30d (inclusive).

          metadata: User-provided metadata stored with the monitor and echoed back in webhook
              notifications and GET responses, so you can map events to objects in your
              application. Keys: max 16 chars; values: max 512 chars.

          settings: Type-specific update settings for an `event_stream` monitor.

          type: Type of the monitor being updated. Required when `settings` is provided; must be
              `event_stream` (snapshot monitors have no updatable type-specific settings).

          webhook: Webhook configuration for a monitor.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not monitor_id:
            raise ValueError(f"Expected a non-empty value for `monitor_id` but received {monitor_id!r}")
        return self._post(
            path_template("/v1/monitors/{monitor_id}/update", monitor_id=monitor_id),
            body=maybe_transform(
                {
                    "frequency": frequency,
                    "metadata": metadata,
                    "settings": settings,
                    "type": type,
                    "webhook": webhook,
                },
                monitor_update_params.MonitorUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Monitor,
        )

    def list(
        self,
        *,
        cursor: Optional[str] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        status: Optional[List[Literal["active", "cancelled"]]] | Omit = omit,
        type: Optional[List[Literal["event_stream", "snapshot"]]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaginatedMonitorResponse:
        """
        List monitors ordered by creation time, newest first.

        Monitors are sorted by `created_at` descending. `limit` defaults to 100. Use
        `next_cursor` from the response and pass it as `cursor` to fetch the next page.
        Pagination ends when `next_cursor` is absent.

        By default only `active` monitors are returned. Pass `status=cancelled` or both
        values to include cancelled monitors.

        The legacy Monitor API (`/v1alpha/monitors` endpoints) is documented under the
        `Monitor (Alpha)` tag.

        Args:
          cursor: Pagination token from `next_cursor` in a previous response. Omit to start from
              the most recently created monitor.

          limit: Maximum number of monitors to return. Defaults to 100. Between 1 and 10000.

          status: Filter by monitor status. Pass multiple times to filter by multiple values.
              Defaults to `active` only.

          type: Filter by monitor type. Pass multiple times to filter by multiple values. Omit
              to return all types.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/monitors",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                        "status": status,
                        "type": type,
                    },
                    monitor_list_params.MonitorListParams,
                ),
            ),
            cast_to=PaginatedMonitorResponse,
        )

    def cancel(
        self,
        monitor_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Monitor:
        """Cancel a monitor.

        Permanently stops the monitor from running.

        Cancellation is irreversible —
        create a new monitor to resume monitoring. Cancelling an already-cancelled
        monitor is a no-op.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not monitor_id:
            raise ValueError(f"Expected a non-empty value for `monitor_id` but received {monitor_id!r}")
        return self._post(
            path_template("/v1/monitors/{monitor_id}/cancel", monitor_id=monitor_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Monitor,
        )

    def events(
        self,
        monitor_id: str,
        *,
        cursor: Optional[str] | Omit = omit,
        event_group_id: Optional[str] | Omit = omit,
        include_completions: bool | Omit = omit,
        limit: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaginatedMonitorEvents:
        """
        List events for a monitor, newest first.

        Pass `event_group_id` to narrow results to a single execution. Otherwise returns
        all executions newest-first; use `next_cursor` to paginate. Set
        `include_completions=true` to also include no-change executions.

        Args:
          cursor: Pass `next_cursor` from a previous response to retrieve more events.

          event_group_id: Filter to a single execution. Values come from `event_group_id` in webhook
              events and listed events. Pagination params are ignored when set.

          include_completions: When true, include completion events for executions that ran but detected no
              material changes. Useful for auditing execution history.

          limit: Maximum number of events to return. Defaults to 20. Between 1 and 100.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not monitor_id:
            raise ValueError(f"Expected a non-empty value for `monitor_id` but received {monitor_id!r}")
        return self._get(
            path_template("/v1/monitors/{monitor_id}/events", monitor_id=monitor_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "event_group_id": event_group_id,
                        "include_completions": include_completions,
                        "limit": limit,
                    },
                    monitor_events_params.MonitorEventsParams,
                ),
            ),
            cast_to=PaginatedMonitorEvents,
        )

    def trigger(
        self,
        monitor_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Trigger an immediate monitor run.

        Enqueues a one-off execution of the monitor outside its normal schedule. The
        monitor's regular schedule is not affected. An event is only emitted if the
        execution detects a material change. Cancelled monitors cannot be triggered.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not monitor_id:
            raise ValueError(f"Expected a non-empty value for `monitor_id` but received {monitor_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            path_template("/v1/monitors/{monitor_id}/trigger", monitor_id=monitor_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncMonitorResource(AsyncAPIResource):
    """The Monitor API watches the web for material changes on a fixed frequency.

    Each monitor runs once on creation and then on its configured schedule, emitting events when meaningful changes are detected.
    - `event_stream` monitors track a search query and emit an event for each new material change.
    - `snapshot` monitors track a specific task run's output and emit an event when the output changes.

    Results can be polled via the events endpoint or delivered via webhooks.
    """

    @cached_property
    def with_raw_response(self) -> AsyncMonitorResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/parallel-web/parallel-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMonitorResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMonitorResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/parallel-web/parallel-sdk-python#with_streaming_response
        """
        return AsyncMonitorResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        frequency: str,
        settings: monitor_create_params.Settings,
        type: Literal["event_stream", "snapshot"],
        metadata: Optional[Dict[str, str]] | Omit = omit,
        processor: Literal["lite", "base"] | Omit = omit,
        webhook: Optional[MonitorWebhookParam] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Monitor:
        """
        Create a monitor.

        Monitors run on a fixed frequency to detect material changes in web content. Set
        `type=event_stream` to monitor a search query, or `type=snapshot` to monitor a
        specific task run's output. The monitor runs once immediately at creation, then
        continues on the configured schedule.

        Args:
          frequency: Frequency of the monitor. Format: '<number><unit>' where unit is 'h' (hours),
              'd' (days), or 'w' (weeks). Must be between 1h and 30d (inclusive).

          settings: Type-specific settings for the monitor. The expected shape is determined by the
              root `type` field: pass `MonitorEventStreamSettings` when `type` is
              `event_stream`, and `MonitorSnapshotSettings` when `type` is `snapshot`.

          type: Type of monitor to create. `event_stream` monitors a search query for material
              changes; `snapshot` monitors a specific task run's output. Determines the
              expected shape of `settings`.

          metadata: User-provided metadata stored with the monitor and echoed back in webhook
              notifications and GET responses, so you can map events to objects in your
              application. Keys: max 16 chars; values: max 512 chars.

          processor: Processor to use for the monitor. `lite` is faster and cheaper; `base` performs
              more thorough analysis at higher cost and latency. Defaults to `lite`.

          webhook: Webhook configuration for a monitor.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/monitors",
            body=await async_maybe_transform(
                {
                    "frequency": frequency,
                    "settings": settings,
                    "type": type,
                    "metadata": metadata,
                    "processor": processor,
                    "webhook": webhook,
                },
                monitor_create_params.MonitorCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Monitor,
        )

    async def retrieve(
        self,
        monitor_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Monitor:
        """Retrieve a monitor.

        Retrieves a specific monitor by `monitor_id`.

        Returns the monitor configuration
        including status, frequency, query, and webhook settings.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not monitor_id:
            raise ValueError(f"Expected a non-empty value for `monitor_id` but received {monitor_id!r}")
        return await self._get(
            path_template("/v1/monitors/{monitor_id}", monitor_id=monitor_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Monitor,
        )

    async def update(
        self,
        monitor_id: str,
        *,
        frequency: Optional[str] | Omit = omit,
        metadata: Optional[Dict[str, str]] | Omit = omit,
        settings: Optional[UpdateMonitorEventStreamSettingsParam] | Omit = omit,
        type: Optional[Literal["event_stream", "snapshot"]] | Omit = omit,
        webhook: Optional[MonitorWebhookParam] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Monitor:
        """
        Update a monitor.

        Only fields explicitly included in the request body are changed. Pass `null` for
        `webhook` or `metadata` to clear those fields. Pass `type` and `settings` to
        update type-specific settings on an `event_stream` monitor. At least one field
        must be provided. Cancelled monitors cannot be updated.

        Args:
          frequency: Frequency of the monitor. Format: '<number><unit>' where unit is 'h' (hours),
              'd' (days), or 'w' (weeks). Must be between 1h and 30d (inclusive).

          metadata: User-provided metadata stored with the monitor and echoed back in webhook
              notifications and GET responses, so you can map events to objects in your
              application. Keys: max 16 chars; values: max 512 chars.

          settings: Type-specific update settings for an `event_stream` monitor.

          type: Type of the monitor being updated. Required when `settings` is provided; must be
              `event_stream` (snapshot monitors have no updatable type-specific settings).

          webhook: Webhook configuration for a monitor.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not monitor_id:
            raise ValueError(f"Expected a non-empty value for `monitor_id` but received {monitor_id!r}")
        return await self._post(
            path_template("/v1/monitors/{monitor_id}/update", monitor_id=monitor_id),
            body=await async_maybe_transform(
                {
                    "frequency": frequency,
                    "metadata": metadata,
                    "settings": settings,
                    "type": type,
                    "webhook": webhook,
                },
                monitor_update_params.MonitorUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Monitor,
        )

    async def list(
        self,
        *,
        cursor: Optional[str] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        status: Optional[List[Literal["active", "cancelled"]]] | Omit = omit,
        type: Optional[List[Literal["event_stream", "snapshot"]]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaginatedMonitorResponse:
        """
        List monitors ordered by creation time, newest first.

        Monitors are sorted by `created_at` descending. `limit` defaults to 100. Use
        `next_cursor` from the response and pass it as `cursor` to fetch the next page.
        Pagination ends when `next_cursor` is absent.

        By default only `active` monitors are returned. Pass `status=cancelled` or both
        values to include cancelled monitors.

        The legacy Monitor API (`/v1alpha/monitors` endpoints) is documented under the
        `Monitor (Alpha)` tag.

        Args:
          cursor: Pagination token from `next_cursor` in a previous response. Omit to start from
              the most recently created monitor.

          limit: Maximum number of monitors to return. Defaults to 100. Between 1 and 10000.

          status: Filter by monitor status. Pass multiple times to filter by multiple values.
              Defaults to `active` only.

          type: Filter by monitor type. Pass multiple times to filter by multiple values. Omit
              to return all types.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/monitors",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                        "status": status,
                        "type": type,
                    },
                    monitor_list_params.MonitorListParams,
                ),
            ),
            cast_to=PaginatedMonitorResponse,
        )

    async def cancel(
        self,
        monitor_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Monitor:
        """Cancel a monitor.

        Permanently stops the monitor from running.

        Cancellation is irreversible —
        create a new monitor to resume monitoring. Cancelling an already-cancelled
        monitor is a no-op.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not monitor_id:
            raise ValueError(f"Expected a non-empty value for `monitor_id` but received {monitor_id!r}")
        return await self._post(
            path_template("/v1/monitors/{monitor_id}/cancel", monitor_id=monitor_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Monitor,
        )

    async def events(
        self,
        monitor_id: str,
        *,
        cursor: Optional[str] | Omit = omit,
        event_group_id: Optional[str] | Omit = omit,
        include_completions: bool | Omit = omit,
        limit: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaginatedMonitorEvents:
        """
        List events for a monitor, newest first.

        Pass `event_group_id` to narrow results to a single execution. Otherwise returns
        all executions newest-first; use `next_cursor` to paginate. Set
        `include_completions=true` to also include no-change executions.

        Args:
          cursor: Pass `next_cursor` from a previous response to retrieve more events.

          event_group_id: Filter to a single execution. Values come from `event_group_id` in webhook
              events and listed events. Pagination params are ignored when set.

          include_completions: When true, include completion events for executions that ran but detected no
              material changes. Useful for auditing execution history.

          limit: Maximum number of events to return. Defaults to 20. Between 1 and 100.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not monitor_id:
            raise ValueError(f"Expected a non-empty value for `monitor_id` but received {monitor_id!r}")
        return await self._get(
            path_template("/v1/monitors/{monitor_id}/events", monitor_id=monitor_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "cursor": cursor,
                        "event_group_id": event_group_id,
                        "include_completions": include_completions,
                        "limit": limit,
                    },
                    monitor_events_params.MonitorEventsParams,
                ),
            ),
            cast_to=PaginatedMonitorEvents,
        )

    async def trigger(
        self,
        monitor_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Trigger an immediate monitor run.

        Enqueues a one-off execution of the monitor outside its normal schedule. The
        monitor's regular schedule is not affected. An event is only emitted if the
        execution detects a material change. Cancelled monitors cannot be triggered.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not monitor_id:
            raise ValueError(f"Expected a non-empty value for `monitor_id` but received {monitor_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            path_template("/v1/monitors/{monitor_id}/trigger", monitor_id=monitor_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class MonitorResourceWithRawResponse:
    def __init__(self, monitor: MonitorResource) -> None:
        self._monitor = monitor

        self.create = to_raw_response_wrapper(
            monitor.create,
        )
        self.retrieve = to_raw_response_wrapper(
            monitor.retrieve,
        )
        self.update = to_raw_response_wrapper(
            monitor.update,
        )
        self.list = to_raw_response_wrapper(
            monitor.list,
        )
        self.cancel = to_raw_response_wrapper(
            monitor.cancel,
        )
        self.events = to_raw_response_wrapper(
            monitor.events,
        )
        self.trigger = to_raw_response_wrapper(
            monitor.trigger,
        )


class AsyncMonitorResourceWithRawResponse:
    def __init__(self, monitor: AsyncMonitorResource) -> None:
        self._monitor = monitor

        self.create = async_to_raw_response_wrapper(
            monitor.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            monitor.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            monitor.update,
        )
        self.list = async_to_raw_response_wrapper(
            monitor.list,
        )
        self.cancel = async_to_raw_response_wrapper(
            monitor.cancel,
        )
        self.events = async_to_raw_response_wrapper(
            monitor.events,
        )
        self.trigger = async_to_raw_response_wrapper(
            monitor.trigger,
        )


class MonitorResourceWithStreamingResponse:
    def __init__(self, monitor: MonitorResource) -> None:
        self._monitor = monitor

        self.create = to_streamed_response_wrapper(
            monitor.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            monitor.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            monitor.update,
        )
        self.list = to_streamed_response_wrapper(
            monitor.list,
        )
        self.cancel = to_streamed_response_wrapper(
            monitor.cancel,
        )
        self.events = to_streamed_response_wrapper(
            monitor.events,
        )
        self.trigger = to_streamed_response_wrapper(
            monitor.trigger,
        )


class AsyncMonitorResourceWithStreamingResponse:
    def __init__(self, monitor: AsyncMonitorResource) -> None:
        self._monitor = monitor

        self.create = async_to_streamed_response_wrapper(
            monitor.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            monitor.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            monitor.update,
        )
        self.list = async_to_streamed_response_wrapper(
            monitor.list,
        )
        self.cancel = async_to_streamed_response_wrapper(
            monitor.cancel,
        )
        self.events = async_to_streamed_response_wrapper(
            monitor.events,
        )
        self.trigger = async_to_streamed_response_wrapper(
            monitor.trigger,
        )
