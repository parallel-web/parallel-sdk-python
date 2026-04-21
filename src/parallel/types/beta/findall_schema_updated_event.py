# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel
from .findall_schema import FindAllSchema

__all__ = ["FindAllSchemaUpdatedEvent", "FindallSchemaUpdatedEvent"]


class FindAllSchemaUpdatedEvent(BaseModel):
    """Event containing full snapshot of FindAll run state."""

    data: FindAllSchema
    """Updated FindAll schema."""

    event_id: str
    """Unique event identifier for the event."""

    timestamp: datetime
    """Timestamp of the event."""

    type: Literal["findall.schema.updated"]
    """Event type; always 'findall.schema.updated'."""


FindallSchemaUpdatedEvent = FindAllSchemaUpdatedEvent  # for backwards compatibility with v0.3.4
"""This is deprecated, `FindAllSchemaUpdatedEvent` should be used instead"""
