# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from pydantic import Field as FieldInfo

from ..._utils import PropertyInfo
from ..._models import BaseModel
from .response_result import ResponseResult

__all__ = [
    "ResponseStreamEvent",
    "ResponseCreatedEvent",
    "ResponseInProgressEvent",
    "ResponseOutputItemAddedEvent",
    "ResponseOutputItemAddedEventItem",
    "ResponseOutputItemAddedEventItemResponseOutputMessage",
    "ResponseOutputItemAddedEventItemResponseOutputMessageContent",
    "ResponseOutputItemAddedEventItemResponseOutputMessageContentAnnotation",
    "ResponseOutputItemAddedEventItemResponseOutputMessageContentLogprob",
    "ResponseOutputItemAddedEventItemResponseOutputMessageContentLogprobTopLogprob",
    "ResponseOutputItemAddedEventItemResponseFunctionWebSearch",
    "ResponseOutputItemAddedEventItemResponseFunctionWebSearchAction",
    "ResponseOutputItemAddedEventItemResponseFunctionWebSearchActionActionSearch",
    "ResponseOutputItemAddedEventItemResponseFunctionWebSearchActionActionSearchSource",
    "ResponseOutputItemAddedEventItemResponseFunctionWebSearchActionActionOpenPage",
    "ResponseOutputItemAddedEventItemResponseMcpCall",
    "ResponseOutputItemAddedEventItemResponseMcpCallError",
    "ResponseOutputItemAddedEventItemResponseMcpCallErrorMcpProtocolError",
    "ResponseOutputItemAddedEventItemResponseMcpCallErrorMcpToolExecutionError",
    "ResponseOutputItemAddedEventItemResponseMcpCallErrorHTTPError",
    "ResponseOutputItemAddedEventItemResponseMcpListTools",
    "ResponseOutputItemAddedEventItemResponseMcpListToolsTool",
    "ResponseWebSearchCallInProgressEvent",
    "ResponseWebSearchCallSearchingEvent",
    "ResponseWebSearchCallCompletedEvent",
    "ResponseMcpCallCompletedEvent",
    "ResponseMcpCallFailedEvent",
    "ResponseMcpListToolsCompletedEvent",
    "ResponseMcpListToolsFailedEvent",
    "ResponseContentPartAddedEvent",
    "ResponseContentPartAddedEventPart",
    "ResponseContentPartAddedEventPartAnnotation",
    "ResponseContentPartAddedEventPartLogprob",
    "ResponseContentPartAddedEventPartLogprobTopLogprob",
    "ResponseTextDeltaEvent",
    "ResponseTextDeltaEventLogprob",
    "ResponseTextDeltaEventLogprobTopLogprob",
    "ResponseTextDoneEvent",
    "ResponseTextDoneEventLogprob",
    "ResponseTextDoneEventLogprobTopLogprob",
    "ResponseOutputTextAnnotationAddedEvent",
    "ResponseOutputTextAnnotationAddedEventAnnotation",
    "ResponseContentPartDoneEvent",
    "ResponseContentPartDoneEventPart",
    "ResponseContentPartDoneEventPartAnnotation",
    "ResponseContentPartDoneEventPartLogprob",
    "ResponseContentPartDoneEventPartLogprobTopLogprob",
    "ResponseOutputItemDoneEvent",
    "ResponseOutputItemDoneEventItem",
    "ResponseOutputItemDoneEventItemResponseOutputMessage",
    "ResponseOutputItemDoneEventItemResponseOutputMessageContent",
    "ResponseOutputItemDoneEventItemResponseOutputMessageContentAnnotation",
    "ResponseOutputItemDoneEventItemResponseOutputMessageContentLogprob",
    "ResponseOutputItemDoneEventItemResponseOutputMessageContentLogprobTopLogprob",
    "ResponseOutputItemDoneEventItemResponseFunctionWebSearch",
    "ResponseOutputItemDoneEventItemResponseFunctionWebSearchAction",
    "ResponseOutputItemDoneEventItemResponseFunctionWebSearchActionActionSearch",
    "ResponseOutputItemDoneEventItemResponseFunctionWebSearchActionActionSearchSource",
    "ResponseOutputItemDoneEventItemResponseFunctionWebSearchActionActionOpenPage",
    "ResponseOutputItemDoneEventItemResponseMcpCall",
    "ResponseOutputItemDoneEventItemResponseMcpCallError",
    "ResponseOutputItemDoneEventItemResponseMcpCallErrorMcpProtocolError",
    "ResponseOutputItemDoneEventItemResponseMcpCallErrorMcpToolExecutionError",
    "ResponseOutputItemDoneEventItemResponseMcpCallErrorHTTPError",
    "ResponseOutputItemDoneEventItemResponseMcpListTools",
    "ResponseOutputItemDoneEventItemResponseMcpListToolsTool",
    "ResponseCompletedEvent",
    "ResponseFailedEvent",
    "ResponseIncompleteEvent",
]


