import pytest
from datetime import datetime
from pytt_events.supported_events import SupportedEvents
from pytt_events.auth import Auth
from pytt_events.event import Event
from pytt_events.properties import Properties
from pytt_events.context import Context, Ad, Page, User

def test_valid_event():
    auth = Auth()
    pixel_code = auth.tik_tok_pixel_id
    event_name = SupportedEvents.ViewContent
    event_id = '1234'
    timestamp = datetime.now().isoformat(timespec='seconds', sep='T'); print(timestamp)
    context = Context(
        user_agent='',
        ip='999.999.999.999',
        ad=Ad(callback='s.s.2.2sssss' ), # ttclid
        page=Page(
            url='https://www.example.com',
            referrer='https://www.google.com'
        ),
        user=User(
            external_id='123456',
            email='test@test.com',
            phone_number='+5541998862934',
            ttp='test_ttp',
        ))
    properties = Properties(
        currency='USD',
        value=1.00,
        description='test description',
        query='test query',
        status='test status',
        contents={"id": "12345", "quantity": 1, "item_price": 1.00}

    )
    event = Event(
        pixel_code=pixel_code,
        event=event_name,
        event_id=event_id,
        timestamp=timestamp,
        context=context,
        properties=properties
    )

    assert event.pixel_code == pixel_code
    assert event.event == event_name
    assert event.event_id == event_id
    assert event.timestamp == timestamp
    assert event.context == context
    assert event.properties == properties

    # assert context.page.url == 'https://www.example.com'
    # assert context.page.referrer == 'https://www.google.com'
    # assert context.user.external_id == '67890'
    # assert context.user.email == 'test@example.com'
    # assert context.user.phone_number == '555-555-5555'
    # assert context.user.ttp == 'test_ttp'





