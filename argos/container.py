"""Dependency container for the ARGOS application."""

from __future__ import annotations

import asyncio
from collections.abc import Awaitable, Callable
from dataclasses import dataclass, field

from argos.db.session import DatabaseService
from argos.graph.runtime import GraphRuntime
from argos.integrations.qdrant import QdrantService
from argos.integrations.redis import RedisService
from argos.llms.runtime import LiteLLMRuntime
from argos.services.health import HealthService
from argos.settings import AppSettings


@dataclass(slots=True)
class AppContainer:
    """Grouped application dependencies managed by the runtime."""

    settings: AppSettings
    database: DatabaseService
    redis: RedisService
    qdrant: QdrantService
    llm: LiteLLMRuntime
    graph: GraphRuntime
    health_service: HealthService
    _startup_attempts: int = field(default=5, init=False, repr=False)
    _startup_delay_seconds: float = field(default=1.0, init=False, repr=False)

    async def startup(self) -> None:
        """Validate critical dependencies during application startup."""

        await self._wait_for_probe("database", self.database.ping)
        await self._wait_for_probe("redis", self.redis.ping)
        await self._wait_for_probe("qdrant", self.qdrant.ping)

    async def shutdown(self) -> None:
        """Release resources in reverse order during shutdown."""

        await self.qdrant.close()
        await self.redis.close()
        await self.database.dispose()

    async def _wait_for_probe(self, name: str, probe: Callable[[], Awaitable[None]]) -> None:
        """Retry a dependency probe until it succeeds or times out."""

        last_error: Exception | None = None
        for attempt in range(self._startup_attempts):
            try:
                await probe()
                return
            except Exception as exc:  # pragma: no cover - defensive boundary
                last_error = exc
                await asyncio.sleep(min(self._startup_delay_seconds * (2**attempt), 8.0))

        message = f"{name} failed health checks during startup"
        raise RuntimeError(message) from last_error


def build_container(settings: AppSettings) -> AppContainer:
    """Instantiate the application dependency container."""

    llm_runtime = LiteLLMRuntime(settings.llm)
    llm_runtime.apply_environment()
    graph_runtime = GraphRuntime(settings.llm)
    database = DatabaseService(settings.database)
    redis = RedisService(settings.redis)
    qdrant = QdrantService(settings.qdrant)
    health_service = HealthService(
        database=database,
        redis=redis,
        qdrant=qdrant,
        environment=settings.environment,
        version=settings.telemetry.service_version,
    )

    return AppContainer(
        settings=settings,
        database=database,
        redis=redis,
        qdrant=qdrant,
        llm=llm_runtime,
        graph=graph_runtime,
        health_service=health_service,
    )
