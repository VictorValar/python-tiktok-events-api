'''
Python wrapper for the TikTok Events API
https://ads.tiktok.com/marketing_api/docs?id=1705001902887214
Author: @ValarVictor
'''

from pydantic import BaseModel, constr
from typing import Optional
from pytt_events.supported_events import SupportedEvents
from pytt_events.context import Context
from pytt_events.properties import Properties
import datetime
from hashlib import sha256

# TikTok event
class Event(BaseModel):
    pixel_code: constr(strip_whitespace=True, min_length=1)
    test_event_code: Optional[constr(strip_whitespace=True)]
    event: SupportedEvents
    event_id: Optional[constr(strip_whitespace=True, min_length=1)]
    timestamp: datetime.datetime # ISO 8601 format
    context: Context
    properties: Optional[Properties]

    def normalize_data(self) -> dict:
        """
        Normalize data to be sent to TikTok API
        Also hashes identifiable data with SHA256
        """
        event = self.dict()
        data = event.get('context').get('user')
        external_id = data.get('external_id')

        if external_id != None:
            external_id = data.get('external_id').lower().replace(' ', '')
            hashed_external_id = sha256(external_id.encode('utf-8')).hexdigest()
            data['external_id'] = hashed_external_id

        email = data.get('email').lower().replace(' ', '')
        hashed_email = sha256(email.encode('utf-8')).hexdigest() if email else None

        phone_number = data.get('phone_number')
        if phone_number != None:
            phone_number.replace(' ', '')
        hashed_phone_number = sha256(
            phone_number.encode('utf-8')
        ).hexdigest() if phone_number else None


        data['email'] = hashed_email
        data['phone_number'] = hashed_phone_number
        data['ttp'] = data.get('ttp').lower().replace(' ', '') if data.get('ttp') else None

        event['context']['user'] = data

        return event

