# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["WebSearchResult"]


class WebSearchResult(BaseModel):
    """A single search result from the web search API."""

    url: str
    """URL associated with the search result."""

    excerpts: Optional[List[str]] = None
    """Relevant excerpted content from the URL, formatted as markdown."""

    publish_date: Optional[str] = None
    """Publish date of the webpage in YYYY-MM-DD format, if available."""

    title: Optional[str] = None
    """Title of the webpage, if available."""
