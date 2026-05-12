# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from ..webhook_param import WebhookParam
from .parallel_beta_param import ParallelBetaParam
from .match_condition_param import MatchConditionParam

__all__ = ["FindAllCreateParams", "FindallCreateParams", "ExcludeList"]


class FindAllCreateParams(TypedDict, total=False):
    entity_type: Required[str]
    """Type of the entity for the FindAll run."""

    generator: Required[Literal["base", "core", "pro", "preview"]]
    """Generator for the FindAll run. One of base, core, pro, preview."""

    match_conditions: Required[Iterable[MatchConditionParam]]
    """List of match conditions for the FindAll run."""

    match_limit: Required[int]
    """Maximum number of matches to find for this FindAll run.

    Must be between 5 and 1000 (inclusive). May return fewer results.
    """

    objective: Required[str]
    """Natural language objective of the FindAll run."""

    exclude_list: Optional[Iterable[ExcludeList]]
    """List of entity names/IDs to exclude from results."""

    metadata: Optional[Dict[str, Union[str, float, bool]]]
    """Metadata for the FindAll run."""

    webhook: Optional[WebhookParam]
    """Webhooks for Task Runs."""

    betas: Annotated[List[ParallelBetaParam], PropertyInfo(alias="parallel-beta")]
    """Optional header to specify the beta version(s) to enable."""


class ExcludeList(TypedDict, total=False):
    """Exclude candidate input model for FindAll run."""

    name: Required[str]
    """Name of the entity to exclude from results."""

    url: Required[str]
    """URL of the entity to exclude from results."""


FindallCreateParams = FindAllCreateParams  # for backwards compatibility with v0.3.4
"""This is deprecated, `FindAllCreateParams` should be used instead"""

# Backwards-compat alias (deprecated). `MatchCondition` was an inline TypedDict
# in this module; it now lives as the top-level `MatchConditionParam`.
MatchCondition = MatchConditionParam
