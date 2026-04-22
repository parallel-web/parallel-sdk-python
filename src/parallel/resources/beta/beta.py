# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import typing_extensions
from typing import List, Optional
from itertools import chain
from typing_extensions import Literal

import httpx

from .findall import (
    FindAllResource,
    AsyncFindAllResource,
    FindAllResourceWithRawResponse,
    AsyncFindAllResourceWithRawResponse,
    FindAllResourceWithStreamingResponse,
    AsyncFindAllResourceWithStreamingResponse,
)
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
from ...types.fetch_policy_param import FetchPolicyParam
from ...types.beta.extract_response import ExtractResponse
from ...types.beta.parallel_beta_param import ParallelBetaParam
from ...types.beta.excerpt_settings_param import ExcerptSettingsParam
from ...types.shared_params.source_policy import SourcePolicy

__all__ = ["BetaResource", "AsyncBetaResource"]


class BetaResource(SyncAPIResource):
    @cached_property
    def task_run(self) -> TaskRunResource:
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
        return TaskRunResource(self._client)

    @cached_property
    def task_group(self) -> TaskGroupResource:
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
        return TaskGroupResource(self._client)

    @cached_property
    def findall(self) -> FindAllResource:
        """
        The FindAll API discovers and evaluates entities that match complex criteria from natural language objectives. Submit a high-level goal and the service automatically generates structured match conditions, discovers relevant candidates, and evaluates each against the criteria. Returns comprehensive results with detailed reasoning, citations, and confidence scores for each match decision. Streaming events and webhooks are supported.
        """
        return FindAllResource(self._client)

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

    @typing_extensions.deprecated(
        "Use client.extract instead. For more info, see https://docs.parallel.ai/extract/extract-migration-guide"
    )
    def extract(
        self,
        *,
        urls: SequenceNotStr[str],
        client_model: Optional[str] | Omit = omit,
        excerpts: beta_extract_params.Excerpts | Omit = omit,
        fetch_policy: Optional[FetchPolicyParam] | Omit = omit,
        full_content: beta_extract_params.FullContent | Omit = omit,
        objective: Optional[str] | Omit = omit,
        search_queries: Optional[SequenceNotStr[str]] | Omit = omit,
        session_id: Optional[str] | Omit = omit,
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
          client_model: The model generating this request and consuming the results. Enables
              optimizations and tailors default settings for the model's capabilities.

          excerpts: Include excerpts from each URL relevant to the search objective and queries.
              Note that if neither objective nor search_queries is provided, excerpts are
              redundant with full content.

          fetch_policy: Policy for live fetching web results.

          full_content: Include full content from each URL. Note that if neither objective nor
              search_queries is provided, excerpts are redundant with full content.

          objective: If provided, focuses extracted content on the specified search objective.

          search_queries: If provided, focuses extracted content on the specified keyword search queries.

          session_id: Session identifier to track calls across separate search and extract calls, to
              be used as part of a larger task. Specifying it may give better contextual
              results for subsequent API calls.

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
                    "client_model": client_model,
                    "excerpts": excerpts,
                    "fetch_policy": fetch_policy,
                    "full_content": full_content,
                    "objective": objective,
                    "search_queries": search_queries,
                    "session_id": session_id,
                },
                beta_extract_params.BetaExtractParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExtractResponse,
        )

    @typing_extensions.deprecated(
        "Use client.search instead. For more info, see https://docs.parallel.ai/search/search-migration-guide"
    )
    def search(
        self,
        *,
        client_model: Optional[str] | Omit = omit,
        excerpts: ExcerptSettingsParam | Omit = omit,
        fetch_policy: Optional[FetchPolicyParam] | Omit = omit,
        location: Optional[str] | Omit = omit,
        max_chars_per_result: Optional[int] | Omit = omit,
        max_results: Optional[int] | Omit = omit,
        mode: Optional[Literal["one-shot", "agentic", "fast"]] | Omit = omit,
        objective: Optional[str] | Omit = omit,
        processor: Optional[Literal["base", "pro"]] | Omit = omit,
        search_queries: Optional[SequenceNotStr[str]] | Omit = omit,
        session_id: Optional[str] | Omit = omit,
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
          client_model: The model generating this request and consuming the results. Enables
              optimizations and tailors default settings for the model's capabilities.

          excerpts: Optional settings to configure excerpt generation.

          fetch_policy: Policy for live fetching web results.

          location: ISO 3166-1 alpha-2 country code for geo-targeted search results.

          max_chars_per_result: DEPRECATED: Use `excerpts.max_chars_per_result` instead.

          max_results: Upper bound on the number of results to return. Defaults to 10 if not provided.

          mode: Presets default values for parameters for different use cases.

              - `one-shot` returns more comprehensive results and longer excerpts to answer
                questions from a single response
              - `agentic` returns more concise, token-efficient results for use in an agentic
                loop
              - `fast` trades some quality for lower latency, with best results when used with
                concise and high-quality objective and keyword queries

          objective: Natural-language description of what the web search is trying to find. May
              include guidance about preferred sources or freshness. At least one of objective
              or search_queries must be provided.

          processor: DEPRECATED: use `mode` instead.

          search_queries: Optional list of traditional keyword search queries to guide the search. May
              contain search operators. At least one of objective or search_queries must be
              provided.

          session_id: Session identifier to track calls across separate search and extract calls, to
              be used as part of a larger task. Specifying it may give better contextual
              results for subsequent API calls.

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
                    "client_model": client_model,
                    "excerpts": excerpts,
                    "fetch_policy": fetch_policy,
                    "location": location,
                    "max_chars_per_result": max_chars_per_result,
                    "max_results": max_results,
                    "mode": mode,
                    "objective": objective,
                    "processor": processor,
                    "search_queries": search_queries,
                    "session_id": session_id,
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
        return AsyncTaskRunResource(self._client)

    @cached_property
    def task_group(self) -> AsyncTaskGroupResource:
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
        return AsyncTaskGroupResource(self._client)

    @cached_property
    def findall(self) -> AsyncFindAllResource:
        """
        The FindAll API discovers and evaluates entities that match complex criteria from natural language objectives. Submit a high-level goal and the service automatically generates structured match conditions, discovers relevant candidates, and evaluates each against the criteria. Returns comprehensive results with detailed reasoning, citations, and confidence scores for each match decision. Streaming events and webhooks are supported.
        """
        return AsyncFindAllResource(self._client)

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

    @typing_extensions.deprecated(
        "Use client.extract instead. For more info, see https://docs.parallel.ai/extract/extract-migration-guide"
    )
    async def extract(
        self,
        *,
        urls: SequenceNotStr[str],
        client_model: Optional[str] | Omit = omit,
        excerpts: beta_extract_params.Excerpts | Omit = omit,
        fetch_policy: Optional[FetchPolicyParam] | Omit = omit,
        full_content: beta_extract_params.FullContent | Omit = omit,
        objective: Optional[str] | Omit = omit,
        search_queries: Optional[SequenceNotStr[str]] | Omit = omit,
        session_id: Optional[str] | Omit = omit,
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
          client_model: The model generating this request and consuming the results. Enables
              optimizations and tailors default settings for the model's capabilities.

          excerpts: Include excerpts from each URL relevant to the search objective and queries.
              Note that if neither objective nor search_queries is provided, excerpts are
              redundant with full content.

          fetch_policy: Policy for live fetching web results.

          full_content: Include full content from each URL. Note that if neither objective nor
              search_queries is provided, excerpts are redundant with full content.

          objective: If provided, focuses extracted content on the specified search objective.

          search_queries: If provided, focuses extracted content on the specified keyword search queries.

          session_id: Session identifier to track calls across separate search and extract calls, to
              be used as part of a larger task. Specifying it may give better contextual
              results for subsequent API calls.

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
                    "client_model": client_model,
                    "excerpts": excerpts,
                    "fetch_policy": fetch_policy,
                    "full_content": full_content,
                    "objective": objective,
                    "search_queries": search_queries,
                    "session_id": session_id,
                },
                beta_extract_params.BetaExtractParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExtractResponse,
        )

    @typing_extensions.deprecated(
        "Use client.search instead. For more info, see https://docs.parallel.ai/search/search-migration-guide"
    )
    async def search(
        self,
        *,
        client_model: Optional[str] | Omit = omit,
        excerpts: ExcerptSettingsParam | Omit = omit,
        fetch_policy: Optional[FetchPolicyParam] | Omit = omit,
        location: Optional[str] | Omit = omit,
        max_chars_per_result: Optional[int] | Omit = omit,
        max_results: Optional[int] | Omit = omit,
        mode: Optional[Literal["one-shot", "agentic", "fast"]] | Omit = omit,
        objective: Optional[str] | Omit = omit,
        processor: Optional[Literal["base", "pro"]] | Omit = omit,
        search_queries: Optional[SequenceNotStr[str]] | Omit = omit,
        session_id: Optional[str] | Omit = omit,
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
          client_model: The model generating this request and consuming the results. Enables
              optimizations and tailors default settings for the model's capabilities.

          excerpts: Optional settings to configure excerpt generation.

          fetch_policy: Policy for live fetching web results.

          location: ISO 3166-1 alpha-2 country code for geo-targeted search results.

          max_chars_per_result: DEPRECATED: Use `excerpts.max_chars_per_result` instead.

          max_results: Upper bound on the number of results to return. Defaults to 10 if not provided.

          mode: Presets default values for parameters for different use cases.

              - `one-shot` returns more comprehensive results and longer excerpts to answer
                questions from a single response
              - `agentic` returns more concise, token-efficient results for use in an agentic
                loop
              - `fast` trades some quality for lower latency, with best results when used with
                concise and high-quality objective and keyword queries

          objective: Natural-language description of what the web search is trying to find. May
              include guidance about preferred sources or freshness. At least one of objective
              or search_queries must be provided.

          processor: DEPRECATED: use `mode` instead.

          search_queries: Optional list of traditional keyword search queries to guide the search. May
              contain search operators. At least one of objective or search_queries must be
              provided.

          session_id: Session identifier to track calls across separate search and extract calls, to
              be used as part of a larger task. Specifying it may give better contextual
              results for subsequent API calls.

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
                    "client_model": client_model,
                    "excerpts": excerpts,
                    "fetch_policy": fetch_policy,
                    "location": location,
                    "max_chars_per_result": max_chars_per_result,
                    "max_results": max_results,
                    "mode": mode,
                    "objective": objective,
                    "processor": processor,
                    "search_queries": search_queries,
                    "session_id": session_id,
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

        self.extract = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                beta.extract,  # pyright: ignore[reportDeprecated],
            )
        )
        self.search = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                beta.search,  # pyright: ignore[reportDeprecated],
            )
        )

    @cached_property
    def task_run(self) -> TaskRunResourceWithRawResponse:
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
        return TaskRunResourceWithRawResponse(self._beta.task_run)

    @cached_property
    def task_group(self) -> TaskGroupResourceWithRawResponse:
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
        return TaskGroupResourceWithRawResponse(self._beta.task_group)

    @cached_property
    def findall(self) -> FindAllResourceWithRawResponse:
        """
        The FindAll API discovers and evaluates entities that match complex criteria from natural language objectives. Submit a high-level goal and the service automatically generates structured match conditions, discovers relevant candidates, and evaluates each against the criteria. Returns comprehensive results with detailed reasoning, citations, and confidence scores for each match decision. Streaming events and webhooks are supported.
        """
        return FindAllResourceWithRawResponse(self._beta.findall)


