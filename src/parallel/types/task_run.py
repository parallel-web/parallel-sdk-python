# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .shared.warning import Warning
from .shared.error_object import ErrorObject

__all__ = [
    "TaskRun",
    "Warning",  # for backwards compatibility with v0.1.3
]


class TaskRun(BaseModel):
    created_at: Optional[str] = None
    """Timestamp of the creation of the task, as an RFC 3339 string."""

    is_active: bool
    """Whether the run is currently active, i.e.

    status is one of {'cancelling', 'queued', 'running'}.
    """

    modified_at: Optional[str] = None
    """Timestamp of the last modification to the task, as an RFC 3339 string."""

    processor: str
    """Processor used for the run."""

    run_id: str
    """ID of the task run."""

    status: Literal["queued", "action_required", "running", "completed", "failed", "cancelling", "cancelled"]
    """Status of the run."""

    error: Optional[ErrorObject] = None
    """An error message."""

    metadata: Optional[Dict[str, Union[str, float, bool]]] = None
    """User-provided metadata stored with the run."""

    task_group_id: Optional[str] = FieldInfo(alias="taskgroup_id", default=None)
    """ID of the taskgroup to which the run belongs."""

    warnings: Optional[List[Warning]] = None
    """Warnings for the run, if any."""
