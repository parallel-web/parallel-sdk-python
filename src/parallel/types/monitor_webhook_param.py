# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, TypedDict

__all__ = ["MonitorWebhookParam"]


class MonitorWebhookParam(TypedDict, total=False):
    """Webhook configuration for a monitor."""

    url: Required[str]
    """URL for the webhook."""

    event_types: List[Literal["monitor.event.detected", "monitor.execution.completed", "monitor.execution.failed"]]
    """Event types to send the webhook notifications for."""
