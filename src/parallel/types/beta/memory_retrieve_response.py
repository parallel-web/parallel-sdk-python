# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union
from typing_extensions import Annotated, TypeAlias

from ..._utils import PropertyInfo
from ..._models import BaseModel
from .task_memory_result import TaskMemoryResult
from .findall_memory_result import FindAllMemoryResult
from .monitor_memory_result import MonitorMemoryResult

__all__ = ["MemoryRetrieveResponse", "Result"]

Result: TypeAlias = Annotated[
    Union[TaskMemoryResult, MonitorMemoryResult, FindAllMemoryResult], PropertyInfo(discriminator="kind")
]


class MemoryRetrieveResponse(BaseModel):
    results: List[Result]
