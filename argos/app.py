"""FastAPI application factory for ARGOS."""

from __future__ import annotations

from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from argos import __version__
from argos.api.router import create_api_router
from argos.container import AppContainer, build_container
from argos.logging import configure_logging
from argos.observability.opentelemetry import build_telemetry_manager
from argos.settings import AppSettings, get_settings
from argos.telemetry.langsmith import LangSmithRuntime


def create_app(
    settings: AppSettings | None = None,
    container: AppContainer | None = None,
) -> FastAPI:
    """Construct and configure the ARGOS FastAPI application."""

    resolved_settings = settings or get_settings()
    configure_logging(resolved_settings)
    telemetry = build_telemetry_manager(resolved_settings.telemetry)
    langsmith_runtime = LangSmithRuntime(resolved_settings.telemetry)
    resolved_container = container or build_container(resolved_settings)

    @asynccontextmanager
    async def lifespan(app: FastAPI) -> AsyncIterator[None]:
        """Manage startup and shutdown for the application."""

        app.state.container = resolved_container
        app.state.settings = resolved_settings
        app.state.langsmith_client = langsmith_runtime.client()
        telemetry.instrument_redis()
        database_engine = getattr(resolved_container.database, "engine", None)
        if database_engine is not None:
            telemetry.instrument_database(database_engine)
        await resolved_container.startup()
        try:
            yield
        finally:
            await resolved_container.shutdown()
            telemetry.shutdown()

    app = FastAPI(
        title=resolved_settings.app_name,
        version=__version__,
        root_path=resolved_settings.api_root_path,
        docs_url="/docs" if resolved_settings.enable_docs else None,
        redoc_url="/redoc" if resolved_settings.enable_docs else None,
        openapi_url="/openapi.json" if resolved_settings.enable_docs else None,
        lifespan=lifespan,
    )

    if resolved_settings.cors_origins:
        app.add_middleware(
            CORSMiddleware,
            allow_origins=resolved_settings.cors_origins,
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

    telemetry.instrument_fastapi(app)
    app.include_router(create_api_router())
    return app
