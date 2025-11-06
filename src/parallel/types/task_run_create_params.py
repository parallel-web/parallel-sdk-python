# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from typing_extensions import Required, TypedDict

from .task_spec_param import TaskSpecParam
from .shared_params.source_policy import SourcePolicy

__all__ = ["TaskRunCreateParams"]


class TaskRunCreateParams(TypedDict, total=False):
    input: Required[Union[str, Dict[str, object]]]
    """Input to the task, either text or a JSON object."""

    processor: Required[str]
    """Processor to use for the task."""

    metadata: Optional[Dict[str, Union[str, float, bool]]]
    """User-provided metadata stored with the run.

    Keys and values must be strings with a maximum length of 16 and 512 characters
    respectively.
    """

    source_policy: Optional[SourcePolicy]
    """Source policy for web search results.

    This policy governs which sources are allowed/disallowed in results.
    """

    task_spec: Optional[TaskSpecParam]
    """Specification for a task.

    Auto output schemas can be specified by setting `output_schema={"type":"auto"}`.
    Not specifying a TaskSpec is the same as setting an auto output schema.

    For convenience bare strings are also accepted as input or output schemas.
    """