class ResponseCreatedEvent(BaseModel):
    response: ResponseResult
    """A response from the `parallel` model.

    A completed response contains one `web_search_call` item per web search the
    model ran, `mcp_list_tools` discovery outcomes, and one `mcp_call` item per MCP
    tool call it made, followed by a single assistant message whose text is
    annotated with URL citations grounding the answer.
    """

    sequence_number: int

    type: Literal["response.created"]

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


class ResponseInProgressEvent(BaseModel):
    response: ResponseResult
    """A response from the `parallel` model.

    A completed response contains one `web_search_call` item per web search the
    model ran, `mcp_list_tools` discovery outcomes, and one `mcp_call` item per MCP
    tool call it made, followed by a single assistant message whose text is
    annotated with URL citations grounding the answer.
    """

    sequence_number: int

    type: Literal["response.in_progress"]

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


class ResponseOutputItemAddedEventItemResponseOutputMessageContentAnnotation(BaseModel):
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


class ResponseOutputItemAddedEventItemResponseOutputMessageContentLogprobTopLogprob(BaseModel):
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


class ResponseOutputItemAddedEventItemResponseOutputMessageContentLogprob(BaseModel):
    """The log probability of a token."""

    token: str

    bytes: List[int]

    logprob: float

    top_logprobs: List[ResponseOutputItemAddedEventItemResponseOutputMessageContentLogprobTopLogprob]

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


class ResponseOutputItemAddedEventItemResponseOutputMessageContent(BaseModel):
    """A text content part of an output message.

    `annotations` carries the URL
    citations grounding the answer.
    """

    annotations: List[ResponseOutputItemAddedEventItemResponseOutputMessageContentAnnotation]

    text: str

    type: Literal["output_text"]

    logprobs: Optional[List[ResponseOutputItemAddedEventItemResponseOutputMessageContentLogprob]] = None

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


class ResponseOutputItemAddedEventItemResponseOutputMessage(BaseModel):
    """An assistant message produced by the model."""

    id: str

    content: List[ResponseOutputItemAddedEventItemResponseOutputMessageContent]

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


class ResponseOutputItemAddedEventItemResponseFunctionWebSearchActionActionSearchSource(BaseModel):
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


class ResponseOutputItemAddedEventItemResponseFunctionWebSearchActionActionSearch(BaseModel):
    """Action type "search" - Performs a web search query."""

    type: Literal["search"]

    queries: Optional[List[str]] = None

    query: Optional[str] = None

    sources: Optional[List[ResponseOutputItemAddedEventItemResponseFunctionWebSearchActionActionSearchSource]] = None

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


class ResponseOutputItemAddedEventItemResponseFunctionWebSearchActionActionOpenPage(BaseModel):
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


