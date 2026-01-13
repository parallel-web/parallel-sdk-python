# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel
from ..field_basis import FieldBasis

__all__ = ["FindAllCandidateMatchStatusEvent", "FindallCandidateMatchStatusEvent", "Data"]


class Data(BaseModel):
    """The candidate whose match status has been updated."""

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


class FindAllCandidateMatchStatusEvent(BaseModel):
    """Event containing a candidate whose match status has changed."""

    data: Data
    """The candidate whose match status has been updated."""

    event_id: str
    """Unique event identifier for the event."""

    timestamp: datetime
    """Timestamp of the event."""

    type: Literal[
        "findall.candidate.generated",
        "findall.candidate.matched",
        "findall.candidate.unmatched",
        "findall.candidate.discarded",
        "findall.candidate.enriched",
    ]
    """
    Event type; one of findall.candidate.generated, findall.candidate.matched,
    findall.candidate.unmatched, findall.candidate.discarded,
    findall.candidate.enriched.
    """


FindallCandidateMatchStatusEvent = FindAllCandidateMatchStatusEvent  # for backwards compatibility with v0.3.4
"""This is deprecated, `FindAllCandidateMatchStatusEvent` should be used instead"""
