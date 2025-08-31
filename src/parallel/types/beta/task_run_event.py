# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from ..._utils import PropertyInfo
from ..._models import BaseModel
from ..task_run import TaskRun
from .beta_run_input import BetaRunInput
from ..task_run_json_output import TaskRunJsonOutput
from ..task_run_text_output import TaskRunTextOutput

__all__ = ["TaskRunEvent", "Output"]

Output: TypeAlias = Annotated[Union[TaskRunTextOutput, TaskRunJsonOutput, None], PropertyInfo(discriminator="type")]


class TaskRunEvent(BaseModel):
    event_id: Optional[str] = None
    """Cursor to resume the event stream. Always empty for non Task Group runs."""

    run: TaskRun
    """Status of a task run."""

    type: Literal["task_run.state"]
    """Event type; always 'task_run.state'."""

    input: Optional[BetaRunInput] = None
    """Task run input with additional beta fields."""

    output: Optional[Output] = None
    """Output from the run; included only if requested and if status == `completed`."""
