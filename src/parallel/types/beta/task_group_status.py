# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from ..._models import BaseModel

__all__ = ["TaskGroupStatus"]


class TaskGroupStatus(BaseModel):
    is_active: bool
    """True if at least one run in the group is currently active, i.e.

    status is one of {'cancelling', 'queued', 'running'}.
    """

    modified_at: Optional[str] = None
    """Timestamp of the last status update to the group, as an RFC 3339 string."""

    num_task_runs: int
    """Number of task runs in the group."""

    status_message: Optional[str] = None
    """Human-readable status message for the group."""

    task_run_status_counts: Dict[str, int]
    """Number of task runs with each status."""
