from pydantic import BaseModel
from typing import Optional
from pytt_events.contents import Contents

class Properties(BaseModel):
    currency: Optional[str]
    value: Optional[float]
    description: Optional[str]
    query: Optional[str]
    status: Optional[str]
    contents: Optional[dict]
