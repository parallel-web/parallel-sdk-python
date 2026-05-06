# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import TypeAlias, TypedDict

from .fetch_policy_param import FetchPolicyParam
from .excerpt_settings_param import ExcerptSettingsParam
from .full_content_settings_param import FullContentSettingsParam

__all__ = ["AdvancedExtractSettingsParam", "FullContent"]

FullContent: TypeAlias = Union[FullContentSettingsParam, bool]


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


# Backwards-compat alias (deprecated). `FullContentFullContentSettings` was the
# auto-generated nested-class name in this module; it now lives as the top-level
# `FullContentSettingsParam`.
FullContentFullContentSettings = FullContentSettingsParam
