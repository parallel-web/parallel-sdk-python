# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from ..._types import SequenceNotStr

__all__ = [
    "ResponseCreateParamsBase",
    "InputUnionMember1",
    "InputUnionMember1ContentUnionMember1",
    "DataSources",
    "Reasoning",
    "Text",
    "TextFormat",
    "TextFormatResponseFormatText",
    "TextFormatResponseFormatTextJsonSchemaConfig",
    "TextFormatResponseFormatJsonObject",
    "Tool",
    "ToolResponseWebSearchTool",
    "ToolResponseWebSearchToolFilters",
    "ToolResponseWebSearchToolUserLocation",
    "ToolResponseMcpTool",
    "ResponseCreateParamsNonStreaming",
    "ResponseCreateParamsStreaming",
]


class ResponseCreateParamsBase(TypedDict, total=False):
    input: Required[Union[str, Iterable[InputUnionMember1]]]
    """
    The input to generate a response for: a plain string, or a list of role/content
    messages that includes at least one `user` message. Must be non-empty, and only
    text content is supported. `input` and `instructions` together may total at most
    20,000 characters.
    """

    model: Required[str]
    """The model to run.

    `parallel` is the only supported value (matched case-insensitively); any other
    value is rejected. To trade response time for answer quality, set
    `reasoning.effort` (low/medium/high/auto) rather than changing the model name.
    """

    background: Optional[bool]
    """
    Background mode is not supported: requests with `background=true` are rejected
    with a 422 validation error. Use the Task API (POST /v1/tasks/runs) for
    long-running work.
    """

    data_sources: Optional[DataSources]
    """
    Data partners to enable for this request, in addition to web search:
    `pay_per_use` partners are billed per call, `free` partners are not. Same names
    and shape as the Task API's `advanced_settings.data_sources`; see the Data
    Sources documentation. Supported at every `reasoning.effort`. Lower efforts make
    fewer partner calls per answer, and `auto` can stop at `low`. For a partner
    whose lookups take several steps, such as a search and then a detail fetch, use
    `medium` (the default) or `high`. A partner name must not collide with an `mcp`
    tool's `server_label`.
    """

    instructions: Optional[str]
    """System instructions for the model."""

    metadata: Optional[Dict[str, str]]
    """Arbitrary key-value pairs, echoed back on the Response object.

    Useful for tagging requests. At most 16 keys; keys up to 64 characters, values
    up to 512 characters.
    """

    previous_response_id: Optional[str]
    """ID of a previous response to use as conversation context."""

    reasoning: Optional[Reasoning]
    """Reasoning configuration (OpenAI-compatible subset)."""

    text: Optional[Text]
    """Text output configuration.

    By default the response is plain text; for structured output set `format` to
    `{"type": "json_schema", "name": ..., "schema": {...}}`. On `/v1/responses` the
    `json_object` format produces plain text and may be refused with a 400; use
    `json_schema` instead.
    """

    tools: Optional[Iterable[Tool]]
    """OpenAI tools.

    Web grounding is always on, so no tool is needed to search; a `web_search`
    tool's `filters` restrict the domains searched and cited (`allowed_domains` maps
    to Parallel's `source_policy.include_domains`, `blocked_domains` to
    `exclude_domains`). An `mcp` tool gives the model a remote MCP server to call;
    at most 10 per request. A tool of any other `type` is accepted and ignored. A
    tool whose `type` is missing or not a string is rejected.
    """


class InputUnionMember1ContentUnionMember1(TypedDict, total=False):
    """A single content part of a message, e.g.
    `{"text": "hi", "type": "input_text"}`.

    Only text parts are supported;
    requests containing image, audio, or file parts fail with a 422 error.
    """

    text: Optional[str]
    """The text payload, when the part carries one."""

    type: Optional[str]
    """The content part type.

    Supported: `input_text`, `output_text`, and `text`. Multimodal types
    (`input_image`, `input_audio`, `input_file`) are rejected with a 422 error.
    """


