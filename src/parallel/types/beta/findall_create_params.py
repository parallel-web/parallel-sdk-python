# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo
from .webhook_param import WebhookParam
from .parallel_beta_param import ParallelBetaParam

__all__ = [
    "FindallCreateParams",
    "FindallRunInput",
    "FindallRunInputMatchCondition",
    "FindallRunInputExcludeList",
    "FindAllRunPayload",
    "FindAllRunPayloadFindallSpec",
    "FindAllRunPayloadFindallSpecColumn",
    "FindAllRunPayloadUpdatesWebhook",
    "FindAllRunPayloadWebhook",
]


class FindallRunInput(TypedDict, total=False):
    entity_type: Required[str]
    """Type of the entity for the FindAll run."""

    generator: Required[Literal["base", "core", "pro", "preview"]]
    """Generator for the FindAll run."""

    match_conditions: Required[Iterable[FindallRunInputMatchCondition]]
    """List of match conditions for the FindAll run."""

    match_limit: Required[int]
    """Maximum number of matches to find for this FindAll run."""

    objective: Required[str]
    """Natural language objective of the FindAll run."""

    exclude_list: Optional[Iterable[FindallRunInputExcludeList]]
    """List of entity names/IDs to exclude from results."""

    metadata: Optional[Dict[str, Union[str, float, bool]]]
    """Metadata for the FindAll run."""

    webhook: Optional[WebhookParam]
    """Webhooks for Task Runs."""

    betas: Annotated[List[ParallelBetaParam], PropertyInfo(alias="parallel-beta")]
    """Optional header to specify the beta version(s) to enable."""


class FindallRunInputMatchCondition(TypedDict, total=False):
    description: Required[str]
    """Detailed description of the match condition.

    Include as much specific information as possible to help improve the quality and
    accuracy of Find All run results.
    """

    name: Required[str]
    """Name of the match condition."""


class FindallRunInputExcludeList(TypedDict, total=False):
    name: Required[str]
    """Name of the entity to exclude from results."""

    url: Required[str]
    """URL of the entity to exclude from results."""


class FindAllRunPayload(TypedDict, total=False):
    findall_spec: Required[FindAllRunPayloadFindallSpec]
    """Represents a view in the database with a title."""

    processor: Required[Literal["lite", "base", "pro", "preview"]]

    candidates: SequenceNotStr[str]

    metadata: Dict[str, Union[str, float, bool]]

    result_limit: int

    updates_webhook: Optional[FindAllRunPayloadUpdatesWebhook]
    """FindAll Webhooks for Clay."""

    webhook: Optional[FindAllRunPayloadWebhook]
    """Webhooks for FindAll."""

    betas: Annotated[List[ParallelBetaParam], PropertyInfo(alias="parallel-beta")]
    """Optional header to specify the beta version(s) to enable."""


class FindAllRunPayloadFindallSpecColumn(TypedDict, total=False):
    description: Required[str]
    """The description of the column"""

    name: Required[str]
    """The name of the column"""

    order_direction: Optional[Literal["ASC", "DESC"]]
    """Direction for ordering results."""

    type: Literal["enrichment", "constraint", "order_by"]
    """Types of columns in a view."""


class FindAllRunPayloadFindallSpec(TypedDict, total=False):
    columns: Required[Iterable[FindAllRunPayloadFindallSpecColumn]]
    """The columns of the view"""

    name: Required[str]
    """The name of the view"""

    query: Required[str]
    """The query of the findall"""

    title: Required[str]
    """The title of the findall query"""


class FindAllRunPayloadUpdatesWebhook(TypedDict, total=False):
    url: Required[str]
    """URL for the webhook."""

    event_types: List[Literal["findall.result"]]
    """The type of event that triggered the webhook."""

    secret: Optional[str]
    """Secret for HMAC signature of the webhook.

    If not provided, webhook signature is generated from the secret created when the
    domain is registered.
    """


class FindAllRunPayloadWebhook(TypedDict, total=False):
    url: Required[str]
    """URL for the webhook."""

    event_types: List[
        Literal[
            "findall.entity.created",
            "findall.entity.discarded",
            "findall.entity.completed",
            "findall.run.completed",
            "findall.run.canceled",
        ]
    ]
    """The type of event that triggered the webhook."""

    secret: Optional[str]
    """Secret for HMAC signature of the webhook.

    If not provided, webhook signature is generated from the secret created when the
    domain is registered.
    """


FindallCreateParams: TypeAlias = Union[FindallRunInput, FindAllRunPayload]
