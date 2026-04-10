# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

from .._types import SequenceNotStr
from .fetch_policy_param import FetchPolicyParam
from .excerpt_settings_param import ExcerptSettingsParam
from .shared_params.source_policy import SourcePolicy

__all__ = ["ClientSearchParams", "Advanced"]


class ClientSearchParams(TypedDict, total=False):
    search_queries: Required[SequenceNotStr[str]]
    """Concise keyword search queries, 3-6 words each.

    At least one query is required, provide 2-3 for best results. Used together with
    objective to focus results on the most relevant content.
    """

    advanced: Optional[Advanced]
    """Advanced search configuration."""

    client_model: Optional[str]
    """The model generating this request and consuming the results.

    Enables optimizations and tailors default settings for the model's capabilities.
    """

    max_chars_total: Optional[int]
    """Upper bound on total characters across excerpts from all results.

    Default is dynamic based on search_queries, objective, and client_model.
    """

    mode: Optional[Literal["basic", "standard"]]
    """Search mode preset: supported values are basic and standard.

    Basic mode offers the lowest latency and works best with 2-3 high-quality
    search_queries. Standard mode provides higher quality with more advanced
    retrieval and compression.
    """

    objective: Optional[str]
    """
    Natural-language description of the underlying question or goal driving the
    search. Used together with search_queries to focus results on the most relevant
    content. Should be self-contained with enough context to understand the intent
    of the search.
    """


class Advanced(TypedDict, total=False):
    """Advanced search configuration."""

    excerpt_settings: Optional[ExcerptSettingsParam]
    """Optional settings for returning relevant excerpts."""

    fetch_policy: Optional[FetchPolicyParam]
    """Policy for live fetching web results."""

    location: Optional[str]
    """ISO 3166-1 alpha-2 country code for geo-targeted search results."""

    source_policy: Optional[SourcePolicy]
    """Source policy for web search results.

    This policy governs which sources are allowed/disallowed in results.
    """
