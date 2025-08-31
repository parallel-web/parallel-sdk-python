# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["McpServer"]


class McpServer(BaseModel):
    name: str
    """Name of the MCP server."""

    url: str
    """URL of the MCP server."""

    allowed_tools: Optional[List[str]] = None
    """List of allowed tools for the MCP server."""

    headers: Optional[Dict[str, str]] = None
    """Headers for the MCP server."""

    type: Optional[Literal["url"]] = None
    """Type of MCP server being configured. Always `url`."""
