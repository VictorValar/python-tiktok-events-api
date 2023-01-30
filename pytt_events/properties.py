from pydantic import (
    BaseModel,
    ValidationError,
    conlist,
    constr,
    PositiveFloat,
    PositiveInt
)
from typing import Optional
from enum import Enum

class ContentType(str, Enum):
    """
    For individual products.
    """
    PRODUCT = 'product'
    """
    For product groups (Items and variants).
    """
    PRODUCT_GROUP = 'product_group'

class Content(BaseModel):
    content_id: constr(strip_whitespace=True, min_length=1)
    quantity: PositiveInt
    price: PositiveFloat
    content_type: ContentType
    content_category: constr(min_length=1)
    content_name: constr(min_length=1)

class Properties(BaseModel):
    currency: Optional[constr(strip_whitespace=True, min_length=3, max_length=3)]
    value: Optional[PositiveFloat]
    description: Optional[constr(min_length=1)]
    query: Optional[constr(min_length=1)]
    status: Optional[constr(min_length=1)]
    contents: Optional[conlist(
        item_type=Content, unique_items=True, min_items=1
    )]


