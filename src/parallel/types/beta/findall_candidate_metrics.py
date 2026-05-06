# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["FindAllCandidateMetrics"]


class FindAllCandidateMetrics(BaseModel):
    """Metrics object for FindAll run."""

    generated_candidates_count: Optional[int] = None
    """Number of candidates that were selected."""

    matched_candidates_count: Optional[int] = None
    """Number of candidates that evaluated to matched."""
