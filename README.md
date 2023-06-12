# Python TikTok Events API

This library is an unoffical Python wrapper arround the TikTok Events API, allowing for easy interaction with the API:
- Pydantic types are used to validate the data to be sent to TikTok.
- Customer identifiable information is hashed using SHA256 before being sent to the TikTok API.
- Events can be sent one at a time or in batches.

The TikTok Events API allows advertisers to share the actions customers take on their websites and offiline directly with TikTok. This allows advertisers to measure the effectiveness of their TikTok campaigns and optimize their ad spend.

Please reference the TikTok Events API documentation for more information on the API and the data it accepts and requires: https://ads.tiktok.com/marketing_api/docs?id=1741601162187777.

TikTok API uses custom return error codes. Reference [this TikTok Events API documentation](https://ads.tiktok.com/marketing_api/docs?id=1737172488964097) for more information on the error codes.
## Disclaimer
This library is in beta.
Feedback and contributions are welcome.

## Installing
You can install pytt_events_api using pip:
``` bash
pip install pytt-events-api
```

## Quick Start Guide
Here's a quick guide on how to use the library to send events to TikTok.
### Authentication
The only thing you need to do to authenticate with TikTok Events API is to set the environment variables listed below.
- `TIKTOK_ACESS_TOKEN`: Events API access token - `Required`
- `TIKTOK_PIXEL_ID`: The ID of the pixel  - `Required`
- `TIKTOK_API_VERSION`:  The API version to use, defaults to `v1.3`.
- `TIKTOK_TEST_EVENT_CODE`: Used so events can be tested without affecting the pixel's data. You may find the test event code in the events manager under the "Test Events" tab.

You can find the values for these variables in the TikTok Events Manager.

The environment variables are loaded when the `TikTokAuth` class is initialized. If the environment variables are not found, the class will raise an exception.
### Importing the library and initializing the API
``` python
from pytt_events.auth import TikTokAuth
from pytt_events.tiktok_events_api import TikTokEventsApi
from pytt_events.event import Event
from pytt_events.properties import Properties
from pytt_events.context import Context, Ad, Page, User
from pytt_events.properties import ContentType
from pytt_events.properties import Content

api = TikTokEventsApi()
auth = TikTokAuth()
```

### Creating an event
``` python
context = Context(
    user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.109 Safari/537.36',
    ip='13.57.97.131',
    ad=Ad(callback='E.C.P.v3fQ2RHacdkfKfofPmlyuStIIHJ4Af1tKYxF9zz2c2PLx1Oaw15oHpcfl5AH' ), # ttclid
    page=Page(
        url='https://www.example.com',
        referrer='https://www.google.com'
    ),
    user=User(
        external_id='123456',
        email='test@test.com',
        phone_number='+5541998862934',
        ttp='94e2a4j9-h3ss-k2h5-98cc-c84a745mk098',
    ))
properties = Properties(
    currency='BRL', # ISO 4217
    value=1.00,
    description='mock description',
    query='mock query',
    status='mock status',
    contents=[Content(
        content_type=ContentType.PRODUCT,
        content_id='123456789',
        content_name='mock content name',
        content_category='mock content category',
        price=1.00,
        quantity=1
    )]
)
event = Event (
    pixel_code=auth.TIKTOK_PIXEL_ID,
    test_event_code=auth.TIKTOK_TEST_EVENT_CODE,
    event='ViewContent',
    event_id='123456789',
    timestamp='2023-02-01T00:00:00-03:00', # str or datetime object
    context=context,
    properties=properties
)
```

#### Errors in the Docs
[TikTok's documentation](https://ads.tiktok.com/marketing_api/docs?id=1741601162187777) says that content_type should be a parameter of the Properties object, but it actually is a parameter of the Content object.

### Sending an event
``` python
response = api.post_event(
    event=event,
    auth=auth
)
```

### Sending events in bulk
``` python
events = []
response = api.post_events_in_bulk(events=events, auth=auth)
```




