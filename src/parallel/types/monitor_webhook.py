# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["MonitorWebhook"]


class MonitorWebhook(BaseModel):
    """Webhook configuration for a monitor."""

    url: str
    """URL for the webhook."""

    event_types: Optional[
        List[Literal["monitor.event.detected", "monitor.execution.completed", "monitor.execution.failed"]]
    ] = None
    """Event types to send the webhook notifications for."""
