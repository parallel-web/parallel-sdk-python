# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["McpToolCall"]


class McpToolCall(BaseModel):
    arguments: str
    """Arguments used to call the MCP tool."""

    server_name: str
    """Name of the MCP server."""

    tool_call_id: str
    """Identifier for the tool call."""

    tool_name: str
    """Name of the tool being called."""

    content: Optional[str] = None
    """Output received from the tool call, if successful."""

    error: Optional[str] = None
    """Error message if the tool call failed."""
