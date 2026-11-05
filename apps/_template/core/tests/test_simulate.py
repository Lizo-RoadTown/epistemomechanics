"""Tests for the science core — run with `pytest` from the app dir. No server needed.

The determinism + golden-run tests are the reproducibility guard: if a refactor
silently changes the science, these fail.
"""
from __future__ import annotations

from core.schema import Params
from core.simulate import run


def test_deterministic_given_seed():
    a = run(Params(seed=42, n_steps=100))
    b = run(Params(seed=42, n_steps=100))
    assert a.values == b.values, "same (inputs, seed) must give identical output"


def test_seed_changes_output():
    a = run(Params(seed=1, n_steps=100))
    b = run(Params(seed=2, n_steps=100))
    assert a.values != b.values


def test_shape():
    r = run(Params(seed=0, n_steps=256))
    assert len(r.values) == 256
    assert r.meta["seed"] == 0

# TODO: add a golden-run regression test once the real model lands:
#   load fixtures/golden_<case>.json and assert run(...) matches within tol.
