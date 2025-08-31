# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .citation import Citation

__all__ = ["TaskRunJsonOutput", "Basis"]


class Basis(BaseModel):
    field: str
    """Name of the output field."""

    reasoning: str
    """Reasoning for the output field."""

    citations: Optional[List[Citation]] = None
    """List of citations supporting the output field."""

    confidence: Optional[str] = None
    """Confidence level for the output field.

    Only certain processors provide confidence levels.
    """


class TaskRunJsonOutput(BaseModel):
    basis: List[Basis]
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
