# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .mcp_server import McpServer
from ..json_schema import JsonSchema

__all__ = ["FindAllEnrichInput"]


class FindAllEnrichInput(BaseModel):
    """Input model for FindAll enrich."""

    output_schema: JsonSchema
    """JSON schema for the enrichment output schema for the FindAll run."""

    mcp_servers: Optional[List[McpServer]] = None
    """List of MCP servers to use for the task."""

    processor: Optional[str] = None
    """Processor to use for the task."""
