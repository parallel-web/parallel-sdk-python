# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["AutoSchema"]


class AutoSchema(BaseModel):
    type: Optional[Literal["auto"]] = None
    """The type of schema being defined. Always `auto`."""
