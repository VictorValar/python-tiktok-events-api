from pydantic import BaseSettings, constr
from typing import Optional
class Auth(BaseSettings):
    tiktok_access_token: str
    tiktok_pixel_id: str
    tiktok_test_event_code: Optional[str]
    tiktok_api_version: constr(strip_whitespace=True, min_length=4) = 'v1.3'

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'