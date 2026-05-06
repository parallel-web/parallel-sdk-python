# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from .._utils import PropertyInfo
from .._models import BaseModel
from .task_run_json_output import TaskRunJsonOutput
from .task_run_text_output import TaskRunTextOutput

__all__ = ["MonitorSnapshotEvent", "ChangedOutput", "PreviousOutput"]

ChangedOutput: TypeAlias = Annotated[Union[TaskRunTextOutput, TaskRunJsonOutput], PropertyInfo(discriminator="type")]

PreviousOutput: TypeAlias = Annotated[Union[TaskRunTextOutput, TaskRunJsonOutput], PropertyInfo(discriminator="type")]


class MonitorSnapshotEvent(BaseModel):
    """Snapshot diff event emitted when a monitored task run's output changes.

    `changed_output` contains only the fields that changed since the previous execution,
    along with their `basis` (reasoning + citations). `previous_output` holds
    the complete output from the prior run for comparison.
    """

    changed_output: ChangedOutput
    """
    Partial output containing only the fields that changed since the previous
    execution, each with its `basis` (reasoning and citations).
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

    previous_output: PreviousOutput
    """The full output from the prior run, including all fields and basis."""

    event_type: Optional[Literal["snapshot"]] = None
    """Discriminant for the snapshot event variant."""
