from typing import Literal

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Production-ready application configuration.
    Values are loaded from environment variables or .env file.
    """

    app_name: str = Field(..., description="Application name")
    environment: Literal["development", "production"] = Field(
        ..., description="Application environment"
    )
    debug: bool = Field(..., description="Debug mode")
    log_level: str = Field(..., description="Application log level")
    service_url: str = Field(..., description="Service URL")
    model_path: str = Field(..., description="Path to ML model")

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )


settings = Settings()