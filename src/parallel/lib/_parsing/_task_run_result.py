from __future__ import annotations

from typing import Any, Type, Union, Callable, Coroutine, cast

from .._time import timeout_retry_context
from ...types import TaskRunResult, ParsedTaskRunResult
from ..._types import Omit
from ..._utils import is_str, is_given
from ..._compat import model_parse, model_parse_json
from ..._models import construct_type_unchecked
from .._pydantic import is_basemodel_type
from ._task_spec import is_output_schema_param
from ...types.task_spec_param import OutputT, OutputSchema


def wait_for_result(
    *,
    run_id: str,
    deadline: float,
    callable: Callable[[str, float], TaskRunResult | ParsedTaskRunResult[OutputT]],
) -> TaskRunResult | ParsedTaskRunResult[OutputT]:
    """Wait for a task run to complete within the given timeout."""
    with timeout_retry_context(run_id, deadline):
        return callable(run_id, deadline)


async def wait_for_result_async(
    *,
    run_id: str,
    deadline: float,
    callable: Callable[[str, float], Coroutine[Any, Any, TaskRunResult | ParsedTaskRunResult[OutputT]]],
) -> TaskRunResult | ParsedTaskRunResult[OutputT]:
    """Wait for a task run to complete within the given timeout."""
    with timeout_retry_context(run_id, deadline):
        return await callable(run_id, deadline)


def task_run_result_parser(
    run_result: TaskRunResult, output_format: Union[OutputSchema, Type[OutputT]] | Omit | None
) -> TaskRunResult | ParsedTaskRunResult[OutputT]:
    """Parse a TaskRunResult object into a ParsedTaskRunResult based on output_format."""
    if not is_given(output_format) or output_format is None or is_output_schema_param(output_format):
        return run_result

    if is_basemodel_type(output_format):
        return _create_parsed_task_run_result(
            task_run_result=run_result,
            response_format=output_format,
        )

    raise TypeError(f"Invalid output_format. Expected pydantic.BaseModel, found: {type(output_format)}")


def _create_parsed_task_run_result(
    *,
    response_format: Type[OutputT],
    task_run_result: TaskRunResult,
) -> ParsedTaskRunResult[OutputT]:
    """Convert a TaskRunResult object into a ParsedTaskRunResult."""
    run_result_output = task_run_result.output
    return cast(
        ParsedTaskRunResult[OutputT],
        construct_type_unchecked(
            type_=cast(Any, ParsedTaskRunResult)[response_format],
            value={
                **task_run_result.to_dict(),
                "output": {
                    **task_run_result.output.to_dict(),
                    "parsed": maybe_parse_content(
                        response_format=response_format,
                        message=run_result_output.content,
                    ),
                },
            },
        ),
    )


def maybe_parse_content(
    *,
    response_format: type[OutputT],
    message: str | object,
) -> OutputT | None:
    """Parse message content based on the response format."""
    return _parse_content(response_format, message)


def _parse_content(response_format: type[OutputT], content: str | object) -> OutputT:
    """Parse content based on the response format.

    Only pydantic basemodels are currently supported.
    """
    if is_basemodel_type(response_format):
        if is_str(content):
            return cast(OutputT, model_parse_json(response_format, content))
        else:
            return cast(OutputT, model_parse(response_format, content))

    raise TypeError(f"Unable to automatically parse response format type {response_format}")
