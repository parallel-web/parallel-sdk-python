# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .shared.source_policy import SourcePolicy

__all__ = ["AdvancedMonitorSettings"]


class AdvancedMonitorSettings(BaseModel):
    """Advanced monitor configuration."""

    location: Optional[str] = None
    """ISO 3166-1 alpha-2 country code for geo-targeted monitor results."""

    source_policy: Optional[SourcePolicy] = None
    """Source policy for web search results.

    This policy governs which sources are allowed/disallowed in results.
    """
