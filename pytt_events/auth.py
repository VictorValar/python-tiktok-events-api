from pydantic import BaseSettings, constr
from typing import Optional
class TikTokAuth(BaseSettings):
    '''
    Handles TikTok Auth data.
    Throws a ValidationError if required environment vars are not set.
    '''
    TIKTOK_ACESS_TOKEN: str
    TIKTOK_PIXEL_ID: str
    TIKTOK_TEST_EVENT_CODE: Optional[str]
    TIKTOK_API_VERSION: constr(strip_whitespace=True, min_length=4) = 'v1.3'

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'