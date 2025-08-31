# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Union, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .task_group_status import TaskGroupStatus

__all__ = ["TaskGroup"]


class TaskGroup(BaseModel):
    created_at: Optional[str] = None
    """Timestamp of the creation of the group, as an RFC 3339 string."""

    status: TaskGroupStatus
    """Status of a task group."""

    task_group_id: str = FieldInfo(alias="taskgroup_id")
    """ID of the group."""

    metadata: Optional[Dict[str, Union[str, float, bool]]] = None
    """User-provided metadata stored with the group."""
