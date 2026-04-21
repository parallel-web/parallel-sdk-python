# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import time
from typing import Any, Dict, List, Type, Union, Iterable, Optional, cast, overload

import httpx

from parallel.lib._time import prepare_timeout_float

from ..types import task_run_create_params, task_run_result_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import is_given, path_template, maybe_transform, strip_not_given, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._streaming import Stream, AsyncStream
from .._base_client import make_request_options
from ..types.task_run import TaskRun
from ..types.webhook_param import WebhookParam
from ..types.task_run_result import TaskRunResult
from ..types.task_spec_param import OutputT, OutputSchema, TaskSpecParam
from ..types.mcp_server_param import McpServerParam
from ..lib._parsing._task_spec import build_task_spec_param
from ..types.parsed_task_run_result import ParsedTaskRunResult
from ..lib._parsing._task_run_result import (
    wait_for_result as _wait_for_result,
    wait_for_result_async as _wait_for_result_async,
    task_run_result_parser,
)
from ..types.beta.parallel_beta_param import ParallelBetaParam
from ..types.task_run_events_response import TaskRunEventsResponse
from ..types.shared_params.source_policy import SourcePolicy

__all__ = ["TaskRunResource", "AsyncTaskRunResource"]


class TaskRunResource(SyncAPIResource):
    """The Task API executes web research and extraction tasks.

    Clients submit a natural-language objective with an optional input schema; the service plans retrieval, fetches relevant URLs, and returns outputs that conform to a provided or inferred JSON schema. Supports deep research style queries and can return rich structured JSON outputs. Processors trade-off between cost, latency, and quality. Each processor supports calibrated confidences.
    - Output metadata: citations, excerpts, reasoning, and confidence per field

    Task Groups enable batch execution of many independent Task runs with group-level monitoring and failure handling.
     - Submit hundreds or thousands of Tasks as a single group
    - Observe group progress and receive results as they complete
    - Real-time updates via Server-Sent Events (SSE)
    - Add tasks to an existing group while it is running
    - Group-level retry and error aggregation
    """

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
        advanced_settings: Optional[task_run_create_params.AdvancedSettings] | Omit = omit,
        enable_events: Optional[bool] | Omit = omit,
        mcp_servers: Optional[Iterable[McpServerParam]] | Omit = omit,
        metadata: Optional[Dict[str, Union[str, float, bool]]] | Omit = omit,
        previous_interaction_id: Optional[str] | Omit = omit,
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

          advanced_settings: Advanced search configuration for a task run.

          enable_events: Controls tracking of task run execution progress. When set to true, progress
              events are recorded and can be accessed via the
              [Task Run events](https://docs.parallel.ai/api-reference) endpoint. When false,
              no progress events are tracked. Note that progress tracking cannot be enabled
              after a run has been created. The flag is set to true by default for premium
              processors (pro and above).

          mcp_servers: Optional list of MCP servers to use for the run.

          metadata: User-provided metadata stored with the run. Keys and values must be strings with
              a maximum length of 16 and 512 characters respectively.

          previous_interaction_id: Interaction ID to use as context for this request.

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
            "/v1/tasks/runs",
            body=maybe_transform(
                {
                    "input": input,
                    "processor": processor,
                    "advanced_settings": advanced_settings,
                    "enable_events": enable_events,
                    "mcp_servers": mcp_servers,
                    "metadata": metadata,
                    "previous_interaction_id": previous_interaction_id,
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

    def retrieve(
        self,
        run_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskRun:
        """
        Retrieves run status by run_id.

        The run result is available from the `/result` endpoint.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not run_id:
            raise ValueError(f"Expected a non-empty value for `run_id` but received {run_id!r}")
        return self._get(
            path_template("/v1/tasks/runs/{run_id}", run_id=run_id),
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
            path_template("/v1/tasks/runs/{run_id}/events", run_id=run_id),
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
    ) -> TaskRunResult:
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
            path_template("/v1/tasks/runs/{run_id}/result", run_id=run_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"api_timeout": api_timeout}, task_run_result_params.TaskRunResultParams),
            ),
            cast_to=TaskRunResult,
        )

    def _wait_for_result(
        self,
        *,
        run_id: str,
        deadline: float,
        output: Optional[OutputSchema] | Type[OutputT] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> TaskRunResult | ParsedTaskRunResult[OutputT]:
        """Wait for a task run to complete within the given timeout."""

        def _fetcher(run_id: str, deadline: float) -> TaskRunResult | ParsedTaskRunResult[OutputT]:
            timeout = deadline - time.monotonic()
            task_run_result = self.result(
                run_id,
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            )
            return task_run_result_parser(task_run_result, output)

        return _wait_for_result(run_id=run_id, deadline=deadline, callable=_fetcher)

    @overload
    def execute(
        self,
        *,
        input: Union[str, Dict[str, object]],
        processor: str,
        metadata: Optional[Dict[str, Union[str, float, bool]]] | Omit = omit,
        output: Optional[OutputSchema] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskRunResult: ...
    @overload
    def execute(
        self,
        *,
        input: Union[str, Dict[str, object]],
        processor: str,
        metadata: Optional[Dict[str, Union[str, float, bool]]] | Omit = omit,
        output: Type[OutputT],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ParsedTaskRunResult[OutputT]: ...
    def execute(
        self,
        *,
        input: Union[str, Dict[str, object]],
        processor: str,
        metadata: Optional[Dict[str, Union[str, float, bool]]] | Omit = omit,
        output: Optional[OutputSchema] | Type[OutputT] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskRunResult | ParsedTaskRunResult[OutputT]:
        """
        Convenience method to create and execute a task run in a single call.

        Awaits run completion. If the run is successful, a `ParsedTaskRunResult`
        is returned when a pydantic was specified in `output`. Otherwise, a
        `TaskRunResult` is returned.

        Possible errors:
        - `TimeoutError`: If the run does not finish within the specified timeout.
        - `APIStatusError`: If the API returns a non-200-range status code.
        - `APIConnectionError`: If the connection to the API fails.

        Args:
          input: Input to the task, either text or a JSON object.

          processor: Processor to use for the task.

          metadata: User-provided metadata stored with the run. Keys and values must be strings with
            a maximum length of 16 and 512 characters respectively.

          output: Optional output schema or pydantic type. If pydantic is provided,
            the response will have a parsed field.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds.
            If the result is not available within the timeout, a `TimeoutError` is raised.
        """
        extra_headers = {"X-Stainless-Poll-Helper": "true", **(extra_headers or {})}

        timeout = prepare_timeout_float(timeout)

        deadline = time.monotonic() + timeout
        task_run = self.create(
            input=input,
            processor=processor,
            metadata=metadata,
            task_spec=build_task_spec_param(output, input),
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )

        return self._wait_for_result(
            run_id=task_run.run_id,
            deadline=deadline,
            output=output,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
        )


class AsyncTaskRunResource(AsyncAPIResource):
    """The Task API executes web research and extraction tasks.

    Clients submit a natural-language objective with an optional input schema; the service plans retrieval, fetches relevant URLs, and returns outputs that conform to a provided or inferred JSON schema. Supports deep research style queries and can return rich structured JSON outputs. Processors trade-off between cost, latency, and quality. Each processor supports calibrated confidences.
    - Output metadata: citations, excerpts, reasoning, and confidence per field

    Task Groups enable batch execution of many independent Task runs with group-level monitoring and failure handling.
     - Submit hundreds or thousands of Tasks as a single group
    - Observe group progress and receive results as they complete
    - Real-time updates via Server-Sent Events (SSE)
    - Add tasks to an existing group while it is running
    - Group-level retry and error aggregation
    """

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
        advanced_settings: Optional[task_run_create_params.AdvancedSettings] | Omit = omit,
        enable_events: Optional[bool] | Omit = omit,
        mcp_servers: Optional[Iterable[McpServerParam]] | Omit = omit,
        metadata: Optional[Dict[str, Union[str, float, bool]]] | Omit = omit,
        previous_interaction_id: Optional[str] | Omit = omit,
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

          advanced_settings: Advanced search configuration for a task run.

          enable_events: Controls tracking of task run execution progress. When set to true, progress
              events are recorded and can be accessed via the
              [Task Run events](https://docs.parallel.ai/api-reference) endpoint. When false,
              no progress events are tracked. Note that progress tracking cannot be enabled
              after a run has been created. The flag is set to true by default for premium
              processors (pro and above).

          mcp_servers: Optional list of MCP servers to use for the run.

          metadata: User-provided metadata stored with the run. Keys and values must be strings with
              a maximum length of 16 and 512 characters respectively.

          previous_interaction_id: Interaction ID to use as context for this request.

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
            "/v1/tasks/runs",
            body=await async_maybe_transform(
                {
                    "input": input,
                    "processor": processor,
                    "advanced_settings": advanced_settings,
                    "enable_events": enable_events,
                    "mcp_servers": mcp_servers,
                    "metadata": metadata,
                    "previous_interaction_id": previous_interaction_id,
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

    async def retrieve(
        self,
        run_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskRun:
        """
        Retrieves run status by run_id.

        The run result is available from the `/result` endpoint.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not run_id:
            raise ValueError(f"Expected a non-empty value for `run_id` but received {run_id!r}")
        return await self._get(
            path_template("/v1/tasks/runs/{run_id}", run_id=run_id),
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
            path_template("/v1/tasks/runs/{run_id}/events", run_id=run_id),
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
    ) -> TaskRunResult:
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
            path_template("/v1/tasks/runs/{run_id}/result", run_id=run_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"api_timeout": api_timeout}, task_run_result_params.TaskRunResultParams
                ),
            ),
            cast_to=TaskRunResult,
        )

    async def _wait_for_result(
        self,
        *,
        run_id: str,
        deadline: float,
        output: Optional[OutputSchema] | Type[OutputT] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> TaskRunResult | ParsedTaskRunResult[OutputT]:
        """Wait for a task run to complete within the given timeout."""

        async def _fetcher(run_id: str, deadline: float) -> TaskRunResult | ParsedTaskRunResult[OutputT]:
            timeout = deadline - time.monotonic()
            task_run_result = await self.result(
                run_id,
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            )
            return task_run_result_parser(task_run_result, output)

        return await _wait_for_result_async(run_id=run_id, deadline=deadline, callable=_fetcher)

    @overload
    async def execute(
        self,
        *,
        input: Union[str, Dict[str, object]],
        processor: str,
        metadata: Optional[Dict[str, Union[str, float, bool]]] | Omit = omit,
        output: Optional[OutputSchema] | Omit = omit,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskRunResult: ...
    @overload
    async def execute(
        self,
        *,
        input: Union[str, Dict[str, object]],
        processor: str,
        metadata: Optional[Dict[str, Union[str, float, bool]]] | Omit = omit,
        output: Type[OutputT],
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ParsedTaskRunResult[OutputT]: ...
    async def execute(
        self,
        *,
        input: Union[str, Dict[str, object]],
        processor: str,
        metadata: Optional[Dict[str, Union[str, float, bool]]] | Omit = omit,
        output: Optional[OutputSchema] | Type[OutputT] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TaskRunResult | ParsedTaskRunResult[OutputT]:
        """
        Convenience method to create and execute a task run in a single call.

        Awaits run completion. If the run is successful, a `ParsedTaskRunResult`
        is returned when a pydantic was specified in `output`. Otherwise, a
        `TaskRunResult` is returned.

        Possible errors:
        - `TimeoutError`: If the run does not finish within the specified timeout.
        - `APIStatusError`: If the API returns a non-200-range status code.
        - `APIConnectionError`: If the connection to the API fails.

        Args:
          input: Input to the task, either text or a JSON object.

          processor: Processor to use for the task.

          metadata: User-provided metadata stored with the run. Keys and values must be strings with
            a maximum length of 16 and 512 characters respectively.

          output: Optional output schema or pydantic type. If pydantic is provided,
            the response will have a parsed field.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds.
            If the result is not available within the timeout, a `TimeoutError` is raised.
        """
        extra_headers = {"X-Stainless-Poll-Helper": "true", **(extra_headers or {})}

        timeout = prepare_timeout_float(timeout)
        deadline = time.monotonic() + timeout

        task_run = await self.create(
            input=input,
            processor=processor,
            metadata=metadata,
            task_spec=build_task_spec_param(output, input),
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )

        return await self._wait_for_result(
            run_id=task_run.run_id,
            deadline=deadline,
            output=output,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
        )


class TaskRunResourceWithRawResponse:
    def __init__(self, task_run: TaskRunResource) -> None:
        self._task_run = task_run

        self.create = to_raw_response_wrapper(
            task_run.create,
        )
        self.retrieve = to_raw_response_wrapper(
            task_run.retrieve,
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
        self.retrieve = async_to_raw_response_wrapper(
            task_run.retrieve,
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
        self.retrieve = to_streamed_response_wrapper(
            task_run.retrieve,
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
        self.retrieve = async_to_streamed_response_wrapper(
            task_run.retrieve,
        )
        self.events = async_to_streamed_response_wrapper(
            task_run.events,
        )
        self.result = async_to_streamed_response_wrapper(
            task_run.result,
        )
