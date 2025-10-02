# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Dict, List, Union, Iterable, Optional, cast
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import is_given, maybe_transform, strip_not_given, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._streaming import Stream, AsyncStream
from ...types.beta import (
    task_group_create_params,
    task_group_events_params,
    task_group_add_runs_params,
    task_group_get_runs_params,
)
from ..._base_client import make_request_options
from ...types.beta.task_group import TaskGroup
from ...types.task_spec_param import TaskSpecParam
from ...types.beta.parallel_beta_param import ParallelBetaParam
from ...types.beta.beta_run_input_param import BetaRunInputParam
from ...types.beta.task_group_run_response import TaskGroupRunResponse
from ...types.beta.task_group_events_response import TaskGroupEventsResponse
from ...types.beta.task_group_get_runs_response import TaskGroupGetRunsResponse

__all__ = ["TaskGroupResource", "AsyncTaskGroupResource"]


class TaskGroupResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TaskGroupResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/parallel-web/parallel-sdk-python#accessing-raw-response-data-eg-headers
        """
        return TaskGroupResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TaskGroupResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/parallel-web/parallel-sdk-python#with_streaming_response
        """
        return TaskGroupResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        metadata: Optional[Dict[str, Union[str, float, bool]]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskGroup:
        """
        Initiates a TaskGroup to group and track multiple runs.

        Args:
          metadata: User-provided metadata stored with the task group.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1beta/tasks/groups",
            body=maybe_transform({"metadata": metadata}, task_group_create_params.TaskGroupCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskGroup,
        )

    def retrieve(
        self,
        task_group_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskGroup:
        """
        Retrieves aggregated status across runs in a TaskGroup.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not task_group_id:
            raise ValueError(f"Expected a non-empty value for `task_group_id` but received {task_group_id!r}")
        return self._get(
            f"/v1beta/tasks/groups/{task_group_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskGroup,
        )

    def add_runs(
        self,
        task_group_id: str,
        *,
        inputs: Iterable[BetaRunInputParam],
        default_task_spec: Optional[TaskSpecParam] | Omit = omit,
        betas: List[ParallelBetaParam] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskGroupRunResponse:
        """
        Initiates multiple task runs within a TaskGroup.

        Args:
          inputs: List of task runs to execute.

          default_task_spec: Specification for a task.

              Auto output schemas can be specified by setting `output_schema={"type":"auto"}`.
              Not specifying a TaskSpec is the same as setting an auto output schema.

              For convenience bare strings are also accepted as input or output schemas.

          betas: Optional header to specify the beta version(s) to enable.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not task_group_id:
            raise ValueError(f"Expected a non-empty value for `task_group_id` but received {task_group_id!r}")
        extra_headers = {
            **strip_not_given({"parallel-beta": ",".join(str(e) for e in betas) if is_given(betas) else not_given}),
            **(extra_headers or {}),
        }
        return self._post(
            f"/v1beta/tasks/groups/{task_group_id}/runs",
            body=maybe_transform(
                {
                    "inputs": inputs,
                    "default_task_spec": default_task_spec,
                },
                task_group_add_runs_params.TaskGroupAddRunsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskGroupRunResponse,
        )

    def events(
        self,
        task_group_id: str,
        *,
        last_event_id: Optional[str] | Omit = omit,
        api_timeout: Optional[float] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Stream[TaskGroupEventsResponse]:
        """
        Streams events from a TaskGroup: status updates and run completions.

        The connection will remain open for up to an hour as long as at least one run in
        the group is still active.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not task_group_id:
            raise ValueError(f"Expected a non-empty value for `task_group_id` but received {task_group_id!r}")
        extra_headers = {"Accept": "text/event-stream", **(extra_headers or {})}
        return self._get(
            f"/v1beta/tasks/groups/{task_group_id}/events",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "last_event_id": last_event_id,
                        "api_timeout": api_timeout,
                    },
                    task_group_events_params.TaskGroupEventsParams,
                ),
            ),
            cast_to=cast(
                Any, TaskGroupEventsResponse
            ),  # Union types cannot be passed in as arguments in the type system
            stream=True,
            stream_cls=Stream[TaskGroupEventsResponse],
        )

    def get_runs(
        self,
        task_group_id: str,
        *,
        include_input: bool | Omit = omit,
        include_output: bool | Omit = omit,
        last_event_id: Optional[str] | Omit = omit,
        status: Optional[
            Literal["queued", "action_required", "running", "completed", "failed", "cancelling", "cancelled"]
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Stream[TaskGroupGetRunsResponse]:
        """
        Retrieves task runs in a TaskGroup and optionally their inputs and outputs.

        All runs within a TaskGroup are returned as a stream. To get the inputs and/or
        outputs back in the stream, set the corresponding `include_input` and
        `include_output` parameters to `true`.

        The stream is resumable using the `event_id` as the cursor. To resume a stream,
        specify the `last_event_id` parameter with the `event_id` of the last event in
        the stream. The stream will resume from the next event after the
        `last_event_id`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not task_group_id:
            raise ValueError(f"Expected a non-empty value for `task_group_id` but received {task_group_id!r}")
        extra_headers = {"Accept": "text/event-stream", **(extra_headers or {})}
        return self._get(
            f"/v1beta/tasks/groups/{task_group_id}/runs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "include_input": include_input,
                        "include_output": include_output,
                        "last_event_id": last_event_id,
                        "status": status,
                    },
                    task_group_get_runs_params.TaskGroupGetRunsParams,
                ),
            ),
            cast_to=cast(
                Any, TaskGroupGetRunsResponse
            ),  # Union types cannot be passed in as arguments in the type system
            stream=True,
            stream_cls=Stream[TaskGroupGetRunsResponse],
        )


class AsyncTaskGroupResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTaskGroupResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/parallel-web/parallel-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTaskGroupResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTaskGroupResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/parallel-web/parallel-sdk-python#with_streaming_response
        """
        return AsyncTaskGroupResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        metadata: Optional[Dict[str, Union[str, float, bool]]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskGroup:
        """
        Initiates a TaskGroup to group and track multiple runs.

        Args:
          metadata: User-provided metadata stored with the task group.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1beta/tasks/groups",
            body=await async_maybe_transform({"metadata": metadata}, task_group_create_params.TaskGroupCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskGroup,
        )

    async def retrieve(
        self,
        task_group_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskGroup:
        """
        Retrieves aggregated status across runs in a TaskGroup.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not task_group_id:
            raise ValueError(f"Expected a non-empty value for `task_group_id` but received {task_group_id!r}")
        return await self._get(
            f"/v1beta/tasks/groups/{task_group_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskGroup,
        )

    async def add_runs(
        self,
        task_group_id: str,
        *,
        inputs: Iterable[BetaRunInputParam],
        default_task_spec: Optional[TaskSpecParam] | Omit = omit,
        betas: List[ParallelBetaParam] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskGroupRunResponse:
        """
        Initiates multiple task runs within a TaskGroup.

        Args:
          inputs: List of task runs to execute.

          default_task_spec: Specification for a task.

              Auto output schemas can be specified by setting `output_schema={"type":"auto"}`.
              Not specifying a TaskSpec is the same as setting an auto output schema.

              For convenience bare strings are also accepted as input or output schemas.

          betas: Optional header to specify the beta version(s) to enable.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not task_group_id:
            raise ValueError(f"Expected a non-empty value for `task_group_id` but received {task_group_id!r}")
        extra_headers = {
            **strip_not_given({"parallel-beta": ",".join(str(e) for e in betas) if is_given(betas) else not_given}),
            **(extra_headers or {}),
        }
        return await self._post(
            f"/v1beta/tasks/groups/{task_group_id}/runs",
            body=await async_maybe_transform(
                {
                    "inputs": inputs,
                    "default_task_spec": default_task_spec,
                },
                task_group_add_runs_params.TaskGroupAddRunsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskGroupRunResponse,
        )

    async def events(
        self,
        task_group_id: str,
        *,
        last_event_id: Optional[str] | Omit = omit,
        api_timeout: Optional[float] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncStream[TaskGroupEventsResponse]:
        """
        Streams events from a TaskGroup: status updates and run completions.

        The connection will remain open for up to an hour as long as at least one run in
        the group is still active.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not task_group_id:
            raise ValueError(f"Expected a non-empty value for `task_group_id` but received {task_group_id!r}")
        extra_headers = {"Accept": "text/event-stream", **(extra_headers or {})}
        return await self._get(
            f"/v1beta/tasks/groups/{task_group_id}/events",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "last_event_id": last_event_id,
                        "api_timeout": api_timeout,
                    },
                    task_group_events_params.TaskGroupEventsParams,
                ),
            ),
            cast_to=cast(
                Any, TaskGroupEventsResponse
            ),  # Union types cannot be passed in as arguments in the type system
            stream=True,
            stream_cls=AsyncStream[TaskGroupEventsResponse],
        )

    async def get_runs(
        self,
        task_group_id: str,
        *,
        include_input: bool | Omit = omit,
        include_output: bool | Omit = omit,
        last_event_id: Optional[str] | Omit = omit,
        status: Optional[
            Literal["queued", "action_required", "running", "completed", "failed", "cancelling", "cancelled"]
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncStream[TaskGroupGetRunsResponse]:
        """
        Retrieves task runs in a TaskGroup and optionally their inputs and outputs.

        All runs within a TaskGroup are returned as a stream. To get the inputs and/or
        outputs back in the stream, set the corresponding `include_input` and
        `include_output` parameters to `true`.

        The stream is resumable using the `event_id` as the cursor. To resume a stream,
        specify the `last_event_id` parameter with the `event_id` of the last event in
        the stream. The stream will resume from the next event after the
        `last_event_id`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not task_group_id:
            raise ValueError(f"Expected a non-empty value for `task_group_id` but received {task_group_id!r}")
        extra_headers = {"Accept": "text/event-stream", **(extra_headers or {})}
        return await self._get(
            f"/v1beta/tasks/groups/{task_group_id}/runs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "include_input": include_input,
                        "include_output": include_output,
                        "last_event_id": last_event_id,
                        "status": status,
                    },
                    task_group_get_runs_params.TaskGroupGetRunsParams,
                ),
            ),
            cast_to=cast(
                Any, TaskGroupGetRunsResponse
            ),  # Union types cannot be passed in as arguments in the type system
            stream=True,
            stream_cls=AsyncStream[TaskGroupGetRunsResponse],
        )


class TaskGroupResourceWithRawResponse:
    def __init__(self, task_group: TaskGroupResource) -> None:
        self._task_group = task_group

        self.create = to_raw_response_wrapper(
            task_group.create,
        )
        self.retrieve = to_raw_response_wrapper(
            task_group.retrieve,
        )
        self.add_runs = to_raw_response_wrapper(
            task_group.add_runs,
        )
        self.events = to_raw_response_wrapper(
            task_group.events,
        )
        self.get_runs = to_raw_response_wrapper(
            task_group.get_runs,
        )


class AsyncTaskGroupResourceWithRawResponse:
    def __init__(self, task_group: AsyncTaskGroupResource) -> None:
        self._task_group = task_group

        self.create = async_to_raw_response_wrapper(
            task_group.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            task_group.retrieve,
        )
        self.add_runs = async_to_raw_response_wrapper(
            task_group.add_runs,
        )
        self.events = async_to_raw_response_wrapper(
            task_group.events,
        )
        self.get_runs = async_to_raw_response_wrapper(
            task_group.get_runs,
        )


class TaskGroupResourceWithStreamingResponse:
    def __init__(self, task_group: TaskGroupResource) -> None:
        self._task_group = task_group

        self.create = to_streamed_response_wrapper(
            task_group.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            task_group.retrieve,
        )
        self.add_runs = to_streamed_response_wrapper(
            task_group.add_runs,
        )
        self.events = to_streamed_response_wrapper(
            task_group.events,
        )
        self.get_runs = to_streamed_response_wrapper(
            task_group.get_runs,
        )


class AsyncTaskGroupResourceWithStreamingResponse:
    def __init__(self, task_group: AsyncTaskGroupResource) -> None:
        self._task_group = task_group

        self.create = async_to_streamed_response_wrapper(
            task_group.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            task_group.retrieve,
        )
        self.add_runs = async_to_streamed_response_wrapper(
            task_group.add_runs,
        )
        self.events = async_to_streamed_response_wrapper(
            task_group.events,
        )
        self.get_runs = async_to_streamed_response_wrapper(
            task_group.get_runs,
        )
