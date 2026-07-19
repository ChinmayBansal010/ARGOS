"""OpenTelemetry configuration for ARGOS."""

from __future__ import annotations

from dataclasses import dataclass, field

from fastapi import FastAPI
from opentelemetry import trace
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from opentelemetry.instrumentation.redis import RedisInstrumentor
from opentelemetry.instrumentation.sqlalchemy import SQLAlchemyInstrumentor
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor, ConsoleSpanExporter
from sqlalchemy.ext.asyncio import AsyncEngine

from argos.settings import TelemetrySettings


@dataclass(slots=True)
class TelemetryManager:
    """Configure tracing providers and instrumentation hooks."""

    settings: TelemetrySettings
    tracer_provider: TracerProvider | None = field(default=None, init=False)
    _fastapi_instrumented: bool = field(default=False, init=False)
    _redis_instrumented: bool = field(default=False, init=False)
    _sqlalchemy_instrumented: bool = field(default=False, init=False)

    def _ensure_provider(self) -> TracerProvider:
        """Create and register the tracer provider once."""

        if self.tracer_provider is not None:
            return self.tracer_provider

        resource = Resource.create(
            {
                "service.name": self.settings.service_name,
                "service.version": self.settings.service_version,
            }
        )
        provider = TracerProvider(resource=resource)
        if self.settings.otlp_endpoint is not None:
            provider.add_span_processor(
                BatchSpanProcessor(OTLPSpanExporter(endpoint=str(self.settings.otlp_endpoint)))
            )
        if self.settings.enable_console_export:
            provider.add_span_processor(BatchSpanProcessor(ConsoleSpanExporter()))

        trace.set_tracer_provider(provider)
        self.tracer_provider = provider
        return provider

    def instrument_fastapi(self, app: FastAPI) -> None:
        """Instrument the FastAPI app once."""

        self._ensure_provider()
        if not self._fastapi_instrumented:
            FastAPIInstrumentor.instrument_app(app)
            self._fastapi_instrumented = True

    def instrument_database(self, engine: AsyncEngine) -> None:
        """Instrument the SQLAlchemy engine once."""

        self._ensure_provider()
        if not self._sqlalchemy_instrumented:
            SQLAlchemyInstrumentor().instrument(engine=engine.sync_engine)
            self._sqlalchemy_instrumented = True

    def instrument_redis(self) -> None:
        """Instrument Redis once."""

        self._ensure_provider()
        if not self._redis_instrumented:
            RedisInstrumentor().instrument()
            self._redis_instrumented = True

    def shutdown(self) -> None:
        """Shut down the tracer provider cleanly."""

        if self.tracer_provider is not None:
            self.tracer_provider.shutdown()
            self.tracer_provider = None
            self._fastapi_instrumented = False
            self._redis_instrumented = False
            self._sqlalchemy_instrumented = False


def build_telemetry_manager(settings: TelemetrySettings) -> TelemetryManager:
    """Create a telemetry manager for the current runtime."""

    return TelemetryManager(settings=settings)
