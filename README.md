# ARGOS

ARGOS (Adaptive Re-anchored Goal Optimization System) is a FastAPI service foundation for a
goal-oriented orchestration platform.

## Stack

- Python 3.13
- FastAPI
- SQLAlchemy 2.x
- Alembic
- PostgreSQL
- Redis
- Qdrant
- LangGraph
- LiteLLM
- Loguru
- OpenTelemetry
- LangSmith
- uv

## Layout

- `argos/` contains the backend service package.
- `apps/api/` contains the API Docker image.
- `apps/frontend/` contains the frontend Docker image.
- `alembic/` contains database migrations.
- `tests/` contains the initial production checks.

## Local development

```bash
uv sync
make dev
```

## Docker

```bash
docker compose up --build
```

## Health

- API health endpoint: `GET /healthz`
- Readiness details include PostgreSQL, Redis, and Qdrant probes.

