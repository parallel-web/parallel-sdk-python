# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .citation import Citation

__all__ = ["FieldBasis"]


class FieldBasis(BaseModel):
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
