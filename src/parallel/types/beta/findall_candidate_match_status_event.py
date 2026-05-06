# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel
from .findall_candidate import FindAllCandidate

__all__ = [ "FindallCandidateMatchStatusEvent", "FindAllCandidateMatchStatusEvent"]


class FindAllCandidateMatchStatusEvent(BaseModel):
    """Event containing a candidate whose match status has changed."""

    data: FindAllCandidate
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

# Backwards-compat alias (deprecated). `Data` was an inline class in earlier
# releases; it is now the top-level `FindAllCandidate` model.
Data = FindAllCandidate
