"""Health check endpoints for ARGOS."""

from __future__ import annotations

from typing import Annotated

from fastapi import APIRouter, Depends

from argos.api.deps import get_health_service
from argos.schemas.health import HealthResponse
from argos.services.health import HealthService

router = APIRouter(tags=["health"])


@router.get("/healthz", response_model=HealthResponse, summary="Health check")
async def health(
    health_service: Annotated[HealthService, Depends(get_health_service)],
) -> HealthResponse:
    """Return the aggregated service health state."""

    return await health_service.check()
