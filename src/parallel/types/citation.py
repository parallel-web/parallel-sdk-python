# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["Citation"]


class Citation(BaseModel):
    url: str
    """URL of the citation."""

    excerpts: Optional[List[str]] = None
    """Excerpts from the citation supporting the output.

    Only certain processors provide excerpts.
    """

    title: Optional[str] = None
    """Title of the citation."""
