# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Dict, List, Union, Iterable, Optional, cast

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
from ...types.beta import task_run_create_params, task_run_result_params
from ..._base_client import make_request_options
from ...types.task_run import TaskRun
from ...types.task_spec_param import TaskSpecParam
from ...types.beta.webhook_param import WebhookParam
from ...types.beta.mcp_server_param import McpServerParam
from ...types.beta.parallel_beta_param import ParallelBetaParam
from ...types.beta.beta_task_run_result import BetaTaskRunResult
from ...types.shared_params.source_policy import SourcePolicy
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

    def create(
        self,
        *,
        input: Union[str, Dict[str, object]],
        processor: str,
        enable_events: Optional[bool] | Omit = omit,
        mcp_servers: Optional[Iterable[McpServerParam]] | Omit = omit,
        metadata: Optional[Dict[str, Union[str, float, bool]]] | Omit = omit,
        source_policy: Optional[SourcePolicy] | Omit = omit,
        task_spec: Optional[TaskSpecParam] | Omit = omit,
        webhook: Optional[WebhookParam] | Omit = omit,
        betas: List[ParallelBetaParam] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskRun:
        """
        Initiates a task run.

        Returns immediately with a run object in status 'queued'.

        Beta features can be enabled by setting the 'parallel-beta' header.

        Args:
          input: Input to the task, either text or a JSON object.

          processor: Processor to use for the task.

          enable_events: Controls tracking of task run execution progress. When set to true, progress
              events are recorded and can be accessed via the
              [Task Run events](https://platform.parallel.ai/api-reference) endpoint. When
              false, no progress events are tracked. Note that progress tracking cannot be
              enabled after a run has been created. The flag is set to true by default for
              premium processors (pro and above). To enable this feature in your requests,
              specify `events-sse-2025-07-24` as one of the values in `parallel-beta` header
              (for API calls) or `betas` param (for the SDKs).

          mcp_servers: Optional list of MCP servers to use for the run. To enable this feature in your
              requests, specify `mcp-server-2025-07-17` as one of the values in
              `parallel-beta` header (for API calls) or `betas` param (for the SDKs).

          metadata: User-provided metadata stored with the run. Keys and values must be strings with
              a maximum length of 16 and 512 characters respectively.

          source_policy: Source policy for web search results.

              This policy governs which sources are allowed/disallowed in results.

          task_spec: Specification for a task.

              Auto output schemas can be specified by setting `output_schema={"type":"auto"}`.
              Not specifying a TaskSpec is the same as setting an auto output schema.

              For convenience bare strings are also accepted as input or output schemas.

          webhook: Webhooks for Task Runs.

          betas: Optional header to specify the beta version(s) to enable.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given({"parallel-beta": ",".join(str(e) for e in betas) if is_given(betas) else not_given}),
            **(extra_headers or {}),
        }
        return self._post(
            "/v1/tasks/runs?beta=true",
            body=maybe_transform(
                {
                    "input": input,
                    "processor": processor,
                    "enable_events": enable_events,
                    "mcp_servers": mcp_servers,
                    "metadata": metadata,
                    "source_policy": source_policy,
                    "task_spec": task_spec,
                    "webhook": webhook,
                },
                task_run_create_params.TaskRunCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskRun,
        )

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
        return self._get(
            f"/v1beta/tasks/runs/{run_id}/events",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=cast(Any, TaskRunEventsResponse),  # Union types cannot be passed in as arguments in the type system
            stream=True,
            stream_cls=Stream[TaskRunEventsResponse],
        )

    def result(
        self,
        run_id: str,
        *,
        api_timeout: int | Omit = omit,
        betas: List[ParallelBetaParam] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BetaTaskRunResult:
        """
        Retrieves a run result by run_id, blocking until the run is completed.

        Args:
          betas: Optional header to specify the beta version(s) to enable.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not run_id:
            raise ValueError(f"Expected a non-empty value for `run_id` but received {run_id!r}")
        extra_headers = {
            **strip_not_given({"parallel-beta": ",".join(str(e) for e in betas) if is_given(betas) else not_given}),
            **(extra_headers or {}),
        }
        return self._get(
            f"/v1/tasks/runs/{run_id}/result?beta=true",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"api_timeout": api_timeout}, task_run_result_params.TaskRunResultParams),
            ),
            cast_to=BetaTaskRunResult,
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

    async def create(
        self,
        *,
        input: Union[str, Dict[str, object]],
        processor: str,
        enable_events: Optional[bool] | Omit = omit,
        mcp_servers: Optional[Iterable[McpServerParam]] | Omit = omit,
        metadata: Optional[Dict[str, Union[str, float, bool]]] | Omit = omit,
        source_policy: Optional[SourcePolicy] | Omit = omit,
        task_spec: Optional[TaskSpecParam] | Omit = omit,
        webhook: Optional[WebhookParam] | Omit = omit,
        betas: List[ParallelBetaParam] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskRun:
        """
        Initiates a task run.

        Returns immediately with a run object in status 'queued'.

        Beta features can be enabled by setting the 'parallel-beta' header.

        Args:
          input: Input to the task, either text or a JSON object.

          processor: Processor to use for the task.

          enable_events: Controls tracking of task run execution progress. When set to true, progress
              events are recorded and can be accessed via the
              [Task Run events](https://platform.parallel.ai/api-reference) endpoint. When
              false, no progress events are tracked. Note that progress tracking cannot be
              enabled after a run has been created. The flag is set to true by default for
              premium processors (pro and above). To enable this feature in your requests,
              specify `events-sse-2025-07-24` as one of the values in `parallel-beta` header
              (for API calls) or `betas` param (for the SDKs).

          mcp_servers: Optional list of MCP servers to use for the run. To enable this feature in your
              requests, specify `mcp-server-2025-07-17` as one of the values in
              `parallel-beta` header (for API calls) or `betas` param (for the SDKs).

          metadata: User-provided metadata stored with the run. Keys and values must be strings with
              a maximum length of 16 and 512 characters respectively.

          source_policy: Source policy for web search results.

              This policy governs which sources are allowed/disallowed in results.

          task_spec: Specification for a task.

              Auto output schemas can be specified by setting `output_schema={"type":"auto"}`.
              Not specifying a TaskSpec is the same as setting an auto output schema.

              For convenience bare strings are also accepted as input or output schemas.

          webhook: Webhooks for Task Runs.

          betas: Optional header to specify the beta version(s) to enable.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given({"parallel-beta": ",".join(str(e) for e in betas) if is_given(betas) else not_given}),
            **(extra_headers or {}),
        }
        return await self._post(
            "/v1/tasks/runs?beta=true",
            body=await async_maybe_transform(
                {
                    "input": input,
                    "processor": processor,
                    "enable_events": enable_events,
                    "mcp_servers": mcp_servers,
                    "metadata": metadata,
                    "source_policy": source_policy,
                    "task_spec": task_spec,
                    "webhook": webhook,
                },
                task_run_create_params.TaskRunCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskRun,
        )

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
        return await self._get(
            f"/v1beta/tasks/runs/{run_id}/events",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=cast(Any, TaskRunEventsResponse),  # Union types cannot be passed in as arguments in the type system
            stream=True,
            stream_cls=AsyncStream[TaskRunEventsResponse],
        )

    async def result(
        self,
        run_id: str,
        *,
        api_timeout: int | Omit = omit,
        betas: List[ParallelBetaParam] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BetaTaskRunResult:
        """
        Retrieves a run result by run_id, blocking until the run is completed.

        Args:
          betas: Optional header to specify the beta version(s) to enable.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not run_id:
            raise ValueError(f"Expected a non-empty value for `run_id` but received {run_id!r}")
        extra_headers = {
            **strip_not_given({"parallel-beta": ",".join(str(e) for e in betas) if is_given(betas) else not_given}),
            **(extra_headers or {}),
        }
        return await self._get(
            f"/v1/tasks/runs/{run_id}/result?beta=true",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"api_timeout": api_timeout}, task_run_result_params.TaskRunResultParams
                ),
            ),
            cast_to=BetaTaskRunResult,
        )


