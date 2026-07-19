FROM python:3.13-slim AS base

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    UV_PROJECT_ENVIRONMENT=/app/.venv \
    PATH="/app/.venv/bin:${PATH}"

WORKDIR /app

RUN apt-get update \
    && apt-get install -y --no-install-recommends build-essential curl \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir uv

COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-dev --no-install-project

COPY argos ./argos
COPY alembic ./alembic
COPY alembic.ini README.md main.py ./
RUN uv sync --frozen --no-dev

EXPOSE 8000

CMD ["uvicorn", "argos.app:create_app", "--factory", "--host", "0.0.0.0", "--port", "8000"]