ResponseOutputItemAddedEventItemResponseFunctionWebSearchAction: TypeAlias = Annotated[
    Union[
        ResponseOutputItemAddedEventItemResponseFunctionWebSearchActionActionSearch,
        ResponseOutputItemAddedEventItemResponseFunctionWebSearchActionActionOpenPage,
    ],
    PropertyInfo(discriminator="type"),
]


class ResponseOutputItemAddedEventItemResponseFunctionWebSearch(BaseModel):
    """
    One web action the `parallel` model took while researching the answer:
    a `search` (`action.queries` are the search queries issued, `action.query`
    the first of them) or an `open_page` (`action.url` is the page it read).
    """

    id: str

    action: ResponseOutputItemAddedEventItemResponseFunctionWebSearchAction
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


class ResponseOutputItemAddedEventItemResponseMcpCallErrorMcpProtocolError(BaseModel):
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


class ResponseOutputItemAddedEventItemResponseMcpCallErrorMcpToolExecutionError(BaseModel):
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


class ResponseOutputItemAddedEventItemResponseMcpCallErrorHTTPError(BaseModel):
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


ResponseOutputItemAddedEventItemResponseMcpCallError: TypeAlias = Annotated[
    Union[
        ResponseOutputItemAddedEventItemResponseMcpCallErrorMcpProtocolError,
        ResponseOutputItemAddedEventItemResponseMcpCallErrorMcpToolExecutionError,
        ResponseOutputItemAddedEventItemResponseMcpCallErrorHTTPError,
        None,
    ],
    PropertyInfo(discriminator="type"),
]


class ResponseOutputItemAddedEventItemResponseMcpCall(BaseModel):
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

    error: Optional[ResponseOutputItemAddedEventItemResponseMcpCallError] = None

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


class ResponseOutputItemAddedEventItemResponseMcpListToolsTool(BaseModel):
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


class ResponseOutputItemAddedEventItemResponseMcpListTools(BaseModel):
    """
    Tools discovered on a customer MCP server, or a connection/listing error.
    Requested data partners report failures only, with an empty tools list.
    """

    id: str

    server_label: str

    tools: List[ResponseOutputItemAddedEventItemResponseMcpListToolsTool]

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


ResponseOutputItemAddedEventItem: TypeAlias = Annotated[
    Union[
        ResponseOutputItemAddedEventItemResponseOutputMessage,
        ResponseOutputItemAddedEventItemResponseFunctionWebSearch,
        ResponseOutputItemAddedEventItemResponseMcpCall,
        ResponseOutputItemAddedEventItemResponseMcpListTools,
    ],
    PropertyInfo(discriminator="type"),
]


class ResponseOutputItemAddedEvent(BaseModel):
    item: ResponseOutputItemAddedEventItem
    """An assistant message produced by the model."""

    output_index: int

    sequence_number: int

    type: Literal["response.output_item.added"]

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


class ResponseWebSearchCallInProgressEvent(BaseModel):
    """Emitted when a web search call is initiated."""

    item_id: str

    output_index: int

    sequence_number: int

    type: Literal["response.web_search_call.in_progress"]

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


class ResponseWebSearchCallSearchingEvent(BaseModel):
    """Emitted when a web search call is executing."""

    item_id: str

    output_index: int

    sequence_number: int

    type: Literal["response.web_search_call.searching"]

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


class ResponseWebSearchCallCompletedEvent(BaseModel):
    """Emitted when a web search call is completed."""

    item_id: str

    output_index: int

    sequence_number: int

    type: Literal["response.web_search_call.completed"]

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


class ResponseMcpCallCompletedEvent(BaseModel):
    """Emitted when an MCP  tool call has completed successfully."""

    item_id: str

    output_index: int

    sequence_number: int

    type: Literal["response.mcp_call.completed"]

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


class ResponseMcpCallFailedEvent(BaseModel):
    """Emitted when an MCP  tool call has failed."""

    item_id: str

    output_index: int

    sequence_number: int

    type: Literal["response.mcp_call.failed"]

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


