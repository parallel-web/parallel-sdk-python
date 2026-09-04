# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["SourcePolicy"]


class SourcePolicy(TypedDict, total=False):
    """Source policy for web search results.

    Plain domains match that domain and its subdomains. Domain/path entries use
    case-sensitive path matching at segment boundaries; trailing slashes are ignored,
    dot segments are normalized, and other percent-encoded path spelling is preserved.
    Entries omit schemes, ports, query strings, and fragments. When include_domains is
    non-empty, it defines the complete allowlist and exclude_domains is ignored.
    """

    after_date: Annotated[Union[str, date, None], PropertyInfo(format="iso8601")]
    """Optional start date for filtering search results.

    Results will be limited to content published on or after this date. Provided as
    an RFC 3339 date string (YYYY-MM-DD).
    """

    exclude_domains: SequenceNotStr[str]
    """List of domains or domain/path prefixes to exclude from results.

    Applied only when include_domains is empty. If specified, matching sources will
    be excluded. Accepts plain domains (e.g., reddit.com), domain/path prefixes
    (e.g., youtube.com/shorts), or bare domain extensions (e.g., .gov, .edu,
    .co.uk). The combined number of entries in include_domains and exclude_domains
    cannot exceed 200.
    """

    include_domains: SequenceNotStr[str]
    """List of domains or domain/path prefixes to restrict results to.

    If specified, only matching sources will be included and exclude_domains will be
    ignored. Accepts plain domains (e.g., wikipedia.org), domain/path prefixes
    (e.g., docs.python.org/3), or bare domain extensions (e.g., .gov, .edu, .co.uk).
    The combined number of entries in include_domains and exclude_domains cannot
    exceed 200.
    """
