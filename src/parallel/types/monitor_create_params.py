# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .monitor_webhook_param import MonitorWebhookParam
from .monitor_snapshot_settings_param import MonitorSnapshotSettingsParam
from .monitor_event_stream_settings_param import MonitorEventStreamSettingsParam

__all__ = ["MonitorCreateParams", "Settings"]


class MonitorCreateParams(TypedDict, total=False):
    frequency: Required[str]
    """Frequency of the monitor.

    Format: '<number><unit>' where unit is 'h' (hours), 'd' (days), or 'w' (weeks).
    Must be between 1h and 30d (inclusive).
    """

    settings: Required[Settings]
    """Type-specific settings for the monitor.

    The expected shape is determined by the root `type` field: pass
    `MonitorEventStreamSettings` when `type` is `event_stream`, and
    `MonitorSnapshotSettings` when `type` is `snapshot`.
    """

    type: Required[Literal["event_stream", "snapshot"]]
    """Type of monitor to create.

    `event_stream` monitors a search query for material changes; `snapshot` monitors
    a specific task run's output. Determines the expected shape of `settings`.
    """

    metadata: Optional[Dict[str, str]]
    """
    User-provided metadata stored with the monitor and echoed back in webhook
    notifications and GET responses, so you can map events to objects in your
    application. Keys: max 16 chars; values: max 512 chars.
    """

    processor: Literal["lite", "base"]
    """Processor to use for the monitor.

    `lite` is faster and cheaper; `base` performs more thorough analysis at higher
    cost and latency. Defaults to `lite`.
    """

    webhook: Optional[MonitorWebhookParam]
    """Webhook configuration for a monitor."""


Settings: TypeAlias = Union[MonitorEventStreamSettingsParam, MonitorSnapshotSettingsParam]
