# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Annotated, TypeAlias

from .._utils import PropertyInfo
from .error_event import ErrorEvent
from .task_run_event import TaskRunEvent
from .task_run_progress_stats_event import TaskRunProgressStatsEvent
from .task_run_progress_message_event import TaskRunProgressMessageEvent

__all__ = ["TaskRunEventsResponse"]

TaskRunEventsResponse: TypeAlias = Annotated[
    Union[TaskRunProgressStatsEvent, TaskRunProgressMessageEvent, TaskRunEvent, ErrorEvent],
    PropertyInfo(discriminator="type"),
]

# Backwards-compat alias (deprecated). `TaskRunProgressStatsEventSourceStats`
# was the auto-generated nested-class name for the source-stats payload; it now
# lives as the top-level `TaskRunSourceStats` model.
from .task_run_source_stats import TaskRunSourceStats  # noqa: E402

TaskRunProgressStatsEventSourceStats = TaskRunSourceStats
