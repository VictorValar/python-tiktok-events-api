'''
Python wrapper for the TikTok Events API
https://ads.tiktok.com/marketing_api/docs?id=1705001902887214
Author: @ValarVictor
'''
import sys
sys.path.append('..')

from pydantic import BaseModel
from typing import Optional, List, Dict, Any
from pytt_events.supported_events import SupportedEvents
from pytt_events.pytt import Auth


# TikTok events
class Event(BaseModel):
    pixel_code: str
    event: SupportedEvents
    event_id: Optional[str]
    timestamp: Optional[str]
    context: dict
    properties: Optional[dict]


