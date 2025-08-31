# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["TaskGroupGetRunsParams"]


class TaskGroupGetRunsParams(TypedDict, total=False):
    include_input: bool

    include_output: bool

    last_event_id: Optional[str]

    status: Optional[Literal["queued", "action_required", "running", "completed", "failed", "cancelling", "cancelled"]]
