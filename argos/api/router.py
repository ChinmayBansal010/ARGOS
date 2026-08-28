"""API router composition for ARGOS."""

from __future__ import annotations

from fastapi import APIRouter

from argos.api.routes.health import router as health_router
from argos.api.routes.ready import router as readiness_router


def create_api_router() -> APIRouter:
    """Assemble the public API routes."""

    router = APIRouter()
    router.include_router(health_router)
    router.include_router(readiness_router)
    return router
