"""API router composition for ARGOS."""

from __future__ import annotations

from fastapi import APIRouter

from argos.api.routes.health import router as health_router


def create_api_router() -> APIRouter:
    """Assemble the public API routes."""

    router = APIRouter()
    router.include_router(health_router)
    return router
