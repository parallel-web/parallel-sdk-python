# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["MonitorSnapshotSettingsParam"]


class MonitorSnapshotSettingsParam(TypedDict, total=False):
    """Type-specific settings for a `snapshot` monitor."""

    task_run_id: Required[str]
    """Task run ID whose output becomes the data and schema for the monitor."""