class InputUnionMember1(TypedDict, total=False):
    """A single input message for the Responses API.

    `content` accepts either a bare string (`"hi"`) or the canonical OpenAI
    list-of-parts (`[{"text": "hi", "type": "input_text"}]`).
    """

    content: Required[Union[str, Iterable[InputUnionMember1ContentUnionMember1]]]
    """Text content of the message.

    Either a string or a list of content parts (`{text, type}` objects) for OpenAI
    SDK clients.
    """

    role: Required[Literal["user", "assistant", "system", "developer"]]
    """The role of the message author."""


class DataSources(TypedDict, total=False):
    """
    Data partners to enable for this request, in addition to web search: `pay_per_use` partners are billed per call, `free` partners are not. Same names and shape as the Task API's `advanced_settings.data_sources`; see the Data Sources documentation. Supported at every `reasoning.effort`. Lower efforts make fewer partner calls per answer, and `auto` can stop at `low`. For a partner whose lookups take several steps, such as a search and then a detail fetch, use `medium` (the default) or `high`. A partner name must not collide with an `mcp` tool's `server_label`.
    """

    excluded: SequenceNotStr[str]
    """Data partners included with the processor to keep out of this task.

    Excluding a partner also blocks its own domains. See the Data Sources
    documentation for the available names.
    """

    free: SequenceNotStr[str]
    """
    Free data partners to enable for this task, in addition to sources included with
    the processor. Never billed. See the Data Sources documentation for the
    available names.
    """

    pay_per_use: SequenceNotStr[str]
    """
    Pay-per-use data partners to enable for this task, in addition to sources
    included with the processor. See the Data Sources documentation for the
    available names.
    """


class Reasoning(TypedDict, total=False):
    """Reasoning configuration (OpenAI-compatible subset)."""

    effort: Optional[Literal["low", "medium", "high", "auto"]]
    """
    Controls how much research is performed, trading response time for answer
    quality. Defaults to `medium` when omitted. `auto` picks the right effort for
    each query.
    """


class TextFormatResponseFormatText(  # type: ignore[call-arg]
    TypedDict,
    total=False,
    extra_items=object,  # pyright: ignore[reportGeneralTypeIssues]
):
    """Default response format. Used to generate text responses."""

    type: Required[Literal["text"]]


class TextFormatResponseFormatTextJsonSchemaConfig(  # type: ignore[call-arg]
    TypedDict,
    total=False,
    extra_items=object,  # pyright: ignore[reportGeneralTypeIssues]
):
    """JSON Schema output format: the response's output text conforms to `schema`."""

    name: Required[str]

    schema: Required[Dict[str, object]]

    type: Required[Literal["json_schema"]]

    description: Optional[str]

    strict: Optional[bool]


class TextFormatResponseFormatJsonObject(  # type: ignore[call-arg]
    TypedDict,
    total=False,
    extra_items=object,  # pyright: ignore[reportGeneralTypeIssues]
):
    """JSON object response format.

    An older method of generating JSON responses.
    Using `json_schema` is recommended for models that support it. Note that the
    model will not generate JSON without a system or user message instructing it
    to do so.
    """

    type: Required[Literal["json_object"]]


TextFormat: TypeAlias = Union[
    TextFormatResponseFormatText, TextFormatResponseFormatTextJsonSchemaConfig, TextFormatResponseFormatJsonObject
]


class Text(  # type: ignore[call-arg]
    TypedDict,
    total=False,
    extra_items=object,  # pyright: ignore[reportGeneralTypeIssues]
):
    """Text output configuration.

    By default the response is plain text; for
    structured output set `format` to
    `{"type": "json_schema", "name": ..., "schema": {...}}`. On `/v1/responses`
    the `json_object` format produces plain text and may be refused with a 400;
    use `json_schema` instead.
    """

    format: Optional[TextFormat]
    """Default response format. Used to generate text responses."""

    verbosity: Optional[Literal["low", "medium", "high"]]