class TaskRunResourceWithRawResponse:
    def __init__(self, task_run: TaskRunResource) -> None:
        self._task_run = task_run

        self.create = to_raw_response_wrapper(
            task_run.create,
        )
        self.events = to_raw_response_wrapper(
            task_run.events,
        )
        self.result = to_raw_response_wrapper(
            task_run.result,
        )


class AsyncTaskRunResourceWithRawResponse:
    def __init__(self, task_run: AsyncTaskRunResource) -> None:
        self._task_run = task_run

        self.create = async_to_raw_response_wrapper(
            task_run.create,
        )
        self.events = async_to_raw_response_wrapper(
            task_run.events,
        )
        self.result = async_to_raw_response_wrapper(
            task_run.result,
        )


class TaskRunResourceWithStreamingResponse:
    def __init__(self, task_run: TaskRunResource) -> None:
        self._task_run = task_run

        self.create = to_streamed_response_wrapper(
            task_run.create,
        )
        self.events = to_streamed_response_wrapper(
            task_run.events,
        )
        self.result = to_streamed_response_wrapper(
            task_run.result,
        )


class AsyncTaskRunResourceWithStreamingResponse:
    def __init__(self, task_run: AsyncTaskRunResource) -> None:
        self._task_run = task_run

        self.create = async_to_streamed_response_wrapper(
            task_run.create,
        )
        self.events = async_to_streamed_response_wrapper(
            task_run.events,
        )
        self.result = async_to_streamed_response_wrapper(
            task_run.result,
        )
