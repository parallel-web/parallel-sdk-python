# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from typing_extensions import Required, Annotated, TypeAlias, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo
from .fetch_policy_param import FetchPolicyParam
from .parallel_beta_param import ParallelBetaParam
from .excerpt_settings_param import ExcerptSettingsParam

__all__ = ["BetaExtractParams", "Excerpts"]


class BetaExtractParams(TypedDict, total=False):
    urls: Required[SequenceNotStr[str]]

    excerpts: Excerpts
    """Include excerpts from each URL relevant to the search objective and queries."""

    fetch_policy: Optional[FetchPolicyParam]
    """Policy for live fetching web results."""

    objective: Optional[str]
    """If provided, focuses extracted content on the specified search objective."""

    search_queries: Optional[SequenceNotStr[str]]
    """If provided, focuses extracted content on the specified keyword search queries."""

    betas: Annotated[List[ParallelBetaParam], PropertyInfo(alias="parallel-beta")]
    """Optional header to specify the beta version(s) to enable."""


Excerpts: TypeAlias = Union[bool, ExcerptSettingsParam]
