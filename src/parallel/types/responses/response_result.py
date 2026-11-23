# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import builtins
from typing import TYPE_CHECKING, Dict, List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from pydantic import Field as FieldInfo

from ..._utils import PropertyInfo
from ..._models import BaseModel

__all__ = [
    "ResponseResult",
    "Output",
    "OutputResponseOutputMessage",
    "OutputResponseOutputMessageContent",
    "OutputResponseOutputMessageContentAnnotation",
    "OutputResponseOutputMessageContentLogprob",
    "OutputResponseOutputMessageContentLogprobTopLogprob",
    "OutputResponseFunctionWebSearch",
    "OutputResponseFunctionWebSearchAction",
    "OutputResponseFunctionWebSearchActionActionSearch",
    "OutputResponseFunctionWebSearchActionActionSearchSource",
    "OutputResponseFunctionWebSearchActionActionOpenPage",
    "OutputResponseMcpCall",
    "OutputResponseMcpCallError",
    "OutputResponseMcpCallErrorMcpProtocolError",
    "OutputResponseMcpCallErrorMcpToolExecutionError",
    "OutputResponseMcpCallErrorHTTPError",
    "OutputResponseMcpListTools",
    "OutputResponseMcpListToolsTool",
    "Error",
    "IncompleteDetails",
    "Moderation",
    "ModerationInput",
    "ModerationInputModerationInputModerationResult",
    "ModerationInputModerationInputError",
    "ModerationOutput",
    "ModerationOutputModerationOutputModerationResult",
    "ModerationOutputModerationOutputError",
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
]


class OutputResponseOutputMessageContentAnnotation(BaseModel):
    """A citation for a web resource used to generate a model response."""

    end_index: int

    start_index: int

    title: str

    type: Literal["url_citation"]

    url: str

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


class OutputResponseOutputMessageContentLogprobTopLogprob(BaseModel):
    """The top log probability of a token."""

    token: str

    bytes: List[int]

    logprob: float

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


class OutputResponseOutputMessageContentLogprob(BaseModel):
    """The log probability of a token."""

    token: str

    bytes: List[int]

    logprob: float

    top_logprobs: List[OutputResponseOutputMessageContentLogprobTopLogprob]

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


class OutputResponseOutputMessageContent(BaseModel):
    """A text content part of an output message.

    `annotations` carries the URL
    citations grounding the answer.
    """

    annotations: List[OutputResponseOutputMessageContentAnnotation]

    text: str

    type: Literal["output_text"]

    logprobs: Optional[List[OutputResponseOutputMessageContentLogprob]] = None

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


class OutputResponseOutputMessage(BaseModel):
    """An assistant message produced by the model."""

    id: str

    content: List[OutputResponseOutputMessageContent]

    role: Literal["assistant"]

    status: Literal["in_progress", "completed", "incomplete"]

    type: Literal["message"]

    phase: Optional[Literal["commentary", "final_answer"]] = None

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


class OutputResponseFunctionWebSearchActionActionSearchSource(BaseModel):
    """A source used in the search."""

    type: Literal["url"]

    url: str

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


class OutputResponseFunctionWebSearchActionActionSearch(BaseModel):
    """Action type "search" - Performs a web search query."""

    type: Literal["search"]

    queries: Optional[List[str]] = None

    query: Optional[str] = None

    sources: Optional[List[OutputResponseFunctionWebSearchActionActionSearchSource]] = None

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


class OutputResponseFunctionWebSearchActionActionOpenPage(BaseModel):
    """Action type "open_page" - Opens a specific URL from search results."""

    type: Literal["open_page"]

    url: Optional[str] = None

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


OutputResponseFunctionWebSearchAction: TypeAlias = Annotated[
    Union[OutputResponseFunctionWebSearchActionActionSearch, OutputResponseFunctionWebSearchActionActionOpenPage],
    PropertyInfo(discriminator="type"),
]


