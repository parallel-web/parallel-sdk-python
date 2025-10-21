# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["FetchPolicyParam"]


class FetchPolicyParam(TypedDict, total=False):
    disable_cache_fallback: bool
    """
    If false, fallback to cached content older than max-age if live fetch fails or
    times out. If true, returns an error instead.
    """

    max_age_seconds: Optional[int]
    """Maximum age of cached content in seconds to trigger a live fetch.

    Minimum value 600 seconds (10 minutes). If not provided, a dynamic age policy
    will be used based on the search objective and url.
    """

    timeout_seconds: Optional[float]
    """Timeout in seconds for fetching live content if unavailable in cache.

    If unspecified a dynamic timeout will be used based on the url, generally 15
    seconds for simple pages and up to 60 seconds for complex pages requiring
    javascript or PDF rendering.
    """
