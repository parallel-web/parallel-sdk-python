# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .extract_error import ExtractError
from .extract_result import ExtractResult

__all__ = ["ExtractResponse"]


class ExtractResponse(BaseModel):
    errors: List[ExtractError]
    """Extract errors: requested URLs not in the results."""

    extract_id: str
    """Extract request ID, e.g. `extract_cad0a6d2dec046bd95ae900527d880e7`"""

    results: List[ExtractResult]
    """Successful extract results."""
