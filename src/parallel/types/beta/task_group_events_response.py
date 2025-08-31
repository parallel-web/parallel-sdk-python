# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Literal, Annotated, TypeAlias

from ..._utils import PropertyInfo
from ..._models import BaseModel
from .error_event import ErrorEvent
from .task_run_event import TaskRunEvent
from .task_group_status import TaskGroupStatus

__all__ = ["TaskGroupEventsResponse", "TaskGroupStatusEvent"]


class TaskGroupStatusEvent(BaseModel):
    event_id: str
    """Cursor to resume the event stream."""

    status: TaskGroupStatus
    """Status of a task group."""

    type: Literal["task_group_status"]
    """Event type; always 'task_group_status'."""


TaskGroupEventsResponse: TypeAlias = Annotated[
    Union[TaskGroupStatusEvent, TaskRunEvent, ErrorEvent], PropertyInfo(discriminator="type")
]
