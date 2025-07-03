# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.
from __future__ import annotations

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel
from .task_run import TaskRun

__all__ = [
    "TaskRunResult",
    "Output",
    "OutputTaskRunTextOutput",
    "OutputTaskRunTextOutputBasis",
    "OutputTaskRunTextOutputBasisCitation",
    "OutputTaskRunJsonOutput",
    "OutputTaskRunJsonOutputBasis",
    "OutputTaskRunJsonOutputBasisCitation",
]


class OutputTaskRunTextOutputBasisCitation(BaseModel):
    url: str
    """URL of the citation."""

    excerpts: list[str] | None = None
    """Excerpts from the citation supporting the output.

    Only certain processors provide excerpts.
    """

    title: str | None = None
    """Title of the citation."""


class OutputTaskRunTextOutputBasis(BaseModel):
    field: str
    """Name of the output field."""

    reasoning: str
    """Reasoning for the output field."""

    citations: list[OutputTaskRunTextOutputBasisCitation] | None = None
    """List of citations supporting the output field."""

    confidence: str | None = None
    """Confidence level for the output field.

    Only certain processors provide confidence levels.
    """


class OutputTaskRunTextOutput(BaseModel):
    basis: list[OutputTaskRunTextOutputBasis]
    """Basis for the output. The basis has a single field 'output'."""

    content: str
    """Text output from the task."""

    type: Literal["text"]
    """
    The type of output being returned, as determined by the output schema of the
    task spec.
    """


class OutputTaskRunJsonOutputBasisCitation(BaseModel):
    url: str
    """URL of the citation."""

    excerpts: list[str] | None = None
    """Excerpts from the citation supporting the output.

    Only certain processors provide excerpts.
    """

    title: str | None = None
    """Title of the citation."""


class OutputTaskRunJsonOutputBasis(BaseModel):
    field: str
    """Name of the output field."""

    reasoning: str
    """Reasoning for the output field."""

    citations: list[OutputTaskRunJsonOutputBasisCitation] | None = None
    """List of citations supporting the output field."""

    confidence: str | None = None
    """Confidence level for the output field.

    Only certain processors provide confidence levels.
    """


class OutputTaskRunJsonOutput(BaseModel):
    basis: list[OutputTaskRunJsonOutputBasis]
    """Basis for each top-level field in the JSON output."""

    content: object
    """
    Output from the task as a native JSON object, as determined by the output schema
    of the task spec.
    """

    type: Literal["json"]
    """
    The type of output being returned, as determined by the output schema of the
    task spec.
    """


Output: TypeAlias = Union[OutputTaskRunTextOutput, OutputTaskRunJsonOutput]


class TaskRunResult(BaseModel):
    output: Output
    """Output from the task conforming to the output schema."""

    run: TaskRun
    """Status of a task."""
