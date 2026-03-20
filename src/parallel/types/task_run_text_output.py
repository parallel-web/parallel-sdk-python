# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .field_basis import FieldBasis
from .mcp_tool_call import McpToolCall

__all__ = ["TaskRunTextOutput"]


class TaskRunTextOutput(BaseModel):
    """Output from a task that returns text."""

    basis: List[FieldBasis]
    """Basis for the output. The basis has a single field 'output'."""

    content: str
    """Text output from the task."""

    type: Literal["text"]
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
