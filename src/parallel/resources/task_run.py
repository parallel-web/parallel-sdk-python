# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import time
from typing import Dict, Type, Union, Optional, overload

import httpx

from parallel.lib._time import prepare_timeout_float

from ..types import task_run_create_params, task_run_result_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.task_run import TaskRun
from ..types.task_run_result import TaskRunResult
from ..types.task_spec_param import OutputT, OutputSchema, TaskSpecParam
from ..lib._parsing._task_spec import build_task_spec_param
from ..types.parsed_task_run_result import ParsedTaskRunResult
from ..lib._parsing._task_run_result import (
    wait_for_result as _wait_for_result,
    wait_for_result_async as _wait_for_result_async,
    task_run_result_parser,
)
from ..types.shared_params.source_policy import SourcePolicy

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
        metadata: Optional[Dict[str, Union[str, float, bool]]] | Omit = omit,
        source_policy: Optional[SourcePolicy] | Omit = omit,
        task_spec: Optional[TaskSpecParam] | Omit = omit,
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

          metadata: User-provided metadata stored with the run. Keys and values must be strings with
              a maximum length of 16 and 512 characters respectively.

          source_policy: Source policy for web search results.

              This policy governs which sources are allowed/disallowed in results.

          task_spec: Specification for a task.

              Auto output schemas can be specified by setting `output_schema={"type":"auto"}`.
              Not specifying a TaskSpec is the same as setting an auto output schema.

              For convenience bare strings are also accepted as input or output schemas.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/tasks/runs",
            body=maybe_transform(
                {
                    "input": input,
                    "processor": processor,
                    "metadata": metadata,
                    "source_policy": source_policy,
                    "task_spec": task_spec,
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
            f"/v1/tasks/runs/{run_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskRun,
        )

    def result(
        self,
        run_id: str,
        *,
        api_timeout: int | Omit = omit,
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
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not run_id:
            raise ValueError(f"Expected a non-empty value for `run_id` but received {run_id!r}")
        return self._get(
            f"/v1/tasks/runs/{run_id}/result",
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
        metadata: Optional[Dict[str, Union[str, float, bool]]] | Omit = omit,
        source_policy: Optional[SourcePolicy] | Omit = omit,
        task_spec: Optional[TaskSpecParam] | Omit = omit,
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

          metadata: User-provided metadata stored with the run. Keys and values must be strings with
              a maximum length of 16 and 512 characters respectively.

          source_policy: Source policy for web search results.

              This policy governs which sources are allowed/disallowed in results.

          task_spec: Specification for a task.

              Auto output schemas can be specified by setting `output_schema={"type":"auto"}`.
              Not specifying a TaskSpec is the same as setting an auto output schema.

              For convenience bare strings are also accepted as input or output schemas.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/tasks/runs",
            body=await async_maybe_transform(
                {
                    "input": input,
                    "processor": processor,
                    "metadata": metadata,
                    "source_policy": source_policy,
                    "task_spec": task_spec,
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
            f"/v1/tasks/runs/{run_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskRun,
        )

    async def result(
        self,
        run_id: str,
        *,
        api_timeout: int | Omit = omit,
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
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not run_id:
            raise ValueError(f"Expected a non-empty value for `run_id` but received {run_id!r}")
        return await self._get(
            f"/v1/tasks/runs/{run_id}/result",
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
        self.result = async_to_streamed_response_wrapper(
            task_run.result,
        )
