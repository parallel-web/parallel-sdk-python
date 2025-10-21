# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["ExtractResult"]


class ExtractResult(BaseModel):
    excerpts: Optional[List[str]] = None
    """Relevant excerpted content from the URL, formatted as markdown."""

    full_content: Optional[str] = None
    """Full content from the URL formatted as markdown, if requested."""

    publish_date: Optional[str] = None
    """Publish date of the webpage, if available."""

    title: Optional[str] = None
    """Title of the webpage, if available."""

    url: str
