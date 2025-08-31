# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["TaskGroupEventsParams"]


class TaskGroupEventsParams(TypedDict, total=False):
    last_event_id: Optional[str]

    api_timeout: Annotated[Optional[float], PropertyInfo(alias="timeout")]