class OutputResponseFunctionWebSearch(BaseModel):
    """
    One web action the `parallel` model took while researching the answer:
    a `search` (`action.queries` are the search queries issued, `action.query`
    the first of them) or an `open_page` (`action.url` is the page it read).
    """

    id: str

    action: OutputResponseFunctionWebSearchAction
    """Action type "search" - Performs a web search query."""

    status: Literal["in_progress", "searching", "completed", "failed", "incomplete"]

    type: Literal["web_search_call"]

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


class OutputResponseMcpCallErrorMcpProtocolError(BaseModel):
    code: int

    message: str

    type: Literal["mcp_protocol_error"]

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


class OutputResponseMcpCallErrorMcpToolExecutionError(BaseModel):
    content: object

    type: Literal["mcp_tool_execution_error"]

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


class OutputResponseMcpCallErrorHTTPError(BaseModel):
    code: int

    message: str

    type: Literal["http_error"]

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


OutputResponseMcpCallError: TypeAlias = Annotated[
    Union[
        OutputResponseMcpCallErrorMcpProtocolError,
        OutputResponseMcpCallErrorMcpToolExecutionError,
        OutputResponseMcpCallErrorHTTPError,
        None,
    ],
    PropertyInfo(discriminator="type"),
]


class OutputResponseMcpCall(BaseModel):
    """
    One tool call the `parallel` model made on an MCP server: a server from
    the request's `mcp` tools, or a partner enabled via `data_sources`.
    `arguments` is the JSON-encoded input; `output` is the text the tool
    returned, or `error` the failure when the call did not succeed.
    """

    id: str

    arguments: str

    name: str

    server_label: str

    status: Literal["completed", "failed"]

    type: Literal["mcp_call"]

    error: Optional[OutputResponseMcpCallError] = None

    output: Optional[str] = None

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


class OutputResponseMcpListToolsTool(BaseModel):
    """A tool available on an MCP server."""

    input_schema: object

    name: str

    annotations: Optional[object] = None

    description: Optional[str] = None

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


class OutputResponseMcpListTools(BaseModel):
    """
    Tools discovered on a customer MCP server, or a connection/listing error.
    Requested data partners report failures only, with an empty tools list.
    """

    id: str

    server_label: str

    tools: List[OutputResponseMcpListToolsTool]

    type: Literal["mcp_list_tools"]

    error: Optional[str] = None

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


Output: TypeAlias = Annotated[
    Union[
        OutputResponseOutputMessage, OutputResponseFunctionWebSearch, OutputResponseMcpCall, OutputResponseMcpListTools
    ],
    PropertyInfo(discriminator="type"),
]


class Error(BaseModel):
    """Details of a failed response."""

    code: Literal["server_error"]
    """Error code; currently always "server_error"."""

    message: str

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


class IncompleteDetails(BaseModel):
    """Details about why the response is incomplete."""

    reason: Optional[Literal["max_output_tokens", "max_messages", "content_filter", "steered"]] = None

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


class ModerationInputModerationInputModerationResult(BaseModel):
    """A moderation result produced for the response input or output."""

    categories: Dict[str, bool]

    category_applied_input_types: Dict[str, List[Literal["text", "image"]]]

    category_scores: Dict[str, float]

    flagged: bool

    model: str

    type: Literal["moderation_result"]

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


class ModerationInputModerationInputError(BaseModel):
    """An error produced while attempting moderation for the response input or output."""

    code: str

    message: str

    type: Literal["error"]

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


ModerationInput: TypeAlias = Union[ModerationInputModerationInputModerationResult, ModerationInputModerationInputError]


class ModerationOutputModerationOutputModerationResult(BaseModel):
    """A moderation result produced for the response input or output."""

    categories: Dict[str, bool]

    category_applied_input_types: Dict[str, List[Literal["text", "image"]]]

    category_scores: Dict[str, float]

    flagged: bool

    model: str

    type: Literal["moderation_result"]

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


