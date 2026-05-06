# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .findall_candidate_metrics import FindAllCandidateMetrics

__all__ = ["FindAllRunStatus"]


class FindAllRunStatus(BaseModel):
    """Status object for FindAll run."""

    is_active: bool
    """Whether the FindAll run is active"""

    metrics: FindAllCandidateMetrics
    """Candidate metrics for the FindAll run."""

    status: Literal["queued", "action_required", "running", "completed", "failed", "cancelling", "cancelled"]
    """Status of the FindAll run."""

    termination_reason: Optional[
        Literal[
            "low_match_rate",
            "match_limit_met",
            "candidates_exhausted",
            "user_cancelled",
            "error_occurred",
            "timeout",
            "insufficient_funds",
        ]
    ] = None
    """Reason for termination when FindAll run is in terminal status."""
