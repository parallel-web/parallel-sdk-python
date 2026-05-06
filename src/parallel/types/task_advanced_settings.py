# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["TaskAdvancedSettings"]


class TaskAdvancedSettings(BaseModel):
    """Advanced search configuration for a task run."""

    location: Optional[str] = None
    """ISO 3166-1 alpha-2 country code for geo-targeted search results."""
