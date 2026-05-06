# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["MonitorCompletionEvent"]


class MonitorCompletionEvent(BaseModel):
    """Emitted when a monitor execution ran but detected no material changes.

    Only returned when `include_completions=true` is passed to the list events
    endpoint. Useful for auditing execution history alongside content events.
    """

    timestamp: datetime
    """Timestamp of when the monitor execution completed, as an RFC 3339 string."""

    event_type: Optional[Literal["completion"]] = None
    """Discriminant for the completion event variant."""
