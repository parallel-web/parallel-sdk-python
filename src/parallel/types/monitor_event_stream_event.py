# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from .._utils import PropertyInfo
from .._models import BaseModel
from .task_run_json_output import TaskRunJsonOutput
from .task_run_text_output import TaskRunTextOutput

__all__ = ["MonitorEventStreamEvent", "Output"]

Output: TypeAlias = Annotated[Union[TaskRunTextOutput, TaskRunJsonOutput], PropertyInfo(discriminator="type")]


class MonitorEventStreamEvent(BaseModel):
    """Append-only event from an event_stream monitor.

    Each event represents a distinct material change detected since the
    previous execution. Events are net-new relative to the cursor; clients
    should treat them as an append-only log.
    """

    event_date: Optional[str] = None
    """Date when this event was produced.

    ISO 8601 date (YYYY-MM-DD) or partial (YYYY-MM or YYYY).
    """

    event_group_id: str
    """ID of the event group that owns this event."""

    event_id: str
    """Stable identifier for this event.

    Safe to use for client-side deduplication across pagination and retries.
    """

    output: Output
    """Text or JSON output describing the detected change."""

    event_type: Optional[Literal["event_stream"]] = None
    """Discriminant for the event_stream event variant."""
