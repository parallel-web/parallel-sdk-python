# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel
from .task_run_source_stats import TaskRunSourceStats

__all__ = ["TaskRunProgressStatsEvent"]


class TaskRunProgressStatsEvent(BaseModel):
    """A progress update for a task run."""

    progress_meter: float
    """Completion percentage of the task run.

    Ranges from 0 to 100 where 0 indicates no progress and 100 indicates completion.
    """

    source_stats: TaskRunSourceStats
    """Source stats describing progress so far."""

    type: Literal["task_run.progress_stats"]
    """Event type; always 'task_run.progress_stats'."""
