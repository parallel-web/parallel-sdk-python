# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from .shared_params.source_policy import SourcePolicy

__all__ = ["AdvancedMonitorSettingsParam"]


class AdvancedMonitorSettingsParam(TypedDict, total=False):
    """Advanced monitor configuration."""

    location: Optional[str]
    """ISO 3166-1 alpha-2 country code for geo-targeted monitor results."""

    source_policy: Optional[SourcePolicy]
    """Source policy for web search results.

    This policy governs which sources are allowed/disallowed in results.
    """
