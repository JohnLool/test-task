from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    api_url: str = "https://nsfw-categorize.it/api/upload"
    allowed_types: set = {"image/jpeg", "image/png"}

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
