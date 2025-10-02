# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from ..._utils import PropertyInfo
from ..._models import BaseModel
from .error_event import ErrorEvent
from .task_run_event import TaskRunEvent

__all__ = [
    "TaskRunEventsResponse",
    "TaskRunProgressStatsEvent",
    "TaskRunProgressStatsEventSourceStats",
    "TaskRunProgressMessageEvent",
]


class TaskRunProgressStatsEventSourceStats(BaseModel):
    num_sources_considered: Optional[int] = None
    """Number of sources considered in processing the task."""

    num_sources_read: Optional[int] = None
    """Number of sources read in processing the task."""

    sources_read_sample: Optional[List[str]] = None
    """A sample of URLs of sources read in processing the task."""


class TaskRunProgressStatsEvent(BaseModel):
    progress_meter: float
    """Completion percentage of the task run.

    Ranges from 0 to 100 where 0 indicates no progress and 100 indicates completion.
    """

    source_stats: TaskRunProgressStatsEventSourceStats
    """Source stats for a task run."""

    type: Literal["task_run.progress_stats"]
    """Event type; always 'task_run.progress_stats'."""


class TaskRunProgressMessageEvent(BaseModel):
    message: str
    """Progress update message."""

    timestamp: Optional[str] = None
    """Timestamp of the message."""

    type: Literal[
        "task_run.progress_msg.plan",
        "task_run.progress_msg.search",
        "task_run.progress_msg.result",
        "task_run.progress_msg.tool_call",
        "task_run.progress_msg.exec_status",
    ]
    """Event type; always starts with 'task_run.progress_msg'."""


TaskRunEventsResponse: TypeAlias = Annotated[
    Union[TaskRunProgressStatsEvent, TaskRunProgressMessageEvent, TaskRunEvent, ErrorEvent],
    PropertyInfo(discriminator="type"),
]
