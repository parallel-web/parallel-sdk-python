# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import Annotated, TypeAlias

from .._utils import PropertyInfo
from .._models import BaseModel
from .task_run_json_output import TaskRunJsonOutput
from .task_run_text_output import TaskRunTextOutput

__all__ = ["MonitorSnapshotOutput", "LatestSnapshot"]

LatestSnapshot: TypeAlias = Annotated[
    Union[TaskRunTextOutput, TaskRunJsonOutput, None], PropertyInfo(discriminator="type")
]


class MonitorSnapshotOutput(BaseModel):
    """Runtime output state for a `snapshot` monitor."""

    latest_snapshot: Optional[LatestSnapshot] = None
    """
    Task run output from the most recent completed execution of this snapshot
    monitor — same structure as the output of the original task run the monitor was
    created from. `null` until the first run completes.
    """
