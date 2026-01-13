# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Dict, List, Union, Iterable, Optional, cast
from itertools import chain
from typing_extensions import Literal

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
from ...types.beta import (
    findall_create_params,
    findall_enrich_params,
    findall_events_params,
    findall_extend_params,
    findall_ingest_params,
)
from ..._base_client import make_request_options
from ...types.beta.findall_run import FindAllRun
from ...types.json_schema_param import JsonSchemaParam
from ...types.beta.webhook_param import WebhookParam
from ...types.beta.findall_schema import FindAllSchema
from ...types.beta.mcp_server_param import McpServerParam
from ...types.beta.findall_run_result import FindAllRunResult
from ...types.beta.parallel_beta_param import ParallelBetaParam
from ...types.beta.findall_events_response import FindAllEventsResponse

__all__ = [
    "FindAllResource",
    "AsyncFindAllResource",
    "FindAllResourceWithRawResponse",
    "AsyncFindAllResourceWithRawResponse",
    "FindAllResourceWithStreamingResponse",
    "AsyncFindAllResourceWithStreamingResponse",
    "FindallResource",
    "AsyncFindallResource",
    "FindallResourceWithRawResponse",
    "AsyncFindallResourceWithRawResponse",
    "FindallResourceWithStreamingResponse",
    "AsyncFindallResourceWithStreamingResponse",
]


class FindAllResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FindAllResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/parallel-web/parallel-sdk-python#accessing-raw-response-data-eg-headers
        """
        return FindAllResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FindAllResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/parallel-web/parallel-sdk-python#with_streaming_response
        """
        return FindAllResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        entity_type: str,
        generator: Literal["base", "core", "pro", "preview"],
        match_conditions: Iterable[findall_create_params.MatchCondition],
        match_limit: int,
        objective: str,
        exclude_list: Optional[Iterable[findall_create_params.ExcludeList]] | Omit = omit,
        metadata: Optional[Dict[str, Union[str, float, bool]]] | Omit = omit,
        webhook: Optional[WebhookParam] | Omit = omit,
        betas: List[ParallelBetaParam] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FindAllRun:
        """
        Starts a FindAll run.

        This endpoint immediately returns a FindAll run object with status set to
        'queued'. You can get the run result snapshot using the GET
        /v1beta/findall/runs/{findall_id}/result endpoint. You can track the progress of
        the run by:

        - Polling the status using the GET /v1beta/findall/runs/{findall_id} endpoint,
        - Subscribing to real-time updates via the
          /v1beta/findall/runs/{findall_id}/events endpoint,
        - Or specifying a webhook with relevant event types during run creation to
          receive notifications.

        Args:
          entity_type: Type of the entity for the FindAll run.

          generator: Generator for the FindAll run. One of base, core, pro, preview.

          match_conditions: List of match conditions for the FindAll run.

          match_limit: Maximum number of matches to find for this FindAll run. Must be between 5 and
              1000 (inclusive).

          objective: Natural language objective of the FindAll run.

          exclude_list: List of entity names/IDs to exclude from results.

          metadata: Metadata for the FindAll run.

          webhook: Webhooks for Task Runs.

          betas: Optional header to specify the beta version(s) to enable.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given(
                {
                    "parallel-beta": ",".join(chain((str(e) for e in betas), ["findall-2025-09-15"]))
                    if is_given(betas)
                    else not_given
                }
            ),
            **(extra_headers or {}),
        }
        extra_headers = {"parallel-beta": "findall-2025-09-15", **(extra_headers or {})}
        return self._post(
            "/v1beta/findall/runs",
            body=maybe_transform(
                {
                    "entity_type": entity_type,
                    "generator": generator,
                    "match_conditions": match_conditions,
                    "match_limit": match_limit,
                    "objective": objective,
                    "exclude_list": exclude_list,
                    "metadata": metadata,
                    "webhook": webhook,
                },
                findall_create_params.FindAllCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FindAllRun,
        )

    def retrieve(
        self,
        findall_id: str,
        *,
        betas: List[ParallelBetaParam] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FindAllRun:
        """
        Retrieve a FindAll run.

        Args:
          betas: Optional header to specify the beta version(s) to enable.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not findall_id:
            raise ValueError(f"Expected a non-empty value for `findall_id` but received {findall_id!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "parallel-beta": ",".join(chain((str(e) for e in betas), ["findall-2025-09-15"]))
                    if is_given(betas)
                    else not_given
                }
            ),
            **(extra_headers or {}),
        }
        extra_headers = {"parallel-beta": "findall-2025-09-15", **(extra_headers or {})}
        return self._get(
            f"/v1beta/findall/runs/{findall_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FindAllRun,
        )

    def cancel(
        self,
        findall_id: str,
        *,
        betas: List[ParallelBetaParam] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Cancel a FindAll run.

        Args:
          betas: Optional header to specify the beta version(s) to enable.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not findall_id:
            raise ValueError(f"Expected a non-empty value for `findall_id` but received {findall_id!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "parallel-beta": ",".join(chain((str(e) for e in betas), ["findall-2025-09-15"]))
                    if is_given(betas)
                    else not_given
                }
            ),
            **(extra_headers or {}),
        }
        extra_headers = {"parallel-beta": "findall-2025-09-15", **(extra_headers or {})}
        return self._post(
            f"/v1beta/findall/runs/{findall_id}/cancel",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def enrich(
        self,
        findall_id: str,
        *,
        output_schema: JsonSchemaParam,
        mcp_servers: Optional[Iterable[McpServerParam]] | Omit = omit,
        processor: str | Omit = omit,
        betas: List[ParallelBetaParam] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FindAllSchema:
        """
        Add an enrichment to a FindAll run.

        Args:
          output_schema: JSON schema for the enrichment output schema for the FindAll run.

          mcp_servers: List of MCP servers to use for the task.

          processor: Processor to use for the task.

          betas: Optional header to specify the beta version(s) to enable.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not findall_id:
            raise ValueError(f"Expected a non-empty value for `findall_id` but received {findall_id!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "parallel-beta": ",".join(chain((str(e) for e in betas), ["findall-2025-09-15"]))
                    if is_given(betas)
                    else not_given
                }
            ),
            **(extra_headers or {}),
        }
        extra_headers = {"parallel-beta": "findall-2025-09-15", **(extra_headers or {})}
        return self._post(
            f"/v1beta/findall/runs/{findall_id}/enrich",
            body=maybe_transform(
                {
                    "output_schema": output_schema,
                    "mcp_servers": mcp_servers,
                    "processor": processor,
                },
                findall_enrich_params.FindAllEnrichParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FindAllSchema,
        )

    def events(
        self,
        findall_id: str,
        *,
        last_event_id: Optional[str] | Omit = omit,
        api_timeout: Optional[float] | Omit = omit,
        betas: List[ParallelBetaParam] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Stream[FindAllEventsResponse]:
        """
        Stream events from a FindAll run.

        Args: request: The Shapi request findall_id: The FindAll run ID last_event_id:
        Optional event ID to resume from. timeout: Optional timeout in seconds. If None,
        keep connection alive as long as the run is going. If set, stop after specified
        duration.

        Args:
          betas: Optional header to specify the beta version(s) to enable.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not findall_id:
            raise ValueError(f"Expected a non-empty value for `findall_id` but received {findall_id!r}")
        extra_headers = {"Accept": "text/event-stream", **(extra_headers or {})}
        extra_headers = {
            **strip_not_given(
                {
                    "parallel-beta": ",".join(chain((str(e) for e in betas), ["findall-2025-09-15"]))
                    if is_given(betas)
                    else not_given
                }
            ),
            **(extra_headers or {}),
        }
        extra_headers = {"parallel-beta": "findall-2025-09-15", **(extra_headers or {})}
        return self._get(
            f"/v1beta/findall/runs/{findall_id}/events",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "last_event_id": last_event_id,
                        "api_timeout": api_timeout,
                    },
                    findall_events_params.FindAllEventsParams,
                ),
            ),
            cast_to=cast(Any, FindAllEventsResponse),  # Union types cannot be passed in as arguments in the type system
            stream=True,
            stream_cls=Stream[FindAllEventsResponse],
        )

    def extend(
        self,
        findall_id: str,
        *,
        additional_match_limit: int,
        betas: List[ParallelBetaParam] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FindAllSchema:
        """
        Extend a FindAll run by adding additional matches to the current match limit.

        Args:
          additional_match_limit: Additional number of matches to find for this FindAll run. This value will be
              added to the current match limit to determine the new total match limit. Must be
              greater than 0.

          betas: Optional header to specify the beta version(s) to enable.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not findall_id:
            raise ValueError(f"Expected a non-empty value for `findall_id` but received {findall_id!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "parallel-beta": ",".join(chain((str(e) for e in betas), ["findall-2025-09-15"]))
                    if is_given(betas)
                    else not_given
                }
            ),
            **(extra_headers or {}),
        }
        extra_headers = {"parallel-beta": "findall-2025-09-15", **(extra_headers or {})}
        return self._post(
            f"/v1beta/findall/runs/{findall_id}/extend",
            body=maybe_transform(
                {"additional_match_limit": additional_match_limit}, findall_extend_params.FindAllExtendParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FindAllSchema,
        )

    def ingest(
        self,
        *,
        objective: str,
        betas: List[ParallelBetaParam] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FindAllSchema:
        """
        Transforms a natural language search objective into a structured FindAll spec.

        Note: Access to this endpoint requires the parallel-beta header.

        The generated specification serves as a suggested starting point and can be
        further customized by the user.

        Args:
          objective: Natural language objective to create a FindAll run spec.

          betas: Optional header to specify the beta version(s) to enable.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given(
                {
                    "parallel-beta": ",".join(chain((str(e) for e in betas), ["findall-2025-09-15"]))
                    if is_given(betas)
                    else not_given
                }
            ),
            **(extra_headers or {}),
        }
        extra_headers = {"parallel-beta": "findall-2025-09-15", **(extra_headers or {})}
        return self._post(
            "/v1beta/findall/ingest",
            body=maybe_transform({"objective": objective}, findall_ingest_params.FindAllIngestParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FindAllSchema,
        )

    def result(
        self,
        findall_id: str,
        *,
        betas: List[ParallelBetaParam] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FindAllRunResult:
        """
        Retrieve the FindAll run result at the time of the request.

        Args:
          betas: Optional header to specify the beta version(s) to enable.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not findall_id:
            raise ValueError(f"Expected a non-empty value for `findall_id` but received {findall_id!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "parallel-beta": ",".join(chain((str(e) for e in betas), ["findall-2025-09-15"]))
                    if is_given(betas)
                    else not_given
                }
            ),
            **(extra_headers or {}),
        }
        extra_headers = {"parallel-beta": "findall-2025-09-15", **(extra_headers or {})}
        return self._get(
            f"/v1beta/findall/runs/{findall_id}/result",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FindAllRunResult,
        )

    def schema(
        self,
        findall_id: str,
        *,
        betas: List[ParallelBetaParam] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FindAllSchema:
        """
        Get FindAll Run Schema

        Args:
          betas: Optional header to specify the beta version(s) to enable.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not findall_id:
            raise ValueError(f"Expected a non-empty value for `findall_id` but received {findall_id!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "parallel-beta": ",".join(chain((str(e) for e in betas), ["findall-2025-09-15"]))
                    if is_given(betas)
                    else not_given
                }
            ),
            **(extra_headers or {}),
        }
        extra_headers = {"parallel-beta": "findall-2025-09-15", **(extra_headers or {})}
        return self._get(
            f"/v1beta/findall/runs/{findall_id}/schema",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FindAllSchema,
        )


class AsyncFindAllResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFindAllResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/parallel-web/parallel-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFindAllResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFindAllResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/parallel-web/parallel-sdk-python#with_streaming_response
        """
        return AsyncFindAllResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        entity_type: str,
        generator: Literal["base", "core", "pro", "preview"],
        match_conditions: Iterable[findall_create_params.MatchCondition],
        match_limit: int,
        objective: str,
        exclude_list: Optional[Iterable[findall_create_params.ExcludeList]] | Omit = omit,
        metadata: Optional[Dict[str, Union[str, float, bool]]] | Omit = omit,
        webhook: Optional[WebhookParam] | Omit = omit,
        betas: List[ParallelBetaParam] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FindAllRun:
        """
        Starts a FindAll run.

        This endpoint immediately returns a FindAll run object with status set to
        'queued'. You can get the run result snapshot using the GET
        /v1beta/findall/runs/{findall_id}/result endpoint. You can track the progress of
        the run by:

        - Polling the status using the GET /v1beta/findall/runs/{findall_id} endpoint,
        - Subscribing to real-time updates via the
          /v1beta/findall/runs/{findall_id}/events endpoint,
        - Or specifying a webhook with relevant event types during run creation to
          receive notifications.

        Args:
          entity_type: Type of the entity for the FindAll run.

          generator: Generator for the FindAll run. One of base, core, pro, preview.

          match_conditions: List of match conditions for the FindAll run.

          match_limit: Maximum number of matches to find for this FindAll run. Must be between 5 and
              1000 (inclusive).

          objective: Natural language objective of the FindAll run.

          exclude_list: List of entity names/IDs to exclude from results.

          metadata: Metadata for the FindAll run.

          webhook: Webhooks for Task Runs.

          betas: Optional header to specify the beta version(s) to enable.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given(
                {
                    "parallel-beta": ",".join(chain((str(e) for e in betas), ["findall-2025-09-15"]))
                    if is_given(betas)
                    else not_given
                }
            ),
            **(extra_headers or {}),
        }
        extra_headers = {"parallel-beta": "findall-2025-09-15", **(extra_headers or {})}
        return await self._post(
            "/v1beta/findall/runs",
            body=await async_maybe_transform(
                {
                    "entity_type": entity_type,
                    "generator": generator,
                    "match_conditions": match_conditions,
                    "match_limit": match_limit,
                    "objective": objective,
                    "exclude_list": exclude_list,
                    "metadata": metadata,
                    "webhook": webhook,
                },
                findall_create_params.FindAllCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FindAllRun,
        )

    async def retrieve(
        self,
        findall_id: str,
        *,
        betas: List[ParallelBetaParam] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FindAllRun:
        """
        Retrieve a FindAll run.

        Args:
          betas: Optional header to specify the beta version(s) to enable.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not findall_id:
            raise ValueError(f"Expected a non-empty value for `findall_id` but received {findall_id!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "parallel-beta": ",".join(chain((str(e) for e in betas), ["findall-2025-09-15"]))
                    if is_given(betas)
                    else not_given
                }
            ),
            **(extra_headers or {}),
        }
        extra_headers = {"parallel-beta": "findall-2025-09-15", **(extra_headers or {})}
        return await self._get(
            f"/v1beta/findall/runs/{findall_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FindAllRun,
        )

    async def cancel(
        self,
        findall_id: str,
        *,
        betas: List[ParallelBetaParam] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Cancel a FindAll run.

        Args:
          betas: Optional header to specify the beta version(s) to enable.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not findall_id:
            raise ValueError(f"Expected a non-empty value for `findall_id` but received {findall_id!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "parallel-beta": ",".join(chain((str(e) for e in betas), ["findall-2025-09-15"]))
                    if is_given(betas)
                    else not_given
                }
            ),
            **(extra_headers or {}),
        }
        extra_headers = {"parallel-beta": "findall-2025-09-15", **(extra_headers or {})}
        return await self._post(
            f"/v1beta/findall/runs/{findall_id}/cancel",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def enrich(
        self,
        findall_id: str,
        *,
        output_schema: JsonSchemaParam,
        mcp_servers: Optional[Iterable[McpServerParam]] | Omit = omit,
        processor: str | Omit = omit,
        betas: List[ParallelBetaParam] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FindAllSchema:
        """
        Add an enrichment to a FindAll run.

        Args:
          output_schema: JSON schema for the enrichment output schema for the FindAll run.

          mcp_servers: List of MCP servers to use for the task.

          processor: Processor to use for the task.

          betas: Optional header to specify the beta version(s) to enable.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not findall_id:
            raise ValueError(f"Expected a non-empty value for `findall_id` but received {findall_id!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "parallel-beta": ",".join(chain((str(e) for e in betas), ["findall-2025-09-15"]))
                    if is_given(betas)
                    else not_given
                }
            ),
            **(extra_headers or {}),
        }
        extra_headers = {"parallel-beta": "findall-2025-09-15", **(extra_headers or {})}
        return await self._post(
            f"/v1beta/findall/runs/{findall_id}/enrich",
            body=await async_maybe_transform(
                {
                    "output_schema": output_schema,
                    "mcp_servers": mcp_servers,
                    "processor": processor,
                },
                findall_enrich_params.FindAllEnrichParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FindAllSchema,
        )

    async def events(
        self,
        findall_id: str,
        *,
        last_event_id: Optional[str] | Omit = omit,
        api_timeout: Optional[float] | Omit = omit,
        betas: List[ParallelBetaParam] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncStream[FindAllEventsResponse]:
        """
        Stream events from a FindAll run.

        Args: request: The Shapi request findall_id: The FindAll run ID last_event_id:
        Optional event ID to resume from. timeout: Optional timeout in seconds. If None,
        keep connection alive as long as the run is going. If set, stop after specified
        duration.

        Args:
          betas: Optional header to specify the beta version(s) to enable.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not findall_id:
            raise ValueError(f"Expected a non-empty value for `findall_id` but received {findall_id!r}")
        extra_headers = {"Accept": "text/event-stream", **(extra_headers or {})}
        extra_headers = {
            **strip_not_given(
                {
                    "parallel-beta": ",".join(chain((str(e) for e in betas), ["findall-2025-09-15"]))
                    if is_given(betas)
                    else not_given
                }
            ),
            **(extra_headers or {}),
        }
        extra_headers = {"parallel-beta": "findall-2025-09-15", **(extra_headers or {})}
        return await self._get(
            f"/v1beta/findall/runs/{findall_id}/events",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "last_event_id": last_event_id,
                        "api_timeout": api_timeout,
                    },
                    findall_events_params.FindAllEventsParams,
                ),
            ),
            cast_to=cast(Any, FindAllEventsResponse),  # Union types cannot be passed in as arguments in the type system
            stream=True,
            stream_cls=AsyncStream[FindAllEventsResponse],
        )

    async def extend(
        self,
        findall_id: str,
        *,
        additional_match_limit: int,
        betas: List[ParallelBetaParam] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FindAllSchema:
        """
        Extend a FindAll run by adding additional matches to the current match limit.

        Args:
          additional_match_limit: Additional number of matches to find for this FindAll run. This value will be
              added to the current match limit to determine the new total match limit. Must be
              greater than 0.

          betas: Optional header to specify the beta version(s) to enable.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not findall_id:
            raise ValueError(f"Expected a non-empty value for `findall_id` but received {findall_id!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "parallel-beta": ",".join(chain((str(e) for e in betas), ["findall-2025-09-15"]))
                    if is_given(betas)
                    else not_given
                }
            ),
            **(extra_headers or {}),
        }
        extra_headers = {"parallel-beta": "findall-2025-09-15", **(extra_headers or {})}
        return await self._post(
            f"/v1beta/findall/runs/{findall_id}/extend",
            body=await async_maybe_transform(
                {"additional_match_limit": additional_match_limit}, findall_extend_params.FindAllExtendParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FindAllSchema,
        )

    async def ingest(
        self,
        *,
        objective: str,
        betas: List[ParallelBetaParam] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FindAllSchema:
        """
        Transforms a natural language search objective into a structured FindAll spec.

        Note: Access to this endpoint requires the parallel-beta header.

        The generated specification serves as a suggested starting point and can be
        further customized by the user.

        Args:
          objective: Natural language objective to create a FindAll run spec.

          betas: Optional header to specify the beta version(s) to enable.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given(
                {
                    "parallel-beta": ",".join(chain((str(e) for e in betas), ["findall-2025-09-15"]))
                    if is_given(betas)
                    else not_given
                }
            ),
            **(extra_headers or {}),
        }
        extra_headers = {"parallel-beta": "findall-2025-09-15", **(extra_headers or {})}
        return await self._post(
            "/v1beta/findall/ingest",
            body=await async_maybe_transform({"objective": objective}, findall_ingest_params.FindAllIngestParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FindAllSchema,
        )

    async def result(
        self,
        findall_id: str,
        *,
        betas: List[ParallelBetaParam] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FindAllRunResult:
        """
        Retrieve the FindAll run result at the time of the request.

        Args:
          betas: Optional header to specify the beta version(s) to enable.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not findall_id:
            raise ValueError(f"Expected a non-empty value for `findall_id` but received {findall_id!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "parallel-beta": ",".join(chain((str(e) for e in betas), ["findall-2025-09-15"]))
                    if is_given(betas)
                    else not_given
                }
            ),
            **(extra_headers or {}),
        }
        extra_headers = {"parallel-beta": "findall-2025-09-15", **(extra_headers or {})}
        return await self._get(
            f"/v1beta/findall/runs/{findall_id}/result",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FindAllRunResult,
        )

    async def schema(
        self,
        findall_id: str,
        *,
        betas: List[ParallelBetaParam] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FindAllSchema:
        """
        Get FindAll Run Schema

        Args:
          betas: Optional header to specify the beta version(s) to enable.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not findall_id:
            raise ValueError(f"Expected a non-empty value for `findall_id` but received {findall_id!r}")
        extra_headers = {
            **strip_not_given(
                {
                    "parallel-beta": ",".join(chain((str(e) for e in betas), ["findall-2025-09-15"]))
                    if is_given(betas)
                    else not_given
                }
            ),
            **(extra_headers or {}),
        }
        extra_headers = {"parallel-beta": "findall-2025-09-15", **(extra_headers or {})}
        return await self._get(
            f"/v1beta/findall/runs/{findall_id}/schema",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FindAllSchema,
        )


class FindAllResourceWithRawResponse:
    def __init__(self, findall: FindAllResource) -> None:
        self._findall = findall

        self.create = to_raw_response_wrapper(
            findall.create,
        )
        self.retrieve = to_raw_response_wrapper(
            findall.retrieve,
        )
        self.cancel = to_raw_response_wrapper(
            findall.cancel,
        )
        self.enrich = to_raw_response_wrapper(
            findall.enrich,
        )
        self.events = to_raw_response_wrapper(
            findall.events,
        )
        self.extend = to_raw_response_wrapper(
            findall.extend,
        )
        self.ingest = to_raw_response_wrapper(
            findall.ingest,
        )
        self.result = to_raw_response_wrapper(
            findall.result,
        )
        self.schema = to_raw_response_wrapper(
            findall.schema,
        )


class AsyncFindAllResourceWithRawResponse:
    def __init__(self, findall: AsyncFindAllResource) -> None:
        self._findall = findall

        self.create = async_to_raw_response_wrapper(
            findall.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            findall.retrieve,
        )
        self.cancel = async_to_raw_response_wrapper(
            findall.cancel,
        )
        self.enrich = async_to_raw_response_wrapper(
            findall.enrich,
        )
        self.events = async_to_raw_response_wrapper(
            findall.events,
        )
        self.extend = async_to_raw_response_wrapper(
            findall.extend,
        )
        self.ingest = async_to_raw_response_wrapper(
            findall.ingest,
        )
        self.result = async_to_raw_response_wrapper(
            findall.result,
        )
        self.schema = async_to_raw_response_wrapper(
            findall.schema,
        )


class FindAllResourceWithStreamingResponse:
    def __init__(self, findall: FindAllResource) -> None:
        self._findall = findall

        self.create = to_streamed_response_wrapper(
            findall.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            findall.retrieve,
        )
        self.cancel = to_streamed_response_wrapper(
            findall.cancel,
        )
        self.enrich = to_streamed_response_wrapper(
            findall.enrich,
        )
        self.events = to_streamed_response_wrapper(
            findall.events,
        )
        self.extend = to_streamed_response_wrapper(
            findall.extend,
        )
        self.ingest = to_streamed_response_wrapper(
            findall.ingest,
        )
        self.result = to_streamed_response_wrapper(
            findall.result,
        )
        self.schema = to_streamed_response_wrapper(
            findall.schema,
        )


class AsyncFindAllResourceWithStreamingResponse:
    def __init__(self, findall: AsyncFindAllResource) -> None:
        self._findall = findall

        self.create = async_to_streamed_response_wrapper(
            findall.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            findall.retrieve,
        )
        self.cancel = async_to_streamed_response_wrapper(
            findall.cancel,
        )
        self.enrich = async_to_streamed_response_wrapper(
            findall.enrich,
        )
        self.events = async_to_streamed_response_wrapper(
            findall.events,
        )
        self.extend = async_to_streamed_response_wrapper(
            findall.extend,
        )
        self.ingest = async_to_streamed_response_wrapper(
            findall.ingest,
        )
        self.result = async_to_streamed_response_wrapper(
            findall.result,
        )
        self.schema = async_to_streamed_response_wrapper(
            findall.schema,
        )


FindallResource = FindAllResource  # for backwards compatibility with v0.3.4
"""This is deprecated, `FindAllResource` should be used instead"""

AsyncFindallResource = AsyncFindAllResource  # for backwards compatibility with v0.3.4
"""This is deprecated, `AsyncFindAllResource` should be used instead"""

FindallResourceWithRawResponse = FindAllResourceWithRawResponse  # for backwards compatibility with v0.3.4
"""This is deprecated, `FindAllResourceWithRawResponse` should be used instead"""

AsyncFindallResourceWithRawResponse = AsyncFindAllResourceWithRawResponse  # for backwards compatibility with v0.3.4
"""This is deprecated, `AsyncFindAllResourceWithRawResponse` should be used instead"""

FindallResourceWithStreamingResponse = FindAllResourceWithStreamingResponse  # for backwards compatibility with v0.3.4
"""This is deprecated, `FindAllResourceWithStreamingResponse` should be used instead"""

AsyncFindallResourceWithStreamingResponse = (
    AsyncFindAllResourceWithStreamingResponse  # for backwards compatibility with v0.3.4
)
"""This is deprecated, `AsyncFindAllResourceWithStreamingResponse` should be used instead"""
