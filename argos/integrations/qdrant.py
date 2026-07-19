"""Qdrant client management for ARGOS."""

from __future__ import annotations

from dataclasses import dataclass, field

from qdrant_client import AsyncQdrantClient

from argos.settings import QdrantSettings


@dataclass(slots=True)
class QdrantService:
    """Manage the Qdrant client used by the service."""

    settings: QdrantSettings
    _client: AsyncQdrantClient = field(init=False, repr=False)

    def __post_init__(self) -> None:
        api_key = self.settings.api_key.get_secret_value() if self.settings.api_key else None
        self._client = AsyncQdrantClient(
            url=str(self.settings.url),
            api_key=api_key,
        )

    @property
    def client(self) -> AsyncQdrantClient:
        """Expose the Qdrant async client."""

        return self._client

    async def ping(self) -> None:
        """Validate Qdrant connectivity."""

        await self._client.get_collections()

    async def close(self) -> None:
        """Close the Qdrant client."""

        await self._client.close()
