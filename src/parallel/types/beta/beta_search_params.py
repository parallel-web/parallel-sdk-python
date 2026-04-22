# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo
from ..fetch_policy_param import FetchPolicyParam
from .parallel_beta_param import ParallelBetaParam
from .excerpt_settings_param import ExcerptSettingsParam
from ..shared_params.source_policy import SourcePolicy

__all__ = ["BetaSearchParams"]


class BetaSearchParams(TypedDict, total=False):
    client_model: Optional[str]
    """The model generating this request and consuming the results.

    Enables optimizations and tailors default settings for the model's capabilities.
    """

    excerpts: ExcerptSettingsParam
    """Optional settings to configure excerpt generation."""

    fetch_policy: Optional[FetchPolicyParam]
    """Policy for live fetching web results."""

    location: Optional[str]
    """ISO 3166-1 alpha-2 country code for geo-targeted search results."""

    max_chars_per_result: Optional[int]
    """DEPRECATED: Use `excerpts.max_chars_per_result` instead."""

    max_results: Optional[int]
    """Upper bound on the number of results to return. Defaults to 10 if not provided."""

    mode: Optional[Literal["one-shot", "agentic", "fast"]]
    """Presets default values for parameters for different use cases.

    - `one-shot` returns more comprehensive results and longer excerpts to answer
      questions from a single response
    - `agentic` returns more concise, token-efficient results for use in an agentic
      loop
    - `fast` trades some quality for lower latency, with best results when used with
      concise and high-quality objective and keyword queries
    """

    objective: Optional[str]
    """Natural-language description of what the web search is trying to find.

    May include guidance about preferred sources or freshness. At least one of
    objective or search_queries must be provided.
    """

    processor: Optional[Literal["base", "pro"]]
    """DEPRECATED: use `mode` instead."""

    search_queries: Optional[SequenceNotStr[str]]
    """Optional list of traditional keyword search queries to guide the search.

    May contain search operators. At least one of objective or search_queries must
    be provided.
    """

    session_id: Optional[str]
    """
    Session identifier to track calls across separate search and extract calls, to
    be used as part of a larger task. Specifying it may give better contextual
    results for subsequent API calls.
    """

    source_policy: Optional[SourcePolicy]
    """Source policy for web search results.

    This policy governs which sources are allowed/disallowed in results.
    """

    betas: Annotated[List[ParallelBetaParam], PropertyInfo(alias="parallel-beta")]
    """Optional header to specify the beta version(s) to enable."""
