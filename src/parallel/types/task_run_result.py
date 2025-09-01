# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Annotated, TypeAlias

from .._utils import PropertyInfo
from .._models import BaseModel
from .citation import Citation
from .task_run import TaskRun
from .field_basis import FieldBasis
from .task_run_json_output import TaskRunJsonOutput
from .task_run_text_output import TaskRunTextOutput

__all__ = [
    "TaskRunResult",
    "Output",
    "OutputTaskRunJsonOutput",
    "OutputTaskRunJsonOutputBasis",
    "OutputTaskRunJsonOutputBasisCitation",
    "OutputTaskRunTextOutput",
    "OutputTaskRunTextOutputBasis",
    "OutputTaskRunTextOutputBasisCitation",
]

OutputTaskRunJsonOutput = TaskRunJsonOutput  # for backwards compatibility with v0.1.3
"""This is deprecated, `TaskRunJsonOutput` should be used instead"""

OutputTaskRunJsonOutputBasis = FieldBasis  # for backwards compatibility with v0.1.3
"""This is deprecated, `FieldBasis` should be used instead"""

OutputTaskRunJsonOutputBasisCitation = Citation  # for backwards compatibility with v0.1.3
"""This is deprecated, `Citation` should be used instead"""

OutputTaskRunTextOutput = TaskRunTextOutput  # for backwards compatibility with v0.1.3
"""This is deprecated, `TaskRunTextOutput` should be used instead"""

OutputTaskRunTextOutputBasis = FieldBasis  # for backwards compatibility with v0.1.3
"""This is deprecated, `FieldBasis` should be used instead"""

OutputTaskRunTextOutputBasisCitation = Citation  # for backwards compatibility with v0.1.3
"""This is deprecated, `Citation` should be used instead"""


Output: TypeAlias = Annotated[Union[TaskRunTextOutput, TaskRunJsonOutput], PropertyInfo(discriminator="type")]


class TaskRunResult(BaseModel):
    output: Output
    """Output from the task conforming to the output schema."""

    run: TaskRun
    """Status of a task run."""
