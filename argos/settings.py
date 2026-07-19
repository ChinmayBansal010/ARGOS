"""Application settings and configuration models for ARGOS."""

from __future__ import annotations

from enum import StrEnum
from functools import lru_cache

from pydantic import BaseModel, Field, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict
from sqlalchemy.engine import URL, make_url


class Environment(StrEnum):
    """Runtime environment for the service."""

    development = "development"
    test = "test"
    staging = "staging"
    production = "production"


class DatabaseSettings(BaseModel):
    """Database connection settings."""

    url: str = Field(default="postgresql+asyncpg://argos:argos@postgres:5432/argos")
    echo: bool = False
    pool_size: int = 10
    max_overflow: int = 20
    pool_timeout_seconds: float = 30.0

    def sqlalchemy_url(self) -> URL:
        """Return the database URL as a SQLAlchemy URL object."""

        return make_url(self.url)


class RedisSettings(BaseModel):
    """Redis connection settings."""

    url: str = Field(default="redis://redis:6379/0")
    socket_timeout_seconds: float = 5.0


class QdrantSettings(BaseModel):
    """Qdrant connection settings."""

    url: str = Field(default="http://qdrant:6333")
    api_key: SecretStr | None = None


class LLMSettings(BaseModel):
    """LiteLLM configuration settings."""

    default_model: str = ""
    api_base: str | None = None
    api_key: SecretStr | None = None
    drop_params: bool = True


class TelemetrySettings(BaseModel):
    """Telemetry and LangSmith settings."""

    service_name: str = "argos-api"
    service_version: str = "0.1.0"
    otlp_endpoint: str | None = None
    enable_console_export: bool = False
    sampling_ratio: float = 1.0
    langsmith_tracing: bool = False
    langsmith_api_key: SecretStr | None = None
    langsmith_project: str = "argos"
    langsmith_endpoint: str | None = None


class AppSettings(BaseSettings):
    """Top-level application settings loaded from the environment."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        env_nested_delimiter="__",
        extra="ignore",
    )

    app_name: str = "ARGOS"
    environment: Environment = Environment.development
    log_level: str = "INFO"
    enable_docs: bool = True
    api_host: str = "0.0.0.0"
    api_port: int = 8000
    api_root_path: str = ""
    cors_origins: list[str] = Field(default_factory=lambda: ["http://localhost:3000"])
    database: DatabaseSettings = Field(default_factory=DatabaseSettings)
    redis: RedisSettings = Field(default_factory=RedisSettings)
    qdrant: QdrantSettings = Field(default_factory=QdrantSettings)
    llm: LLMSettings = Field(default_factory=LLMSettings)
    telemetry: TelemetrySettings = Field(default_factory=TelemetrySettings)


@lru_cache(maxsize=1)
def get_settings() -> AppSettings:
    """Return the singleton application settings instance."""

    return AppSettings()
