# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["TaskRunProgressMessageEvent"]


class TaskRunProgressMessageEvent(BaseModel):
    """A message for a task run progress update."""

    message: str
    """Progress update message."""

    timestamp: Optional[str] = None
    """Timestamp of the message."""

    type: Literal[
        "task_run.progress_msg.plan",
        "task_run.progress_msg.search",
        "task_run.progress_msg.result",
        "task_run.progress_msg.tool_call",
        "task_run.progress_msg.exec_status",
    ]
    """Event type; always starts with 'task_run.progress_msg'."""
