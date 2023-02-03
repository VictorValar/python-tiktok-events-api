# Tests for the Event class
from pytt_events.properties import ContentType

def test_valid_event(event):

    assert event.pixel_code == 'CFAFTJJC77U9H3ERQ210'
    assert event.context.user_agent == 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.109 Safari/537.36'
    assert str(event.context.ip) == '13.57.97.131'
    assert event.context.ad.callback == 'E.C.P.v3fQ2RHacdksKfofPmlyuStIIHJ4Af1tKYxF9zz2c2PLx1Oaw15oHpcfl5AH'
    assert event.context.page.url == 'https://www.example.com'
    assert event.context.page.referrer == 'https://www.google.com'
    assert event.context.user.email == 'test@test.com'
    assert event.properties.currency == 'USD'
    assert event.properties.value == 1.00
    assert event.properties.description == 'test description'
    assert event.properties.contents == [{"content_id": "12345", "quantity": 1, "price": 1.00, "content_type": ContentType.PRODUCT, "content_name": "test content name", "content_category": "test content category"}]
    assert event.properties.query == 'test query'
    assert event.properties.status == 'test status'
    assert event.event.value == 'ViewContent'
    assert event.event_id == '1234'
    assert event.context.page.url == 'https://www.example.com'
    assert event.context.page.referrer == 'https://www.google.com'
    assert event.context.user.phone_number == '+5541998862934'
    assert event.context.user.ttp == '94e2a4j9-h3j5-k2h5-98cc-c84a745mk098'
    assert event.context.user.external_id == '123456'


