# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Annotated, TypeAlias

from ..._utils import PropertyInfo
from .error_event import ErrorEvent
from .findall_run_status_event import FindallRunStatusEvent
from .findall_schema_updated_event import FindallSchemaUpdatedEvent
from .findall_candidate_match_status_event import FindallCandidateMatchStatusEvent

__all__ = ["FindallEventsResponse"]

FindallEventsResponse: TypeAlias = Annotated[
    Union[FindallSchemaUpdatedEvent, FindallRunStatusEvent, FindallCandidateMatchStatusEvent, ErrorEvent],
    PropertyInfo(discriminator="type"),
]
