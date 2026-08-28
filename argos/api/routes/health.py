"""Health check endpoints for ARGOS."""

from __future__ import annotations

from typing import Annotated

from fastapi import APIRouter, Depends, Response, status

from argos.api.deps import get_health_service
from argos.schemas.health import HealthResponse
from argos.services.health import HealthService

router = APIRouter(tags=["health"])


@router.get("/healthz", response_model=HealthResponse, summary="Health check")
async def health(
    response: Response,
    health_service: Annotated[HealthService, Depends(get_health_service)],
) -> HealthResponse:
    """Return the aggregated service health state."""

    result = await health_service.check()
    if result.status is result.status.unhealthy:
        response.status_code = status.HTTP_503_SERVICE_UNAVAILABLE
    return result
