# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from .shared_params.source_policy import SourcePolicy

__all__ = ["AdvancedMonitorSettingsParam"]


class AdvancedMonitorSettingsParam(TypedDict, total=False):
    """Advanced monitor configuration."""

    location: Optional[str]
    """ISO 3166-1 alpha-2 country code for geo-targeted monitor results."""

    source_policy: Optional[SourcePolicy]
    """Source policy for web search results.

    Plain domains match that domain and its subdomains. Domain/path entries use
    case-sensitive path matching at segment boundaries; trailing slashes are
    ignored, dot segments are normalized, and other percent-encoded path spelling is
    preserved. Entries omit schemes, ports, query strings, and fragments. When
    include_domains is non-empty, it defines the complete allowlist and
    exclude_domains is ignored.
    """
