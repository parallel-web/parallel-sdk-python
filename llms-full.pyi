"""
Parallel SDK - Complete Usage Stub File
This file demonstrates the complete API surface and usage patterns for the Parallel SDK.
"""

from __future__ import annotations

import httpx
from datetime import datetime
from typing import Any, Dict, List, Optional, Union, Type, TypeVar, Generic, Literal, overload
from typing_extensions import TypedDict, Annotated

# Core client imports
from parallel import (
    Parallel,
    AsyncParallel,
    Client,
    AsyncClient,
    BaseModel,
    NOT_GIVEN,
    NotGiven,
    Timeout,
    RequestOptions,
    APIResponse,
    AsyncAPIResponse,
    ParallelError,
    APIStatusError,
)

# Type definitions for better understanding
T = TypeVar('T', bound=BaseModel)
OutputT = TypeVar('OutputT')

# Schema definitions for task specifications
class JsonSchemaParam(TypedDict, total=False):
    type: Literal["json"]
    json_schema: Dict[str, Any]

class TextSchemaParam(TypedDict, total=False):
    type: Literal["text"] 
    description: str

class AutoSchemaParam(TypedDict, total=False):
    type: Literal["auto"]

# Union types for schema parameters
InputSchema = Union[str, JsonSchemaParam, TextSchemaParam, AutoSchemaParam]
OutputSchema = Union[str, JsonSchemaParam, TextSchemaParam, AutoSchemaParam]

# Task specification parameter
class TaskSpecParam(TypedDict, total=False):
    input_schema: InputSchema
    output_schema: OutputSchema

# Core response models
class TaskRunJsonOutput(BaseModel):
    content: str
    type: Literal["json"]

class TaskRunTextOutput(BaseModel):
    content: str
    type: Literal["text"]

TaskRunOutput = Union[TaskRunJsonOutput, TaskRunTextOutput]

class TaskRunResult(BaseModel):
    id: str
    status: Literal["completed", "failed", "running", "pending"]
    output: TaskRunOutput
    created_at: datetime
    completed_at: Optional[datetime]
    error: Optional[str]

class ParsedTaskRunResult(BaseModel, Generic[OutputT]):
    """Parsed task run result with strongly typed output"""
    id: str
    status: Literal["completed", "failed", "running", "pending"] 
    output: ParsedOutput[OutputT]
    created_at: datetime
    completed_at: Optional[datetime]
    error: Optional[str]

class ParsedOutput(BaseModel, Generic[OutputT]):
    content: str
    type: str
    parsed: OutputT

# Request parameter types
class TaskRunCreateParams(TypedDict, total=False):
    input: Union[str, Dict[str, Any]]
    task_spec: TaskSpecParam
    timeout: Union[float, Timeout, None, NotGiven]

# Beta types for advanced features
class BetaRunInput(BaseModel):
    input: Union[str, Dict[str, Any]]
    task_spec: Optional[TaskSpecParam]

class TaskGroup(BaseModel):
    id: str
    name: Optional[str]
    status: str
    created_at: datetime

class TaskGroupCreateParams(TypedDict, total=False):
    name: str
    runs: List[BetaRunInput]

class TaskRunEvent(BaseModel):
    type: str
    data: Dict[str, Any]
    timestamp: datetime

class TaskRunEventsResponse(BaseModel):
    events: List[TaskRunEvent]
    has_more: bool

# Main client class definitions
class Parallel:
    """
    Synchronous Parallel client for AI task execution.
    
    Example usage:
    ```python
    import parallel
    
    client = parallel.Parallel(api_key="your-api-key")
    
    # Simple text completion
    result = client.task_run.create(
        input="Write a haiku about coding",
        timeout=30.0
    )
    
    # With structured output
    class CodeReview(parallel.BaseModel):
        rating: int
        comments: List[str]
        
    result = client.task_run.create(
        input="Review this Python code: def hello(): print('hi')",
        output_format=CodeReview,
        timeout=60.0
    )
    ```
    """
    
    api_key: str
    task_run: TaskRunResource
    beta: BetaResource
    
    def __init__(
        self,
        *,
        api_key: Optional[str] = None,
        base_url: Optional[Union[str, httpx.URL]] = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = 2,
        default_headers: Optional[Dict[str, str]] = None,
        default_query: Optional[Dict[str, Any]] = None,
        http_client: Optional[httpx.Client] = None,
        _strict_response_validation: bool = False,
    ) -> None: ...
    
    def copy(self, **kwargs: Any) -> Parallel: ...
    def close(self) -> None: ...
    def __enter__(self) -> Parallel: ...
    def __exit__(self, *args: Any) -> None: ...

