# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["MemoryRetrieveParams"]


class MemoryRetrieveParams(TypedDict, total=False):
    kind: Optional[Literal["task", "monitor", "findall"]]
    """Filter memories by kind: `task`, `monitor`, or `findall`."""

    limit: int
    """Maximum number of memories to return."""

    memory_scope_key: Optional[str]
    """User-provided key identifying the memory scope to use.

    Omit to use personal memory, if available.
    """

    query: Optional[str]
    """Concise query describing the memories to retrieve.

    Empty queries return the most recent memories.
    """

    since: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """
    Only return memories sourced from task, monitor, or FindAll runs completed at or
    after this RFC 3339 timestamp.
    """
