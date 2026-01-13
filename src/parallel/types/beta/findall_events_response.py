# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Annotated, TypeAlias

from ..._utils import PropertyInfo
from .error_event import ErrorEvent
from .findall_run_status_event import FindAllRunStatusEvent
from .findall_schema_updated_event import FindAllSchemaUpdatedEvent
from .findall_candidate_match_status_event import FindAllCandidateMatchStatusEvent

__all__ = ["FindAllEventsResponse", "FindallEventsResponse"]

FindAllEventsResponse: TypeAlias = Annotated[
    Union[FindAllSchemaUpdatedEvent, FindAllRunStatusEvent, FindAllCandidateMatchStatusEvent, ErrorEvent],
    PropertyInfo(discriminator="type"),
]


FindallEventsResponse = FindAllEventsResponse  # for backwards compatibility with v0.3.4
"""This is deprecated, `FindAllEventsResponse` should be used instead"""
