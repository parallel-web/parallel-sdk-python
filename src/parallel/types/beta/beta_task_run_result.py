# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from ..._utils import PropertyInfo
from ..._models import BaseModel
from ..task_run import TaskRun
from ..field_basis import FieldBasis
from .mcp_tool_call import McpToolCall

__all__ = ["BetaTaskRunResult", "Output", "OutputBetaTaskRunTextOutput", "OutputBetaTaskRunJsonOutput"]


class OutputBetaTaskRunTextOutput(BaseModel):
    basis: List[FieldBasis]
    """Basis for the output."""

    content: str
    """Text output from the task."""

    type: Literal["text"]
    """
    The type of output being returned, as determined by the output schema of the
    task spec.
    """

    beta_fields: Optional[Dict[str, object]] = None
    """Always None."""

    mcp_tool_calls: Optional[List[McpToolCall]] = None
    """MCP tool calls made by the task."""


class OutputBetaTaskRunJsonOutput(BaseModel):
    basis: List[FieldBasis]
    """Basis for the output."""

    content: Dict[str, object]
    """
    Output from the task as a native JSON object, as determined by the output schema
    of the task spec.
    """

    type: Literal["json"]
    """
    The type of output being returned, as determined by the output schema of the
    task spec.
    """

    beta_fields: Optional[Dict[str, object]] = None
    """Always None."""

    mcp_tool_calls: Optional[List[McpToolCall]] = None
    """MCP tool calls made by the task."""

    output_schema: Optional[Dict[str, object]] = None
    """Output schema for the Task Run.

    Populated only if the task was executed with an auto schema.
    """


Output: TypeAlias = Annotated[
    Union[OutputBetaTaskRunTextOutput, OutputBetaTaskRunJsonOutput], PropertyInfo(discriminator="type")
]


class BetaTaskRunResult(BaseModel):
    output: Output
    """Output from the task conforming to the output schema."""

    run: TaskRun
    """Status of a task run."""
