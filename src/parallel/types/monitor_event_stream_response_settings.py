# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .json_schema import JsonSchema
from .advanced_monitor_settings import AdvancedMonitorSettings

__all__ = ["MonitorEventStreamResponseSettings"]


class MonitorEventStreamResponseSettings(BaseModel):
    """Type-specific response fields for an `event_stream` monitor."""

    query: str
    """The search query being monitored."""

    advanced_settings: Optional[AdvancedMonitorSettings] = None
    """Advanced monitor configuration."""

    include_backfill: Optional[bool] = None
    """
    If true, the first execution returns a sample of recent historical events
    matching the query (preview only — not exhaustive). If false or omitted, only
    events from the monitor's creation date onward are returned. Subsequent
    executions are always incremental.
    """

    output_schema: Optional[JsonSchema] = None
    """JSON schema for a task input or output."""
