from typing import Union, Generic, TypeVar, Optional

from pydantic import BaseModel

from .._models import GenericModel
from .task_run_result import TaskRunResult
from .task_run_json_output import TaskRunJsonOutput
from .task_run_text_output import TaskRunTextOutput

ContentType = TypeVar("ContentType", bound=BaseModel)


# we need to disable this check because we're overriding properties
# with subclasses of their types which is technically unsound as
# properties can be mutated.
# pyright: reportIncompatibleVariableOverride=false


class ParsedTaskRunTextOutput(TaskRunTextOutput, GenericModel, Generic[ContentType]):
    parsed: None
    """The parsed output from the task run."""


class ParsedTaskRunJsonOutput(TaskRunJsonOutput, GenericModel, Generic[ContentType]):
    parsed: Optional[ContentType] = None
    """The parsed output from the task run."""


class ParsedTaskRunResult(TaskRunResult, GenericModel, Generic[ContentType]):
    output: Union[ParsedTaskRunTextOutput[ContentType], ParsedTaskRunJsonOutput[ContentType]]  # type: ignore[assignment]
    """The parsed output from the task run."""


ParsedOutputTaskRunTextOutput = ParsedTaskRunTextOutput  # for backwards compatibility with v0.1.3
"""This is deprecated, `ParsedTaskRunTextOutput` should be used instead"""

ParsedOutputTaskRunJsonOutput = ParsedTaskRunJsonOutput  # for backwards compatibility with v0.1.3
"""This is deprecated, `ParsedTaskRunJsonOutput` should be used instead"""
