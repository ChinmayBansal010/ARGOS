"""Readiness endpoint for ARGOS."""

from __future__ import annotations

from typing import Annotated

from fastapi import APIRouter, Depends, Response, status

from argos.api.deps import get_health_service
from argos.services.health import HealthService

router = APIRouter(tags=["health"])


@router.get("/readyz", summary="Readiness check")
async def readiness(
    response: Response,
    health_service: Annotated[HealthService, Depends(get_health_service)],
) -> dict[str, str]:
    """Report whether ARGOS dependencies are ready to receive traffic."""

    health = await health_service.check()
    if health.status.value == "unhealthy":
        response.status_code = status.HTTP_503_SERVICE_UNAVAILABLE
        return {"status": "not_ready"}

    return {"status": "ready"}
