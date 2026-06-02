# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel

__all__ = ["FindAllEntitySearchResponse", "Entity"]


class Entity(BaseModel):
    description: str
    """Descriptive text about the entity."""

    name: str
    """Entity name."""

    url: str
    """Canonical URL for the entity."""


class FindAllEntitySearchResponse(BaseModel):
    entities: List[Entity]
    """Ranked list of entities."""

    entity_set_id: str
    """Entity set request ID. Example: `entity_set_cad0a6d2dec046bd95ae900527d880e7`"""
