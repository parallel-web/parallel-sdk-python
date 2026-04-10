# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["FetchPolicyParam"]


class FetchPolicyParam(TypedDict, total=False):
    """Policy for live fetching web results."""

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