class ModerationOutputModerationOutputError(BaseModel):
    """An error produced while attempting moderation for the response input or output."""

    code: str

    message: str

    type: Literal["error"]

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


ModerationOutput: TypeAlias = Union[
    ModerationOutputModerationOutputModerationResult, ModerationOutputModerationOutputError
]


class Moderation(BaseModel):
    """
    Moderation results for the response input and output, if moderated completions were requested.
    """

    input: ModerationInput
    """A moderation result produced for the response input or output."""

    output: ModerationOutput
    """A moderation result produced for the response input or output."""

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


class Reasoning(BaseModel):
    """Reasoning configuration (OpenAI-compatible subset)."""

    effort: Optional[Literal["low", "medium", "high", "auto"]] = None
    """
    Controls how much research is performed, trading response time for answer
    quality. Defaults to `medium` when omitted. `auto` picks the right effort for
    each query.
    """


class TextFormatResponseFormatText(BaseModel):
    """Default response format. Used to generate text responses."""

    type: Literal["text"]

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


class TextFormatResponseFormatTextJsonSchemaConfig(BaseModel):
    """JSON Schema output format: the response's output text conforms to `schema`."""

    name: str

    schema_: Dict[str, object] = FieldInfo(alias="schema")

    type: Literal["json_schema"]

    description: Optional[str] = None

    strict: Optional[bool] = None

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


class TextFormatResponseFormatJsonObject(BaseModel):
    """JSON object response format.

    An older method of generating JSON responses.
    Using `json_schema` is recommended for models that support it. Note that the
    model will not generate JSON without a system or user message instructing it
    to do so.
    """

    type: Literal["json_object"]

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


TextFormat: TypeAlias = Union[
    TextFormatResponseFormatText, TextFormatResponseFormatTextJsonSchemaConfig, TextFormatResponseFormatJsonObject, None
]


class Text(BaseModel):
    """Text output configuration.

    By default the response is plain text; for
    structured output set `format` to
    `{"type": "json_schema", "name": ..., "schema": {...}}`. On `/v1/responses`
    the `json_object` format produces plain text and may be refused with a 400;
    use `json_schema` instead.
    """

    format: Optional[TextFormat] = None
    """Default response format. Used to generate text responses."""

    verbosity: Optional[Literal["low", "medium", "high"]] = None

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


class ToolResponseWebSearchToolFilters(BaseModel):
    """
    Domain filters on the OpenAI `web_search` tool, mapped onto Parallel's
    source policy: `allowed_domains` -> `include_domains`, `blocked_domains` ->
    `exclude_domains`. Entries follow the Source Policy rules (plain domains
    match their subdomains; no schemes, ports, query strings or fragments; at
    most 200 entries in total). With both lists, a source must be on an allowed
    domain and not on a blocked one.
    """

    allowed_domains: Optional[List[str]] = None
    """Only sources on these domains (and their subdomains) are used.

    Maps to `source_policy.include_domains`.
    """

    blocked_domains: Optional[List[str]] = None
    """
    Sources on these domains (and their subdomains) are excluded, also inside
    `allowed_domains`. Maps to `source_policy.exclude_domains`.
    """


class ToolResponseWebSearchToolUserLocation(BaseModel):
    """The approximate location of the user."""

    city: Optional[str] = None

    country: Optional[str] = None

    region: Optional[str] = None

    timezone: Optional[str] = None

    type: Optional[Literal["approximate"]] = None


class ToolResponseWebSearchTool(BaseModel):
    """The OpenAI `web_search` tool.

    Web grounding is always on, so the tool
    itself changes nothing; its `filters` restrict which domains are searched.
    `search_context_size` and `user_location` are accepted and ignored.
    Searches always fetch live content, so `external_web_access: false` is
    rejected. Any other key is rejected.
    """

    type: Literal["web_search", "web_search_2025_08_26"]

    filters: Optional[ToolResponseWebSearchToolFilters] = None
    """
    Domain filters on the OpenAI `web_search` tool, mapped onto Parallel's source
    policy: `allowed_domains` -> `include_domains`, `blocked_domains` ->
    `exclude_domains`. Entries follow the Source Policy rules (plain domains match
    their subdomains; no schemes, ports, query strings or fragments; at most 200
    entries in total). With both lists, a source must be on an allowed domain and
    not on a blocked one.
    """

    search_context_size: Optional[Literal["low", "medium", "high"]] = None

    user_location: Optional[ToolResponseWebSearchToolUserLocation] = None
    """The approximate location of the user."""


