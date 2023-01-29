from requests.exceptions import HTTPError
from . event import Event
from . auth import Auth
import requests
import logging

class EventWrapper(object):
    ROOT = 'https://business-api.tiktok.com/open_api/'
    EVENT_PATH = '/pixel/track/'

    def post_event(self, event: Event, auth: Auth) -> str:

        url = self.ROOT + auth.tiktok_api_version + self.EVENT_PATH
        payload = event.json()

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

        except Exception as exeption:
            logging.error(exeption)
            raise exeption
