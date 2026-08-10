# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["MemoryEvictParams"]


class MemoryEvictParams(TypedDict, total=False):
    id: Required[str]
    """ID of the task run, monitor, or FindAll run to evict."""

    kind: Required[Literal["task", "monitor", "findall"]]
    """Kind of source to evict: `task`, `monitor`, or `findall`."""

    memory_scope_key: Optional[str]
    """User-provided key identifying the memory scope to use.

    Omit to use personal memory, if available.
    """
