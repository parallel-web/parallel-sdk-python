# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Annotated, TypeAlias

from ..._utils import PropertyInfo
from ..error_event import ErrorEvent
from ..task_run_event import TaskRunEvent
from ..task_group_status_event import TaskGroupStatusEvent

__all__ = ["TaskGroupEventsResponse"]

TaskGroupEventsResponse: TypeAlias = Annotated[
    Union[TaskGroupStatusEvent, TaskRunEvent, ErrorEvent], PropertyInfo(discriminator="type")
]
