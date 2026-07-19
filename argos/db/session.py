"""Database session and engine management for ARGOS."""

from __future__ import annotations

from collections.abc import AsyncIterator
from contextlib import asynccontextmanager
from dataclasses import dataclass, field

from sqlalchemy import text
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from argos.settings import DatabaseSettings


@dataclass(slots=True)
class DatabaseService:
    """Manage the SQLAlchemy async engine and session factory."""

    settings: DatabaseSettings
    _engine: AsyncEngine = field(init=False, repr=False)
    _session_factory: async_sessionmaker[AsyncSession] = field(init=False, repr=False)

    def __post_init__(self) -> None:
        self._engine = create_async_engine(
            self.settings.url,
            echo=self.settings.echo,
            pool_pre_ping=True,
            pool_size=self.settings.pool_size,
            max_overflow=self.settings.max_overflow,
            pool_timeout=self.settings.pool_timeout_seconds,
        )
        self._session_factory = async_sessionmaker(
            self._engine,
            expire_on_commit=False,
        )

    @property
    def engine(self) -> AsyncEngine:
        """Expose the underlying async engine for instrumentation."""

        return self._engine

    @asynccontextmanager
    async def session(self) -> AsyncIterator[AsyncSession]:
        """Yield a managed SQLAlchemy async session."""

        async with self._session_factory() as session:
            yield session

    async def ping(self) -> None:
        """Validate database connectivity with a lightweight query."""

        async with self._engine.connect() as connection:
            await connection.execute(text("SELECT 1"))

    async def dispose(self) -> None:
        """Dispose the engine and release the connection pool."""

        await self._engine.dispose()
