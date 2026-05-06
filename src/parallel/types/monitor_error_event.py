# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["MonitorErrorEvent"]


class MonitorErrorEvent(BaseModel):
    """Emitted when a monitor execution failed (e.g. payment or quota error).

    Always included in the events list regardless of `include_completions`.
    """

    error_message: str
    """Human-readable description of the failure."""

    timestamp: datetime
    """Timestamp of when the monitor execution failed, as an RFC 3339 string."""

    event_type: Optional[Literal["error"]] = None
    """Discriminant for the error event variant."""
