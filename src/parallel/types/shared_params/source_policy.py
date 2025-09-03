# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from ..._types import SequenceNotStr

__all__ = ["SourcePolicy"]


class SourcePolicy(TypedDict, total=False):
    exclude_domains: SequenceNotStr[str]
    """List of domains to exclude from results.

    If specified, sources from these domains will be excluded.
    """

    include_domains: SequenceNotStr[str]
    """List of domains to restrict the results to.

    If specified, only sources from these domains will be included.
    """
