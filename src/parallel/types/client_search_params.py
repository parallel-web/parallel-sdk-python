# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

from .._types import SequenceNotStr
from .advanced_search_settings_param import AdvancedSearchSettingsParam

__all__ = ["ClientSearchParams"]


class ClientSearchParams(TypedDict, total=False):
    search_queries: Required[SequenceNotStr[str]]
    """Concise keyword search queries, 3-6 words each.

    At least one query is required, provide 2-3 for best results. Used together with
    objective to focus results on the most relevant content.
    """

    advanced_settings: Optional[AdvancedSearchSettingsParam]
    """Advanced search configuration.

    These settings may impact result quality and latency unless used carefully. See
    https://docs.parallel.ai/search/advanced-search-settings for more info.
    """

    client_model: Optional[str]
    """The model generating this request and consuming the results.

    Enables optimizations and tailors default settings for the model's capabilities.
    """

    max_chars_total: Optional[int]
    """Upper bound on total characters across excerpts from all results."""

    mode: Optional[Literal["basic", "advanced"]]
    """Search mode preset: supported values are `basic` and `advanced`.

    Basic mode offers the lowest latency and works best with 2-3 high-quality
    search_queries. Advanced mode provides higher quality with more advanced
    retrieval and compression. Defaults to `advanced` when omitted.
    """

    objective: Optional[str]
    """
    Natural-language description of the underlying question or goal driving the
    search. Used together with search_queries to focus results on the most relevant
    content. Should be self-contained with enough context to understand the intent
    of the search.
    """

    session_id: Optional[str]
    """
    Session identifier to track calls across separate search and extract calls, to
    be used as part of a larger task. Specifying it may give better contextual
    results for subsequent API calls.
    """
