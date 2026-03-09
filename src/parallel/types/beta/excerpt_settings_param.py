# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["ExcerptSettingsParam"]


class ExcerptSettingsParam(TypedDict, total=False):
    """Optional settings for returning relevant excerpts."""

    max_chars_per_result: Optional[int]
    """Optional upper bound on the total number of characters to include per url.

    Excerpts may contain fewer characters than this limit to maximize relevance and
    token efficiency. Values below 1000 will be automatically set to 1000.
    """

    max_chars_total: Optional[int]
    """
    Optional upper bound on the total number of characters to include across all
    urls. Results may contain fewer characters than this limit to maximize relevance
    and token efficiency. Values below 1000 will be automatically set to 1000. This
    overall limit applies in addition to max_chars_per_result.
    """
