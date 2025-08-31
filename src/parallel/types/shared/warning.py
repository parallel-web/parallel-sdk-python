# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["Warning"]


class Warning(BaseModel):
    message: str
    """Human-readable message."""

    type: Literal["spec_validation_warning", "input_validation_warning", "warning"]
    """Type of warning.

    Note that adding new warning types is considered a backward-compatible change.
    """

    detail: Optional[Dict[str, object]] = None
    """Optional detail supporting the warning."""
