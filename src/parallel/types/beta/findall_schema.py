# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .findall_enrich_input import FindAllEnrichInput

__all__ = ["FindAllSchema", "FindallSchema", "MatchCondition"]


class MatchCondition(BaseModel):
    """Match condition model for FindAll ingest."""

    description: str
    """Detailed description of the match condition.

    Include as much specific information as possible to help improve the quality and
    accuracy of Find All run results.
    """

    name: str
    """Name of the match condition."""


class FindAllSchema(BaseModel):
    """Response model for FindAll ingest."""

    entity_type: str
    """Type of the entity for the FindAll run."""

    match_conditions: List[MatchCondition]
    """List of match conditions for the FindAll run."""

    objective: str
    """Natural language objective of the FindAll run."""

    enrichments: Optional[List[FindAllEnrichInput]] = None
    """List of enrichment inputs for the FindAll run."""

    generator: Optional[Literal["base", "core", "pro", "preview"]] = None
    """The generator of the FindAll run."""

    match_limit: Optional[int] = None
    """Max number of candidates to evaluate"""


FindallSchema = FindAllSchema  # for backwards compatibility with v0.3.4
"""This is deprecated, `FindAllSchema` should be used instead"""
