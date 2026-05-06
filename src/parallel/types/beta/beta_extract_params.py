# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from typing_extensions import Required, Annotated, TypeAlias, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo
from ..fetch_policy_param import FetchPolicyParam
from .parallel_beta_param import ParallelBetaParam
from .excerpt_settings_param import ExcerptSettingsParam
from ..full_content_settings_param import FullContentSettingsParam

__all__ = ["BetaExtractParams", "Excerpts", "FullContent"]


class BetaExtractParams(TypedDict, total=False):
    urls: Required[SequenceNotStr[str]]

    client_model: Optional[str]
    """The model generating this request and consuming the results.

    Enables optimizations and tailors default settings for the model's capabilities.
    """

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

    session_id: Optional[str]
    """
    Session identifier to track calls across separate search and extract calls, to
    be used as part of a larger task. Specifying it may give better contextual
    results for subsequent API calls.
    """

    betas: Annotated[List[ParallelBetaParam], PropertyInfo(alias="parallel-beta")]
    """Optional header to specify the beta version(s) to enable."""


Excerpts: TypeAlias = Union[bool, ExcerptSettingsParam]

FullContent: TypeAlias = Union[bool, FullContentSettingsParam]

# Backwards-compat alias (deprecated). `FullContentFullContentSettings` was an
# inline TypedDict in this module; it now lives as the top-level
# `FullContentSettingsParam`.
FullContentFullContentSettings = FullContentSettingsParam
