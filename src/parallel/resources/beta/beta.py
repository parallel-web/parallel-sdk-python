# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from itertools import chain
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import is_given, maybe_transform, strip_not_given, async_maybe_transform
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
from ...types.beta import beta_search_params, beta_extract_params
from ..._base_client import make_request_options
from ...types.beta.search_result import SearchResult
from ...types.beta.extract_response import ExtractResponse
from ...types.beta.fetch_policy_param import FetchPolicyParam
from ...types.beta.parallel_beta_param import ParallelBetaParam
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

    def extract(
        self,
        *,
        urls: SequenceNotStr[str],
        excerpts: beta_extract_params.Excerpts | Omit = omit,
        fetch_policy: Optional[FetchPolicyParam] | Omit = omit,
        full_content: beta_extract_params.FullContent | Omit = omit,
        objective: Optional[str] | Omit = omit,
        search_queries: Optional[SequenceNotStr[str]] | Omit = omit,
        betas: List[ParallelBetaParam] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExtractResponse:
        """
        Extracts relevant content from specific web URLs.

        To access this endpoint, pass the `parallel-beta` header with the value
        `search-extract-2025-10-10`.

        Args:
          excerpts: Include excerpts from each URL relevant to the search objective and queries.
              Note that if neither objective nor search_queries is provided, excerpts are
              redundant with full content.

          fetch_policy: Fetch policy.

              Determines when to return content from the cache (faster) vs fetching live
              content (fresher).

          full_content: Include full content from each URL. Note that if neither objective nor
              search_queries is provided, excerpts are redundant with full content.

          objective: If provided, focuses extracted content on the specified search objective.

          search_queries: If provided, focuses extracted content on the specified keyword search queries.

          betas: Optional header to specify the beta version(s) to enable.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given(
                {
                    "parallel-beta": ",".join(chain((str(e) for e in betas), ["search-extract-2025-10-10"]))
                    if is_given(betas)
                    else not_given
                }
            ),
            **(extra_headers or {}),
        }
        extra_headers = {"parallel-beta": "search-extract-2025-10-10", **(extra_headers or {})}
        return self._post(
            "/v1beta/extract",
            body=maybe_transform(
                {
                    "urls": urls,
                    "excerpts": excerpts,
                    "fetch_policy": fetch_policy,
                    "full_content": full_content,
                    "objective": objective,
                    "search_queries": search_queries,
                },
                beta_extract_params.BetaExtractParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExtractResponse,
        )

    def search(
        self,
        *,
        max_chars_per_result: Optional[int] | Omit = omit,
        max_results: Optional[int] | Omit = omit,
        objective: Optional[str] | Omit = omit,
        processor: Optional[Literal["base", "pro"]] | Omit = omit,
        search_queries: Optional[SequenceNotStr[str]] | Omit = omit,
        source_policy: Optional[SourcePolicy] | Omit = omit,
        betas: List[ParallelBetaParam] | Omit = omit,
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

          betas: Optional header to specify the beta version(s) to enable.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given(
                {
                    "parallel-beta": ",".join(chain((str(e) for e in betas), ["search-extract-2025-10-10"]))
                    if is_given(betas)
                    else not_given
                }
            ),
            **(extra_headers or {}),
        }
        extra_headers = {"parallel-beta": "search-extract-2025-10-10", **(extra_headers or {})}
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

    async def extract(
        self,
        *,
        urls: SequenceNotStr[str],
        excerpts: beta_extract_params.Excerpts | Omit = omit,
        fetch_policy: Optional[FetchPolicyParam] | Omit = omit,
        full_content: beta_extract_params.FullContent | Omit = omit,
        objective: Optional[str] | Omit = omit,
        search_queries: Optional[SequenceNotStr[str]] | Omit = omit,
        betas: List[ParallelBetaParam] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExtractResponse:
        """
        Extracts relevant content from specific web URLs.

        To access this endpoint, pass the `parallel-beta` header with the value
        `search-extract-2025-10-10`.

        Args:
          excerpts: Include excerpts from each URL relevant to the search objective and queries.
              Note that if neither objective nor search_queries is provided, excerpts are
              redundant with full content.

          fetch_policy: Fetch policy.

              Determines when to return content from the cache (faster) vs fetching live
              content (fresher).

          full_content: Include full content from each URL. Note that if neither objective nor
              search_queries is provided, excerpts are redundant with full content.

          objective: If provided, focuses extracted content on the specified search objective.

          search_queries: If provided, focuses extracted content on the specified keyword search queries.

          betas: Optional header to specify the beta version(s) to enable.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given(
                {
                    "parallel-beta": ",".join(chain((str(e) for e in betas), ["search-extract-2025-10-10"]))
                    if is_given(betas)
                    else not_given
                }
            ),
            **(extra_headers or {}),
        }
        extra_headers = {"parallel-beta": "search-extract-2025-10-10", **(extra_headers or {})}
        return await self._post(
            "/v1beta/extract",
            body=await async_maybe_transform(
                {
                    "urls": urls,
                    "excerpts": excerpts,
                    "fetch_policy": fetch_policy,
                    "full_content": full_content,
                    "objective": objective,
                    "search_queries": search_queries,
                },
                beta_extract_params.BetaExtractParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExtractResponse,
        )

    async def search(
        self,
        *,
        max_chars_per_result: Optional[int] | Omit = omit,
        max_results: Optional[int] | Omit = omit,
        objective: Optional[str] | Omit = omit,
        processor: Optional[Literal["base", "pro"]] | Omit = omit,
        search_queries: Optional[SequenceNotStr[str]] | Omit = omit,
        source_policy: Optional[SourcePolicy] | Omit = omit,
        betas: List[ParallelBetaParam] | Omit = omit,
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

          betas: Optional header to specify the beta version(s) to enable.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given(
                {
                    "parallel-beta": ",".join(chain((str(e) for e in betas), ["search-extract-2025-10-10"]))
                    if is_given(betas)
                    else not_given
                }
            ),
            **(extra_headers or {}),
        }
        extra_headers = {"parallel-beta": "search-extract-2025-10-10", **(extra_headers or {})}
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

        self.extract = to_raw_response_wrapper(
            beta.extract,
        )
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

        self.extract = async_to_raw_response_wrapper(
            beta.extract,
        )
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

        self.extract = to_streamed_response_wrapper(
            beta.extract,
        )
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

        self.extract = async_to_streamed_response_wrapper(
            beta.extract,
        )
        self.search = async_to_streamed_response_wrapper(
            beta.search,
        )

    @cached_property
    def task_run(self) -> AsyncTaskRunResourceWithStreamingResponse:
        return AsyncTaskRunResourceWithStreamingResponse(self._beta.task_run)

    @cached_property
    def task_group(self) -> AsyncTaskGroupResourceWithStreamingResponse:
        return AsyncTaskGroupResourceWithStreamingResponse(self._beta.task_group)
