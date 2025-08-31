# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["AutoSchemaParam"]


class AutoSchemaParam(TypedDict, total=False):
    type: Literal["auto"]
    """The type of schema being defined. Always `auto`."""
