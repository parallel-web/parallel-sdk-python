# Backwards-compatible re-export module (deprecated).
#
# Historically this module exposed `TaskGroup` as the data shape for a beta
# task group. The Stainless config no longer aliases the GA `TaskGroup` model
# under `beta` (to avoid a TypeScript class+type collision). Importers that
# still reference `parallel.types.beta.task_group.TaskGroup` should switch to
# `parallel.types.task_group.TaskGroup` instead. This module preserves the old
# import path as a deprecated shim.

from .. import task_group

__all__ = ["TaskGroup"]

TaskGroup = task_group.TaskGroup
