# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .findall import (
    FindAllResource,
    AsyncFindAllResource,
    FindAllResourceWithRawResponse,
    AsyncFindAllResourceWithRawResponse,
    FindAllResourceWithStreamingResponse,
    AsyncFindAllResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["BetaResource", "AsyncBetaResource"]


class BetaResource(SyncAPIResource):
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


class AsyncBetaResource(AsyncAPIResource):
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


class BetaResourceWithRawResponse:
    def __init__(self, beta: BetaResource) -> None:
        self._beta = beta

    @cached_property
    def findall(self) -> FindAllResourceWithRawResponse:
        """
        The FindAll API discovers and evaluates entities that match complex criteria from natural language objectives. Submit a high-level goal and the service automatically generates structured match conditions, discovers relevant candidates, and evaluates each against the criteria. Returns comprehensive results with detailed reasoning, citations, and confidence scores for each match decision. Streaming events and webhooks are supported.
        """
        return FindAllResourceWithRawResponse(self._beta.findall)


class AsyncBetaResourceWithRawResponse:
    def __init__(self, beta: AsyncBetaResource) -> None:
        self._beta = beta

    @cached_property
    def findall(self) -> AsyncFindAllResourceWithRawResponse:
        """
        The FindAll API discovers and evaluates entities that match complex criteria from natural language objectives. Submit a high-level goal and the service automatically generates structured match conditions, discovers relevant candidates, and evaluates each against the criteria. Returns comprehensive results with detailed reasoning, citations, and confidence scores for each match decision. Streaming events and webhooks are supported.
        """
        return AsyncFindAllResourceWithRawResponse(self._beta.findall)


class BetaResourceWithStreamingResponse:
    def __init__(self, beta: BetaResource) -> None:
        self._beta = beta

    @cached_property
    def findall(self) -> FindAllResourceWithStreamingResponse:
        """
        The FindAll API discovers and evaluates entities that match complex criteria from natural language objectives. Submit a high-level goal and the service automatically generates structured match conditions, discovers relevant candidates, and evaluates each against the criteria. Returns comprehensive results with detailed reasoning, citations, and confidence scores for each match decision. Streaming events and webhooks are supported.
        """
        return FindAllResourceWithStreamingResponse(self._beta.findall)


class AsyncBetaResourceWithStreamingResponse:
    def __init__(self, beta: AsyncBetaResource) -> None:
        self._beta = beta

    @cached_property
    def findall(self) -> AsyncFindAllResourceWithStreamingResponse:
        """
        The FindAll API discovers and evaluates entities that match complex criteria from natural language objectives. Submit a high-level goal and the service automatically generates structured match conditions, discovers relevant candidates, and evaluates each against the criteria. Returns comprehensive results with detailed reasoning, citations, and confidence scores for each match decision. Streaming events and webhooks are supported.
        """
        return AsyncFindAllResourceWithStreamingResponse(self._beta.findall)
