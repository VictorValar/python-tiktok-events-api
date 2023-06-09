from requests.exceptions import HTTPError
from .event import Event
from .auth import TikTokAuth
import requests
import logging
import json
from requests import Response

class TikTokEventsApi:
    '''
    TikTok Events API class for reporting web events to TikTok.
    Allows for reporting of web events one at a time or in bulk.
    '''

    def __init__(self):
        self.ROOT = 'https://business-api.tiktok.com/open_api/'

    def post_events_in_bulk(self, events: list, auth: TikTokAuth) -> Response:
        '''
        Reports web events in bulk, returning list of errors in the case of partial failures.
        /pixel/batch/
        '''
        EVENT_PATH = '/pixel/batch/'
        batch = []

        for event in events:
            batch.append(event.normalize_data())

        url = self.ROOT + auth.TIKTOK_API_VERSION + EVENT_PATH

        headers = {'Content-Type': 'application/json', 'Access-Token': auth.TIKTOK_ACCESS_TOKEN}

        payload = {
            "pixel_code": auth.TIKTOK_PIXEL_ID,
            "batch": batch
        }

        payload = json.dumps(payload, indent=4, sort_keys=True, default=str)

        try:
            response = requests.post(url, data=payload, headers=headers)
            json_response = response.json()

            # TikTok API uses custom error codes:
            # https://ads.tiktok.com/marketing_api/docs?id=1737172488964097
            if json_response['code'] != 0:
                raise HTTPError(json_response['code'], json_response['message'])
            else :
                logging.info('TikTok Event Response: ' + str(json_response))

                return response

        except Exception as exp_info:
            logging.error(exp_info)
            raise exp_info

    def post_event(self, event: Event, auth: TikTokAuth) -> Response:
        '''
        Reports a single web event.
        /pixel/track/
        '''

        EVENT_PATH = '/pixel/track/'

        url = self.ROOT + auth.TIKTOK_API_VERSION + EVENT_PATH

        payload = json.dumps(event.normalize_data(), indent=4, sort_keys=True, default=str)

        headers = {'Content-Type': 'application/json', 'Access-Token': auth.TIKTOK_ACCESS_TOKEN}

        try:
            response = requests.post(url, data=payload, headers=headers)
            json_response = response.json()

            # TikTok API uses custom error codes:
            # https://ads.tiktok.com/marketing_api/docs?id=1737172488964097
            if json_response['code'] != 0:
                raise HTTPError(json_response['code'], json_response['message'])
            else :
                logging.info('TikTok Event Response: ' + str(json_response))

                return response

        except Exception as exp_info:
            logging.error(exp_info)
            raise exp_info
