# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, cast

import httpx

from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._streaming import Stream, AsyncStream
from ..._base_client import make_request_options
from ...types.beta.task_run_events_response import TaskRunEventsResponse

__all__ = ["TaskRunResource", "AsyncTaskRunResource"]


class TaskRunResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TaskRunResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/parallel-web/parallel-sdk-python#accessing-raw-response-data-eg-headers
        """
        return TaskRunResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TaskRunResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/parallel-web/parallel-sdk-python#with_streaming_response
        """
        return TaskRunResourceWithStreamingResponse(self)

    def events(
        self,
        run_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Stream[TaskRunEventsResponse]:
        """
        Streams events for a task run.

        Returns a stream of events showing progress updates and state changes for the
        task run.

        For task runs that did not have enable_events set to true during creation, the
        frequency of events will be reduced.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not run_id:
            raise ValueError(f"Expected a non-empty value for `run_id` but received {run_id!r}")
        extra_headers = {"Accept": "text/event-stream", **(extra_headers or {})}
        extra_headers = {"parallel-beta": "search-extract-2025-10-10", **(extra_headers or {})}
        return self._get(
            f"/v1beta/tasks/runs/{run_id}/events",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=cast(Any, TaskRunEventsResponse),  # Union types cannot be passed in as arguments in the type system
            stream=True,
            stream_cls=Stream[TaskRunEventsResponse],
        )


class AsyncTaskRunResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTaskRunResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/parallel-web/parallel-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTaskRunResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTaskRunResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/parallel-web/parallel-sdk-python#with_streaming_response
        """
        return AsyncTaskRunResourceWithStreamingResponse(self)

    async def events(
        self,
        run_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncStream[TaskRunEventsResponse]:
        """
        Streams events for a task run.

        Returns a stream of events showing progress updates and state changes for the
        task run.

        For task runs that did not have enable_events set to true during creation, the
        frequency of events will be reduced.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not run_id:
            raise ValueError(f"Expected a non-empty value for `run_id` but received {run_id!r}")
        extra_headers = {"Accept": "text/event-stream", **(extra_headers or {})}
        extra_headers = {"parallel-beta": "search-extract-2025-10-10", **(extra_headers or {})}
        return await self._get(
            f"/v1beta/tasks/runs/{run_id}/events",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=cast(Any, TaskRunEventsResponse),  # Union types cannot be passed in as arguments in the type system
            stream=True,
            stream_cls=AsyncStream[TaskRunEventsResponse],
        )


class TaskRunResourceWithRawResponse:
    def __init__(self, task_run: TaskRunResource) -> None:
        self._task_run = task_run

        self.events = to_raw_response_wrapper(
            task_run.events,
        )


class AsyncTaskRunResourceWithRawResponse:
    def __init__(self, task_run: AsyncTaskRunResource) -> None:
        self._task_run = task_run

        self.events = async_to_raw_response_wrapper(
            task_run.events,
        )


class TaskRunResourceWithStreamingResponse:
    def __init__(self, task_run: TaskRunResource) -> None:
        self._task_run = task_run

        self.events = to_streamed_response_wrapper(
            task_run.events,
        )


class AsyncTaskRunResourceWithStreamingResponse:
    def __init__(self, task_run: AsyncTaskRunResource) -> None:
        self._task_run = task_run

        self.events = async_to_streamed_response_wrapper(
            task_run.events,
        )
