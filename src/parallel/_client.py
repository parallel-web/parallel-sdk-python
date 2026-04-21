# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import TYPE_CHECKING, Any, Mapping, Optional
from typing_extensions import Self, Literal, override

import httpx

from . import _exceptions
from ._qs import Querystring
from .types import client_search_params, client_extract_params
from ._types import (
    Body,
    Omit,
    Query,
    Headers,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    SequenceNotStr,
    omit,
    not_given,
)
from ._utils import (
    is_given,
    maybe_transform,
    get_async_library,
    async_maybe_transform,
)
from ._compat import cached_property
from ._version import __version__
from ._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import ParallelError, APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
    make_request_options,
)
from .types.search_result import SearchResult
from .types.extract_response import ExtractResponse
from .types.advanced_search_settings_param import AdvancedSearchSettingsParam
from .types.advanced_extract_settings_param import AdvancedExtractSettingsParam

if TYPE_CHECKING:
    from .resources import beta, task_run
    from .resources.task_run import TaskRunResource, AsyncTaskRunResource
    from .resources.beta.beta import BetaResource, AsyncBetaResource

__all__ = [
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "Parallel",
    "AsyncParallel",
    "Client",
    "AsyncClient",
]


class Parallel(SyncAPIClient):
    # client options
    api_key: str

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous Parallel client instance.

        This automatically infers the `api_key` argument from the `PARALLEL_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("PARALLEL_API_KEY")
        if api_key is None:
            raise ParallelError(
                "The api_key client option must be set either by passing api_key to the client or by setting the PARALLEL_API_KEY environment variable"
            )
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("PARALLEL_BASE_URL")
        if base_url is None:
            base_url = f"https://api.parallel.ai"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

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
        from .resources.task_run import TaskRunResource

        return TaskRunResource(self)

    @cached_property
    def beta(self) -> BetaResource:
        from .resources.beta import BetaResource

        return BetaResource(self)

    @cached_property
    def with_raw_response(self) -> ParallelWithRawResponse:
        return ParallelWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ParallelWithStreamedResponse:
        return ParallelWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"x-api-key": api_key}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    def extract(
        self,
        *,
        urls: SequenceNotStr[str],
        advanced_settings: Optional[AdvancedExtractSettingsParam] | Omit = omit,
        client_model: Optional[str] | Omit = omit,
        max_chars_total: Optional[int] | Omit = omit,
        objective: Optional[str] | Omit = omit,
        search_queries: Optional[SequenceNotStr[str]] | Omit = omit,
        session_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExtractResponse:
        """
        Extracts relevant content from specific web URLs.

        The legacy Extract API reference (`/v1beta/extract` endpoint) is available
        [here](https://docs.parallel.ai/api-reference/legacy/extract-beta/extract), and
        migration guide is
        [here](https://docs.parallel.ai/extract/extract-migration-guide).

        Args:
          urls: URLs to extract content from. Up to 20 URLs.

          advanced_settings: Advanced extract configuration.

              These settings may impact result quality and latency unless used carefully. See
              https://docs.parallel.ai/search/advanced-extract-settings for more info.

          client_model: The model generating this request and consuming the results. Enables
              optimizations and tailors default settings for the model's capabilities.

          max_chars_total: Upper bound on total characters across excerpts from all extracted results.

          objective: As in SearchRequest, a natural-language description of the underlying question
              or goal driving the request. Used together with search_queries to focus excerpts
              on the most relevant content.

          search_queries: Optional keyword search queries, as in SearchRequest. Used together with
              objective to focus excerpts on the most relevant content.

          session_id: Session identifier to track calls across separate search and extract calls, to
              be used as part of a larger task. Specifying it may give better contextual
              results for subsequent API calls.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self.post(
            "/v1/extract",
            body=maybe_transform(
                {
                    "urls": urls,
                    "advanced_settings": advanced_settings,
                    "client_model": client_model,
                    "max_chars_total": max_chars_total,
                    "objective": objective,
                    "search_queries": search_queries,
                    "session_id": session_id,
                },
                client_extract_params.ClientExtractParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExtractResponse,
        )

    def search(
        self,
        *,
        search_queries: SequenceNotStr[str],
        advanced_settings: Optional[AdvancedSearchSettingsParam] | Omit = omit,
        client_model: Optional[str] | Omit = omit,
        max_chars_total: Optional[int] | Omit = omit,
        mode: Optional[Literal["basic", "advanced"]] | Omit = omit,
        objective: Optional[str] | Omit = omit,
        session_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SearchResult:
        """
        Searches the web.

        The legacy Search API reference (`/v1beta/search` endpoint) is available
        [here](https://docs.parallel.ai/api-reference/legacy/search-beta/search), and
        migration guide is
        [here](https://docs.parallel.ai/search/search-migration-guide).

        Args:
          search_queries: Concise keyword search queries, 3-6 words each. At least one query is required,
              provide 2-3 for best results. Used together with objective to focus results on
              the most relevant content.

          advanced_settings: Advanced search configuration.

              These settings may impact result quality and latency unless used carefully. See
              https://docs.parallel.ai/search/advanced-search-settings for more info.

          client_model: The model generating this request and consuming the results. Enables
              optimizations and tailors default settings for the model's capabilities.

          max_chars_total: Upper bound on total characters across excerpts from all results.

          mode: Search mode preset: supported values are `basic` and `advanced`. Basic mode
              offers the lowest latency and works best with 2-3 high-quality search_queries.
              Advanced mode provides higher quality with more advanced retrieval and
              compression. Defaults to `advanced` when omitted.

          objective: Natural-language description of the underlying question or goal driving the
              search. Used together with search_queries to focus results on the most relevant
              content. Should be self-contained with enough context to understand the intent
              of the search.

          session_id: Session identifier to track calls across separate search and extract calls, to
              be used as part of a larger task. Specifying it may give better contextual
              results for subsequent API calls.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self.post(
            "/v1/search",
            body=maybe_transform(
                {
                    "search_queries": search_queries,
                    "advanced_settings": advanced_settings,
                    "client_model": client_model,
                    "max_chars_total": max_chars_total,
                    "mode": mode,
                    "objective": objective,
                    "session_id": session_id,
                },
                client_search_params.ClientSearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SearchResult,
        )

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncParallel(AsyncAPIClient):
    # client options
    api_key: str

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncParallel client instance.

        This automatically infers the `api_key` argument from the `PARALLEL_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("PARALLEL_API_KEY")
        if api_key is None:
            raise ParallelError(
                "The api_key client option must be set either by passing api_key to the client or by setting the PARALLEL_API_KEY environment variable"
            )
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("PARALLEL_BASE_URL")
        if base_url is None:
            base_url = f"https://api.parallel.ai"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

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
        from .resources.task_run import AsyncTaskRunResource

        return AsyncTaskRunResource(self)

    @cached_property
    def beta(self) -> AsyncBetaResource:
        from .resources.beta import AsyncBetaResource

        return AsyncBetaResource(self)

    @cached_property
    def with_raw_response(self) -> AsyncParallelWithRawResponse:
        return AsyncParallelWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncParallelWithStreamedResponse:
        return AsyncParallelWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"x-api-key": api_key}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    async def extract(
        self,
        *,
        urls: SequenceNotStr[str],
        advanced_settings: Optional[AdvancedExtractSettingsParam] | Omit = omit,
        client_model: Optional[str] | Omit = omit,
        max_chars_total: Optional[int] | Omit = omit,
        objective: Optional[str] | Omit = omit,
        search_queries: Optional[SequenceNotStr[str]] | Omit = omit,
        session_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExtractResponse:
        """
        Extracts relevant content from specific web URLs.

        The legacy Extract API reference (`/v1beta/extract` endpoint) is available
        [here](https://docs.parallel.ai/api-reference/legacy/extract-beta/extract), and
        migration guide is
        [here](https://docs.parallel.ai/extract/extract-migration-guide).

        Args:
          urls: URLs to extract content from. Up to 20 URLs.

          advanced_settings: Advanced extract configuration.

              These settings may impact result quality and latency unless used carefully. See
              https://docs.parallel.ai/search/advanced-extract-settings for more info.

          client_model: The model generating this request and consuming the results. Enables
              optimizations and tailors default settings for the model's capabilities.

          max_chars_total: Upper bound on total characters across excerpts from all extracted results.

          objective: As in SearchRequest, a natural-language description of the underlying question
              or goal driving the request. Used together with search_queries to focus excerpts
              on the most relevant content.

          search_queries: Optional keyword search queries, as in SearchRequest. Used together with
              objective to focus excerpts on the most relevant content.

          session_id: Session identifier to track calls across separate search and extract calls, to
              be used as part of a larger task. Specifying it may give better contextual
              results for subsequent API calls.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self.post(
            "/v1/extract",
            body=await async_maybe_transform(
                {
                    "urls": urls,
                    "advanced_settings": advanced_settings,
                    "client_model": client_model,
                    "max_chars_total": max_chars_total,
                    "objective": objective,
                    "search_queries": search_queries,
                    "session_id": session_id,
                },
                client_extract_params.ClientExtractParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExtractResponse,
        )

    async def search(
        self,
        *,
        search_queries: SequenceNotStr[str],
        advanced_settings: Optional[AdvancedSearchSettingsParam] | Omit = omit,
        client_model: Optional[str] | Omit = omit,
        max_chars_total: Optional[int] | Omit = omit,
        mode: Optional[Literal["basic", "advanced"]] | Omit = omit,
        objective: Optional[str] | Omit = omit,
        session_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SearchResult:
        """
        Searches the web.

        The legacy Search API reference (`/v1beta/search` endpoint) is available
        [here](https://docs.parallel.ai/api-reference/legacy/search-beta/search), and
        migration guide is
        [here](https://docs.parallel.ai/search/search-migration-guide).

        Args:
          search_queries: Concise keyword search queries, 3-6 words each. At least one query is required,
              provide 2-3 for best results. Used together with objective to focus results on
              the most relevant content.

          advanced_settings: Advanced search configuration.

              These settings may impact result quality and latency unless used carefully. See
              https://docs.parallel.ai/search/advanced-search-settings for more info.

          client_model: The model generating this request and consuming the results. Enables
              optimizations and tailors default settings for the model's capabilities.

          max_chars_total: Upper bound on total characters across excerpts from all results.

          mode: Search mode preset: supported values are `basic` and `advanced`. Basic mode
              offers the lowest latency and works best with 2-3 high-quality search_queries.
              Advanced mode provides higher quality with more advanced retrieval and
              compression. Defaults to `advanced` when omitted.

          objective: Natural-language description of the underlying question or goal driving the
              search. Used together with search_queries to focus results on the most relevant
              content. Should be self-contained with enough context to understand the intent
              of the search.

          session_id: Session identifier to track calls across separate search and extract calls, to
              be used as part of a larger task. Specifying it may give better contextual
              results for subsequent API calls.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self.post(
            "/v1/search",
            body=await async_maybe_transform(
                {
                    "search_queries": search_queries,
                    "advanced_settings": advanced_settings,
                    "client_model": client_model,
                    "max_chars_total": max_chars_total,
                    "mode": mode,
                    "objective": objective,
                    "session_id": session_id,
                },
                client_search_params.ClientSearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SearchResult,
        )

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class ParallelWithRawResponse:
    _client: Parallel

    def __init__(self, client: Parallel) -> None:
        self._client = client

        self.extract = to_raw_response_wrapper(
            client.extract,
        )
        self.search = to_raw_response_wrapper(
            client.search,
        )

    @cached_property
    def task_run(self) -> task_run.TaskRunResourceWithRawResponse:
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
        from .resources.task_run import TaskRunResourceWithRawResponse

        return TaskRunResourceWithRawResponse(self._client.task_run)

    @cached_property
    def beta(self) -> beta.BetaResourceWithRawResponse:
        from .resources.beta import BetaResourceWithRawResponse

        return BetaResourceWithRawResponse(self._client.beta)


class AsyncParallelWithRawResponse:
    _client: AsyncParallel

    def __init__(self, client: AsyncParallel) -> None:
        self._client = client

        self.extract = async_to_raw_response_wrapper(
            client.extract,
        )
        self.search = async_to_raw_response_wrapper(
            client.search,
        )

    @cached_property
    def task_run(self) -> task_run.AsyncTaskRunResourceWithRawResponse:
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
        from .resources.task_run import AsyncTaskRunResourceWithRawResponse

        return AsyncTaskRunResourceWithRawResponse(self._client.task_run)

    @cached_property
    def beta(self) -> beta.AsyncBetaResourceWithRawResponse:
        from .resources.beta import AsyncBetaResourceWithRawResponse

        return AsyncBetaResourceWithRawResponse(self._client.beta)


class ParallelWithStreamedResponse:
    _client: Parallel

    def __init__(self, client: Parallel) -> None:
        self._client = client

        self.extract = to_streamed_response_wrapper(
            client.extract,
        )
        self.search = to_streamed_response_wrapper(
            client.search,
        )

    @cached_property
    def task_run(self) -> task_run.TaskRunResourceWithStreamingResponse:
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
        from .resources.task_run import TaskRunResourceWithStreamingResponse

        return TaskRunResourceWithStreamingResponse(self._client.task_run)

    @cached_property
    def beta(self) -> beta.BetaResourceWithStreamingResponse:
        from .resources.beta import BetaResourceWithStreamingResponse

        return BetaResourceWithStreamingResponse(self._client.beta)


class AsyncParallelWithStreamedResponse:
    _client: AsyncParallel

    def __init__(self, client: AsyncParallel) -> None:
        self._client = client

        self.extract = async_to_streamed_response_wrapper(
            client.extract,
        )
        self.search = async_to_streamed_response_wrapper(
            client.search,
        )

    @cached_property
    def task_run(self) -> task_run.AsyncTaskRunResourceWithStreamingResponse:
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
        from .resources.task_run import AsyncTaskRunResourceWithStreamingResponse

        return AsyncTaskRunResourceWithStreamingResponse(self._client.task_run)

    @cached_property
    def beta(self) -> beta.AsyncBetaResourceWithStreamingResponse:
        from .resources.beta import AsyncBetaResourceWithStreamingResponse

        return AsyncBetaResourceWithStreamingResponse(self._client.beta)


Client = Parallel

AsyncClient = AsyncParallel
