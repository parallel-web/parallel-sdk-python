# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from typing_extensions import Required, Annotated, TypeAlias, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo
from .fetch_policy_param import FetchPolicyParam
from .parallel_beta_param import ParallelBetaParam
from .excerpt_settings_param import ExcerptSettingsParam

__all__ = ["BetaExtractParams", "Excerpts", "FullContent", "FullContentFullContentSettings"]


class BetaExtractParams(TypedDict, total=False):
    urls: Required[SequenceNotStr[str]]

    betas: Required[Annotated[List[ParallelBetaParam], PropertyInfo(alias="parallel-beta")]]
    """Optional header to specify the beta version(s) to enable."""

    excerpts: Excerpts
    """Include excerpts from each URL relevant to the search objective and queries.

    Note that if neither objective nor search_queries is provided, excerpts are
    redundant with full content.
    """

    fetch_policy: Optional[FetchPolicyParam]
    """Policy for live fetching web results."""

    full_content: FullContent
    """Include full content from each URL.

    Note that if neither objective nor search_queries is provided, excerpts are
    redundant with full content.
    """

    objective: Optional[str]
    """If provided, focuses extracted content on the specified search objective."""

    search_queries: Optional[SequenceNotStr[str]]
    """If provided, focuses extracted content on the specified keyword search queries."""


Excerpts: TypeAlias = Union[bool, ExcerptSettingsParam]


class FullContentFullContentSettings(TypedDict, total=False):
    """Optional settings for returning full content."""

    max_chars_per_result: Optional[int]
    """
    Optional limit on the number of characters to include in the full content for
    each url. Full content always starts at the beginning of the page and is
    truncated at the limit if necessary.
    """


FullContent: TypeAlias = Union[bool, FullContentFullContentSettings]
