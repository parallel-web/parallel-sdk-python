# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .parallel_beta_param import ParallelBetaParam

__all__ = ["FindAllExtendParams", "FindallExtendParams"]


class FindAllExtendParams(TypedDict, total=False):
    additional_match_limit: Required[int]
    """Additional number of matches to find for this FindAll run.

    This value will be added to the current match limit to determine the new total
    match limit. Must be greater than 0.
    """

    betas: Annotated[List[ParallelBetaParam], PropertyInfo(alias="parallel-beta")]
    """Optional header to specify the beta version(s) to enable."""


FindallExtendParams = FindAllExtendParams  # for backwards compatibility with v0.3.4
"""This is deprecated, `FindAllExtendParams` should be used instead"""
