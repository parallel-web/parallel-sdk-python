# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .parallel_beta_param import ParallelBetaParam

__all__ = ["FindAllIngestParams", "FindallIngestParams"]


class FindAllIngestParams(TypedDict, total=False):
    objective: Required[str]
    """Natural language objective to create a FindAll run spec."""

    betas: Annotated[List[ParallelBetaParam], PropertyInfo(alias="parallel-beta")]
    """Optional header to specify the beta version(s) to enable."""


FindallIngestParams = FindAllIngestParams  # for backwards compatibility with v0.3.4
"""This is deprecated, `FindAllIngestParams` should be used instead"""
