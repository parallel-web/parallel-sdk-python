# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["TaskAdvancedSettingsParam"]


class TaskAdvancedSettingsParam(TypedDict, total=False):
    """Advanced search configuration for a task run."""

    location: Optional[str]
    """ISO 3166-1 alpha-2 country code for geo-targeted search results."""
