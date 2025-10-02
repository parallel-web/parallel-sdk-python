# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .web_search_result import WebSearchResult

__all__ = ["SearchResult"]


class SearchResult(BaseModel):
    results: List[WebSearchResult]
    """A list of WebSearchResult objects, ordered by decreasing relevance."""

    search_id: str
    """Search ID. Example: `search_cad0a6d2dec046bd95ae900527d880e7`"""
