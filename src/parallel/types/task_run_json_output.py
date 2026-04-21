# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .field_basis import FieldBasis
from .mcp_tool_call import McpToolCall

__all__ = ["TaskRunJsonOutput"]


class TaskRunJsonOutput(BaseModel):
    """Output from a task that returns JSON."""

    basis: List[FieldBasis]
    """Basis for each top-level field in the JSON output.

    Per-list-element basis entries are available only when the
    `parallel-beta: field-basis-2025-11-25` header is supplied.
    """

    content: Dict[str, object]
    """
    Output from the task as a native JSON object, as determined by the output schema
    of the task spec.
    """

    type: Literal["json"]
    """
    The type of output being returned, as determined by the output schema of the
    task spec.
    """

    beta_fields: Optional[Dict[str, object]] = None
    """Deprecated.

    mcp-server-2025-07-17 is now included directly in the output (e.g.
    mcp_tool_calls).
    """

    mcp_tool_calls: Optional[List[McpToolCall]] = None
    """MCP tool calls made by the task."""

    output_schema: Optional[Dict[str, object]] = None
    """Output schema for the Task Run.

    Populated only if the task was executed with an auto schema.
    """
