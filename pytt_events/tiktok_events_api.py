from requests.exceptions import HTTPError
from .event import Event
from .auth import TikTokAuth
import requests
import logging
import json
from requests import Response

class TikTokEventsApi:
    ROOT = 'https://business-api.tiktok.com/open_api/'

    def post_events_in_bulk(self, events: list, auth: TikTokAuth) -> Response:
        '''
        Reports web events in bulk, returning list of errors in the case of partial failures.
        /pixel/batch/
        '''
        EVENT_PATH = '/pixel/batch/'
        batch = []

        for event in events:
            batch.append(event.normalize_data())

        url = self.ROOT + auth.tiktok_api_version + EVENT_PATH

        headers = {'Content-Type': 'application/json', 'Access-Token': auth.tiktok_access_token}

        payload = {
            "pixel_code": auth.tiktok_pixel_id,
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

        url = self.ROOT + auth.tiktok_api_version + EVENT_PATH

        payload = json.dumps(event.normalize_data(), indent=4, sort_keys=True, default=str)

        headers = {'Content-Type': 'application/json', 'Access-Token': auth.tiktok_access_token}

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
