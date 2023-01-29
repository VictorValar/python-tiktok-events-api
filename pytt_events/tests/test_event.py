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
    event_name = "ViewContent"
    event_id = '1234'
    timestamp = "2023-01-29 13:37:26-03:00"
    # print(f'Event time: {timestamp}')
    context = Context(
        user_agent='Chrome/87.0.4280.88 Safari/537.36 OPR/73.0.3856.344 (Edition Yx GX)',
        ip='186.212.33.108',
        ad=Ad(callback='x.x.x.xxxxxxxxxxxx' ), # ttclid
        page=Page(
            url='https://www.example.com',
            referrer='https://www.google.com'
        ),
        user=User(
            external_id='123456',
            email='test@test.com',
            phone_number='+5541998862934',
            ttp='94e2a4j9-h3j5-k2h5-98cc-c84a745mk098',
        ))
    properties = Properties(
        currency='USD',
        value=1.00,
        description='test description',
        query='test query',
        status='test status',
        contents=[{"content_id": "12345", "quantity": 1, "price": 1.00, "content_type": "product"}]

    )
    event = Event(
        pixel_code=pixel_code,
        event=event_name,
        event_id=event_id,
        timestamp=timestamp,
        context=context,
        properties=properties
    )

    print(event.json(indent=4))

    assert event.pixel_code == pixel_code
    assert event.event.value == event_name
    assert event.event_id == event_id
    assert str(event.timestamp) == timestamp
    assert event.context == context
    assert event.properties == properties
    assert context.page.url == 'https://www.example.com'
    assert context.page.referrer == 'https://www.google.com'
    assert context.user.external_id == '123456'
    assert context.user.email == 'test@test.com'
    assert context.user.phone_number == '+5541998862934'
    assert context.user.ttp == '94e2a4j9-h3j5-k2h5-98cc-c84a745mk098'

def test_invalid_event():
    pass





