# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from .task_run import (
    TaskRunResource,
    AsyncTaskRunResource,
    TaskRunResourceWithRawResponse,
    AsyncTaskRunResourceWithRawResponse,
    TaskRunResourceWithStreamingResponse,
    AsyncTaskRunResourceWithStreamingResponse,
)
from ..._compat import cached_property
from .task_group import (
    TaskGroupResource,
    AsyncTaskGroupResource,
    TaskGroupResourceWithRawResponse,
    AsyncTaskGroupResourceWithRawResponse,
    TaskGroupResourceWithStreamingResponse,
    AsyncTaskGroupResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.beta import beta_search_params
from ..._base_client import make_request_options
from ...types.beta.search_result import SearchResult
from ...types.shared_params.source_policy import SourcePolicy

__all__ = ["BetaResource", "AsyncBetaResource"]


class BetaResource(SyncAPIResource):
    @cached_property
    def task_run(self) -> TaskRunResource:
        return TaskRunResource(self._client)

    @cached_property
    def task_group(self) -> TaskGroupResource:
        return TaskGroupResource(self._client)

    @cached_property
    def with_raw_response(self) -> BetaResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/parallel-web/parallel-sdk-python#accessing-raw-response-data-eg-headers
        """
        return BetaResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BetaResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/parallel-web/parallel-sdk-python#with_streaming_response
        """
        return BetaResourceWithStreamingResponse(self)

    def search(
        self,
        *,
        max_chars_per_result: Optional[int] | Omit = omit,
        max_results: Optional[int] | Omit = omit,
        objective: Optional[str] | Omit = omit,
        processor: Literal["base", "pro"] | Omit = omit,
        search_queries: Optional[SequenceNotStr[str]] | Omit = omit,
        source_policy: Optional[SourcePolicy] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SearchResult:
        """
        Searches the web.

        Args:
          max_chars_per_result: Upper bound on the number of characters to include in excerpts for each search
              result.

          max_results: Upper bound on the number of results to return. May be limited by the processor.
              Defaults to 10 if not provided.

          objective: Natural-language description of what the web search is trying to find. May
              include guidance about preferred sources or freshness. At least one of objective
              or search_queries must be provided.

          processor: Search processor.

          search_queries: Optional list of traditional keyword search queries to guide the search. May
              contain search operators. At least one of objective or search_queries must be
              provided.

          source_policy: Source policy for web search results.

              This policy governs which sources are allowed/disallowed in results.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1beta/search",
            body=maybe_transform(
                {
                    "max_chars_per_result": max_chars_per_result,
                    "max_results": max_results,
                    "objective": objective,
                    "processor": processor,
                    "search_queries": search_queries,
                    "source_policy": source_policy,
                },
                beta_search_params.BetaSearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SearchResult,
        )


class AsyncBetaResource(AsyncAPIResource):
    @cached_property
    def task_run(self) -> AsyncTaskRunResource:
        return AsyncTaskRunResource(self._client)

    @cached_property
    def task_group(self) -> AsyncTaskGroupResource:
        return AsyncTaskGroupResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncBetaResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/parallel-web/parallel-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBetaResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBetaResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/parallel-web/parallel-sdk-python#with_streaming_response
        """
        return AsyncBetaResourceWithStreamingResponse(self)

    async def search(
        self,
        *,
        max_chars_per_result: Optional[int] | Omit = omit,
        max_results: Optional[int] | Omit = omit,
        objective: Optional[str] | Omit = omit,
        processor: Literal["base", "pro"] | Omit = omit,
        search_queries: Optional[SequenceNotStr[str]] | Omit = omit,
        source_policy: Optional[SourcePolicy] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SearchResult:
        """
        Searches the web.

        Args:
          max_chars_per_result: Upper bound on the number of characters to include in excerpts for each search
              result.

          max_results: Upper bound on the number of results to return. May be limited by the processor.
              Defaults to 10 if not provided.

          objective: Natural-language description of what the web search is trying to find. May
              include guidance about preferred sources or freshness. At least one of objective
              or search_queries must be provided.

          processor: Search processor.

          search_queries: Optional list of traditional keyword search queries to guide the search. May
              contain search operators. At least one of objective or search_queries must be
              provided.

          source_policy: Source policy for web search results.

              This policy governs which sources are allowed/disallowed in results.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1beta/search",
            body=await async_maybe_transform(
                {
                    "max_chars_per_result": max_chars_per_result,
                    "max_results": max_results,
                    "objective": objective,
                    "processor": processor,
                    "search_queries": search_queries,
                    "source_policy": source_policy,
                },
                beta_search_params.BetaSearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SearchResult,
        )


class BetaResourceWithRawResponse:
    def __init__(self, beta: BetaResource) -> None:
        self._beta = beta

        self.search = to_raw_response_wrapper(
            beta.search,
        )

    @cached_property
    def task_run(self) -> TaskRunResourceWithRawResponse:
        return TaskRunResourceWithRawResponse(self._beta.task_run)

    @cached_property
    def task_group(self) -> TaskGroupResourceWithRawResponse:
        return TaskGroupResourceWithRawResponse(self._beta.task_group)


class AsyncBetaResourceWithRawResponse:
    def __init__(self, beta: AsyncBetaResource) -> None:
        self._beta = beta

        self.search = async_to_raw_response_wrapper(
            beta.search,
        )

    @cached_property
    def task_run(self) -> AsyncTaskRunResourceWithRawResponse:
        return AsyncTaskRunResourceWithRawResponse(self._beta.task_run)

    @cached_property
    def task_group(self) -> AsyncTaskGroupResourceWithRawResponse:
        return AsyncTaskGroupResourceWithRawResponse(self._beta.task_group)


class BetaResourceWithStreamingResponse:
    def __init__(self, beta: BetaResource) -> None:
        self._beta = beta

        self.search = to_streamed_response_wrapper(
            beta.search,
        )

    @cached_property
    def task_run(self) -> TaskRunResourceWithStreamingResponse:
        return TaskRunResourceWithStreamingResponse(self._beta.task_run)

    @cached_property
    def task_group(self) -> TaskGroupResourceWithStreamingResponse:
        return TaskGroupResourceWithStreamingResponse(self._beta.task_group)


class AsyncBetaResourceWithStreamingResponse:
    def __init__(self, beta: AsyncBetaResource) -> None:
        self._beta = beta

        self.search = async_to_streamed_response_wrapper(
            beta.search,
        )

    @cached_property
    def task_run(self) -> AsyncTaskRunResourceWithStreamingResponse:
        return AsyncTaskRunResourceWithStreamingResponse(self._beta.task_run)

    @cached_property
    def task_group(self) -> AsyncTaskGroupResourceWithStreamingResponse:
        return AsyncTaskGroupResourceWithStreamingResponse(self._beta.task_group)
