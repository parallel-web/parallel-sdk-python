# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import TypeAlias, TypedDict

from .fetch_policy_param import FetchPolicyParam
from .excerpt_settings_param import ExcerptSettingsParam

__all__ = ["AdvancedExtractSettingsParam", "FullContent", "FullContentFullContentSettings"]


class FullContentFullContentSettings(TypedDict, total=False):
    """Optional settings for returning full content."""

    max_chars_per_result: Optional[int]
    """
    Optional limit on the number of characters to include in the full content for
    each url. Full content always starts at the beginning of the page and is
    truncated at the limit if necessary.
    """


FullContent: TypeAlias = Union[FullContentFullContentSettings, bool]


class AdvancedExtractSettingsParam(TypedDict, total=False):
    """Advanced extract configuration.

    These settings may impact result quality and latency unless used carefully.
    See https://docs.parallel.ai/search/advanced-extract-settings for more info.
    """

    excerpt_settings: Optional[ExcerptSettingsParam]
    """Optional settings for returning relevant excerpts."""

    fetch_policy: Optional[FetchPolicyParam]
    """Policy for live fetching web results."""

    full_content: FullContent
    """Controls full content extraction.

    Set to true to enable with defaults, false to disable, or provide
    FullContentSettings for fine-grained control.
    """