class ResponseMcpListToolsCompletedEvent(BaseModel):
    """Emitted when the list of available MCP tools has been successfully retrieved."""

    item_id: str

    output_index: int

    sequence_number: int

    type: Literal["response.mcp_list_tools.completed"]

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


class ResponseMcpListToolsFailedEvent(BaseModel):
    """Emitted when the attempt to list available MCP tools has failed."""

    item_id: str

    output_index: int

    sequence_number: int

    type: Literal["response.mcp_list_tools.failed"]

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


class ResponseContentPartAddedEventPartAnnotation(BaseModel):
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


class ResponseContentPartAddedEventPartLogprobTopLogprob(BaseModel):
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


class ResponseContentPartAddedEventPartLogprob(BaseModel):
    """The log probability of a token."""

    token: str

    bytes: List[int]

    logprob: float

    top_logprobs: List[ResponseContentPartAddedEventPartLogprobTopLogprob]

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


class ResponseContentPartAddedEventPart(BaseModel):
    """A text content part of an output message.

    `annotations` carries the URL
    citations grounding the answer.
    """

    annotations: List[ResponseContentPartAddedEventPartAnnotation]

    text: str

    type: Literal["output_text"]

    logprobs: Optional[List[ResponseContentPartAddedEventPartLogprob]] = None

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


class ResponseContentPartAddedEvent(BaseModel):
    content_index: int

    item_id: str

    output_index: int

    part: ResponseContentPartAddedEventPart
    """A text content part of an output message.

    `annotations` carries the URL citations grounding the answer.
    """

    sequence_number: int

    type: Literal["response.content_part.added"]

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


class ResponseTextDeltaEventLogprobTopLogprob(BaseModel):
    token: Optional[str] = None

    logprob: Optional[float] = None

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


class ResponseTextDeltaEventLogprob(BaseModel):
    """
    A logprob is the logarithmic probability that the model assigns to producing
    a particular token at a given position in the sequence. Less-negative (higher)
    logprob values indicate greater model confidence in that token choice.
    """

    token: str

    logprob: float

    top_logprobs: Optional[List[ResponseTextDeltaEventLogprobTopLogprob]] = None

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


class ResponseTextDeltaEvent(BaseModel):
    """Emitted when there is an additional text delta."""

    content_index: int

    delta: str

    item_id: str

    logprobs: List[ResponseTextDeltaEventLogprob]

    output_index: int

    sequence_number: int

    type: Literal["response.output_text.delta"]

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


class ResponseTextDoneEventLogprobTopLogprob(BaseModel):
    token: Optional[str] = None

    logprob: Optional[float] = None

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


class ResponseTextDoneEventLogprob(BaseModel):
    """
    A logprob is the logarithmic probability that the model assigns to producing
    a particular token at a given position in the sequence. Less-negative (higher)
    logprob values indicate greater model confidence in that token choice.
    """

    token: str

    logprob: float

    top_logprobs: Optional[List[ResponseTextDoneEventLogprobTopLogprob]] = None

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


class ResponseTextDoneEvent(BaseModel):
    """Emitted when text content is finalized."""

    content_index: int

    item_id: str

    logprobs: List[ResponseTextDoneEventLogprob]

    output_index: int

    sequence_number: int

    text: str

    type: Literal["response.output_text.done"]

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


class ResponseOutputTextAnnotationAddedEventAnnotation(BaseModel):
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


class ResponseOutputTextAnnotationAddedEvent(BaseModel):
    annotation: ResponseOutputTextAnnotationAddedEventAnnotation
    """A citation for a web resource used to generate a model response."""

    annotation_index: int

    content_index: int

    item_id: str

    output_index: int

    sequence_number: int

    type: Literal["response.output_text.annotation.added"]

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


class ResponseContentPartDoneEventPartAnnotation(BaseModel):
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


class ResponseContentPartDoneEventPartLogprobTopLogprob(BaseModel):
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


