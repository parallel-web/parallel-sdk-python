# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel
from .monitor_webhook import MonitorWebhook
from .monitor_snapshot_output import MonitorSnapshotOutput
from .monitor_snapshot_response_settings import MonitorSnapshotResponseSettings
from .monitor_event_stream_response_settings import MonitorEventStreamResponseSettings

__all__ = ["Monitor", "Settings"]

Settings: TypeAlias = Union[MonitorEventStreamResponseSettings, MonitorSnapshotResponseSettings]


class Monitor(BaseModel):
    """Response object for a monitor.

    The `type` field at the root determines the concrete shape of `settings`:
    `event_stream` uses `MonitorEventStreamResponseSettings`, and `snapshot`
    uses `MonitorSnapshotResponseSettings`. Snapshot monitors also carry an
    `output` field (`MonitorSnapshotOutput`) with the latest computed state.
    """

    created_at: datetime
    """Timestamp of the creation of the monitor, as an RFC 3339 string."""

    frequency: str
    """Frequency of the monitor.

    Format: '<number><unit>' where unit is 'h' (hours), 'd' (days), or 'w' (weeks).
    Must be between 1h and 30d (inclusive).
    """

    monitor_id: str
    """ID of the monitor."""

    processor: Literal["lite", "base"]
    """Processor to use for the monitor.

    `lite` is faster and cheaper; `base` performs more thorough analysis at higher
    cost and latency. Defaults to `lite`.
    """

    settings: Settings
    """Type-specific configuration.

    Shape is determined by `type`: `MonitorEventStreamResponseSettings` for
    `event_stream`, `MonitorSnapshotResponseSettings` for `snapshot`.
    """

    status: Literal["active", "cancelled"]
    """Status of the monitor."""

    type: Literal["event_stream", "snapshot"]
    """The type of monitor."""

    last_run_at: Optional[str] = None
    """Timestamp of the last run for the monitor, as an RFC 3339 string."""

    metadata: Optional[Dict[str, str]] = None
    """
    User-provided metadata stored with the monitor and echoed back in webhook
    notifications and GET responses, so you can map events to objects in your
    application. Keys: max 16 chars; values: max 512 chars.
    """

    output: Optional[MonitorSnapshotOutput] = None
    """Runtime output state for a `snapshot` monitor."""

    webhook: Optional[MonitorWebhook] = None
    """Webhook configuration for a monitor."""
