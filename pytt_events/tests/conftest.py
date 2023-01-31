from pytest  import  fixture
from pytt_events.auth import TikTokAuth
from pytt_events.event import Event
from pytt_events.properties import Properties
from pytt_events.context import Context, Ad, Page, User

@fixture
def auth() -> TikTokAuth:
    auth = TikTokAuth()
    yield auth

@fixture
def event() -> Event:
    event_name = "ViewContent"
    event_id = '1234'
    timestamp = "2023-01-29 13:37:26-03:00"
    context = Context(
        user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.109 Safari/537.36',
        ip='13.57.97.131',
        ad=Ad(callback='E.C.P.v3fQ2RHacdksKfofPmlyuStIIHJ4Af1tKYxF9zz2c2PLx1Oaw15oHpcfl5AH' ), # ttclid
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
        currency='USD', # ISO 4217
        value=1.00,
        description='test description',
        query='test query',
        status='test status',
        contents=[{"content_id": "12345", "quantity": 1, "price": 1.00, "content_type": "product", "content_name": "test content name", "content_category": "test content category"}]

    )
    auth = TikTokAuth()
    pixel_code = auth.tiktok_pixel_id
    event = Event(
        pixel_code=pixel_code,
        test_event_code=auth.tiktok_test_event_code,
        event=event_name,
        event_id=event_id,
        timestamp=timestamp,
        context=context,
        properties=properties
    )

    yield event

