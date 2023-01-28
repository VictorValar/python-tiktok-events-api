from pydantic import BaseSettings

class Auth(BaseSettings):
    tik_tok_access_token: str
    tik_tok_pixel_id: str
    tik_tok_api_version: str = '1.3'

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'