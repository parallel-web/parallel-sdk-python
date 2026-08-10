# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["FindAllMemoryResult"]


class FindAllMemoryResult(BaseModel):
    id: str
    """ID of the FindAll run."""

    input_excerpt: str
    """Preview of the run's objective. May be truncated."""

    matched_count: int
    """Current number of matched entities."""

    updated_at: datetime
    """When the FindAll result was last updated, as an RFC 3339 timestamp."""

    kind: Optional[Literal["findall"]] = None
