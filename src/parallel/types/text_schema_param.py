# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["TextSchemaParam"]


class TextSchemaParam(TypedDict, total=False):
    description: Optional[str]
    """A text description of the desired output from the task."""

    type: Literal["text"]
    """The type of schema being defined. Always `text`."""
