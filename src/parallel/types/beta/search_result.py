# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .usage_item import UsageItem
from ..shared.warning import Warning
from .web_search_result import WebSearchResult

__all__ = ["SearchResult"]


class SearchResult(BaseModel):
    """Output for the Search API."""

    results: List[WebSearchResult]
    """A list of WebSearchResult objects, ordered by decreasing relevance."""

    search_id: str
    """Search ID. Example: `search_cad0a6d2dec046bd95ae900527d880e7`"""

    usage: Optional[List[UsageItem]] = None
    """Usage metrics for the search request."""

    warnings: Optional[List[Warning]] = None
    """Warnings for the search request, if any."""
