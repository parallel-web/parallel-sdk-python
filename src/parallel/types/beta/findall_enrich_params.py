# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable, Optional
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .mcp_server_param import McpServerParam
from ..json_schema_param import JsonSchemaParam
from .parallel_beta_param import ParallelBetaParam

__all__ = ["FindallEnrichParams"]


class FindallEnrichParams(TypedDict, total=False):
    output_schema: Required[JsonSchemaParam]
    """JSON schema for a task input or output."""

    mcp_servers: Optional[Iterable[McpServerParam]]
    """List of MCP servers to use for the task."""

    processor: str
    """Processor to use for the task."""

    betas: Annotated[List[ParallelBetaParam], PropertyInfo(alias="parallel-beta")]
    """Optional header to specify the beta version(s) to enable."""
