# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .shared.source_policy import SourcePolicy

__all__ = ["AdvancedMonitorSettings"]


class AdvancedMonitorSettings(BaseModel):
    """Advanced monitor configuration."""

    location: Optional[str] = None
    """ISO 3166-1 alpha-2 country code for geo-targeted monitor results."""

    source_policy: Optional[SourcePolicy] = None
    """Source policy for web search results.

    Plain domains match that domain and its subdomains. Domain/path entries use
    case-sensitive path matching at segment boundaries; trailing slashes are
    ignored, dot segments are normalized, and other percent-encoded path spelling is
    preserved. Entries omit schemes, ports, query strings, and fragments. A source
    must match include_domains, when set, and must not match exclude_domains. Use
    exclude_domains to block a subdomain or path of an allowed domain. Only the same
    entry in both lists fails validation, compared after lowercasing the domain and
    dropping a leading www. and a trailing slash.
    """
