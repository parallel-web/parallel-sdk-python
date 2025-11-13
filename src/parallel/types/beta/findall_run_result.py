# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .findall_run import FindallRun
from ..field_basis import FieldBasis

__all__ = ["FindallRunResult", "Candidate"]


class Candidate(BaseModel):
    candidate_id: str
    """ID of the candidate."""

    match_status: Literal["generated", "matched", "unmatched", "discarded"]
    """Status of the candidate. One of generated, matched, unmatched, discarded."""

    name: str
    """Name of the candidate."""

    url: str
    """URL that provides context or details of the entity for disambiguation."""

    basis: Optional[List[FieldBasis]] = None
    """List of FieldBasis objects supporting the output."""

    description: Optional[str] = None
    """
    Brief description of the entity that can help answer whether entity satisfies
    the query.
    """

    output: Optional[Dict[str, object]] = None
    """Results of the match condition evaluations for this candidate.

    This object contains the structured output that determines whether the candidate
    matches the overall FindAll objective.
    """


class FindallRunResult(BaseModel):
    candidates: List[Candidate]
    """All evaluated candidates at the time of the snapshot."""

    run: FindallRun
    """FindAll run object with status and metadata."""

    last_event_id: Optional[str] = None
    """ID of the last event of the run at the time of the request.

    This can be used to resume streaming from the last event.
    """
