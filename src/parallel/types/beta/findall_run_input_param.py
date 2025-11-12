# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

from .webhook_param import WebhookParam

__all__ = ["FindallRunInputParam", "MatchCondition", "ExcludeList"]


class MatchCondition(TypedDict, total=False):
    description: Required[str]
    """Detailed description of the match condition.

    Include as much specific information as possible to help improve the quality and
    accuracy of Find All run results.
    """

    name: Required[str]
    """Name of the match condition."""


class ExcludeList(TypedDict, total=False):
    name: Required[str]
    """Name of the entity to exclude from results."""

    url: Required[str]
    """URL of the entity to exclude from results."""


class FindallRunInputParam(TypedDict, total=False):
    entity_type: Required[str]
    """Type of the entity for the FindAll run."""

    generator: Required[Literal["base", "core", "pro", "preview"]]
    """Generator for the FindAll run."""

    match_conditions: Required[Iterable[MatchCondition]]
    """List of match conditions for the FindAll run."""

    match_limit: Required[int]
    """Maximum number of matches to find for this FindAll run."""

    objective: Required[str]
    """Natural language objective of the FindAll run."""

    exclude_list: Optional[Iterable[ExcludeList]]
    """List of entity names/IDs to exclude from results."""

    metadata: Optional[Dict[str, Union[str, float, bool]]]
    """Metadata for the FindAll run."""

    webhook: Optional[WebhookParam]
    """Webhooks for Task Runs."""
