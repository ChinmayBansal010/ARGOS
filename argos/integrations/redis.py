"""Redis client management for ARGOS."""

from __future__ import annotations

from dataclasses import dataclass, field

from redis.asyncio import Redis, from_url

from argos.settings import RedisSettings


@dataclass(slots=True)
class RedisService:
    """Manage the Redis client used by the service."""

    settings: RedisSettings
    _client: Redis = field(init=False, repr=False)

    def __post_init__(self) -> None:
        self._client = from_url(
            self.settings.url,
            decode_responses=True,
            socket_timeout=self.settings.socket_timeout_seconds,
        )

    @property
    def client(self) -> Redis:
        """Expose the Redis client."""

        return self._client

    async def ping(self) -> None:
        """Validate Redis connectivity."""

        await self._client.ping()

    async def close(self) -> None:
        """Close the Redis connection pool."""

        await self._client.aclose()
