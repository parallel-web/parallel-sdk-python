# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .mcp_server import McpServer
from ..json_schema import JsonSchema

__all__ = ["FindallEnrichInput"]


class FindallEnrichInput(BaseModel):
    output_schema: JsonSchema
    """JSON schema for a task input or output."""

    mcp_servers: Optional[List[McpServer]] = None
    """List of MCP servers to use for the task."""

    processor: Optional[str] = None
    """Processor to use for the task."""
