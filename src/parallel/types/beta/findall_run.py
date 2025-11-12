# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Union, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["FindallRun", "Status", "StatusMetrics"]


class StatusMetrics(BaseModel):
    generated_candidates_count: Optional[int] = None
    """Number of candidates that were selected."""

    matched_candidates_count: Optional[int] = None
    """Number of candidates that evaluated to matched."""


class Status(BaseModel):
    is_active: bool
    """Whether the FindAll run is active"""

    metrics: StatusMetrics
    """Metrics object for FindAll run."""

    status: Literal["queued", "action_required", "running", "completed", "failed", "cancelling", "cancelled"]
    """Status of the FindAll run."""

    termination_reason: Optional[str] = None
    """Reason for termination when FindAll run is in terminal status."""


class FindallRun(BaseModel):
    findall_id: str
    """ID of the FindAll run."""

    generator: Literal["base", "core", "pro", "preview"]
    """Generator for the FindAll run."""

    status: Status
    """Status object for FindAll run."""

    created_at: Optional[str] = None
    """Timestamp of the creation of the run, in RFC 3339 format."""

    metadata: Optional[Dict[str, Union[str, float, bool]]] = None
    """Metadata for the FindAll run."""

    modified_at: Optional[str] = None
    """
    Timestamp of the latest modification to the FindAll run result, in RFC 3339
    format.
    """
