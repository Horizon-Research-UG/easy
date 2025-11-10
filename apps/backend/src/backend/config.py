"""Application configuration and settings management."""

from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Runtime configuration surfaced via environment variables."""

    app_name: str = "Easy Platform API"
    debug: bool = False
    allowed_origins: list[str] = ["http://localhost:5173"]

    model_config = SettingsConfigDict(env_prefix="EASY_", case_sensitive=False)


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    """Return cached settings instance to avoid repeated parsing."""

    return Settings()  # Was passiert: Settings instanziieren; Wer ruft wen: get_settings->Settings; Relevanz: zentrale Konfiguration.