class ResponseContentPartDoneEventPartLogprob(BaseModel):
    """The log probability of a token."""

    token: str

    bytes: List[int]

    logprob: float

    top_logprobs: List[ResponseContentPartDoneEventPartLogprobTopLogprob]

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


class ResponseContentPartDoneEventPart(BaseModel):
    """A text content part of an output message.

    `annotations` carries the URL
    citations grounding the answer.
    """

    annotations: List[ResponseContentPartDoneEventPartAnnotation]

    text: str

    type: Literal["output_text"]

    logprobs: Optional[List[ResponseContentPartDoneEventPartLogprob]] = None

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


class ResponseContentPartDoneEvent(BaseModel):
    content_index: int

    item_id: str

    output_index: int

    part: ResponseContentPartDoneEventPart
    """A text content part of an output message.

    `annotations` carries the URL citations grounding the answer.
    """

    sequence_number: int

    type: Literal["response.content_part.done"]

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


class ResponseOutputItemDoneEventItemResponseOutputMessageContentAnnotation(BaseModel):
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


class ResponseOutputItemDoneEventItemResponseOutputMessageContentLogprobTopLogprob(BaseModel):
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


class ResponseOutputItemDoneEventItemResponseOutputMessageContentLogprob(BaseModel):
    """The log probability of a token."""

    token: str

    bytes: List[int]

    logprob: float

    top_logprobs: List[ResponseOutputItemDoneEventItemResponseOutputMessageContentLogprobTopLogprob]

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


class ResponseOutputItemDoneEventItemResponseOutputMessageContent(BaseModel):
    """A text content part of an output message.

    `annotations` carries the URL
    citations grounding the answer.
    """

    annotations: List[ResponseOutputItemDoneEventItemResponseOutputMessageContentAnnotation]

    text: str

    type: Literal["output_text"]

    logprobs: Optional[List[ResponseOutputItemDoneEventItemResponseOutputMessageContentLogprob]] = None

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


class ResponseOutputItemDoneEventItemResponseOutputMessage(BaseModel):
    """An assistant message produced by the model."""

    id: str

    content: List[ResponseOutputItemDoneEventItemResponseOutputMessageContent]

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


class ResponseOutputItemDoneEventItemResponseFunctionWebSearchActionActionSearchSource(BaseModel):
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


class ResponseOutputItemDoneEventItemResponseFunctionWebSearchActionActionSearch(BaseModel):
    """Action type "search" - Performs a web search query."""

    type: Literal["search"]

    queries: Optional[List[str]] = None

    query: Optional[str] = None

    sources: Optional[List[ResponseOutputItemDoneEventItemResponseFunctionWebSearchActionActionSearchSource]] = None

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


class ResponseOutputItemDoneEventItemResponseFunctionWebSearchActionActionOpenPage(BaseModel):
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


ResponseOutputItemDoneEventItemResponseFunctionWebSearchAction: TypeAlias = Annotated[
    Union[
        ResponseOutputItemDoneEventItemResponseFunctionWebSearchActionActionSearch,
        ResponseOutputItemDoneEventItemResponseFunctionWebSearchActionActionOpenPage,
    ],
    PropertyInfo(discriminator="type"),
]


class ResponseOutputItemDoneEventItemResponseFunctionWebSearch(BaseModel):
    """
    One web action the `parallel` model took while researching the answer:
    a `search` (`action.queries` are the search queries issued, `action.query`
    the first of them) or an `open_page` (`action.url` is the page it read).
    """

    id: str

    action: ResponseOutputItemDoneEventItemResponseFunctionWebSearchAction
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


class ResponseOutputItemDoneEventItemResponseMcpCallErrorMcpProtocolError(BaseModel):
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


class ResponseOutputItemDoneEventItemResponseMcpCallErrorMcpToolExecutionError(BaseModel):
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


class ResponseOutputItemDoneEventItemResponseMcpCallErrorHTTPError(BaseModel):
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


