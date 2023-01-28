import sys
sys.path.append('..')
import pytest
from datetime import datetime
from pytt_events.supported_events import SupportedEvents
from pytt_events.pytt import Auth
from pytt_events.event import Event


def test_valid_event():
    auth = Auth()
    pixel_code = auth.tik_tok_pixel_id
    event_name = SupportedEvents.ViewContent
    event_id = '1234'
    timestamp = datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
    context = {'user_id': '12345'}
    properties = {'content_id': '54321'}
    event = Event(pixel_code=pixel_code, event=event_name, event_id=event_id, timestamp=timestamp, context=context, properties=properties)
    assert event.pixel_code == pixel_code
    assert event.event == event_name
    assert event.event_id == event_id
    assert event.timestamp == timestamp
    assert event.context == context
    assert event.properties == properties




