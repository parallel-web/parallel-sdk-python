# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["TaskMemoryResult"]


class TaskMemoryResult(BaseModel):
    id: str
    """ID of the task run."""

    input_excerpt: str
    """Preview of the run's input. May be truncated."""

    output_excerpt: str
    """Preview of the run's output. May be truncated."""

    updated_at: datetime
    """When the run completed, as an RFC 3339 timestamp."""

    kind: Optional[Literal["task"]] = None
