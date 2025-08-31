# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .task_group_status import TaskGroupStatus

__all__ = ["TaskGroupRunResponse"]


class TaskGroupRunResponse(BaseModel):
    event_cursor: Optional[str] = None
    """
    Cursor for these runs in the event stream at
    taskgroup/events?last_event_id=<event_cursor>. Empty for the first runs in the
    group.
    """

    run_cursor: Optional[str] = None
    """
    Cursor for these runs in the run stream at
    taskgroup/runs?last_event_id=<run_cursor>. Empty for the first runs in the
    group.
    """

    run_ids: List[str]
    """IDs of the newly created runs."""

    status: TaskGroupStatus
    """Status of a task group."""
