from typing import Union, Generic, TypeVar, Optional

from pydantic import BaseModel

from .._models import GenericModel
from .task_run_result import TaskRunResult, OutputTaskRunJsonOutput, OutputTaskRunTextOutput

ContentType = TypeVar("ContentType", bound=BaseModel)


# we need to disable this check because we're overriding properties
# with subclasses of their types which is technically unsound as
# properties can be mutated.
# pyright: reportIncompatibleVariableOverride=false


class ParsedOutputTaskRunTextOutput(OutputTaskRunTextOutput, GenericModel, Generic[ContentType]):
    parsed: None
    """The parsed output from the task run."""


class ParsedOutputTaskRunJsonOutput(OutputTaskRunJsonOutput, GenericModel, Generic[ContentType]):
    parsed: Optional[ContentType] = None
    """The parsed output from the task run."""


class ParsedTaskRunResult(TaskRunResult, GenericModel, Generic[ContentType]):
    output: Union[ParsedOutputTaskRunTextOutput[ContentType], ParsedOutputTaskRunJsonOutput[ContentType]]  # type: ignore[assignment]
    """The parsed output from the task run."""
