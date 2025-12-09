# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel
from ..shared.error_object import ErrorObject

__all__ = ["ErrorEvent"]


class ErrorEvent(BaseModel):
    """Event indicating an error."""

    error: ErrorObject
    """Error."""

    type: Literal["error"]
    """Event type; always 'error'."""
