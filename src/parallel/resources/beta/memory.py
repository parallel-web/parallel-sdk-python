# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.beta import memory_clear_params, memory_evict_params, memory_retrieve_params
from ..._base_client import make_request_options
from ...types.beta.memory_retrieve_response import MemoryRetrieveResponse

__all__ = ["MemoryResource", "AsyncMemoryResource"]


class MemoryResource(SyncAPIResource):
    """
    The Memory API retrieves and manages memories created by Tasks, Monitors, and FindAll runs. Memories can be personal or isolated with a `memory_scope_key`.
    """

    @cached_property
    def with_raw_response(self) -> MemoryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/parallel-web/parallel-sdk-python#accessing-raw-response-data-eg-headers
        """
        return MemoryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MemoryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/parallel-web/parallel-sdk-python#with_streaming_response
        """
        return MemoryResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        kind: Optional[Literal["task", "monitor", "findall"]] | Omit = omit,
        limit: int | Omit = omit,
        memory_scope_key: Optional[str] | Omit = omit,
        query: Optional[str] | Omit = omit,
        since: Union[str, datetime, None] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MemoryRetrieveResponse:
        """Retrieves relevant or recent runs from the selected memory.

        Provide a query to
        rank results by relevance; leave it empty to return the most recent runs.

        Args:
          kind: Filter memories by kind: `task`, `monitor`, or `findall`.

          limit: Maximum number of memories to return.

          memory_scope_key: User-provided key identifying the memory scope to use. Omit to use personal
              memory, if available.

          query: Concise query describing the memories to retrieve. Empty queries return the most
              recent memories.

          since: Only return memories sourced from task, monitor, or FindAll runs completed at or
              after this RFC 3339 timestamp.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"parallel-beta": "search-extract-2025-10-10", **(extra_headers or {})}
        return self._post(
            "/v1beta/memory/retrieve",
            body=maybe_transform(
                {
                    "kind": kind,
                    "limit": limit,
                    "memory_scope_key": memory_scope_key,
                    "query": query,
                    "since": since,
                },
                memory_retrieve_params.MemoryRetrieveParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MemoryRetrieveResponse,
        )

    def clear(
        self,
        *,
        memory_scope_key: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Clears all entries from the selected memory without deleting the underlying
        tasks, monitors, or FindAll runs.

        Args:
          memory_scope_key: User-provided key identifying the memory scope to use. Omit to use personal
              memory, if available.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        extra_headers.update({"parallel-beta": "search-extract-2025-10-10"})
        return self._post(
            "/v1beta/memory/clear",
            body=maybe_transform({"memory_scope_key": memory_scope_key}, memory_clear_params.MemoryClearParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def evict(
        self,
        *,
        id: str,
        kind: Literal["task", "monitor", "findall"],
        memory_scope_key: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Removes a task run, monitor, or FindAll run from the selected memory without
        deleting the original resource.

        Args:
          id: ID of the task run, monitor, or FindAll run to evict.

          kind: Kind of source to evict: `task`, `monitor`, or `findall`.

          memory_scope_key: User-provided key identifying the memory scope to use. Omit to use personal
              memory, if available.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        extra_headers.update({"parallel-beta": "search-extract-2025-10-10"})
        return self._post(
            "/v1beta/memory/evict",
            body=maybe_transform(
                {
                    "id": id,
                    "kind": kind,
                    "memory_scope_key": memory_scope_key,
                },
                memory_evict_params.MemoryEvictParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncMemoryResource(AsyncAPIResource):
    """
    The Memory API retrieves and manages memories created by Tasks, Monitors, and FindAll runs. Memories can be personal or isolated with a `memory_scope_key`.
    """

    @cached_property
    def with_raw_response(self) -> AsyncMemoryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/parallel-web/parallel-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMemoryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMemoryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/parallel-web/parallel-sdk-python#with_streaming_response
        """
        return AsyncMemoryResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        kind: Optional[Literal["task", "monitor", "findall"]] | Omit = omit,
        limit: int | Omit = omit,
        memory_scope_key: Optional[str] | Omit = omit,
        query: Optional[str] | Omit = omit,
        since: Union[str, datetime, None] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MemoryRetrieveResponse:
        """Retrieves relevant or recent runs from the selected memory.

        Provide a query to
        rank results by relevance; leave it empty to return the most recent runs.

        Args:
          kind: Filter memories by kind: `task`, `monitor`, or `findall`.

          limit: Maximum number of memories to return.

          memory_scope_key: User-provided key identifying the memory scope to use. Omit to use personal
              memory, if available.

          query: Concise query describing the memories to retrieve. Empty queries return the most
              recent memories.

          since: Only return memories sourced from task, monitor, or FindAll runs completed at or
              after this RFC 3339 timestamp.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"parallel-beta": "search-extract-2025-10-10", **(extra_headers or {})}
        return await self._post(
            "/v1beta/memory/retrieve",
            body=await async_maybe_transform(
                {
                    "kind": kind,
                    "limit": limit,
                    "memory_scope_key": memory_scope_key,
                    "query": query,
                    "since": since,
                },
                memory_retrieve_params.MemoryRetrieveParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MemoryRetrieveResponse,
        )

    async def clear(
        self,
        *,
        memory_scope_key: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Clears all entries from the selected memory without deleting the underlying
        tasks, monitors, or FindAll runs.

        Args:
          memory_scope_key: User-provided key identifying the memory scope to use. Omit to use personal
              memory, if available.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        extra_headers.update({"parallel-beta": "search-extract-2025-10-10"})
        return await self._post(
            "/v1beta/memory/clear",
            body=await async_maybe_transform(
                {"memory_scope_key": memory_scope_key}, memory_clear_params.MemoryClearParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def evict(
        self,
        *,
        id: str,
        kind: Literal["task", "monitor", "findall"],
        memory_scope_key: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Removes a task run, monitor, or FindAll run from the selected memory without
        deleting the original resource.

        Args:
          id: ID of the task run, monitor, or FindAll run to evict.

          kind: Kind of source to evict: `task`, `monitor`, or `findall`.

          memory_scope_key: User-provided key identifying the memory scope to use. Omit to use personal
              memory, if available.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        extra_headers.update({"parallel-beta": "search-extract-2025-10-10"})
        return await self._post(
            "/v1beta/memory/evict",
            body=await async_maybe_transform(
                {
                    "id": id,
                    "kind": kind,
                    "memory_scope_key": memory_scope_key,
                },
                memory_evict_params.MemoryEvictParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class MemoryResourceWithRawResponse:
    def __init__(self, memory: MemoryResource) -> None:
        self._memory = memory

        self.retrieve = to_raw_response_wrapper(
            memory.retrieve,
        )
        self.clear = to_raw_response_wrapper(
            memory.clear,
        )
        self.evict = to_raw_response_wrapper(
            memory.evict,
        )


class AsyncMemoryResourceWithRawResponse:
    def __init__(self, memory: AsyncMemoryResource) -> None:
        self._memory = memory

        self.retrieve = async_to_raw_response_wrapper(
            memory.retrieve,
        )
        self.clear = async_to_raw_response_wrapper(
            memory.clear,
        )
        self.evict = async_to_raw_response_wrapper(
            memory.evict,
        )


class MemoryResourceWithStreamingResponse:
    def __init__(self, memory: MemoryResource) -> None:
        self._memory = memory

        self.retrieve = to_streamed_response_wrapper(
            memory.retrieve,
        )
        self.clear = to_streamed_response_wrapper(
            memory.clear,
        )
        self.evict = to_streamed_response_wrapper(
            memory.evict,
        )


class AsyncMemoryResourceWithStreamingResponse:
    def __init__(self, memory: AsyncMemoryResource) -> None:
        self._memory = memory

        self.retrieve = async_to_streamed_response_wrapper(
            memory.retrieve,
        )
        self.clear = async_to_streamed_response_wrapper(
            memory.clear,
        )
        self.evict = async_to_streamed_response_wrapper(
            memory.evict,
        )
