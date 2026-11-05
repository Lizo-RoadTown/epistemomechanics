"""Typed data contract for {{APP_NAME}}.

The single source of truth for what goes into and comes out of the science core.
Pure data classes — no web, no rendering. Used by core/, tested directly, and
re-exported to the API layer.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(frozen=True)
class Params:
    """Inputs to one run. Keep it hashable + explicit; every field is provenance.

    Replace these placeholders with the app's real parameters.
    """
    seed: int = 0
    n_steps: int = 1000
    # ... app-specific parameters go here ...
    extra: dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class Result:
    """Outputs of one run. Arrays are plain lists/ndarrays; no view objects."""
    values: list[float]
    meta: dict[str, Any]
