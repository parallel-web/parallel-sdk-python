# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel
from .findall_run import FindallRun

__all__ = ["FindallRunStatusEvent"]


class FindallRunStatusEvent(BaseModel):
    data: FindallRun
    """FindAll run object with status and metadata."""

    event_id: str
    """Unique event identifier for the event."""

    timestamp: datetime
    """Timestamp of the event."""

    type: Literal["findall.status"]
    """Event type; always 'findall.status'."""
