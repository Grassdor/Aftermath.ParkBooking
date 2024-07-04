from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    postgres_dsn: str

    model_config = SettingsConfigDict(env_file=".env")


def get_settings():
    return Settings()


settings = get_settings()
