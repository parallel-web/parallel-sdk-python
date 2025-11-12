# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel
from .findall_run import FindallRun

__all__ = [
    "FindallRetrieveResponse",
    "FindAllPollResponse",
    "FindAllPollResponseBillingMetrics",
    "FindAllPollResponseCandidate",
    "FindAllPollResponseEnrichment",
    "FindAllPollResponseFilter",
    "FindAllPollResponseResult",
    "FindAllPollResponseResultEnrichmentResult",
    "FindAllPollResponseResultEnrichmentResultEnhancedCitation",
    "FindAllPollResponseResultFilterResult",
    "FindAllPollResponseResultFilterResultEnhancedCitation",
    "FindAllPollResponseSpec",
    "FindAllPollResponseSpecColumn",
    "FindAllPollResponseStep",
    "FindAllPollResponseEnrichmentRecommendation",
]


class FindAllPollResponseBillingMetrics(BaseModel):
    enrichment_cells: int
    """Number of enrichment cells processed"""

    rows_processed: int
    """Number of rows processed"""

    cost_mode: Optional[Literal["lite", "base", "pro", "preview"]] = None


class FindAllPollResponseCandidate(BaseModel):
    entity_id: str
    """Unique entity identifier"""

    name: str
    """Entity name"""


class FindAllPollResponseEnrichment(BaseModel):
    description: str
    """Human-readable description of the column"""

    name: str
    """Column identifier"""

    type: str
    """Column type ('enrichment' or 'filter')"""

    status: Optional[str] = None
    """Status of the column ('running', 'done', 'failed')"""


class FindAllPollResponseFilter(BaseModel):
    description: str
    """Human-readable description of the column"""

    name: str
    """Column identifier"""

    type: str
    """Column type ('enrichment' or 'filter')"""

    status: Optional[str] = None
    """Status of the column ('running', 'done', 'failed')"""


class FindAllPollResponseResultEnrichmentResultEnhancedCitation(BaseModel):
    url: str
    """Citation URL"""

    excerpts: Optional[List[str]] = None
    """List of relevant excerpts from the cited page"""

    title: Optional[str] = None
    """Title of the cited page"""


class FindAllPollResponseResultEnrichmentResult(BaseModel):
    key: str
    """Name of column"""

    value: str
    """Result of column"""

    citations: Optional[str] = None
    """Space separated list of citation urls"""

    confidence: Optional[str] = None
    """Confidence score (e.g. 'high', 'medium', 'low')"""

    enhanced_citations: Optional[List[FindAllPollResponseResultEnrichmentResultEnhancedCitation]] = None
    """List of enhanced citations with title and excerpts"""

    reasoning: Optional[str] = None
    """Reasoning behind the value"""


class FindAllPollResponseResultFilterResultEnhancedCitation(BaseModel):
    url: str
    """Citation URL"""

    excerpts: Optional[List[str]] = None
    """List of relevant excerpts from the cited page"""

    title: Optional[str] = None
    """Title of the cited page"""


class FindAllPollResponseResultFilterResult(BaseModel):
    key: str
    """Name of column"""

    value: str
    """Result of column"""

    citations: Optional[str] = None
    """Space separated list of citation urls"""

    confidence: Optional[str] = None
    """Confidence score (e.g. 'high', 'medium', 'low')"""

    enhanced_citations: Optional[List[FindAllPollResponseResultFilterResultEnhancedCitation]] = None
    """List of enhanced citations with title and excerpts"""

    reasoning: Optional[str] = None
    """Reasoning behind the value"""


class FindAllPollResponseResult(BaseModel):
    entity_id: str
    """Unique entity identifier"""

    name: str
    """Entity name"""

    description: Optional[str] = None
    """Entity description if available"""

    enrichment_results: Optional[List[FindAllPollResponseResultEnrichmentResult]] = None
    """List of enrichment results"""

    filter_results: Optional[List[FindAllPollResponseResultFilterResult]] = None
    """List of filter results"""

    score: Optional[float] = None
    """Confidence score (positive real number)"""

    url: Optional[str] = None
    """Entity URL if available"""


class FindAllPollResponseSpecColumn(BaseModel):
    description: str
    """Human-readable description of the column"""

    name: str
    """Column identifier"""

    type: str
    """Column type ('enrichment' or 'filter')"""

    status: Optional[str] = None
    """Status of the column ('running', 'done', 'failed')"""


class FindAllPollResponseSpec(BaseModel):
    columns: List[FindAllPollResponseSpecColumn]
    """List of columns in the view"""

    name: str
    """Name of the view"""


class FindAllPollResponseStep(BaseModel):
    description: str
    """Human-readable description of the step"""

    name: str
    """Step identifier"""

    status: str
    """Current status of the step"""


class FindAllPollResponseEnrichmentRecommendation(BaseModel):
    column_name: str
    """Recommended column name"""

    description: str
    """Description of the recommended enrichment"""

    recommendation_run_id: str
    """Run ID that generated this recommendation"""

    recommendation_task_id: str
    """Task ID that generated this recommendation"""


class FindAllPollResponse(BaseModel):
    billing_metrics: FindAllPollResponseBillingMetrics
    """Billing metrics for the run."""

    candidates: List[FindAllPollResponseCandidate]
    """List of candidates being processed"""

    enrichments: List[FindAllPollResponseEnrichment]
    """List of enrichments derived from the query"""

    filters: List[FindAllPollResponseFilter]
    """List of filters derived from the query"""

    is_active: bool
    """True if the run is still processing candidates"""

    max_results: int
    """Max results processed for the run"""

    query: str
    """Query for the run"""

    results: List[FindAllPollResponseResult]
    """List of entities which are fully processed"""

    spec: FindAllPollResponseSpec
    """View model for the run."""

    status: str
    """Derived overall status (e.g., 'running', 'completed', 'failed')"""

    steps: List[FindAllPollResponseStep]
    """List of processing steps undertaken with their status"""

    title: str
    """Title of the run"""

    are_enrichments_active: Optional[bool] = None
    """True if enrichments are still being processed"""

    created_at: Optional[str] = None
    """Timestamp of the request"""

    enrichment_recommendations: Optional[List[FindAllPollResponseEnrichmentRecommendation]] = None
    """List of recommended enrichments that could be added"""

    modified_at: Optional[str] = None
    """Timestamp of the last status update"""

    pages_considered: Optional[int] = None
    """Number of web pages considered for this entity"""

    pages_read: Optional[int] = None
    """Number of web pages read for this entity"""


FindallRetrieveResponse: TypeAlias = Union[FindallRun, FindAllPollResponse]
