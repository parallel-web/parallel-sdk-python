# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from ..._models import BaseModel
from ..field_basis import FieldBasis

__all__ = ["FindAllCandidate"]


class FindAllCandidate(BaseModel):
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
