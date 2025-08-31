# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, TypeAlias

__all__ = ["ParallelBetaParam"]

ParallelBetaParam: TypeAlias = Union[
    Literal["mcp-server-2025-07-17", "events-sse-2025-07-24", "webhook-2025-08-12"], str
]
