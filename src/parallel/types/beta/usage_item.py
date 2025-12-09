# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["UsageItem"]


class UsageItem(BaseModel):
    """Usage item for a single operation."""

    count: int
    """Count of the SKU."""

    name: str
    """Name of the SKU."""
