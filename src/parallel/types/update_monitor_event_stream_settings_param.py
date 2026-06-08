# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from .advanced_monitor_settings_param import AdvancedMonitorSettingsParam

__all__ = ["UpdateMonitorEventStreamSettingsParam"]


class UpdateMonitorEventStreamSettingsParam(TypedDict, total=False):
    """Type-specific update settings for an `event_stream` monitor."""

    advanced_settings: Optional[AdvancedMonitorSettingsParam]
    """Advanced monitor configuration."""

    query: Optional[str]
    """Updated search query for the monitor.

    Use this for minor updates to prompts and instructions only. Major changes to
    the query may lead to unexpected results in change detection, as the monitor
    compares new results with what was previously seen.
    """
