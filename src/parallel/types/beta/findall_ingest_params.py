# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["FindAllIngestParams"]


class FindAllIngestParams(TypedDict, total=False):
    objective: Required[str]
    """Natural language objective to create a FindAll run spec."""

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
