# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel
from .findall_schema import FindallSchema

__all__ = ["FindallSchemaUpdatedEvent"]


class FindallSchemaUpdatedEvent(BaseModel):
    data: FindallSchema
    """Response model for FindAll ingest."""

    event_id: str
    """Unique event identifier for the event."""

    timestamp: datetime
    """Timestamp of the event."""

    type: Literal["findall.schema.updated"]
    """Event type; always 'findall.schema.updated'."""
