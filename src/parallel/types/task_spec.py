# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import TypeAlias

from .._models import BaseModel
from .auto_schema import AutoSchema
from .json_schema import JsonSchema
from .text_schema import TextSchema

__all__ = ["TaskSpec", "OutputSchema", "InputSchema"]

OutputSchema: TypeAlias = Union[JsonSchema, TextSchema, AutoSchema, str]

InputSchema: TypeAlias = Union[str, JsonSchema, TextSchema, None]


class TaskSpec(BaseModel):
    output_schema: OutputSchema
    """JSON schema or text fully describing the desired output from the task.

    Descriptions of output fields will determine the form and content of the
    response. A bare string is equivalent to a text schema with the same
    description.
    """

    input_schema: Optional[InputSchema] = None
    """Optional JSON schema or text description of expected input to the task.

    A bare string is equivalent to a text schema with the same description.
    """
