from __future__ import annotations

import inspect
from typing import Any
from typing_extensions import TypeGuard

import pydantic

from .._compat import PYDANTIC_V1, model_json_schema


def to_json_schema(
    model_type: type[pydantic.BaseModel] | pydantic.TypeAdapter[Any],
) -> dict[str, Any]:
    """Convert a Pydantic model/type adapter to a JSON schema."""
    if is_basemodel_type(model_type):
        schema = model_json_schema(model_type)
    elif isinstance(model_type, pydantic.TypeAdapter):
        if PYDANTIC_V1:
            raise TypeError(f"TypeAdapters are not supported with Pydantic v1 - {model_type}")
        schema = model_type.json_schema()
    else:
        raise TypeError(f"Unsupported type: {model_type}")

    # modify the schema to make it compatible with the API format
    schema["additionalProperties"] = False
    return schema


def is_basemodel_type(model_type: object) -> TypeGuard[type[pydantic.BaseModel]]:
    """Check if a type is a Pydantic BaseModel to avoid using type: ignore."""
    return inspect.isclass(model_type) and issubclass(model_type, pydantic.BaseModel)
