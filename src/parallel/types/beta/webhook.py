# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["Webhook"]


class Webhook(BaseModel):
    url: str
    """URL for the webhook."""

    event_types: Optional[List[Literal["task_run.status"]]] = None
    """Event types to send the webhook notifications for."""
