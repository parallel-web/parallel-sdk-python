# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel

__all__ = ["WebSearchResult"]


class WebSearchResult(BaseModel):
    excerpts: List[str]
    """Text excerpts from the search result which are relevant to the request."""

    title: str
    """Title of the search result."""

    url: str
    """URL associated with the search result."""
