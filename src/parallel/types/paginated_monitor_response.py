# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .monitor import Monitor
from .._models import BaseModel

__all__ = ["PaginatedMonitorResponse"]


class PaginatedMonitorResponse(BaseModel):
    """Paginated list of monitors."""

    monitors: List[Monitor]
    """List of monitors for the current page."""

    next_cursor: Optional[str] = None
    """Opaque pagination token.

    Pass as `cursor` to retrieve the next page. Absent when there are no more pages.
    """
