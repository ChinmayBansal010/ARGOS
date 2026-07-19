"""CLI helpers for running the ARGOS API service."""

from __future__ import annotations

from uvicorn import run

from argos.app import create_app
from argos.settings import get_settings


def main() -> None:
    """Start the API server with the configured runtime settings."""

    settings = get_settings()
    run(
        create_app(),
        host=settings.api_host,
        port=settings.api_port,
        root_path=settings.api_root_path,
        log_level=settings.log_level.lower(),
        factory=False,
    )
