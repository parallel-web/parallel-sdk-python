# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from typing_extensions import Required, Annotated, TypeAlias, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo
from .parallel_beta_param import ParallelBetaParam
from .excerpt_settings_param import ExcerptSettingsParam

__all__ = ["BetaExtractParams", "Excerpts", "FetchPolicy", "FullContent", "FullContentFullContentSettings"]


class BetaExtractParams(TypedDict, total=False):
    urls: Required[SequenceNotStr[str]]

    excerpts: Excerpts
    """Include excerpts from each URL relevant to the search objective and queries.

    Note that if neither objective nor search_queries is provided, excerpts are
    redundant with full content.
    """

    fetch_policy: Optional[FetchPolicy]
    """Fetch policy.

    Determines when to return content from the cache (faster) vs fetching live
    content (fresher).
    """

    full_content: FullContent
    """Include full content from each URL.

    Note that if neither objective nor search_queries is provided, excerpts are
    redundant with full content.
    """

    objective: Optional[str]
    """If provided, focuses extracted content on the specified search objective."""

    search_queries: Optional[SequenceNotStr[str]]
    """If provided, focuses extracted content on the specified keyword search queries."""

    betas: Annotated[List[ParallelBetaParam], PropertyInfo(alias="parallel-beta")]
    """Optional header to specify the beta version(s) to enable."""


Excerpts: TypeAlias = Union[bool, ExcerptSettingsParam]


class FetchPolicy(TypedDict, total=False):
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


class FullContentFullContentSettings(TypedDict, total=False):
    max_chars_per_result: Optional[int]
    """
    Optional limit on the number of characters to include in the full content for
    each url. Full content always starts at the beginning of the page and is
    truncated at the limit if necessary.
    """


FullContent: TypeAlias = Union[bool, FullContentFullContentSettings]
