# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from ..mcp_server_param import McpServerParam
from ..json_schema_param import JsonSchemaParam

__all__ = ["FindAllEnrichParams", "FindallEnrichParams"]


class FindAllEnrichParams(TypedDict, total=False):
    output_schema: Required[JsonSchemaParam]
    """JSON schema for the enrichment output schema for the FindAll run."""

    mcp_servers: Optional[Iterable[McpServerParam]]
    """List of MCP servers to use for the task."""

    processor: str
    """Processor to use for the task."""

    betas: Annotated[
        List[
            Union[
                Literal[
                    "mcp-server-2025-07-17",
                    "events-sse-2025-07-24",
                    "webhook-2025-08-12",
                    "findall-2025-09-15",
                    "search-extract-2025-10-10",
                    "field-basis-2025-11-25",
                ],
                str,
            ]
        ],
        PropertyInfo(alias="parallel-beta"),
    ]
    """Optional header to specify the beta version(s) to enable."""


FindallEnrichParams = FindAllEnrichParams  # for backwards compatibility with v0.3.4
"""This is deprecated, `FindAllEnrichParams` should be used instead"""
