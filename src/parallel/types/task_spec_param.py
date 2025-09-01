# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import TypeVar, Required, TypeAlias, TypedDict, NotRequired

from pydantic import BaseModel

from .auto_schema_param import AutoSchemaParam
from .json_schema_param import JsonSchemaParam
from .text_schema_param import TextSchemaParam

__all__ = ["TaskSpecParam", "OutputSchema", "InputSchema"]

OutputSchema: TypeAlias = Union[JsonSchemaParam, TextSchemaParam, AutoSchemaParam, str]

InputSchema: TypeAlias = Union[str, JsonSchemaParam, TextSchemaParam]

OutputT = TypeVar("OutputT", bound=BaseModel)


class TaskSpecParam(TypedDict, total=False):
    output_schema: Required[OutputSchema]
    """JSON schema or text fully describing the desired output from the task.

    Descriptions of output fields will determine the form and content of the
    response. A bare string is equivalent to a text schema with the same
    description.
    """

    input_schema: NotRequired[Optional[InputSchema]]
    """Optional JSON schema or text description of expected input to the task.

    A bare string is equivalent to a text schema with the same description.
    """
