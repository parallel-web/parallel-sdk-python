# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Union, Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .findall_run_status import FindAllRunStatus

__all__ = [ "FindallRun", "FindAllRun"]


class FindAllRun(BaseModel):
    """FindAll run object with status and metadata."""

    findall_id: str
    """ID of the FindAll run."""

    generator: Literal["base", "core", "pro", "preview"]
    """Generator for the FindAll run."""

    status: FindAllRunStatus
    """Status object for the FindAll run."""

    created_at: Optional[str] = None
    """Timestamp of the creation of the run, in RFC 3339 format."""

    metadata: Optional[Dict[str, Union[str, float, bool]]] = None
    """Metadata for the FindAll run."""

    modified_at: Optional[str] = None
    """
    Timestamp of the latest modification to the FindAll run result, in RFC 3339
    format.
    """


FindallRun = FindAllRun  # for backwards compatibility with v0.3.4
"""This is deprecated, `FindAllRun` should be used instead"""

# Backwards-compat aliases (deprecated). `Status` and `StatusMetrics` were
# inline classes in this module; they now live as top-level `FindAllRunStatus`
# and `FindAllCandidateMetrics` models.
from .findall_candidate_metrics import FindAllCandidateMetrics  # noqa: E402

Status = FindAllRunStatus
StatusMetrics = FindAllCandidateMetrics
