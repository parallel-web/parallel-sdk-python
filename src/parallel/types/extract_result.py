# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["ExtractResult"]


class ExtractResult(BaseModel):
    """Extract result for a single URL."""

    excerpts: List[str]
    """Relevant excerpted content from the URL, formatted as markdown."""

    url: str
    """URL associated with the search result."""

    acquired_at: Optional[str] = None
    """
    When the returned content was acquired, as an RFC 3339 timestamp truncated to
    the start of the UTC day. Null when unknown.
    """

    full_content: Optional[str] = None
    """Full content from the URL formatted as markdown, if requested."""

    links: Optional[List[str]] = None
    """
    Links from the page's rendered content, if requested: up to 512 unique absolute
    URLs in document order. Empty for pages with no links, including PDFs. Present
    only when advanced_settings.links was requested.
    """

    publish_date: Optional[str] = None
    """Publish date of the webpage in YYYY-MM-DD format, if available."""

    title: Optional[str] = None
    """Title of the webpage, if available."""
