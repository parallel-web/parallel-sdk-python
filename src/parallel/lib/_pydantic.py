from __future__ import annotations

import inspect
from typing import Any
from typing_extensions import TypeGuard

import pydantic

from .._compat import PYDANTIC_V2, model_json_schema


def to_json_schema(
    model: type[pydantic.BaseModel] | pydantic.TypeAdapter[Any],
) -> dict[str, Any]:
    """Convert a Pydantic model/type adapter to a JSON schema."""
    if inspect.isclass(model) and is_basemodel_type(model):
        return model_json_schema(model)

    if PYDANTIC_V2 and isinstance(model, pydantic.TypeAdapter):
        return model.json_schema()

    raise TypeError(f"Non BaseModel types are only supported with Pydantic v2 - {model}")


def is_basemodel_type(typ: type | object) -> TypeGuard[type[pydantic.BaseModel]]:
    """Check if a type is a Pydantic BaseModel."""
    if not inspect.isclass(typ):
        return False
    return issubclass(typ, pydantic.BaseModel)
