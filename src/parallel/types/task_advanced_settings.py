# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["TaskAdvancedSettings", "DataSources"]


class DataSources(BaseModel):
    """Optional partner data sources to enable for this task run.

    Supported on standard processors only; a selected partner name must not collide with an `mcp_servers` entry.
    """

    free: Optional[List[str]] = None
    """
    Free data partners to enable for this task, in addition to sources included with
    the processor. Never billed. See the Data Sources documentation for the
    available names.
    """

    pay_per_use: Optional[List[str]] = None
    """
    Pay-per-use data partners to enable for this task, in addition to sources
    included with the processor. See the Data Sources documentation for the
    available names.
    """


class TaskAdvancedSettings(BaseModel):
    """Advanced search configuration for a task run."""

    data_sources: Optional[DataSources] = None
    """Optional partner data sources to enable for this task run.

    Supported on standard processors only; a selected partner name must not collide
    with an `mcp_servers` entry.
    """

    location: Optional[str] = None
    """ISO 3166-1 alpha-2 country code for geo-targeted search results."""
