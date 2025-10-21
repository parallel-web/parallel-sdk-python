# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["ExtractError"]


class ExtractError(BaseModel):
    content: Optional[str] = None
    """Content returned for http client or server errors, if any."""

    error_type: str
    """Error type."""

    http_status_code: Optional[int] = None
    """HTTP status code, if available."""

    url: str
