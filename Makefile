.PHONY: install sync format lint typecheck test check dev up down build migrate revision

UV ?= uv
COMPOSE ?= docker compose

install: sync

sync:
	$(UV) sync

format:
	$(UV) run black .
	$(UV) run ruff format .

lint:
	$(UV) run ruff check .

typecheck:
	$(UV) run mypy argos tests

test:
	$(UV) run pytest

check: lint typecheck test

dev:
	$(UV) run uvicorn argos.app:create_app --factory --reload --host 0.0.0.0 --port 8000

up:
	$(COMPOSE) up --build

down:
	$(COMPOSE) down -v

build:
	$(COMPOSE) build

migrate:
	$(UV) run alembic upgrade head

revision:
	$(UV) run alembic revision --autogenerate -m "$(message)"

