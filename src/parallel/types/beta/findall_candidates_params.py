# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["FindAllCandidatesParams"]


class FindAllCandidatesParams(TypedDict, total=False):
    entity_type: Required[Literal["company", "people"]]
    """Type of entity to search for."""

    objective: Required[str]
    """Natural language description of target entities."""

    match_limit: int
    """Maximum number of candidates to return.

    Must be between 5 and 1000 (inclusive). May return fewer results. Defaults
    to 100.
    """
