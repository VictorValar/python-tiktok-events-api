'''
Python wrapper for the TikTok Events API
https://ads.tiktok.com/marketing_api/docs?id=1705001902887214
Author: @ValarVictor
'''

from pydantic import BaseModel, constr
from typing import Optional
from pytt_events.supported_events import SupportedEvents
from pytt_events.auth import Auth
from pytt_events.context import Context
from pytt_events.properties import Properties
import datetime

# TikTok event
class Event(BaseModel):
    pixel_code: constr(strip_whitespace=True, min_length=1)
    test_event_code: Optional[constr(strip_whitespace=True)]
    event: SupportedEvents
    event_id: Optional[constr(strip_whitespace=True, min_length=1)]
    timestamp: datetime.datetime # ISO 8601 format
    context: Context
    properties: Optional[Properties]

