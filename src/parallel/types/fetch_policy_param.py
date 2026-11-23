# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["FetchPolicyParam"]


class FetchPolicyParam(TypedDict, total=False):
    """Policy for live fetching web results."""

    as_of: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Accepts an ISO 8601 date or timestamp.

    A date is treated as 00:00 UTC. Timestamps without an offset are treated as UTC.
    Timestamps are rounded down to the start of the UTC hour. Serves the latest
    available version of each page captured at or before that cutoff. Contact sales
    for access.
    """

    disable_cache_fallback: bool
    """
    If false, fallback to cached content older than max-age if live fetch fails or
    times out. If true, returns an error instead.
    """

    max_age_seconds: Optional[int]
    """Maximum age of cached content in seconds to trigger a live fetch.

    Minimum value 600 seconds (10 minutes).
    """

    timeout_seconds: Optional[float]
    """Timeout in seconds for fetching live content if unavailable in cache."""
