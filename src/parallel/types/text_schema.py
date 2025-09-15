# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["TextSchema"]


class TextSchema(BaseModel):
    description: Optional[str] = None
    """A text description of the desired output from the task."""

    type: Optional[Literal["text"]] = None
    """The type of schema being defined. Always `text`."""
