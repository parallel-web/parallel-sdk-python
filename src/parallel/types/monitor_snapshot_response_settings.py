# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .json_schema import JsonSchema

__all__ = ["MonitorSnapshotResponseSettings"]


class MonitorSnapshotResponseSettings(BaseModel):
    """Configuration settings for a `snapshot` monitor."""

    query: str
    """The original task input from the baseline task run that this monitor tracks."""

    task_run_id: str
    """ID of the task run used as the monitoring baseline."""

    output_schema: Optional[JsonSchema] = None
    """JSON schema for a task input or output."""
