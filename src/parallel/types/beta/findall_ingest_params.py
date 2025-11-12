# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from typing_extensions import Required, Annotated, TypeAlias, TypedDict

from ..._utils import PropertyInfo
from .parallel_beta_param import ParallelBetaParam

__all__ = ["FindallIngestParams", "IngestInput", "IngestPayload"]


class IngestInput(TypedDict, total=False):
    objective: Required[str]
    """Natural language objective to create a FindAll run spec."""

    betas: Annotated[List[ParallelBetaParam], PropertyInfo(alias="parallel-beta")]
    """Optional header to specify the beta version(s) to enable."""


class IngestPayload(TypedDict, total=False):
    query: Required[str]

    return_evidence_enrichments: bool

    betas: Annotated[List[ParallelBetaParam], PropertyInfo(alias="parallel-beta")]
    """Optional header to specify the beta version(s) to enable."""


FindallIngestParams: TypeAlias = Union[IngestInput, IngestPayload]
