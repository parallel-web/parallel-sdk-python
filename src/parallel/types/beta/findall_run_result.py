# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .findall_run import FindAllRun
from .findall_candidate import FindAllCandidate

__all__ = [ "FindallRunResult", "FindAllRunResult"]


class FindAllRunResult(BaseModel):
    """Complete FindAll search results.

    Represents a snapshot of a FindAll run, including run metadata and a list of
    candidate entities with their match status and details at the time the snapshot was
    taken.
    """

    candidates: List[FindAllCandidate]
    """All evaluated candidates at the time of the snapshot."""

    run: FindAllRun
    """FindAll run object."""

    last_event_id: Optional[str] = None
    """ID of the last event of the run at the time of the request.

    This can be used to resume streaming from the last event.
    """


FindallRunResult = FindAllRunResult  # for backwards compatibility with v0.3.4
"""This is deprecated, `FindAllRunResult` should be used instead"""

# Backwards-compat alias (deprecated). `Candidate` was an inline class in this
# module; it now lives as the top-level `FindAllCandidate` model.
Candidate = FindAllCandidate
