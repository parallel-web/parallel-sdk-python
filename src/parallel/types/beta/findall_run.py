# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Union, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["FindAllRun", "FindallRun", "Status", "StatusMetrics"]


class StatusMetrics(BaseModel):
    """Candidate metrics for the FindAll run."""

    generated_candidates_count: Optional[int] = None
    """Number of candidates that were selected."""

    matched_candidates_count: Optional[int] = None
    """Number of candidates that evaluated to matched."""


class Status(BaseModel):
    """Status object for the FindAll run."""

    is_active: bool
    """Whether the FindAll run is active"""

    metrics: StatusMetrics
    """Candidate metrics for the FindAll run."""

    status: Literal["queued", "action_required", "running", "completed", "failed", "cancelling", "cancelled"]
    """Status of the FindAll run."""

    termination_reason: Optional[
        Literal[
            "low_match_rate", "match_limit_met", "candidates_exhausted", "user_cancelled", "error_occurred", "timeout"
        ]
    ] = None
    """Reason for termination when FindAll run is in terminal status."""


class FindAllRun(BaseModel):
    """FindAll run object with status and metadata."""

    findall_id: str
    """ID of the FindAll run."""

    generator: Literal["base", "core", "pro", "preview"]
    """Generator for the FindAll run."""

    status: Status
    """Status object for the FindAll run."""

    created_at: Optional[str] = None
    """Timestamp of the creation of the run, in RFC 3339 format."""

    metadata: Optional[Dict[str, Union[str, float, bool]]] = None
    """Metadata for the FindAll run."""

    modified_at: Optional[str] = None
    """
    Timestamp of the latest modification to the FindAll run result, in RFC 3339
    format.
    """


FindallRun = FindAllRun  # for backwards compatibility with v0.3.4
"""This is deprecated, `FindAllRun` should be used instead"""
