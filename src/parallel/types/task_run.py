# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["TaskRun", "Warning"]


class Warning(BaseModel):
    message: str
    """Human-readable message."""

    type: str
    """Type of warning.

    Note that adding new warning types is considered a backward-compatible change.
    """

    detail: Optional[object] = None
    """Optional detail supporting the warning."""


class TaskRun(BaseModel):
    created_at: Optional[str] = None
    """Timestamp of the creation of the task, as an RFC 3339 string."""

    is_active: bool
    """Whether the run is currently active; i.e.

    status is one of {'queued', 'running', 'cancelling'}.
    """

    message: Optional[str] = None
    """Human-readable status message for the run."""

    modified_at: Optional[str] = None
    """Timestamp of the last modification to the task, as an RFC 3339 string."""

    processor: str
    """Processor used for the run."""

    run_id: str
    """ID of the task run."""

    status: Literal["queued", "action_required", "running", "completed", "failed", "cancelling", "cancelled"]
    """Status of the run."""

    metadata: Optional[Dict[str, Union[str, float, bool]]] = None
    """User-provided metadata stored with the run."""

    warnings: Optional[List[Warning]] = None
    """Warnings for the run."""
