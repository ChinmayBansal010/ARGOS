"""FastAPI dependency helpers for ARGOS."""

from __future__ import annotations

from typing import cast

from fastapi import Request

from argos.container import AppContainer
from argos.services.health import HealthService


def get_container(request: Request) -> AppContainer:
    """Return the application container attached to the FastAPI state."""

    return cast(AppContainer, request.app.state.container)


def get_health_service(request: Request) -> HealthService:
    """Return the health service from the application container."""

    return get_container(request).health_service
