# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from typing_extensions import Required, TypedDict

from .task_spec_param import TaskSpecParam

__all__ = ["TaskRunCreateParams"]


class TaskRunCreateParams(TypedDict, total=False):
    input: Required[Union[str, object]]
    """Input to the task, either text or a JSON object."""

    processor: Required[str]
    """Processor to use for the task."""

    metadata: Optional[Dict[str, Union[str, float, bool]]]
    """User-provided metadata stored with the run.

    Keys and values must be strings with a maximum length of 16 and 512 characters
    respectively.
    """

    task_spec: Optional[TaskSpecParam]
    """Specification for a task.

    For convenience we allow bare strings as input or output schemas, which is
    equivalent to a text schema with the same description.
    """
