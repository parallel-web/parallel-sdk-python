# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["MemoryClearParams"]


class MemoryClearParams(TypedDict, total=False):
    memory_scope_key: Optional[str]
    """User-provided key identifying the memory scope to use.

    Omit to use personal memory, if available.
    """
