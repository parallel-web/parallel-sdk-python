# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Annotated, TypeAlias

from ..._utils import PropertyInfo
from ..task_run_result import TaskRunResult
from ..task_run_json_output import TaskRunJsonOutput
from ..task_run_text_output import TaskRunTextOutput

__all__ = [
    "BetaTaskRunResult",
    "Output",
    "OutputBetaTaskRunJsonOutput",
    "OutputBetaTaskRunTextOutput",
]

BetaTaskRunResult = TaskRunResult
"""This is deprecated, `TaskRunResult` should be used instead"""

OutputBetaTaskRunJsonOutput = TaskRunJsonOutput
"""This is deprecated, `TaskRunJsonOutput` should be used instead"""

OutputBetaTaskRunTextOutput = TaskRunTextOutput
"""This is deprecated, `TaskRunTextOutput` should be used instead"""

Output: TypeAlias = Annotated[
    Union[OutputBetaTaskRunTextOutput, OutputBetaTaskRunJsonOutput],
    PropertyInfo(discriminator="type"),
]
"""This is deprecated, use `Union[TaskRunTextOutput, TaskRunJsonOutput]` instead"""
