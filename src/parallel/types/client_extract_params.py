# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr
from .advanced_extract_settings_param import AdvancedExtractSettingsParam

__all__ = ["ClientExtractParams"]


class ClientExtractParams(TypedDict, total=False):
    urls: Required[SequenceNotStr[str]]
    """URLs to extract content from. Up to 20 URLs."""

    advanced_settings: Optional[AdvancedExtractSettingsParam]
    """Advanced extract configuration.

    These settings may impact result quality and latency unless used carefully. See
    https://docs.parallel.ai/search/advanced-extract-settings for more info.
    """

    client_model: Optional[str]
    """The model generating this request and consuming the results.

    Enables optimizations and tailors default settings for the model's capabilities.
    """

    max_chars_total: Optional[int]
    """Upper bound on total characters across excerpts from all extracted results."""

    objective: Optional[str]
    """
    As in SearchRequest, a natural-language description of the underlying question
    or goal driving the request. Used together with search_queries to focus excerpts
    on the most relevant content.
    """

    search_queries: Optional[SequenceNotStr[str]]
    """Optional keyword search queries, as in SearchRequest.

    Used together with objective to focus excerpts on the most relevant content.
    """

    session_id: Optional[str]
    """
    Session identifier to track calls across separate search and extract calls, to
    be used as part of a larger task. Specifying it may give better contextual
    results for subsequent API calls.
    """
