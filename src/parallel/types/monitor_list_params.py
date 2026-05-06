# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, TypedDict

__all__ = ["MonitorListParams"]


class MonitorListParams(TypedDict, total=False):
    cursor: Optional[str]
    """Pagination token from `next_cursor` in a previous response.

    Omit to start from the most recently created monitor.
    """

    limit: Optional[int]
    """Maximum number of monitors to return. Defaults to 100. Between 1 and 10000."""

    status: Optional[List[Literal["active", "cancelled"]]]
    """Filter by monitor status.

    Pass multiple times to filter by multiple values. Defaults to `active` only.
    """

    type: Optional[List[Literal["event_stream", "snapshot"]]]
    """Filter by monitor type.

    Pass multiple times to filter by multiple values. Omit to return all types.
    """
