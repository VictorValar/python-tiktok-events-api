# Tests for the Event class
from pytt_events.properties import Properties, ContentType, Content
from pytt_events.context import Context, Ad, Page, User
import pytest
from pydantic import ValidationError

def test_ad_instance(ad):
    assert isinstance(ad, Ad)
    assert ad.callback == ''


def test_page_instance(page):
    assert isinstance(page, Page)
    assert page.url == 'https://www.example.com'
    assert page.referrer == 'https://www.google.com'

def test_user_instance(user):
    assert isinstance(user, User)
    assert user.external_id == '123456'
    assert user.phone_number == '+5541999999999'
    assert user.ttp == '94e2a4j9-h3j5-k2h5-98cc-c84a745mk098'

def test_context_instance(ad, page, user):
    context = Context(
        user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.109 Safari/537.36',
        ip='13.57.97.131',
        ad=ad,  # ttclid
        page=page,
        user=user
    )

    assert context.user.external_id == '123456'
    assert context.page.url == 'https://www.example.com'
    assert context.ad.callback == ''
    assert context.page.referrer == 'https://www.google.com'

def test_content_instance():
    content = Content(
        content_id='12345',
        quantity=1,
        price=1.00,
        content_category='test content category',
        content_name='test content name'
    )

    assert content.content_id == '12345'
    assert content.quantity == 1
    assert content.price == 1.00
    assert content.content_category == 'test content category'
    assert content.content_name == 'test content name'

def test_wrong_content_types_raises_excp():
     with pytest.raises(ValidationError):
        Content(
            content_id='12345',
            quantity='1',
            price='1,00',
            content_category='test content category',
            content_name=111,
            content_type=222
        )


def test_properties_instance(contents):
    properties = Properties(
        currency='BRL',  # ISO 4217
        value=3.00,
        content_type=ContentType.PRODUCT,
        description='test description',
        query='test query',
        status='test status',
        contents=contents
    )

    assert properties.currency == "BRL"
    assert properties.contents[0].price == 1
    assert properties.contents[1].price == 2

def test_valid_event(auth, ad, page, user, contents):
    from pytt_events.event import Event, SupportedEvents

    context = Context(
        user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.109 Safari/537.36',
        ip='13.57.97.131',
        ad=ad,  # ttclid
        page=page,
        user=user
    )

    properties = Properties(
        currency='BRL',  # ISO 4217
        value=3.00,
        content_type=ContentType.PRODUCT,
        description='test description',
        query='test query',
        status='test status',
        contents=contents
    )

    event = Event(
        pixel_code=auth.TIKTOK_PIXEL_ID,
        test_event_code=auth.TIKTOK_TEST_EVENT_CODE,
        event=SupportedEvents.VIEW_CONTENT,
        event_id='123456789',
        timestamp="2023-06-09 13:37:26-03:00",
        context=context,
        properties=properties
    )

    assert event.context.user_agent == 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.109 Safari/537.36'
    assert str(event.context.ip) == '13.57.97.131'
    assert event.context.ad.callback == ''
    assert event.context.page.url == 'https://www.example.com'
    assert event.context.page.referrer == 'https://www.google.com'
    assert event.context.user.email == 'test@test.com'
    assert event.properties.currency == 'BRL'
    assert event.properties.value == 3.00
    assert event.properties.description == 'test description'
    assert event.properties.query == 'test query'
    assert event.properties.status == 'test status'
    assert event.event.value == 'ViewContent'
    assert event.event_id == '123456789'
    assert event.context.page.url == 'https://www.example.com'
    assert event.context.page.referrer == 'https://www.google.com'
    assert event.context.user.phone_number == '+5541999999999'
    assert event.context.user.ttp == '94e2a4j9-h3j5-k2h5-98cc-c84a745mk098'
    assert event.context.user.external_id == '123456'


