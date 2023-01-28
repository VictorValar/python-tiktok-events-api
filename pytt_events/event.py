'''
Python wrapper for the TikTok Events API
https://ads.tiktok.com/marketing_api/docs?id=1705001902887214
Author: @ValarVictor
'''

from pydantic import BaseModel
from typing import Optional, List, Dict, Any
from pytt_events.supported_events import SupportedEvents
from pytt_events.auth import Auth
from pytt_events.context import Context


# TikTok events
class Event(BaseModel):
    pixel_code: str
    event: SupportedEvents
    event_id: Optional[str]
    timestamp: Optional[str] # ISO 8601 format
    context: Context
    properties: Optional[dict]


