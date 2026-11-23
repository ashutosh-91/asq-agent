import os

from dotenv import load_dotenv
from pydantic import SecretStr
from pydantic_settings import BaseSettings,SettingsConfigDict

class ModelConfigs(BaseSettings):
        Model_Api_Key:SecretStr
        Model_Name:str
        Model_Base_Url:str
        model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
        )
