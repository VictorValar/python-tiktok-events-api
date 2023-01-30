import pytest
from datetime import datetime
from pytt_events.supported_events import SupportedEvents
from pytt_events.auth import Auth
from pytt_events.event import Event
from pytt_events.properties import Properties
from pytt_events.context import Context, Ad, Page, User
from pydantic import ValidationError
from ..context import ContextFormatError

def test_valid_event():
    auth = Auth()
    pixel_code = auth.tiktok_pixel_id
    event_name = "ViewContent"
    event_id = '1234'
    timestamp = "2023-01-29 13:37:26-03:00"
    context = Context(
        user_agent='Mozilla/5.0 (platform; rv:geckoversion) Gecko/geckotrail Firefox/firefoxversion',
        ip='13.57.97.131',
        ad=Ad(callback='E.C.P.v3fQ2RHacdksKfofPmlyuStIIHJ4Af1tKYxF9zz2c2PLx1Oaw15oHpcfl5AH' ), # ttclid
        page=Page(
            url='https://www.example.com',
            referrer='https://www.google.com'
        ),
        user=User(
            external_id='123456_ssx',
            email='test@test.com',
            phone_number='+5541998552955',
            ttp='94e2a4j9-h3j5-k2h5-98cc-c84a745mk098',
        ))
    properties = Properties(
        currency='USD', # ISO 4217
        value=1.00,
        description='test description',
        query='test query',
        status='test status',
        contents=[{"content_id": "12345", "quantity": 1, "price": 1.00, "content_type": "product", "content_name": "test content name", "content_category": "test content category"}]

    )
    event = Event(
        pixel_code=pixel_code,
        event=event_name,
        event_id=event_id,
        timestamp=timestamp,
        test_event_code=auth.tiktok_test_event_code,
        context=context,
        properties=properties
    )

    # print(event.json(indent=4))
    print(event.timestamp)

    assert event.pixel_code == pixel_code
    assert event.event.value == event_name
    assert event.event_id == event_id
    assert str(event.timestamp) == timestamp
    assert event.context == context
    assert event.properties == properties
    assert context.page.url == 'https://www.example.com'
    assert context.page.referrer == 'https://www.google.com'
    assert context.user.external_id == '123456_ssx'
    assert context.user.email == 'test@test.com'
    assert context.user.phone_number == '+5541998552955'
    assert context.user.ttp == '94e2a4j9-h3j5-k2h5-98cc-c84a745mk098'