class AsyncParallel:
    """
    Asynchronous Parallel client for AI task execution.
    
    Example usage:
    ```python
    import parallel
    import asyncio
    
    async def main():
        client = parallel.AsyncParallel(api_key="your-api-key")
        
        # Simple async task
        result = await client.task_run.create(
            input="Generate a creative story",
            timeout=45.0
        )
        
        # Batch processing with task groups
        runs = [
            {"input": f"Analyze sentiment: {text}"}
            for text in ["Great product!", "Terrible service", "Okay experience"]
        ]
        
        group = await client.beta.task_group.create(
            name="sentiment-analysis-batch",
            runs=runs
        )
        
        await client.close()
    
    asyncio.run(main())
    ```
    """
    
    api_key: str 
    task_run: AsyncTaskRunResource
    beta: AsyncBetaResource
    
    def __init__(
        self,
        *,
        api_key: Optional[str] = None,
        base_url: Optional[Union[str, httpx.URL]] = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = 2,
        default_headers: Optional[Dict[str, str]] = None,
        default_query: Optional[Dict[str, Any]] = None,
        http_client: Optional[httpx.AsyncClient] = None,
        _strict_response_validation: bool = False,
    ) -> None: ...
    
    def copy(self, **kwargs: Any) -> AsyncParallel: ...
    async def close(self) -> None: ...
    async def __aenter__(self) -> AsyncParallel: ...
    async def __aexit__(self, *args: Any) -> None: ...

