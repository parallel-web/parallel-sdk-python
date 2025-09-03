# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal, Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["McpServerParam"]


class McpServerParam(TypedDict, total=False):
    name: Required[str]
    """Name of the MCP server."""

    url: Required[str]
    """URL of the MCP server."""

    allowed_tools: Optional[SequenceNotStr[str]]
    """List of allowed tools for the MCP server."""

    headers: Optional[Dict[str, str]]
    """Headers for the MCP server."""

    type: Literal["url"]
    """Type of MCP server being configured. Always `url`."""
