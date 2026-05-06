# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["MatchConditionParam"]


class MatchConditionParam(TypedDict, total=False):
    """Match condition model for FindAll ingest."""

    description: Required[str]
    """Detailed description of the match condition.

    Include as much specific information as possible to help improve the quality and
    accuracy of Find All run results.
    """

    name: Required[str]
    """Name of the match condition."""
