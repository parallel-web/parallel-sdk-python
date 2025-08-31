# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable, Optional
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from ..task_spec_param import TaskSpecParam
from .parallel_beta_param import ParallelBetaParam
from .beta_run_input_param import BetaRunInputParam

__all__ = ["TaskGroupAddRunsParams"]


class TaskGroupAddRunsParams(TypedDict, total=False):
    inputs: Required[Iterable[BetaRunInputParam]]
    """List of task runs to execute."""

    default_task_spec: Optional[TaskSpecParam]
    """Specification for a task.

    Auto output schemas can be specified by setting `output_schema={"type":"auto"}`.
    Not specifying a TaskSpec is the same as setting an auto output schema.

    For convenience bare strings are also accepted as input or output schemas.
    """

    betas: Annotated[List[ParallelBetaParam], PropertyInfo(alias="parallel-beta")]
    """Optional header to specify the beta version(s) to enable."""
