# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo
from .parallel_beta_param import ParallelBetaParam

__all__ = ["TaskRunResultParams"]


class TaskRunResultParams(TypedDict, total=False):
    api_timeout: Annotated[int, PropertyInfo(alias="timeout")]

    betas: Annotated[List[ParallelBetaParam], PropertyInfo(alias="parallel-beta")]
    """Optional header to specify the beta version(s) to enable."""
