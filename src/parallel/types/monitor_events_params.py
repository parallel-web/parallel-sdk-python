# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["MonitorEventsParams"]


class MonitorEventsParams(TypedDict, total=False):
    cursor: Optional[str]
    """Pass `next_cursor` from a previous response to retrieve more events."""

    event_group_id: Optional[str]
    """Filter to a single execution.

    Values come from `event_group_id` in webhook events and listed events.
    Pagination params are ignored when set.
    """

    include_completions: bool
    """
    When true, include completion events for executions that ran but detected no
    material changes. Useful for auditing execution history.
    """

    limit: Optional[int]
    """Maximum number of events to return. Defaults to 20. Between 1 and 100."""
