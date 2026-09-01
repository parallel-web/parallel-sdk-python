# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal, TypedDict

from .monitor_webhook_param import MonitorWebhookParam
from .update_monitor_event_stream_settings_param import UpdateMonitorEventStreamSettingsParam

__all__ = ["MonitorUpdateParams"]


class MonitorUpdateParams(TypedDict, total=False):
    frequency: Optional[str]
    """Frequency of the monitor.

    Format: '<number><unit>' where unit is 'h' (hours), 'd' (days), or 'w' (weeks).
    Must be between 1h and 30d (inclusive). Omit to keep the current frequency;
    `null` is rejected.
    """

    metadata: Optional[Dict[str, str]]
    """
    User-provided metadata stored with the monitor and echoed back in webhook
    notifications and GET responses, so you can map events to objects in your
    application. Keys: max 16 chars; values: max 512 chars.
    """

    processor: Optional[Literal["lite", "base"]]
    """Processor to use for subsequent monitor runs.

    `lite` is faster and cheaper; `base` performs more thorough analysis at higher
    cost and latency. Omit to keep the current processor; `null` is rejected.
    """

    settings: Optional[UpdateMonitorEventStreamSettingsParam]
    """Type-specific update settings for an `event_stream` monitor."""

    type: Optional[Literal["event_stream", "snapshot"]]
    """Type of the monitor being updated.

    Required when `settings` is provided; must be `event_stream` (snapshot monitors
    have no updatable type-specific settings). Omit when `settings` is not provided;
    `null` is rejected.
    """

    webhook: Optional[MonitorWebhookParam]
    """Webhook configuration for a monitor."""
