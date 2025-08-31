# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal, Required, TypedDict

__all__ = ["JsonSchemaParam"]


class JsonSchemaParam(TypedDict, total=False):
    json_schema: Required[Dict[str, object]]
    """A JSON Schema object. Only a subset of JSON Schema is supported."""

    type: Literal["json"]
    """The type of schema being defined. Always `json`."""
