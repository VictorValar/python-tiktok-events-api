'''
Python wrapper for the TikTok Events API
'''

from pydantic import BaseModel, BaseSettings

class Settings(BaseSettings):
    tik_tok_access_token: str
    tik_tok_pixel_id: str
    tik_tok_api_version: str = '1.3'

# setting = Settings()
# print(setting.tik_tok_access_token)

class Event(BaseModel):
    pass