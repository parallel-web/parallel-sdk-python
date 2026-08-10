# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from ..._models import BaseModel

__all__ = ["MonitorMemoryEvent"]


class MonitorMemoryEvent(BaseModel):
    detected_at: datetime
    """When the event was detected, as an RFC 3339 timestamp."""

    event_group_id: str
    """ID of the execution that produced this event."""

    event_id: str
    """ID of the monitor event."""

    excerpt: str
    """Excerpt of the monitor event. May be truncated."""
