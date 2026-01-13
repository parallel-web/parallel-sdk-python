# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel
from .findall_run import FindAllRun

__all__ = ["FindAllRunStatusEvent", "FindallRunStatusEvent"]


class FindAllRunStatusEvent(BaseModel):
    """Event containing status update for FindAll run."""

    data: FindAllRun
    """Updated FindAll run information."""

    event_id: str
    """Unique event identifier for the event."""

    timestamp: datetime
    """Timestamp of the event."""

    type: Literal["findall.status"]
    """Event type; always 'findall.status'."""


FindallRunStatusEvent = FindAllRunStatusEvent  # for backwards compatibility with v0.3.4
"""This is deprecated, `FindAllRunStatusEvent` should be used instead"""
