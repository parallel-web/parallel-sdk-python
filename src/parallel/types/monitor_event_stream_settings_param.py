# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .json_schema_param import JsonSchemaParam
from .advanced_monitor_settings_param import AdvancedMonitorSettingsParam

__all__ = ["MonitorEventStreamSettingsParam"]


class MonitorEventStreamSettingsParam(TypedDict, total=False):
    """Type-specific settings for an `event_stream` monitor."""

    query: Required[str]
    """Search query to monitor for material changes."""

    advanced_settings: Optional[AdvancedMonitorSettingsParam]
    """Advanced monitor configuration."""

    include_backfill: Optional[bool]
    """
    If true, the first execution returns a sample of recent historical events
    matching the query (preview only — not exhaustive). If false or omitted, only
    events from the monitor's creation date onward are returned. Subsequent
    executions are always incremental.
    """

    output_schema: Optional[JsonSchemaParam]
    """JSON schema for a task input or output."""
