# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo
from .parallel_beta_param import ParallelBetaParam

__all__ = ["FindAllEventsParams", "FindallEventsParams"]


class FindAllEventsParams(TypedDict, total=False):
    last_event_id: Optional[str]

    api_timeout: Annotated[Optional[float], PropertyInfo(alias="timeout")]

    betas: Annotated[List[ParallelBetaParam], PropertyInfo(alias="parallel-beta")]
    """Optional header to specify the beta version(s) to enable."""


FindallEventsParams = FindAllEventsParams  # for backwards compatibility with v0.3.4
"""This is deprecated, `FindAllEventsParams` should be used instead"""
