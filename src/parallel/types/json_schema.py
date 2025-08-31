# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["JsonSchema"]


class JsonSchema(BaseModel):
    json_schema: Dict[str, object]
    """A JSON Schema object. Only a subset of JSON Schema is supported."""

    type: Optional[Literal["json"]] = None
    """The type of schema being defined. Always `json`."""
