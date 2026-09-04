# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from .fetch_policy_param import FetchPolicyParam
from .excerpt_settings_param import ExcerptSettingsParam
from .shared_params.source_policy import SourcePolicy

__all__ = ["AdvancedSearchSettingsParam"]


class AdvancedSearchSettingsParam(TypedDict, total=False):
    """Advanced search configuration.

    These settings may impact result quality and latency unless used carefully.
    See https://docs.parallel.ai/search/advanced-search-settings for more info.
    """

    excerpt_settings: Optional[ExcerptSettingsParam]
    """Optional settings for returning relevant excerpts."""

    fetch_policy: Optional[FetchPolicyParam]
    """Policy for live fetching web results."""

    location: Optional[str]
    """ISO 3166-1 alpha-2 country code for geo-targeted search results."""

    max_results: Optional[int]
    """Upper bound on the number of results to return. Defaults to 10 if not provided."""

    source_policy: Optional[SourcePolicy]
    """Source policy for web search results.

    Plain domains match that domain and its subdomains. Domain/path entries use
    case-sensitive path matching at segment boundaries; trailing slashes are
    ignored, dot segments are normalized, and other percent-encoded path spelling is
    preserved. Entries omit schemes, ports, query strings, and fragments. When
    include_domains is non-empty, it defines the complete allowlist and
    exclude_domains is ignored.
    """
