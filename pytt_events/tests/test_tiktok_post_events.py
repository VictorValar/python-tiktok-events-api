from pytt_events.tiktok_events_api import TikTokEventsApi
import logging

# Logging configuration
# logging.basicConfig(
#     level=logging.INFO,
#     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s' #,
#     # filename='pytt_events.log',
#     # filemode='w'
# )


def test_post_event(event, auth):

    response = TikTokEventsApi().post_event(
        event=event,
        auth=auth
    )

    logging.info(response.json())
    json_response = response.json()

    assert json_response['code'] == 0


def test_post_events_in_bulk(event, auth):

    api = TikTokEventsApi()

    events = [event, event, event]

    batch_response = api.post_events_in_bulk(
        events=events,
        auth=auth
    )

    logging.info(batch_response.json())
    json_response = batch_response.json()

    assert json_response['code'] == 0
