# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .findall_run import FindAllRun
from ..field_basis import FieldBasis

__all__ = ["FindAllRunResult", "FindallRunResult", "Candidate"]


class Candidate(BaseModel):
    """Candidate for a find all run that may end up as a match.

    Contains all the candidate's metadata and the output of the match conditions.
    A candidate is a match if all match conditions are satisfied.
    """

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


class FindAllRunResult(BaseModel):
    """Complete FindAll search results.

    Represents a snapshot of a FindAll run, including run metadata and a list of
    candidate entities with their match status and details at the time the snapshot was
    taken.
    """

    candidates: List[Candidate]
    """All evaluated candidates at the time of the snapshot."""

    run: FindAllRun
    """FindAll run object."""

    last_event_id: Optional[str] = None
    """ID of the last event of the run at the time of the request.

    This can be used to resume streaming from the last event.
    """


FindallRunResult = FindAllRunResult  # for backwards compatibility with v0.3.4
"""This is deprecated, `FindAllRunResult` should be used instead"""
