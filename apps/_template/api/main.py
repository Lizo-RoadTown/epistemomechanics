"""Thin transport layer for {{APP_NAME}}. Imports core/; core never imports this.

Responsibilities ONLY: accept a request, call the pure science core, return/stream
the result, and (on export) stamp provenance. No science lives here.
"""
from __future__ import annotations

import hashlib
import json
from dataclasses import asdict

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from core.schema import Params
from core.simulate import run

app = FastAPI(title="{{APP_NAME}}")
app.add_middleware(
    CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"]
)


class SimRequest(BaseModel):
    seed: int = 0
    n_steps: int = 1000


@app.get("/api/health")
def health() -> dict:
    return {"ok": True, "app": "{{APP_SLUG}}"}


@app.post("/api/simulate")
def simulate(req: SimRequest) -> dict:
    """Run the core and return the result. Transient/interactive runs are NOT
    provenance-recorded — only an explicit /api/export is (see below)."""
    params = Params(seed=req.seed, n_steps=req.n_steps)
    result = run(params)
    return {"result": asdict(result), "input_hash": _hash(params)}


@app.post("/api/export")
def export(req: SimRequest) -> dict:
    """An explicit capture: run, then stamp provenance. Wire this to write a row
    into ../../docs/PROVENANCE.md + this app's app.manifest.yaml `derived` and save
    the output under data/runs/<run_id>/. Left as a TODO so provenance is a
    deliberate, implemented step, not a silent no-op."""
    params = Params(seed=req.seed, n_steps=req.n_steps)
    result = run(params)
    # TODO: write data/runs/<run_id>/, append docs/PROVENANCE.md, update manifest derived.
    return {"result": asdict(result), "input_hash": _hash(params), "exported": False}


def _hash(params: Params) -> str:
    return hashlib.sha256(
        json.dumps(asdict(params), sort_keys=True, default=str).encode()
    ).hexdigest()[:16]
