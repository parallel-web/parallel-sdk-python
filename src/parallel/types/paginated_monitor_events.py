# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Annotated, TypeAlias

from .._utils import PropertyInfo
from .._models import BaseModel
from .shared.warning import Warning
from .monitor_error_event import MonitorErrorEvent
from .monitor_snapshot_event import MonitorSnapshotEvent
from .monitor_completion_event import MonitorCompletionEvent
from .monitor_event_stream_event import MonitorEventStreamEvent

__all__ = ["PaginatedMonitorEvents", "Event"]

Event: TypeAlias = Annotated[
    Union[MonitorEventStreamEvent, MonitorSnapshotEvent, MonitorCompletionEvent, MonitorErrorEvent],
    PropertyInfo(discriminator="event_type"),
]


class PaginatedMonitorEvents(BaseModel):
    """Paginated list of monitor events, newest first."""

    events: List[Event]
    """Monitor events returned by this request, ordered newest first."""

    next_cursor: Optional[str] = None
    """Pass as `cursor` to retrieve more events. Absent when there are no more events."""

    warnings: Optional[List[Warning]] = None
    """Execution caveats for this page of events, e.g. compute limits."""
