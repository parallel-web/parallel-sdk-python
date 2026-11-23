# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date

from ..._models import BaseModel

__all__ = ["SourcePolicy"]


class SourcePolicy(BaseModel):
    """Source policy for web search results.

    Plain domains match that domain and its subdomains. Domain/path entries use
    case-sensitive path matching at segment boundaries; trailing slashes are ignored,
    dot segments are normalized, and other percent-encoded path spelling is preserved.
    Entries omit schemes, ports, query strings, and fragments. A source must match
    include_domains, when set, and must not match exclude_domains. Use exclude_domains
    to block a subdomain or path of an allowed domain. Only the same entry in both
    lists fails validation, compared after lowercasing the domain and dropping a
    leading www. and a trailing slash.
    """

    after_date: Optional[date] = None
    """Optional start date for filtering search results.

    Results will be limited to content published on or after this date. Provided as
    an RFC 3339 date string (YYYY-MM-DD).
    """

    exclude_domains: Optional[List[str]] = None
    """List of domains or domain/path prefixes to exclude from results.

    If specified, matching sources will be excluded, also inside include_domains.
    Accepts plain domains (e.g., reddit.com), domain/path prefixes (e.g.,
    youtube.com/shorts), or bare domain extensions (e.g., .gov, .edu, .co.uk). The
    combined number of entries in include_domains and exclude_domains cannot
    exceed 200.
    """

    include_domains: Optional[List[str]] = None
    """List of domains or domain/path prefixes to restrict results to.

    If specified, only matching sources will be included. Accepts plain domains
    (e.g., wikipedia.org), domain/path prefixes (e.g., docs.python.org/3), or bare
    domain extensions (e.g., .gov, .edu, .co.uk). The combined number of entries in
    include_domains and exclude_domains cannot exceed 200.
    """
