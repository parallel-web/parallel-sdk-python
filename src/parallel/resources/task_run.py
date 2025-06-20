# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional

import httpx

from ..types import task_run_create_params, task_run_result_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
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
from ..types.task_spec_param import TaskSpecParam

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
        input: Union[str, object],
        processor: str,
        metadata: Optional[Dict[str, Union[str, float, bool]]] | NotGiven = NOT_GIVEN,
        task_spec: Optional[TaskSpecParam] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskRun:
        """
        Initiates a single task run.

        Args:
          input: Input to the task, either text or a JSON object.

          processor: Processor to use for the task.

          metadata: User-provided metadata stored with the run. Keys and values must be strings with
              a maximum length of 16 and 512 characters respectively.

          task_spec: Specification for a task.

              For convenience we allow bare strings as input or output schemas, which is
              equivalent to a text schema with the same description.

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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskRun:
        """
        Retrieves a run by run_id.

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
        api_timeout: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskRunResult:
        """
        Retrieves a run by run_id, blocking until the run is completed.

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
        input: Union[str, object],
        processor: str,
        metadata: Optional[Dict[str, Union[str, float, bool]]] | NotGiven = NOT_GIVEN,
        task_spec: Optional[TaskSpecParam] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskRun:
        """
        Initiates a single task run.

        Args:
          input: Input to the task, either text or a JSON object.

          processor: Processor to use for the task.

          metadata: User-provided metadata stored with the run. Keys and values must be strings with
              a maximum length of 16 and 512 characters respectively.

          task_spec: Specification for a task.

              For convenience we allow bare strings as input or output schemas, which is
              equivalent to a text schema with the same description.

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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskRun:
        """
        Retrieves a run by run_id.

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
        api_timeout: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskRunResult:
        """
        Retrieves a run by run_id, blocking until the run is completed.

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
