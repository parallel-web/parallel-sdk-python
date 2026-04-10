# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Required, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .fetch_policy_param import FetchPolicyParam
from .excerpt_settings_param import ExcerptSettingsParam

__all__ = ["ClientExtractParams", "Advanced", "AdvancedFullContent", "AdvancedFullContentFullContentSettings"]


class ClientExtractParams(TypedDict, total=False):
    urls: Required[SequenceNotStr[str]]
    """URLs to extract content from. Up to 20 URLs."""

    advanced: Optional[Advanced]
    """Advanced extract configuration."""

    client_model: Optional[str]
    """The model generating this request and consuming the results.

    Enables optimizations and tailors default settings for the model's capabilities.
    """

    max_chars_total: Optional[int]
    """Upper bound on total characters across excerpts from all extracted results.

    Does not affect full_content if requested. Default is dynamic based on urls,
    objective, and client_model.
    """

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


class AdvancedFullContentFullContentSettings(TypedDict, total=False):
    """Optional settings for returning full content."""

    max_chars_per_result: Optional[int]
    """
    Optional limit on the number of characters to include in the full content for
    each url. Full content always starts at the beginning of the page and is
    truncated at the limit if necessary.
    """


AdvancedFullContent: TypeAlias = Union[AdvancedFullContentFullContentSettings, bool]


class Advanced(TypedDict, total=False):
    """Advanced extract configuration."""

    excerpt_settings: Optional[ExcerptSettingsParam]
    """Optional settings for returning relevant excerpts."""

    fetch_policy: Optional[FetchPolicyParam]
    """Policy for live fetching web results."""

    full_content: AdvancedFullContent
    """Controls full content extraction.

    Set to true to enable with defaults, false to disable, or provide
    FullContentSettings for fine-grained control.
    """
