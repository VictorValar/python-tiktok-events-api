from pytest  import  fixture
from pytt_events.auth import TikTokAuth
from pytt_events.event import Event
from pytt_events.properties import Properties, ContentType, Content
from pytt_events.context import Context, Ad, Page, User
from pytt_events.supported_events import SupportedEvents
from typing import List

@fixture
def auth() -> TikTokAuth:
    yield TikTokAuth()

@fixture
def ad() -> Ad:
    yield Ad(callback='' )

@fixture
def page() -> Page:
    yield Page(
            url='https://www.example.com',
            referrer='https://www.google.com'
        )
@fixture
def user() -> User:
    yield User(
            external_id='123456',
            email='test@test.com',
            phone_number='+5541999999999',
            ttp='94e2a4j9-h3j5-k2h5-98cc-c84a745mk098',
        )

@fixture
def contents() -> List[Content]:

    items = [
        {
            "content_id": "12345",
            "quantity": 1,
            "price": 1.00,
            "content_name": "test content name",
            "content_category": "test content category"
        }, {
            "content_id": "123456",
            "quantity": 2,
            "price": 2.00,
            "content_name": "test second content name",
            "content_category": "test second content category"
        }
    ]

    contents = []
    for item in items:
        content = Content(
            content_id=item.get('content_id'),
            quantity=item.get('quantity'),
            price=item.get('price'),
            content_category=item.get('content_category'),
            content_name=item.get('content_name'),

        )
        contents.append(content)

    yield contents


@fixture
def event() -> Event:
    context = Context(
        user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.109 Safari/537.36',
        ip='13.57.97.131',
        ad=Ad(callback='E.C.P.152545565'),  # ttclid
        page=Page(
            url='https://www.example.com',
            referrer='https://www.google.com'
        ),
        user=User(
            external_id='123456',
            email='test@test.com',
            phone_number='+55 (41)9.9886-2934',
            ttp='94e2a4j9-h3j5-k2h5-98cc-c84a745mk098',
        ))
    properties = Properties(
        currency='BRL',  # ISO 4217
        value=1.00,
        content_type=ContentType.PRODUCT,
        description='test description',
        query='test query',
        status='test status',
        contents=[{"content_id": "12345", "quantity": 1, "price": 1.00, "content_name": "test content name", "content_category": "test content category"}]

    )
    auth = TikTokAuth()

    yield Event(
        pixel_code=auth.TIKTOK_PIXEL_ID,
        test_event_code=auth.TIKTOK_TEST_EVENT_CODE,
        event=SupportedEvents.VIEW_CONTENT,
        event_id='123456789',
        timestamp="2023-06-09 13:37:26-03:00",  # ISO 8601 format
        context=context,
        properties=properties
    )
# @fixture
# def simple_event():
#     """Event in which most of the fields are not present."""
#
#     context = Context(

