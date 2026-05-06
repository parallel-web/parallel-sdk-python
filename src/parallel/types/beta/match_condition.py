# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["MatchCondition"]


class MatchCondition(BaseModel):
    """Match condition model for FindAll ingest."""

    description: str
    """Detailed description of the match condition.

    Include as much specific information as possible to help improve the quality and
    accuracy of Find All run results.
    """

    name: str
    """Name of the match condition."""
