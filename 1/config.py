import os.path
from pydantic_settings import BaseSettings
from typing import List

class Config(BaseSettings):

    APP_DEBUG: bool = True

    VERSION: str = '0.0.1'
    PROJECT_NAME: str = 'fastapidemo'
    DESCRIPTION: str = 'fastapidemo'

    STATIC_DIR: str = os.path.join(os.getcwd(),"../static")

    CORS_ORIGINS: List[str] = ['*']
    CORS_ALLOW_CREDENTIALS: bool = True
    CORS_ALLOW_METHODS: List[str] = ['*']
    CORS_ALLOW_HEADERS: List[str] = ['*']


settings = Config()