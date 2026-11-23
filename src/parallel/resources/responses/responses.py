# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal, overload

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import required_args, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._streaming import Stream, AsyncStream
from ..._base_client import make_request_options
from ...types.responses import response_create_params
from ...types.responses.response_result import ResponseResult
from ...types.responses.response_stream_event import ResponseStreamEvent

__all__ = ["ResponsesResource", "AsyncResponsesResource"]


class ResponsesResource(SyncAPIResource):
    """
    An OpenAI-Responses-compatible interface for answers grounded in live web research, with URL citations. Point any Responses-API client — the OpenAI Python SDK, OpenAI TypeScript SDK, the Agents SDK, or raw HTTP — at `https://api.parallel.ai` with your Parallel API key, set `model` to `parallel`, and call `/v1/responses`.
    - `input` accepts a plain string or an array of role/content messages (canonical OpenAI shape; text content only).
    - `reasoning.effort` (`low`/`medium`/`high`/`auto`) controls how much research is performed, trading response time for answer quality.
    - Multi-turn via `previous_response_id`.
    - Structured outputs via `text.format = {"type": "json_schema", "name": ..., "schema": {...}}`.
    - Streaming (`stream=true`) emits the standard OpenAI Responses SSE lifecycle: `response.created` and `response.in_progress`, then output item / content part / text delta events with URL-citation annotations, the matching `*.done` events, and a terminal `response.completed` — or `response.failed` if the request fails mid-stream.
    """

    @cached_property
    def with_raw_response(self) -> ResponsesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/parallel-web/parallel-sdk-python#accessing-raw-response-data-eg-headers
        """
        return ResponsesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ResponsesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/parallel-web/parallel-sdk-python#with_streaming_response
        """
        return ResponsesResourceWithStreamingResponse(self)

    @overload
    def create(
        self,
        *,
        input: Union[str, Iterable[response_create_params.InputUnionMember1]],
        model: str,
        background: Optional[bool] | Omit = omit,
        data_sources: Optional[response_create_params.DataSources] | Omit = omit,
        instructions: Optional[str] | Omit = omit,
        metadata: Optional[Dict[str, str]] | Omit = omit,
        previous_response_id: Optional[str] | Omit = omit,
        reasoning: Optional[response_create_params.Reasoning] | Omit = omit,
        stream: Optional[Literal[False]] | Omit = omit,
        text: Optional[response_create_params.Text] | Omit = omit,
        tools: Optional[Iterable[response_create_params.Tool]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ResponseResult:
        """
        Create a response.

        Generates an answer to the given input, grounded in live web research and
        annotated with URL citations. Set `model` to `parallel`; `reasoning.effort`
        (`low`/`medium`/`high`/`auto`) controls how much research is performed, trading
        response time for answer quality. Returns an OpenAI-format `Response` as
        `application/json`, or a `text/event-stream` of OpenAI Responses SSE events when
        `stream=true`.

        Args:
          input: The input to generate a response for: a plain string, or a list of role/content
              messages that includes at least one `user` message. Must be non-empty, and only
              text content is supported. `input` and `instructions` together may total at most
              20,000 characters.

          model: The model to run. `parallel` is the only supported value (matched
              case-insensitively); any other value is rejected. To trade response time for
              answer quality, set `reasoning.effort` (low/medium/high/auto) rather than
              changing the model name.

          background: Background mode is not supported: requests with `background=true` are rejected
              with a 422 validation error. Use the Task API (POST /v1/tasks/runs) for
              long-running work.

          data_sources:
              Data partners to enable for this request, in addition to web search:
              `pay_per_use` partners are billed per call, `free` partners are not. Same names
              and shape as the Task API's `advanced_settings.data_sources`; see the Data
              Sources documentation. Supported at every `reasoning.effort`. Lower efforts make
              fewer partner calls per answer, and `auto` can stop at `low`. For a partner
              whose lookups take several steps, such as a search and then a detail fetch, use
              `medium` (the default) or `high`. A partner name must not collide with an `mcp`
              tool's `server_label`.

          instructions: System instructions for the model.

          metadata: Arbitrary key-value pairs, echoed back on the Response object. Useful for
              tagging requests. At most 16 keys; keys up to 64 characters, values up to 512
              characters.

          previous_response_id: ID of a previous response to use as conversation context.

          reasoning: Reasoning configuration (OpenAI-compatible subset).

          stream: Whether to stream the response.

          text: Text output configuration. By default the response is plain text; for structured
              output set `format` to `{"type": "json_schema", "name": ..., "schema": {...}}`.
              On `/v1/responses` the `json_object` format produces plain text and may be
              refused with a 400; use `json_schema` instead.

          tools: OpenAI tools. Web grounding is always on, so no tool is needed to search; a
              `web_search` tool's `filters` restrict the domains searched and cited
              (`allowed_domains` maps to Parallel's `source_policy.include_domains`,
              `blocked_domains` to `exclude_domains`). An `mcp` tool gives the model a remote
              MCP server to call; at most 10 per request. A tool of any other `type` is
              accepted and ignored. A tool whose `type` is missing or not a string is
              rejected.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        *,
        input: Union[str, Iterable[response_create_params.InputUnionMember1]],
        model: str,
        stream: Literal[True],
        background: Optional[bool] | Omit = omit,
        data_sources: Optional[response_create_params.DataSources] | Omit = omit,
        instructions: Optional[str] | Omit = omit,
        metadata: Optional[Dict[str, str]] | Omit = omit,
        previous_response_id: Optional[str] | Omit = omit,
        reasoning: Optional[response_create_params.Reasoning] | Omit = omit,
        text: Optional[response_create_params.Text] | Omit = omit,
        tools: Optional[Iterable[response_create_params.Tool]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Stream[ResponseStreamEvent]:
        """
        Create a response.

        Generates an answer to the given input, grounded in live web research and
        annotated with URL citations. Set `model` to `parallel`; `reasoning.effort`
        (`low`/`medium`/`high`/`auto`) controls how much research is performed, trading
        response time for answer quality. Returns an OpenAI-format `Response` as
        `application/json`, or a `text/event-stream` of OpenAI Responses SSE events when
        `stream=true`.

        Args:
          input: The input to generate a response for: a plain string, or a list of role/content
              messages that includes at least one `user` message. Must be non-empty, and only
              text content is supported. `input` and `instructions` together may total at most
              20,000 characters.

          model: The model to run. `parallel` is the only supported value (matched
              case-insensitively); any other value is rejected. To trade response time for
              answer quality, set `reasoning.effort` (low/medium/high/auto) rather than
              changing the model name.

          stream: Whether to stream the response.

          background: Background mode is not supported: requests with `background=true` are rejected
              with a 422 validation error. Use the Task API (POST /v1/tasks/runs) for
              long-running work.

          data_sources:
              Data partners to enable for this request, in addition to web search:
              `pay_per_use` partners are billed per call, `free` partners are not. Same names
              and shape as the Task API's `advanced_settings.data_sources`; see the Data
              Sources documentation. Supported at every `reasoning.effort`. Lower efforts make
              fewer partner calls per answer, and `auto` can stop at `low`. For a partner
              whose lookups take several steps, such as a search and then a detail fetch, use
              `medium` (the default) or `high`. A partner name must not collide with an `mcp`
              tool's `server_label`.

          instructions: System instructions for the model.

          metadata: Arbitrary key-value pairs, echoed back on the Response object. Useful for
              tagging requests. At most 16 keys; keys up to 64 characters, values up to 512
              characters.

          previous_response_id: ID of a previous response to use as conversation context.

          reasoning: Reasoning configuration (OpenAI-compatible subset).

          text: Text output configuration. By default the response is plain text; for structured
              output set `format` to `{"type": "json_schema", "name": ..., "schema": {...}}`.
              On `/v1/responses` the `json_object` format produces plain text and may be
              refused with a 400; use `json_schema` instead.

          tools: OpenAI tools. Web grounding is always on, so no tool is needed to search; a
              `web_search` tool's `filters` restrict the domains searched and cited
              (`allowed_domains` maps to Parallel's `source_policy.include_domains`,
              `blocked_domains` to `exclude_domains`). An `mcp` tool gives the model a remote
              MCP server to call; at most 10 per request. A tool of any other `type` is
              accepted and ignored. A tool whose `type` is missing or not a string is
              rejected.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        *,
        input: Union[str, Iterable[response_create_params.InputUnionMember1]],
        model: str,
        stream: bool,
        background: Optional[bool] | Omit = omit,
        data_sources: Optional[response_create_params.DataSources] | Omit = omit,
        instructions: Optional[str] | Omit = omit,
        metadata: Optional[Dict[str, str]] | Omit = omit,
        previous_response_id: Optional[str] | Omit = omit,
        reasoning: Optional[response_create_params.Reasoning] | Omit = omit,
        text: Optional[response_create_params.Text] | Omit = omit,
        tools: Optional[Iterable[response_create_params.Tool]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ResponseResult | Stream[ResponseStreamEvent]:
        """
        Create a response.

        Generates an answer to the given input, grounded in live web research and
        annotated with URL citations. Set `model` to `parallel`; `reasoning.effort`
        (`low`/`medium`/`high`/`auto`) controls how much research is performed, trading
        response time for answer quality. Returns an OpenAI-format `Response` as
        `application/json`, or a `text/event-stream` of OpenAI Responses SSE events when
        `stream=true`.

        Args:
          input: The input to generate a response for: a plain string, or a list of role/content
              messages that includes at least one `user` message. Must be non-empty, and only
              text content is supported. `input` and `instructions` together may total at most
              20,000 characters.

          model: The model to run. `parallel` is the only supported value (matched
              case-insensitively); any other value is rejected. To trade response time for
              answer quality, set `reasoning.effort` (low/medium/high/auto) rather than
              changing the model name.

          stream: Whether to stream the response.

          background: Background mode is not supported: requests with `background=true` are rejected
              with a 422 validation error. Use the Task API (POST /v1/tasks/runs) for
              long-running work.

          data_sources:
              Data partners to enable for this request, in addition to web search:
              `pay_per_use` partners are billed per call, `free` partners are not. Same names
              and shape as the Task API's `advanced_settings.data_sources`; see the Data
              Sources documentation. Supported at every `reasoning.effort`. Lower efforts make
              fewer partner calls per answer, and `auto` can stop at `low`. For a partner
              whose lookups take several steps, such as a search and then a detail fetch, use
              `medium` (the default) or `high`. A partner name must not collide with an `mcp`
              tool's `server_label`.

          instructions: System instructions for the model.

          metadata: Arbitrary key-value pairs, echoed back on the Response object. Useful for
              tagging requests. At most 16 keys; keys up to 64 characters, values up to 512
              characters.

          previous_response_id: ID of a previous response to use as conversation context.

          reasoning: Reasoning configuration (OpenAI-compatible subset).

          text: Text output configuration. By default the response is plain text; for structured
              output set `format` to `{"type": "json_schema", "name": ..., "schema": {...}}`.
              On `/v1/responses` the `json_object` format produces plain text and may be
              refused with a 400; use `json_schema` instead.

          tools: OpenAI tools. Web grounding is always on, so no tool is needed to search; a
              `web_search` tool's `filters` restrict the domains searched and cited
              (`allowed_domains` maps to Parallel's `source_policy.include_domains`,
              `blocked_domains` to `exclude_domains`). An `mcp` tool gives the model a remote
              MCP server to call; at most 10 per request. A tool of any other `type` is
              accepted and ignored. A tool whose `type` is missing or not a string is
              rejected.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["input", "model"], ["input", "model", "stream"])
    def create(
        self,
        *,
        input: Union[str, Iterable[response_create_params.InputUnionMember1]],
        model: str,
        background: Optional[bool] | Omit = omit,
        data_sources: Optional[response_create_params.DataSources] | Omit = omit,
        instructions: Optional[str] | Omit = omit,
        metadata: Optional[Dict[str, str]] | Omit = omit,
        previous_response_id: Optional[str] | Omit = omit,
        reasoning: Optional[response_create_params.Reasoning] | Omit = omit,
        stream: Optional[Literal[False]] | Literal[True] | Omit = omit,
        text: Optional[response_create_params.Text] | Omit = omit,
        tools: Optional[Iterable[response_create_params.Tool]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ResponseResult | Stream[ResponseStreamEvent]:
        return self._post(
            "/v1/responses",
            body=maybe_transform(
                {
                    "input": input,
                    "model": model,
                    "background": background,
                    "data_sources": data_sources,
                    "instructions": instructions,
                    "metadata": metadata,
                    "previous_response_id": previous_response_id,
                    "reasoning": reasoning,
                    "stream": stream,
                    "text": text,
                    "tools": tools,
                },
                response_create_params.ResponseCreateParamsStreaming
                if stream
                else response_create_params.ResponseCreateParamsNonStreaming,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResponseResult,
            stream=stream or False,
            stream_cls=Stream[ResponseStreamEvent],
        )


class AsyncResponsesResource(AsyncAPIResource):
    """
    An OpenAI-Responses-compatible interface for answers grounded in live web research, with URL citations. Point any Responses-API client — the OpenAI Python SDK, OpenAI TypeScript SDK, the Agents SDK, or raw HTTP — at `https://api.parallel.ai` with your Parallel API key, set `model` to `parallel`, and call `/v1/responses`.
    - `input` accepts a plain string or an array of role/content messages (canonical OpenAI shape; text content only).
    - `reasoning.effort` (`low`/`medium`/`high`/`auto`) controls how much research is performed, trading response time for answer quality.
    - Multi-turn via `previous_response_id`.
    - Structured outputs via `text.format = {"type": "json_schema", "name": ..., "schema": {...}}`.
    - Streaming (`stream=true`) emits the standard OpenAI Responses SSE lifecycle: `response.created` and `response.in_progress`, then output item / content part / text delta events with URL-citation annotations, the matching `*.done` events, and a terminal `response.completed` — or `response.failed` if the request fails mid-stream.
    """

    @cached_property
    def with_raw_response(self) -> AsyncResponsesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/parallel-web/parallel-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncResponsesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncResponsesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/parallel-web/parallel-sdk-python#with_streaming_response
        """
        return AsyncResponsesResourceWithStreamingResponse(self)

    @overload
    async def create(
        self,
        *,
        input: Union[str, Iterable[response_create_params.InputUnionMember1]],
        model: str,
        background: Optional[bool] | Omit = omit,
        data_sources: Optional[response_create_params.DataSources] | Omit = omit,
        instructions: Optional[str] | Omit = omit,
        metadata: Optional[Dict[str, str]] | Omit = omit,
        previous_response_id: Optional[str] | Omit = omit,
        reasoning: Optional[response_create_params.Reasoning] | Omit = omit,
        stream: Optional[Literal[False]] | Omit = omit,
        text: Optional[response_create_params.Text] | Omit = omit,
        tools: Optional[Iterable[response_create_params.Tool]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ResponseResult:
        """
        Create a response.

        Generates an answer to the given input, grounded in live web research and
        annotated with URL citations. Set `model` to `parallel`; `reasoning.effort`
        (`low`/`medium`/`high`/`auto`) controls how much research is performed, trading
        response time for answer quality. Returns an OpenAI-format `Response` as
        `application/json`, or a `text/event-stream` of OpenAI Responses SSE events when
        `stream=true`.

        Args:
          input: The input to generate a response for: a plain string, or a list of role/content
              messages that includes at least one `user` message. Must be non-empty, and only
              text content is supported. `input` and `instructions` together may total at most
              20,000 characters.

          model: The model to run. `parallel` is the only supported value (matched
              case-insensitively); any other value is rejected. To trade response time for
              answer quality, set `reasoning.effort` (low/medium/high/auto) rather than
              changing the model name.

          background: Background mode is not supported: requests with `background=true` are rejected
              with a 422 validation error. Use the Task API (POST /v1/tasks/runs) for
              long-running work.

          data_sources:
              Data partners to enable for this request, in addition to web search:
              `pay_per_use` partners are billed per call, `free` partners are not. Same names
              and shape as the Task API's `advanced_settings.data_sources`; see the Data
              Sources documentation. Supported at every `reasoning.effort`. Lower efforts make
              fewer partner calls per answer, and `auto` can stop at `low`. For a partner
              whose lookups take several steps, such as a search and then a detail fetch, use
              `medium` (the default) or `high`. A partner name must not collide with an `mcp`
              tool's `server_label`.

          instructions: System instructions for the model.

          metadata: Arbitrary key-value pairs, echoed back on the Response object. Useful for
              tagging requests. At most 16 keys; keys up to 64 characters, values up to 512
              characters.

          previous_response_id: ID of a previous response to use as conversation context.

          reasoning: Reasoning configuration (OpenAI-compatible subset).

          stream: Whether to stream the response.

          text: Text output configuration. By default the response is plain text; for structured
              output set `format` to `{"type": "json_schema", "name": ..., "schema": {...}}`.
              On `/v1/responses` the `json_object` format produces plain text and may be
              refused with a 400; use `json_schema` instead.

          tools: OpenAI tools. Web grounding is always on, so no tool is needed to search; a
              `web_search` tool's `filters` restrict the domains searched and cited
              (`allowed_domains` maps to Parallel's `source_policy.include_domains`,
              `blocked_domains` to `exclude_domains`). An `mcp` tool gives the model a remote
              MCP server to call; at most 10 per request. A tool of any other `type` is
              accepted and ignored. A tool whose `type` is missing or not a string is
              rejected.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        *,
        input: Union[str, Iterable[response_create_params.InputUnionMember1]],
        model: str,
        stream: Literal[True],
        background: Optional[bool] | Omit = omit,
        data_sources: Optional[response_create_params.DataSources] | Omit = omit,
        instructions: Optional[str] | Omit = omit,
        metadata: Optional[Dict[str, str]] | Omit = omit,
        previous_response_id: Optional[str] | Omit = omit,
        reasoning: Optional[response_create_params.Reasoning] | Omit = omit,
        text: Optional[response_create_params.Text] | Omit = omit,
        tools: Optional[Iterable[response_create_params.Tool]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncStream[ResponseStreamEvent]:
        """
        Create a response.

        Generates an answer to the given input, grounded in live web research and
        annotated with URL citations. Set `model` to `parallel`; `reasoning.effort`
        (`low`/`medium`/`high`/`auto`) controls how much research is performed, trading
        response time for answer quality. Returns an OpenAI-format `Response` as
        `application/json`, or a `text/event-stream` of OpenAI Responses SSE events when
        `stream=true`.

        Args:
          input: The input to generate a response for: a plain string, or a list of role/content
              messages that includes at least one `user` message. Must be non-empty, and only
              text content is supported. `input` and `instructions` together may total at most
              20,000 characters.

          model: The model to run. `parallel` is the only supported value (matched
              case-insensitively); any other value is rejected. To trade response time for
              answer quality, set `reasoning.effort` (low/medium/high/auto) rather than
              changing the model name.

          stream: Whether to stream the response.

          background: Background mode is not supported: requests with `background=true` are rejected
              with a 422 validation error. Use the Task API (POST /v1/tasks/runs) for
              long-running work.

          data_sources:
              Data partners to enable for this request, in addition to web search:
              `pay_per_use` partners are billed per call, `free` partners are not. Same names
              and shape as the Task API's `advanced_settings.data_sources`; see the Data
              Sources documentation. Supported at every `reasoning.effort`. Lower efforts make
              fewer partner calls per answer, and `auto` can stop at `low`. For a partner
              whose lookups take several steps, such as a search and then a detail fetch, use
              `medium` (the default) or `high`. A partner name must not collide with an `mcp`
              tool's `server_label`.

          instructions: System instructions for the model.

          metadata: Arbitrary key-value pairs, echoed back on the Response object. Useful for
              tagging requests. At most 16 keys; keys up to 64 characters, values up to 512
              characters.

          previous_response_id: ID of a previous response to use as conversation context.

          reasoning: Reasoning configuration (OpenAI-compatible subset).

          text: Text output configuration. By default the response is plain text; for structured
              output set `format` to `{"type": "json_schema", "name": ..., "schema": {...}}`.
              On `/v1/responses` the `json_object` format produces plain text and may be
              refused with a 400; use `json_schema` instead.

          tools: OpenAI tools. Web grounding is always on, so no tool is needed to search; a
              `web_search` tool's `filters` restrict the domains searched and cited
              (`allowed_domains` maps to Parallel's `source_policy.include_domains`,
              `blocked_domains` to `exclude_domains`). An `mcp` tool gives the model a remote
              MCP server to call; at most 10 per request. A tool of any other `type` is
              accepted and ignored. A tool whose `type` is missing or not a string is
              rejected.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        *,
        input: Union[str, Iterable[response_create_params.InputUnionMember1]],
        model: str,
        stream: bool,
        background: Optional[bool] | Omit = omit,
        data_sources: Optional[response_create_params.DataSources] | Omit = omit,
        instructions: Optional[str] | Omit = omit,
        metadata: Optional[Dict[str, str]] | Omit = omit,
        previous_response_id: Optional[str] | Omit = omit,
        reasoning: Optional[response_create_params.Reasoning] | Omit = omit,
        text: Optional[response_create_params.Text] | Omit = omit,
        tools: Optional[Iterable[response_create_params.Tool]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ResponseResult | AsyncStream[ResponseStreamEvent]:
        """
        Create a response.

        Generates an answer to the given input, grounded in live web research and
        annotated with URL citations. Set `model` to `parallel`; `reasoning.effort`
        (`low`/`medium`/`high`/`auto`) controls how much research is performed, trading
        response time for answer quality. Returns an OpenAI-format `Response` as
        `application/json`, or a `text/event-stream` of OpenAI Responses SSE events when
        `stream=true`.

        Args:
          input: The input to generate a response for: a plain string, or a list of role/content
              messages that includes at least one `user` message. Must be non-empty, and only
              text content is supported. `input` and `instructions` together may total at most
              20,000 characters.

          model: The model to run. `parallel` is the only supported value (matched
              case-insensitively); any other value is rejected. To trade response time for
              answer quality, set `reasoning.effort` (low/medium/high/auto) rather than
              changing the model name.

          stream: Whether to stream the response.

          background: Background mode is not supported: requests with `background=true` are rejected
              with a 422 validation error. Use the Task API (POST /v1/tasks/runs) for
              long-running work.

          data_sources:
              Data partners to enable for this request, in addition to web search:
              `pay_per_use` partners are billed per call, `free` partners are not. Same names
              and shape as the Task API's `advanced_settings.data_sources`; see the Data
              Sources documentation. Supported at every `reasoning.effort`. Lower efforts make
              fewer partner calls per answer, and `auto` can stop at `low`. For a partner
              whose lookups take several steps, such as a search and then a detail fetch, use
              `medium` (the default) or `high`. A partner name must not collide with an `mcp`
              tool's `server_label`.

          instructions: System instructions for the model.

          metadata: Arbitrary key-value pairs, echoed back on the Response object. Useful for
              tagging requests. At most 16 keys; keys up to 64 characters, values up to 512
              characters.

          previous_response_id: ID of a previous response to use as conversation context.

          reasoning: Reasoning configuration (OpenAI-compatible subset).

          text: Text output configuration. By default the response is plain text; for structured
              output set `format` to `{"type": "json_schema", "name": ..., "schema": {...}}`.
              On `/v1/responses` the `json_object` format produces plain text and may be
              refused with a 400; use `json_schema` instead.

          tools: OpenAI tools. Web grounding is always on, so no tool is needed to search; a
              `web_search` tool's `filters` restrict the domains searched and cited
              (`allowed_domains` maps to Parallel's `source_policy.include_domains`,
              `blocked_domains` to `exclude_domains`). An `mcp` tool gives the model a remote
              MCP server to call; at most 10 per request. A tool of any other `type` is
              accepted and ignored. A tool whose `type` is missing or not a string is
              rejected.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["input", "model"], ["input", "model", "stream"])
    async def create(
        self,
        *,
        input: Union[str, Iterable[response_create_params.InputUnionMember1]],
        model: str,
        background: Optional[bool] | Omit = omit,
        data_sources: Optional[response_create_params.DataSources] | Omit = omit,
        instructions: Optional[str] | Omit = omit,
        metadata: Optional[Dict[str, str]] | Omit = omit,
        previous_response_id: Optional[str] | Omit = omit,
        reasoning: Optional[response_create_params.Reasoning] | Omit = omit,
        stream: Optional[Literal[False]] | Literal[True] | Omit = omit,
        text: Optional[response_create_params.Text] | Omit = omit,
        tools: Optional[Iterable[response_create_params.Tool]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ResponseResult | AsyncStream[ResponseStreamEvent]:
        return await self._post(
            "/v1/responses",
            body=await async_maybe_transform(
                {
                    "input": input,
                    "model": model,
                    "background": background,
                    "data_sources": data_sources,
                    "instructions": instructions,
                    "metadata": metadata,
                    "previous_response_id": previous_response_id,
                    "reasoning": reasoning,
                    "stream": stream,
                    "text": text,
                    "tools": tools,
                },
                response_create_params.ResponseCreateParamsStreaming
                if stream
                else response_create_params.ResponseCreateParamsNonStreaming,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResponseResult,
            stream=stream or False,
            stream_cls=AsyncStream[ResponseStreamEvent],
        )


class ResponsesResourceWithRawResponse:
    def __init__(self, responses: ResponsesResource) -> None:
        self._responses = responses

        self.create = to_raw_response_wrapper(
            responses.create,
        )


class AsyncResponsesResourceWithRawResponse:
    def __init__(self, responses: AsyncResponsesResource) -> None:
        self._responses = responses

        self.create = async_to_raw_response_wrapper(
            responses.create,
        )


class ResponsesResourceWithStreamingResponse:
    def __init__(self, responses: ResponsesResource) -> None:
        self._responses = responses

        self.create = to_streamed_response_wrapper(
            responses.create,
        )


class AsyncResponsesResourceWithStreamingResponse:
    def __init__(self, responses: AsyncResponsesResource) -> None:
        self._responses = responses

        self.create = async_to_streamed_response_wrapper(
            responses.create,
        )