class AsyncBetaResourceWithRawResponse:
    def __init__(self, beta: AsyncBetaResource) -> None:
        self._beta = beta

        self.extract = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                beta.extract,  # pyright: ignore[reportDeprecated],
            )
        )
        self.search = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                beta.search,  # pyright: ignore[reportDeprecated],
            )
        )

    @cached_property
    def task_run(self) -> AsyncTaskRunResourceWithRawResponse:
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
        return AsyncTaskRunResourceWithRawResponse(self._beta.task_run)

    @cached_property
    def task_group(self) -> AsyncTaskGroupResourceWithRawResponse:
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
        return AsyncTaskGroupResourceWithRawResponse(self._beta.task_group)

    @cached_property
    def findall(self) -> AsyncFindAllResourceWithRawResponse:
        """
        The FindAll API discovers and evaluates entities that match complex criteria from natural language objectives. Submit a high-level goal and the service automatically generates structured match conditions, discovers relevant candidates, and evaluates each against the criteria. Returns comprehensive results with detailed reasoning, citations, and confidence scores for each match decision. Streaming events and webhooks are supported.
        """
        return AsyncFindAllResourceWithRawResponse(self._beta.findall)


class BetaResourceWithStreamingResponse:
    def __init__(self, beta: BetaResource) -> None:
        self._beta = beta

        self.extract = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                beta.extract,  # pyright: ignore[reportDeprecated],
            )
        )
        self.search = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                beta.search,  # pyright: ignore[reportDeprecated],
            )
        )

    @cached_property
    def task_run(self) -> TaskRunResourceWithStreamingResponse:
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
        return TaskRunResourceWithStreamingResponse(self._beta.task_run)

    @cached_property
    def task_group(self) -> TaskGroupResourceWithStreamingResponse:
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
        return TaskGroupResourceWithStreamingResponse(self._beta.task_group)

    @cached_property
    def findall(self) -> FindAllResourceWithStreamingResponse:
        """
        The FindAll API discovers and evaluates entities that match complex criteria from natural language objectives. Submit a high-level goal and the service automatically generates structured match conditions, discovers relevant candidates, and evaluates each against the criteria. Returns comprehensive results with detailed reasoning, citations, and confidence scores for each match decision. Streaming events and webhooks are supported.
        """
        return FindAllResourceWithStreamingResponse(self._beta.findall)


class AsyncBetaResourceWithStreamingResponse:
    def __init__(self, beta: AsyncBetaResource) -> None:
        self._beta = beta

        self.extract = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                beta.extract,  # pyright: ignore[reportDeprecated],
            )
        )
        self.search = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                beta.search,  # pyright: ignore[reportDeprecated],
            )
        )

    @cached_property
    def task_run(self) -> AsyncTaskRunResourceWithStreamingResponse:
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
        return AsyncTaskRunResourceWithStreamingResponse(self._beta.task_run)

    @cached_property
    def task_group(self) -> AsyncTaskGroupResourceWithStreamingResponse:
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
        return AsyncTaskGroupResourceWithStreamingResponse(self._beta.task_group)

    @cached_property
    def findall(self) -> AsyncFindAllResourceWithStreamingResponse:
        """
        The FindAll API discovers and evaluates entities that match complex criteria from natural language objectives. Submit a high-level goal and the service automatically generates structured match conditions, discovers relevant candidates, and evaluates each against the criteria. Returns comprehensive results with detailed reasoning, citations, and confidence scores for each match decision. Streaming events and webhooks are supported.
        """
        return AsyncFindAllResourceWithStreamingResponse(self._beta.findall)
