# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from .._types import SequenceNotStr

__all__ = ["TaskAdvancedSettingsParam", "DataSources"]


class DataSources(TypedDict, total=False):
    """Optional partner data sources to enable for this task run.

    Supported on standard processors only; a selected partner name must not collide with an `mcp_servers` entry.
    """

    free: SequenceNotStr[str]
    """
    Free data partners to enable for this task, in addition to sources included with
    the processor. Never billed. See the Data Sources documentation for the
    available names.
    """

    pay_per_use: SequenceNotStr[str]
    """
    Pay-per-use data partners to enable for this task, in addition to sources
    included with the processor. See the Data Sources documentation for the
    available names.
    """


class TaskAdvancedSettingsParam(TypedDict, total=False):
    """Advanced search configuration for a task run."""

    data_sources: Optional[DataSources]
    """Optional partner data sources to enable for this task run.

    Supported on standard processors only; a selected partner name must not collide
    with an `mcp_servers` entry.
    """

    location: Optional[str]
    """ISO 3166-1 alpha-2 country code for geo-targeted search results."""
