"""Health aggregation service for ARGOS."""

from __future__ import annotations

import asyncio
from dataclasses import dataclass
from time import perf_counter
from typing import Protocol

from argos.schemas.health import ComponentHealth, ComponentStatus, HealthResponse
from argos.settings import Environment


class HealthProbe(Protocol):
    """Protocol implemented by dependencies that expose a ping operation."""

    async def ping(self) -> None:
        """Validate service connectivity."""


@dataclass(slots=True)
class HealthService:
    """Collect and summarize health information for runtime dependencies."""

    database: HealthProbe
    redis: HealthProbe
    qdrant: HealthProbe
    environment: Environment
    version: str

    async def check(self) -> HealthResponse:
        """Run health probes and return a structured response."""

        checks = await asyncio.gather(
            self._probe("database", self.database),
            self._probe("redis", self.redis),
            self._probe("qdrant", self.qdrant),
        )
        components = {name: component for name, component in checks}
        status = self._overall_status(components)
        return HealthResponse(
            status=status,
            environment=self.environment,
            version=self.version,
            components=components,
        )

    async def _probe(self, name: str, probe: HealthProbe) -> tuple[str, ComponentHealth]:
        """Measure the latency and result of a single probe."""

        started = perf_counter()
        try:
            await probe.ping()
        except Exception as exc:  # pragma: no cover - defensive boundary
            latency_ms = (perf_counter() - started) * 1000.0
            return (
                name,
                ComponentHealth(
                    status=ComponentStatus.unhealthy,
                    latency_ms=latency_ms,
                    detail={"error": str(exc)},
                ),
            )

        latency_ms = (perf_counter() - started) * 1000.0
        return (
            name,
            ComponentHealth(
                status=ComponentStatus.healthy,
                latency_ms=latency_ms,
                detail={},
            ),
        )

    @staticmethod
    def _overall_status(components: dict[str, ComponentHealth]) -> ComponentStatus:
        """Derive the overall service health from component probes."""

        statuses = {component.status for component in components.values()}
        if statuses == {ComponentStatus.healthy}:
            return ComponentStatus.healthy
        if ComponentStatus.unhealthy in statuses and ComponentStatus.healthy in statuses:
            return ComponentStatus.degraded
        if ComponentStatus.degraded in statuses:
            return ComponentStatus.degraded
        return ComponentStatus.unhealthy
