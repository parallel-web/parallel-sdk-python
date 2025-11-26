# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Annotated, TypeAlias

from .._utils import PropertyInfo
from .._models import BaseModel
from .task_run import TaskRun
from .task_run_json_output import TaskRunJsonOutput
from .task_run_text_output import TaskRunTextOutput

__all__ = ["TaskRunResult", "Output"]

Output: TypeAlias = Annotated[Union[TaskRunTextOutput, TaskRunJsonOutput], PropertyInfo(discriminator="type")]


class TaskRunResult(BaseModel):
    output: Output
    """Output from the task conforming to the output schema."""

    run: TaskRun
    """Task run object with status 'completed'."""