class ToolResponseMcpTool(BaseModel):
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

    require_approval: Literal["never"]
    """Must be `never`: tool calls run without an approval step."""

    server_label: str
    """Name for this server.

    Appears as `server_label` on its `mcp_call` items and must not collide with a
    `data_sources` partner name.
    """

    server_url: str
    """URL of the MCP server."""

    type: Literal["mcp"]

    allowed_tools: Optional[List[str]] = None
    """Tool names the model may call on this server.

    Omit to allow every tool; an empty list is rejected.
    """

    headers: Optional[Dict[str, str]] = None
    """
    HTTP headers sent on every request to the server, for authentication or other
    purposes.
    """

    server_description: Optional[str] = None


Tool: TypeAlias = Union[ToolResponseWebSearchTool, ToolResponseMcpTool]


class ResponseResult(BaseModel):
    """A response from the `parallel` model.

    A completed response contains one
    `web_search_call` item per web search the model ran, `mcp_list_tools`
    discovery outcomes, and one `mcp_call` item per MCP tool call it made,
    followed by a single assistant message
    whose text is annotated with URL citations grounding the answer.
    """

    id: str

    created_at: float

    object: Literal["response"]

    output: List[Output]

    parallel_tool_calls: bool

    background: Optional[bool] = None

    completed_at: Optional[float] = None

    conversation: None = None

    effort_used: Optional[Literal["low", "medium", "high"]] = None
    """The effort this response was served and billed at.

    For `auto`, the effort it picked for this query (either `low` or `medium`). Null
    until the response completes.
    """

    error: Optional[Error] = None
    """Details of a failed response."""

    incomplete_details: Optional[IncompleteDetails] = None
    """Details about why the response is incomplete."""

    instructions: Optional[str] = None

    max_output_tokens: Optional[int] = None

    max_tool_calls: Optional[int] = None

    metadata: Optional[Dict[str, str]] = None

    model: Optional[Literal["parallel"]] = None

    moderation: Optional[Moderation] = None
    """
    Moderation results for the response input and output, if moderated completions
    were requested.
    """

    previous_response_id: Optional[str] = None

    prompt: None = None

    prompt_cache_key: Optional[str] = None

    prompt_cache_retention: Optional[Literal["in_memory", "24h"]] = None

    reasoning: Optional[Reasoning] = None
    """Reasoning configuration (OpenAI-compatible subset)."""

    safety_identifier: Optional[str] = None

    service_tier: Optional[Literal["auto", "default", "flex", "scale", "priority", "fast", "ultrafast"]] = None

    status: Optional[Literal["completed", "failed", "in_progress", "cancelled", "queued", "incomplete"]] = None

    temperature: Optional[float] = None

    text: Optional[Text] = None
    """Text output configuration.

    By default the response is plain text; for structured output set `format` to
    `{"type": "json_schema", "name": ..., "schema": {...}}`. On `/v1/responses` the
    `json_object` format produces plain text and may be refused with a 400; use
    `json_schema` instead.
    """

    tool_choice: Optional[str] = None

    tools: Optional[List[Tool]] = None

    top_logprobs: Optional[int] = None

    top_p: Optional[float] = None

    truncation: Optional[Literal["auto", "disabled"]] = None

    usage: None = None
    """Always null: Parallel bills per request, not per token."""

    user: Optional[str] = None

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, builtins.object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> builtins.object: ...
    else:
        __pydantic_extra__: Dict[str, builtins.object]
