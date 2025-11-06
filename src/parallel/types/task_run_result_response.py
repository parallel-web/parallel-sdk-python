# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import TypeAlias

from .task_run_result import TaskRunResult
from .beta.beta_task_run_result import BetaTaskRunResult

__all__ = ["TaskRunResultResponse"]

TaskRunResultResponse: TypeAlias = Union[TaskRunResult, BetaTaskRunResult]
