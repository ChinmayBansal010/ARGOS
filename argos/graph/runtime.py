"""LangGraph runtime scaffolding for ARGOS."""

from __future__ import annotations

from dataclasses import dataclass
from typing import TypedDict

from langgraph.graph import StateGraph

from argos.settings import LLMSettings


class GraphState(TypedDict, total=False):
    """Future state contract for ARGOS agent graphs."""

    prompt: str
    response: str
    metadata: dict[str, str]


@dataclass(slots=True)
class GraphRuntime:
    """Hold future graph configuration without defining agent behavior."""

    settings: LLMSettings

    def build_graph(self) -> StateGraph[GraphState]:
        """Create an empty state graph ready for future node wiring."""

        return StateGraph(GraphState)
