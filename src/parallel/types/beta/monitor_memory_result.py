# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel
from .monitor_memory_event import MonitorMemoryEvent

__all__ = ["MonitorMemoryResult"]


class MonitorMemoryResult(BaseModel):
    id: str
    """ID of the monitor."""

    input_excerpt: str
    """Preview of the monitor's query. May be truncated."""

    status: Literal["active", "cancelled"]
    """Current status of the monitor."""

    updated_at: datetime
    """When the monitor last ran, as an RFC 3339 timestamp."""

    kind: Optional[Literal["monitor"]] = None

    matched_events: Optional[List[MonitorMemoryEvent]] = None
    """
    Detected events matching the retrieval query, ordered by relevance with more
    recent events favored. For an empty query, events are ordered by recency.
    """
