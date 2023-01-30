from ..tiktok_events_api import TikTokEventsApi
from ..event import Event
from ..auth import Auth
from ..context import Context, Page, User, Ad
from ..properties import Properties
import json

def test_post_event():
    event_request = TikTokEventsApi()
    auth = Auth()
    pixel_code = auth.tiktok_pixel_id
    event_name = "ViewContent"
    event_id = '1234'
    timestamp = "2023-01-29 13:37:26-03:00"
    context = Context(
        user_agent='Chrome/87.0.4280.88 Safari/537.36 OPR/73.0.3856.344 (Edition Yx GX)',
        ip='186.212.33.108',
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
    event = Event(
        pixel_code=pixel_code,
        test_event_code=auth.tiktok_test_event_code,
        event=event_name,
        event_id=event_id,
        timestamp=timestamp,
        context=context,
        properties=properties
    )

    # print(event.json(indent=4, exclude_none=True))

    event_response = event_request.post_event(
        event=event,
        auth=auth
    )
    # print('Code:',event_response.json()['code'])
    # print('request_id:',event_response.json()['request_id'])
    # print('message:',event_response.json()['message'])
    # print(event_response.status_code, event_response.reason)

    json_response= event_response.json()
    assert json_response['code'] == 0

