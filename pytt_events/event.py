""" TikTok event model.
Python wrapper for the TikTok Events API
https://ads.tiktok.com/marketing_api/docs?id=1705001902887214
Author: @ValarVictor
"""

from pydantic import BaseModel, constr
from typing import Optional
from pytt_events.supported_events import SupportedEvents
from pytt_events.context import Context
from pytt_events.properties import Properties
import datetime
from hashlib import sha256


class Event(BaseModel):
    """ TikTok event model.

    Attributes:
        pixel_code (str):
            [Required] Pixel ID that can be found in Events Manager of the TikTok Ads Manager
        test_event_code (str):
            [Optional] TikTok test event code found in events manager
        event (SupportedEvents):
            [Required] Conversion event name.
        event_id (str):
            [Optional] Random Event ID
        timestamp (datetime):
            [Optional] ISO 8601 format. If not provided, the time when TikTok receives the event via the server will be used.
        context (Context):
            [Required] Information about the circumstances when the event was triggered, such as User data and conversion URL.
        properties (Properties):
            [Optional] Properties associated with the event like contents, value and description.
    """
    pixel_code: constr(strip_whitespace=True, min_length=1)
    test_event_code: Optional[constr(strip_whitespace=True)]
    event: SupportedEvents
    event_id: Optional[constr(strip_whitespace=True, min_length=1)]
    timestamp: Optional[datetime.datetime]
    context: Context
    properties: Optional[Properties]

    def normalize_data(self) -> dict:
        """ Normalizes data to be sent to TikTok API.

        Strings are transformed to lowercase, white spaces are removed. Also hashes identifiable data with SHA256

        Returns:
            dict: Normalized data dictionary
        """
        event = self.dict(exclude_none=True)
        data = event.get('context').get('user', {})
        external_id = data.get('external_id', None)
        email = data.get('email', None)
        phone_number = data.get('phone_number', None)
        ttp = data.get('ttp', None)

        if external_id is not None:
            external_id = data.get('external_id').replace(' ', '')
            hashed_external_id = sha256(external_id.encode('utf-8')).hexdigest()
            data['external_id'] = hashed_external_id

        if email:
            email = data.get('email').lower().replace(' ', '')
            hashed_email = sha256(email.encode('utf-8')).hexdigest()
            data['email'] = hashed_email

        if phone_number:
            # Phone number comes E.164 formatted from User class instance
            phone_number = data.get('phone_number')
            hashed_phone_number = sha256(
                phone_number.encode('utf-8')
            ).hexdigest()
            data['phone_number'] = hashed_phone_number

        if ttp:
            trimmed_ttp = data.get('ttp').replace(' ', '')
            data['ttp'] = trimmed_ttp

        event['context']['user'] = data

        return event