# Resource classes
class TaskRunResource:
    """
    Synchronous task run operations.
    
    Provides methods for creating, retrieving, and managing AI task executions.
    """
    
    def create(
        self,
        *,
        input: Union[str, Dict[str, Any]],
        output_format: Optional[Union[OutputSchema, Type[OutputT]]] = None,
        task_spec: Optional[TaskSpecParam] = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        extra_headers: Optional[Dict[str, str]] = None,
        extra_query: Optional[Dict[str, Any]] = None,
    ) -> Union[TaskRunResult, ParsedTaskRunResult[OutputT]]: ...
    
    @overload
    def create(
        self,
        *,
        input: Union[str, Dict[str, Any]],
        output_format: Type[OutputT],
        **kwargs: Any,
    ) -> ParsedTaskRunResult[OutputT]: ...
    
    @overload 
    def create(
        self,
        *,
        input: Union[str, Dict[str, Any]], 
        output_format: None = None,
        **kwargs: Any,
    ) -> TaskRunResult: ...
    
    def retrieve(
        self,
        run_id: str,
        *,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> TaskRunResult: ...
    
    def result(
        self,
        run_id: str,
        *,
        output_format: Optional[Union[OutputSchema, Type[OutputT]]] = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> Union[TaskRunResult, ParsedTaskRunResult[OutputT]]: ...

class AsyncTaskRunResource:
    """
    Asynchronous task run operations.
    
    All methods are async versions of TaskRunResource.
    """
    
    async def create(
        self,
        *,
        input: Union[str, Dict[str, Any]],
        output_format: Optional[Union[OutputSchema, Type[OutputT]]] = None,
        task_spec: Optional[TaskSpecParam] = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        extra_headers: Optional[Dict[str, str]] = None,
        extra_query: Optional[Dict[str, Any]] = None,
    ) -> Union[TaskRunResult, ParsedTaskRunResult[OutputT]]: ...
    
    async def retrieve(
        self,
        run_id: str,
        *,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> TaskRunResult: ...
    
    async def result(
        self,
        run_id: str,
        *,
        output_format: Optional[Union[OutputSchema, Type[OutputT]]] = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> Union[TaskRunResult, ParsedTaskRunResult[OutputT]]: ...

# Beta resources for advanced features
class BetaResource:
    """Beta features and experimental functionality."""
    task_run: BetaTaskRunResource
    task_group: TaskGroupResource

class AsyncBetaResource:
    """Async beta features and experimental functionality."""
    task_run: AsyncBetaTaskRunResource  
    task_group: AsyncTaskGroupResource

class TaskGroupResource:
    """
    Task group operations for batch processing.
    
    Example usage:
    ```python
    # Create a group of related tasks
    group = client.beta.task_group.create(
        name="data-processing-batch",
        runs=[
            {"input": "Process dataset A"},
            {"input": "Process dataset B"}, 
            {"input": "Process dataset C"},
        ]
    )
    
    # Monitor progress
    status = client.beta.task_group.retrieve(group.id)
    
    # Get all results
    results = client.beta.task_group.get_runs(group.id)
    ```
    """
    
    def create(
        self,
        *,
        runs: List[BetaRunInput],
        name: Optional[str] = None,
    ) -> TaskGroup: ...
    
    def retrieve(self, group_id: str) -> TaskGroup: ...
    
    def get_runs(
        self, 
        group_id: str,
        *,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
    ) -> List[TaskRunResult]: ...
    
    def add_runs(
        self,
        group_id: str,
        *,
        runs: List[BetaRunInput],
    ) -> TaskGroup: ...

class AsyncTaskGroupResource:
    """Async version of TaskGroupResource."""
    
    async def create(
        self,
        *,
        runs: List[BetaRunInput],
        name: Optional[str] = None,
    ) -> TaskGroup: ...
    
    async def retrieve(self, group_id: str) -> TaskGroup: ...
    
    async def get_runs(
        self,
        group_id: str, 
        *,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
    ) -> List[TaskRunResult]: ...
    
    async def add_runs(
        self,
        group_id: str,
        *,
        runs: List[BetaRunInput],
    ) -> TaskGroup: ...

class BetaTaskRunResource:
    """Beta task run features with advanced capabilities."""
    
    def events(
        self,
        run_id: str,
        *,
        since: Optional[str] = None,
        limit: Optional[int] = None,
    ) -> TaskRunEventsResponse: ...

class AsyncBetaTaskRunResource:
    """Async beta task run features."""
    
    async def events(
        self,
        run_id: str,
        *,
        since: Optional[str] = None,
        limit: Optional[int] = None,
    ) -> TaskRunEventsResponse: ...

# Client aliases for convenience
Client = Parallel
AsyncClient = AsyncParallel

# Usage examples and patterns
class UsageExamples:
    """
    Complete usage examples for the Parallel SDK.
    
    Basic Usage:
    ```python
    import parallel
    
    # Initialize client
    client = parallel.Parallel(api_key="your-api-key")
    
    # Simple text generation
    result = client.task_run.create(
        input="Write a Python function to calculate fibonacci numbers"
    )
    print(result.output.content)
    ```
    
    Structured Output:
    ```python
    class CodeAnalysis(parallel.BaseModel):
        complexity: int
        suggestions: List[str]
        bugs: List[str]
        
    result = client.task_run.create(
        input="def buggy_func(x): return x / 0",
        output_format=CodeAnalysis
    )
    
    analysis = result.output.parsed  # Type: CodeAnalysis
    print(f"Complexity: {analysis.complexity}")
    ```
    
    Batch Processing:
    ```python
    # Process multiple items
    inputs = ["Translate to French: Hello", "Translate to French: Goodbye"]
    runs = [{"input": text} for text in inputs]
    
    group = client.beta.task_group.create(
        name="translation-batch",
        runs=runs
    )
    
    # Wait for completion and get results
    results = client.beta.task_group.get_runs(group.id)
    ```
    
    Error Handling:
    ```python
    try:
        result = client.task_run.create(
            input="Complex task",
            timeout=30.0
        )
    except parallel.APITimeoutError:
        print("Task timed out")
    except parallel.APIStatusError as e:
        print(f"API error: {e.status_code} - {e.message}")
    except parallel.ParallelError as e:
        print(f"SDK error: {e}")
    ```
    
    Async Usage:
    ```python
    import asyncio
    
    async def process_tasks():
        async with parallel.AsyncParallel(api_key="your-api-key") as client:
            tasks = [
                client.task_run.create(input=f"Task {i}")
                for i in range(10)
            ]
            results = await asyncio.gather(*tasks)
            return results
    
    results = asyncio.run(process_tasks())
    ```
    
    Custom Schemas:
    ```python
    # Define custom JSON schema
    custom_schema = {
        "type": "json",
        "json_schema": {
            "type": "object",
            "properties": {
                "summary": {"type": "string"},
                "score": {"type": "number", "minimum": 0, "maximum": 10}
            },
            "required": ["summary", "score"],
            "additionalProperties": False
        }
    }
    
    result = client.task_run.create(
        input="Analyze this text: 'Great product, highly recommend!'",
        task_spec={"output_schema": custom_schema}
    )
    ```
    """
    pass

# Environment configuration
class Config:
    """
    SDK configuration options.
    
    Environment Variables:
    - PARALLEL_API_KEY: Default API key
    - PARALLEL_BASE_URL: Custom API base URL  
    - PARALLEL_LOG: Logging level ("debug" or "info")
    """
    pass