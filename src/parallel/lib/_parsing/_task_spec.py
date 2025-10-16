from __future__ import annotations

from typing import Type, Union
from typing_extensions import TypeGuard

import pydantic

from ..._types import Omit
from ..._utils import is_str, is_dict, is_given
from .._pydantic import to_json_schema, is_basemodel_type
from ...types.task_spec_param import (
    OutputT,
    InputSchema,
    OutputSchema,
    TaskSpecParam,
)
from ...types.json_schema_param import JsonSchemaParam
from ...types.text_schema_param import TextSchemaParam


def is_json_schema_param(schema: object) -> TypeGuard[JsonSchemaParam]:
    """Check if a schema is a JsonSchemaParam."""
    if not is_dict(schema):
        return False

    if not set(schema.keys()).issubset(set(JsonSchemaParam.__annotations__.keys())):
        return False

    if not schema.get("type") == "json":
        return False

    return True


def is_text_schema_param(schema: object) -> TypeGuard[TextSchemaParam]:
    """Check if a schema is a TextSchemaParam."""
    if not is_dict(schema):
        return False

    if not set(TextSchemaParam.__annotations__.keys()) == set(schema.keys()):
        return False

    if not schema.get("type") == "text":
        return False

    return is_str(schema.get("description"))


def _is_schema_param(schema: object) -> TypeGuard[OutputSchema | InputSchema]:
    """Check if a schema is an OutputSchema or InputSchema."""
    if is_str(schema):
        return True
    return is_json_schema_param(schema) or is_text_schema_param(schema)


def is_output_schema_param(output_schema: object) -> TypeGuard[OutputSchema]:
    """Check if a schema is an OutputSchema."""
    return _is_schema_param(output_schema)


def is_input_schema_param(input_schema: object) -> TypeGuard[InputSchema]:
    """Check if a schema is an InputSchema."""
    return _is_schema_param(input_schema)


def _to_json_schema_param(output_format: Type[pydantic.BaseModel]) -> JsonSchemaParam:
    """Convert a pydantic basemodel to a JsonSchemaParam."""
    return {"json_schema": to_json_schema(output_format), "type": "json"}


def _generate_output_schema(output_format: OutputSchema | Type[OutputT]) -> OutputSchema:
    """Generate an OutputSchema from an OutputSchema or a generic output type."""
    if is_output_schema_param(output_format):
        return output_format

    if is_basemodel_type(output_format):
        json_schema_param = _to_json_schema_param(output_format)
        return json_schema_param

    raise TypeError(f"Invalid output_type. Type: {type(output_format)}")


def build_task_spec_param(
    output_format: OutputSchema | Type[OutputT] | Omit | None,
    _: Union[str, object],  # placeholder for input
) -> TaskSpecParam | Omit:
    """Build a TaskSpecParam from an OutputSchema or Type[OutputT] if provided."""
    if not is_given(output_format) or output_format is None:
        return Omit()

    # output format has type OutputSchema | Type[OutputT] here
    output_schema = _generate_output_schema(output_format)  # type: ignore[arg-type]
    return TaskSpecParam(output_schema=output_schema)