class ToolResponseWebSearchToolFilters(TypedDict, total=False):
    """
    Domain filters on the OpenAI `web_search` tool, mapped onto Parallel's
    source policy: `allowed_domains` -> `include_domains`, `blocked_domains` ->
    `exclude_domains`. Entries follow the Source Policy rules (plain domains
    match their subdomains; no schemes, ports, query strings or fragments; at
    most 200 entries in total). With both lists, a source must be on an allowed
    domain and not on a blocked one.
    """

    allowed_domains: Optional[SequenceNotStr[str]]
    """Only sources on these domains (and their subdomains) are used.

    Maps to `source_policy.include_domains`.
    """

    blocked_domains: Optional[SequenceNotStr[str]]
    """
    Sources on these domains (and their subdomains) are excluded, also inside
    `allowed_domains`. Maps to `source_policy.exclude_domains`.
    """


class ToolResponseWebSearchToolUserLocation(TypedDict, total=False):
    """The approximate location of the user."""

    city: Optional[str]

    country: Optional[str]

    region: Optional[str]

    timezone: Optional[str]

    type: Optional[Literal["approximate"]]


class ToolResponseWebSearchTool(TypedDict, total=False):
    """The OpenAI `web_search` tool.

    Web grounding is always on, so the tool
    itself changes nothing; its `filters` restrict which domains are searched.
    `search_context_size` and `user_location` are accepted and ignored.
    Searches always fetch live content, so `external_web_access: false` is
    rejected. Any other key is rejected.
    """

    type: Required[Literal["web_search", "web_search_2025_08_26"]]

    filters: Optional[ToolResponseWebSearchToolFilters]
    """
    Domain filters on the OpenAI `web_search` tool, mapped onto Parallel's source
    policy: `allowed_domains` -> `include_domains`, `blocked_domains` ->
    `exclude_domains`. Entries follow the Source Policy rules (plain domains match
    their subdomains; no schemes, ports, query strings or fragments; at most 200
    entries in total). With both lists, a source must be on an allowed domain and
    not on a blocked one.
    """

    search_context_size: Optional[Literal["low", "medium", "high"]]

    user_location: Optional[ToolResponseWebSearchToolUserLocation]
    """The approximate location of the user."""


class ToolResponseMcpTool(TypedDict, total=False):
    """
    The OpenAI `mcp` tool: a remote MCP server the `parallel` model may call
    while researching, alongside web search. Each call is reported as an
    `mcp_call` output item. `headers` and `authorization` are sent to the
    server and never echoed back. Parallel runs tool calls without an approval
    round trip, so `require_approval` must be set to `never` explicitly.
    The model calls tools directly, so `allowed_callers`, when set, must
    include `direct`. `connector_id` and `tunnel_id` are not supported. Any
    other key is rejected.
    """

    require_approval: Required[Literal["never"]]
    """Must be `never`: tool calls run without an approval step."""

    server_label: Required[str]
    """Name for this server.

    Appears as `server_label` on its `mcp_call` items and must not collide with a
    `data_sources` partner name.
    """

    server_url: Required[str]
    """URL of the MCP server."""

    type: Required[Literal["mcp"]]

    allowed_tools: Optional[SequenceNotStr[str]]
    """Tool names the model may call on this server.

    Omit to allow every tool; an empty list is rejected.
    """

    authorization: Optional[str]
    """OAuth access token, sent as `Authorization: Bearer <token>`."""

    headers: Optional[Dict[str, str]]
    """
    HTTP headers sent on every request to the server, for authentication or other
    purposes.
    """

    server_description: Optional[str]


Tool: TypeAlias = Union[ToolResponseWebSearchTool, ToolResponseMcpTool, Dict[str, object]]


class ResponseCreateParamsNonStreaming(ResponseCreateParamsBase, total=False):
    stream: Optional[Literal[False]]
    """Whether to stream the response."""


class ResponseCreateParamsStreaming(ResponseCreateParamsBase):
    stream: Required[Literal[True]]
    """Whether to stream the response."""


ResponseCreateParams = Union[ResponseCreateParamsNonStreaming, ResponseCreateParamsStreaming]