ResponseOutputItemDoneEventItemResponseMcpCallError: TypeAlias = Annotated[
    Union[
        ResponseOutputItemDoneEventItemResponseMcpCallErrorMcpProtocolError,
        ResponseOutputItemDoneEventItemResponseMcpCallErrorMcpToolExecutionError,
        ResponseOutputItemDoneEventItemResponseMcpCallErrorHTTPError,
        None,
    ],
    PropertyInfo(discriminator="type"),
]


class ResponseOutputItemDoneEventItemResponseMcpCall(BaseModel):
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

    error: Optional[ResponseOutputItemDoneEventItemResponseMcpCallError] = None

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


class ResponseOutputItemDoneEventItemResponseMcpListToolsTool(BaseModel):
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


class ResponseOutputItemDoneEventItemResponseMcpListTools(BaseModel):
    """
    Tools discovered on a customer MCP server, or a connection/listing error.
    Requested data partners report failures only, with an empty tools list.
    """

    id: str

    server_label: str

    tools: List[ResponseOutputItemDoneEventItemResponseMcpListToolsTool]

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


ResponseOutputItemDoneEventItem: TypeAlias = Annotated[
    Union[
        ResponseOutputItemDoneEventItemResponseOutputMessage,
        ResponseOutputItemDoneEventItemResponseFunctionWebSearch,
        ResponseOutputItemDoneEventItemResponseMcpCall,
        ResponseOutputItemDoneEventItemResponseMcpListTools,
    ],
    PropertyInfo(discriminator="type"),
]


class ResponseOutputItemDoneEvent(BaseModel):
    item: ResponseOutputItemDoneEventItem
    """An assistant message produced by the model."""

    output_index: int

    sequence_number: int

    type: Literal["response.output_item.done"]

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


class ResponseCompletedEvent(BaseModel):
    response: ResponseResult
    """A response from the `parallel` model.

    A completed response contains one `web_search_call` item per web search the
    model ran, `mcp_list_tools` discovery outcomes, and one `mcp_call` item per MCP
    tool call it made, followed by a single assistant message whose text is
    annotated with URL citations grounding the answer.
    """

    sequence_number: int

    type: Literal["response.completed"]

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


class ResponseFailedEvent(BaseModel):
    response: ResponseResult
    """A response from the `parallel` model.

    A completed response contains one `web_search_call` item per web search the
    model ran, `mcp_list_tools` discovery outcomes, and one `mcp_call` item per MCP
    tool call it made, followed by a single assistant message whose text is
    annotated with URL citations grounding the answer.
    """

    sequence_number: int

    type: Literal["response.failed"]

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


class ResponseIncompleteEvent(BaseModel):
    response: ResponseResult
    """A response from the `parallel` model.

    A completed response contains one `web_search_call` item per web search the
    model ran, `mcp_list_tools` discovery outcomes, and one `mcp_call` item per MCP
    tool call it made, followed by a single assistant message whose text is
    annotated with URL citations grounding the answer.
    """

    sequence_number: int

    type: Literal["response.incomplete"]

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


ResponseStreamEvent: TypeAlias = Union[
    ResponseCreatedEvent,
    ResponseInProgressEvent,
    ResponseOutputItemAddedEvent,
    ResponseWebSearchCallInProgressEvent,
    ResponseWebSearchCallSearchingEvent,
    ResponseWebSearchCallCompletedEvent,
    ResponseMcpCallCompletedEvent,
    ResponseMcpCallFailedEvent,
    ResponseMcpListToolsCompletedEvent,
    ResponseMcpListToolsFailedEvent,
    ResponseContentPartAddedEvent,
    ResponseTextDeltaEvent,
    ResponseTextDoneEvent,
    ResponseOutputTextAnnotationAddedEvent,
    ResponseContentPartDoneEvent,
    ResponseOutputItemDoneEvent,
    ResponseCompletedEvent,
    ResponseFailedEvent,
    ResponseIncompleteEvent,
]
