from pydantic import BaseModel
from typing import Optional, List, Dict, Any


class Ad(BaseModel):
    ttclid: str

class Page(BaseModel):
    url: str
    referrer: Optional[str]

class User(BaseModel):
    external_id: str
    email: str
    phone_number: str
    ttp: str

# Context object parameters
class Context(BaseModel):
    user_agent: str
    ip: str
    ad: Ad
    page: Page
    user: User
