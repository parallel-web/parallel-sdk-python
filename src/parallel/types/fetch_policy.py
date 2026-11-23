# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["FetchPolicy"]


class FetchPolicy(BaseModel):
    """Policy for live fetching web results."""

    as_of: Optional[datetime] = None
    """Accepts an ISO 8601 date or timestamp.

    A date is treated as 00:00 UTC. Timestamps without an offset are treated as UTC.
    Timestamps are rounded down to the start of the UTC hour. Serves the latest
    available version of each page captured at or before that cutoff. Contact sales
    for access.
    """

    disable_cache_fallback: Optional[bool] = None
    """
    If false, fallback to cached content older than max-age if live fetch fails or
    times out. If true, returns an error instead.
    """

    max_age_seconds: Optional[int] = None
    """Maximum age of cached content in seconds to trigger a live fetch.

    Minimum value 600 seconds (10 minutes).
    """

    timeout_seconds: Optional[float] = None
    """Timeout in seconds for fetching live content if unavailable in cache."""
