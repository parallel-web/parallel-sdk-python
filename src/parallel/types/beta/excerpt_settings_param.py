# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["ExcerptSettingsParam"]


class ExcerptSettingsParam(TypedDict, total=False):
    max_chars_per_result: Optional[int]
    """
    Optional upper bound on the total number of characters to include across all
    excerpts for each url. Excerpts may contain fewer characters than this limit to
    maximize relevance and token efficiency.
    """
