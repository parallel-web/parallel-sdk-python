# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, TypedDict

__all__ = ["WebhookParam"]


class WebhookParam(TypedDict, total=False):
    url: Required[str]
    """URL for the webhook."""

    event_types: List[Literal["task_run.status"]]
    """Event types to send the webhook notifications for."""
