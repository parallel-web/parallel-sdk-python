# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel

__all__ = ["FindAllCandidatesResponse", "Candidate"]


class Candidate(BaseModel):
    description: str
    """Descriptive text about the entity."""

    name: str
    """Entity name."""

    url: str
    """Canonical URL for the entity."""


class FindAllCandidatesResponse(BaseModel):
    candidate_set_id: str
    """Candidate set request ID.

    Example: `candidate_set_cad0a6d2dec046bd95ae900527d880e7`
    """

    candidates: List[Candidate]
    """Ranked list of entity candidates."""
