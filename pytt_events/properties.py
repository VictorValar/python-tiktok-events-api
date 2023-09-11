from pydantic import (
    BaseModel,
    conlist,
    constr,
    PositiveFloat,
    PositiveInt,
    root_validator
)
from typing import Optional
from enum import Enum
from . import utils

class ContentType(str, Enum):
    """ Content type enum."""

    """
    For individual products.
    """
    PRODUCT = 'product'
    """
    For product groups (Items and variants).
    """
    PRODUCT_GROUP = 'product_group'

    def __str__(self):
        return self.value


class Content(BaseModel):
    """ A list of content objects that represent products.

    Attributes:
        content_id (str): [Required] Unique ID of the product or content.
        quantity (int): [Required] The quantity of the content.
        price (float): [Required] The price of the item.
        content_category (str): [Optional] The category of the content.
        content_name (str): [Optional] The name of the content.
    """

    content_id: Optional[constr(strip_whitespace=True, min_length=1)]
    quantity: PositiveInt
    price: PositiveFloat
    content_category: Optional[constr(min_length=1)]
    content_name: Optional[constr(min_length=1)]


class Properties(BaseModel):
    """ Properties associated with the event.

    Attributes:
        currency (str): [Optional] ISO 4217 currency code.
        value (float): [Optional] The value of the event.
        description (str): [Optional] The description of the event.
        query (str): [Optional] The query of the event.
        status (str): [Optional] The status of the event.
        content_type (ContentType): [Optional] The content type of the event.
        contents (list[Content]): [Optional] A list of content objects that represent products.
    """
    currency: Optional[constr(
        strip_whitespace=True, min_length=3, max_length=3
    )]
    value: Optional[PositiveFloat]
    description: Optional[constr(min_length=1)]
    query: Optional[constr(min_length=1)]
    status: Optional[constr(min_length=1)]
    content_type: Optional[ContentType]
    contents: Optional[conlist(
        item_type=Content, unique_items=True, min_items=1
    )]

    @root_validator(pre=True)
    @classmethod
    def validate_user(cls, values):
        if not any(values.values()):
            raise utils.PropertiesFormatError(
                value=values,
                message='Properties must have at least one attribute.'
            )
        return values


