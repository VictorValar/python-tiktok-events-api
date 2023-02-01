# Python TikTok Events API

The TikTok Events API allows advertisers to share the actions customers take on their websites and offiline directly with TikTok. This allows advertisers to measure the effectiveness of their TikTok campaigns and optimize their ad spend.

This library is an unoffical Python wrapper arround the TikTok Events API, allowing for easy interaction with the API:
- Pydantic types are used to validate the data to be sent to TikTok.
- Customer identifiable information is hashed using SHA256 before being sent to the TikTok API.
- Events can be sent one at a time or in batches.

Please reference the TikTok Events API documentation for more information on the API and the data it accepts and requires: https://ads.tiktok.com/marketing_api/docs?id=1741601162187777.

## Installing
You can install pytt_events_api by using:
``` bash
pip install pytt_events_api
```

## Getting Started
### Authentication
The only thing you need to do to authenticate with TikTok Events API is to set the environment variables listed below.
- `TIKTOK_ACESS_TOKEN`: Events API access token - `Required`
- `TIKTOK_PIXEL_ID`: The ID of the pixel  - `Required`
- `TIKTOK_API_VERSION`:  The API version to use, defaults to `v1.3`.
- `TIKTOK_TEST_EVENT_CODE`: Used so events can be tested without affecting the pixel's data. You may find the test event code in the events manager under the "Test Events" tab.

You can find the values for these variables in the TikTok Events Manager.

The environment variables are loaded when the `TikTokAuth` class is initialized. If the environment variables are not found, the class will raise an exception.
### Importing the library
``` python
from pytt_events_api import TikTokEventsAPI, SupportedEvents, \
Event, Context, Properties, Content, ContentType

api = TikTokEventsApi()
auth = TikTokAuth()
```
### Sending an event
``` python

response = api.post_event(
    event=event,
    auth=auth
)
```



### Sending events in bulk
``` python
response = api.post_events_in_bulk(events=events, auth=auth)
```
### Creating an event
``` python
#todo
```

## Examples


## Classes
### Event
The main class in this code is the `Event` class, which defines the structure of a TikTok event and the methods associated with it.

The `Event` class uses the `BaseModel` from the `pydantic` library to validate the data. The `normalize_data` method modifies the `Context` object to hash identifiable data for privacy purposes before returning the entire event as a dictionary.

#### Fields
- `pixel_code`: A string that represents the pixel code for the event. The field is stripped of whitespaces and must have a minimum length of 1.
- `test_event_code`: An optional string that represents the test event code. The field is stripped of whitespaces.
- `event`: A `SupportedEvents` object that represents the type of event.
- `event_id`: An optional string that represents the event ID. The field is stripped of whitespaces and must have a minimum length of 1.
- `timestamp`: A `datetime` object that represents the event's timestamp in ISO 8601 format.
- `context`: A `Context` object that provides additional information about the event such as the circumstances when the event was triggered and user information.
- `properties`: An optional `Properties` object that provides additional properties for the event like the value, currency and items added to cart/purchased.

#### Methods
- `normalize_data`: This method normalizes the data to be sent to the TikTok API. It also hashes identifiable data (such as email and phone number) using SHA256. The method returns a dictionary that contains the normalized data.



