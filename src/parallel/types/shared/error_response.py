# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel
from .error_object import ErrorObject

__all__ = ["ErrorResponse"]


class ErrorResponse(BaseModel):
    """Response object used for non-200 status codes."""

    error: ErrorObject
    """Error."""

    type: Literal["error"]
    """Always 'error'."""
