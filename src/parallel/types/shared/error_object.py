# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["ErrorObject"]


class ErrorObject(BaseModel):
    message: str
    """Human-readable message."""

    ref_id: str
    """Reference ID for the error."""

    detail: Optional[object] = None
    """Optional detail supporting the error."""
