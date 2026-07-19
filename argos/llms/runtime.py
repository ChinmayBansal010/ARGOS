"""LiteLLM runtime configuration for ARGOS."""

from __future__ import annotations

import os
from dataclasses import dataclass
from typing import Any

from argos.settings import LLMSettings


@dataclass(slots=True)
class LiteLLMRuntime:
    """Materialize LiteLLM-related environment configuration."""

    settings: LLMSettings

    def apply_environment(self) -> None:
        """Publish LiteLLM settings into the process environment."""

        os.environ["LITELLM_DROP_PARAMS"] = "true" if self.settings.drop_params else "false"
        if self.settings.default_model:
            os.environ["LITELLM_MODEL"] = self.settings.default_model
        if self.settings.api_base is not None:
            os.environ["LITELLM_API_BASE"] = str(self.settings.api_base)
        if self.settings.api_key is not None:
            os.environ["LITELLM_API_KEY"] = self.settings.api_key.get_secret_value()

    def model_configuration(self) -> dict[str, Any]:
        """Return the resolved LiteLLM configuration payload."""

        return {
            "default_model": self.settings.default_model,
            "api_base": str(self.settings.api_base) if self.settings.api_base else None,
            "drop_params": self.settings.drop_params,
        }
