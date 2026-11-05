"""The science core for {{APP_NAME}}.

PURE compute. Imports only numpy + this app's schema. NO FastAPI, NO rendering,
NO file/network I/O, NO global state. This is the rule that keeps the science
reusable + testable + runnable from a notebook with zero HTTP:

    from apps.<slug>.core.simulate import run      # works in a notebook
    result = run(Params(seed=0))                    # deterministic given (inputs, seed)

If you ever need `requests`, `fastapi`, or a Three.js call in this file, the
boundary has leaked — move that code to api/ or frontend/ instead.
"""
from __future__ import annotations

import numpy as np

from .schema import Params, Result


def run(params: Params) -> Result:
    """Deterministic given (params including seed). Replace the body with the model.

    The placeholder below is a stand-in so the scaffold runs end-to-end; delete it
    and implement the actual epistemomechanics model for this app.
    """
    rng = np.random.default_rng(params.seed)
    # --- placeholder model: a seeded random walk; REPLACE with the real model ---
    steps = rng.standard_normal(params.n_steps)
    values = np.cumsum(steps)
    # --------------------------------------------------------------------------
    return Result(
        values=values.tolist(),
        meta={"n_steps": params.n_steps, "seed": params.seed, "model": "PLACEHOLDER"},
    )
