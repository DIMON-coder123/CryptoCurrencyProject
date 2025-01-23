from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    API_KEY: str
    JWT_KEY: str
    model_config = SettingsConfigDict(env_file="/home/dmytro/repo/CryptoCurrencyProject/backend/src/.env", extra='forbid')


settings = Settings()

