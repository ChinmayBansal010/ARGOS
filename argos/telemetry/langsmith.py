"""LangSmith support for ARGOS."""

from __future__ import annotations

import os
from dataclasses import dataclass

from langsmith import Client

from argos.settings import TelemetrySettings


@dataclass(slots=True)
class LangSmithRuntime:
    """Create a LangSmith client from runtime settings when enabled."""

    settings: TelemetrySettings

    def client(self) -> Client | None:
        """Return a configured LangSmith client or ``None`` if disabled."""

        if not self.settings.langsmith_tracing:
            return None

        os.environ["LANGCHAIN_TRACING_V2"] = "true"
        os.environ["LANGCHAIN_PROJECT"] = self.settings.langsmith_project
        api_key = (
            self.settings.langsmith_api_key.get_secret_value()
            if self.settings.langsmith_api_key is not None
            else None
        )
        if api_key is not None:
            os.environ["LANGCHAIN_API_KEY"] = api_key
        if self.settings.langsmith_endpoint is not None:
            os.environ["LANGCHAIN_ENDPOINT"] = str(self.settings.langsmith_endpoint)

        return Client()
