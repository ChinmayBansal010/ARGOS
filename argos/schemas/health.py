"""Health response schemas for ARGOS."""

from __future__ import annotations

from datetime import UTC, datetime
from enum import StrEnum

from pydantic import BaseModel, Field

from argos.settings import Environment


class ComponentStatus(StrEnum):
    """Component health state."""

    healthy = "healthy"
    degraded = "degraded"
    unhealthy = "unhealthy"


class ComponentHealth(BaseModel):
    """Health details for one subsystem."""

    status: ComponentStatus
    latency_ms: float
    detail: dict[str, str] = Field(default_factory=dict)


class HealthResponse(BaseModel):
    """Aggregated health response returned by the API."""

    status: ComponentStatus
    environment: Environment
    version: str
    components: dict[str, ComponentHealth]
    timestamp: datetime = Field(default_factory=lambda: datetime.now(UTC))
