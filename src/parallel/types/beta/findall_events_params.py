# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["FindAllEventsParams", "FindallEventsParams"]


class FindAllEventsParams(TypedDict, total=False):
    last_event_id: Optional[str]

    api_timeout: Annotated[Optional[float], PropertyInfo(alias="timeout")]

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


FindallEventsParams = FindAllEventsParams  # for backwards compatibility with v0.3.4
"""This is deprecated, `FindAllEventsParams` should be used instead"""
