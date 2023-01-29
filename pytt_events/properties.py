from pydantic import BaseModel, ValidationError, conlist
from typing import Optional
from enum import Enum

class ContentType(Enum):
    """
    For individual products.
    """
    PRODUCT = 'product'
    """
    For product groups (Items and variants).
    """
    PRODUCT_GROUP = 'product_group'

class Content(BaseModel):
    content_id: str
    quantity: int
    price: float
    content_type: ContentType
    content_category: Optional[str]
    content_name: Optional[str]

class Properties(BaseModel):
    currency: Optional[str]
    value: Optional[float]
    description: Optional[str]
    query: Optional[str]
    status: Optional[str]
    contents: Optional[conlist(
        item_type=Content, unique_items=True, min_items=1
    )]


