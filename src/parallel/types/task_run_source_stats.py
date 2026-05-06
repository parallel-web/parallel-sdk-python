# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["TaskRunSourceStats"]


class TaskRunSourceStats(BaseModel):
    """Source stats for a task run."""

    num_sources_considered: Optional[int] = None
    """Number of sources considered in processing the task."""

    num_sources_read: Optional[int] = None
    """Number of sources read in processing the task."""

    sources_read_sample: Optional[List[str]] = None
    """A sample of URLs of sources read in processing the task."""
