"""Health endpoint tests for the ARGOS API foundation."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, cast

import pytest
from httpx import ASGITransport, AsyncClient

from argos.app import create_app
from argos.container import AppContainer
from argos.schemas.health import ComponentStatus, HealthResponse
from argos.services.health import HealthService
from argos.settings import AppSettings, Environment


@dataclass(slots=True)
class StaticProbe:
    """Simple probe used to exercise the health endpoint in tests."""

    async def ping(self) -> None:
        """Return successfully without external dependencies."""

    async def close(self) -> None:
        """Allow the container shutdown path to complete."""

    async def dispose(self) -> None:
        """Allow the container shutdown path to complete."""


@pytest.mark.asyncio
async def test_health_endpoint_returns_structured_status() -> None:
    """The health endpoint should expose a stable, typed JSON payload."""

    settings = AppSettings(environment=Environment.test, cors_origins=[])
    probe = StaticProbe()
    health_service = HealthService(
        database=probe,
        redis=probe,
        qdrant=probe,
        environment=settings.environment,
        version="0.1.0",
    )
    container = AppContainer(
        settings=settings,
        database=cast(Any, probe),
        redis=cast(Any, probe),
        qdrant=cast(Any, probe),
        llm=cast(Any, object()),
        graph=cast(Any, object()),
        health_service=health_service,
    )

    app = create_app(settings=settings, container=container)
    transport = ASGITransport(app=app)

    async with AsyncClient(transport=transport, base_url="http://test") as client:
        response = await client.get("/healthz")

    assert response.status_code == 200
    payload = HealthResponse.model_validate(response.json())
    assert payload.status is ComponentStatus.healthy
    assert payload.environment is Environment.test
    assert set(payload.components) == {"database", "redis", "qdrant"}
    assert all(
        component.status is ComponentStatus.healthy for component in payload.components.values()
    )
    assert all(component.latency_ms >= 0.0 for component in payload.components.values())
