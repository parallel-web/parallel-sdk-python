# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel
from .task_group_status import TaskGroupStatus

__all__ = ["TaskGroupStatusEvent"]


class TaskGroupStatusEvent(BaseModel):
    """Event indicating an update to group status."""

    event_id: str
    """Cursor to resume the event stream."""

    status: TaskGroupStatus
    """Task group status object."""

    type: Literal["task_group_status"]
    """Event type; always 'task_group_status'."""
