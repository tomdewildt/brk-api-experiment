from collections.abc import Sequence
from enum import StrEnum

from pydantic import computed_field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Environment(StrEnum):
    DEV = "dev"
    PROD = "prod"


class LogLevel(StrEnum):
    TRACE = "trace"
    DEBUG = "debug"
    INFO = "info"
    SUCCESS = "success"
    WARNING = "warning"
    ERROR = "error"
    CRITICAL = "critical"


class AppConfig(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="BRK_", env_file=".env", env_file_encoding="utf-8")

    ENV: Environment = Environment.PROD
    LOG_LEVEL: LogLevel = LogLevel.INFO

    TITLE: str = "<todo>"
    DESCRIPTION: str = "<todo>"

    @computed_field
    @property
    def VERSION(self) -> str:  # noqa: N802
        try:
            with open("./VERSION", encoding="utf-8") as file:
                return file.read().strip()
        except FileNotFoundError:
            return "dev"

    CORS_ALLOW_ORIGINS: Sequence[str] = ("*",)
    CORS_ALLOW_METHODS: Sequence[str] = ("GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS")
    CORS_ALLOW_HEADERS: Sequence[str] = ("X-Requested-With", "X-Request-ID")
    CORS_EXPOSE_HEADERS: Sequence[str] = ("X-Request-ID",)

    OTEL_SERVICE_NAME: str = "brk-api-experiment"
    OTEL_EXPORTER_PROTOCOL: str = "grpc"
    OTEL_EXPORTER_ENDPOINT: str = "localhost:4317"
    OTEL_EXPORTER_INSECURE: bool = True

    KADASTER_BASE_URL: str = "https://api.kadastralekaart.com/api/v1"
    KADASTRALE_KAART_BASE_URL: str = "https://kadastralekaart.com"
    PDOK_BASE_URL: str = "https://api.pdok.nl/bzk/locatieserver/search/v3_1"


config = AppConfig()
