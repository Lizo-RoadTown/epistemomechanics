# Epistemomechanics

**A new scientific field — and the scientific-visualization + simulation applications that
produce and express its domain knowledge.**

Epistemomechanics is developed here as a field in its own right. It *adds* domain knowledge; it
is not a study of other studies. The applications in `apps/` are instruments for the science;
the research in `research/` is where findings are formed and verified. See
[`docs/CHARTER.md`](docs/CHARTER.md) for what this project is and is not.

## Layout

| Path | What lives here |
|---|---|
| `apps/` | The visualization + simulation applications. One folder per app; `apps/_template/` is the stamp. |
| `packages/` | Shared code reused across apps — `viz-core` (3D / rendering primitives), `sim-core` (numeric kernels). |
| `data/` | Shared **input** datasets (`data/raw/`, gitignored) + a provenance manifest. |
| `research/` | The doing-science surface: `notebooks/`, `findings/`, and the `Agent Drafts/` → `Human validated/` integrity boundary. |
| `results/` | Publishable **outputs** — `figures/`, `exports/`. |
| `docs/` | `CHARTER.md`, `PROVENANCE.md` (the run ledger), `architecture/`, `adr/`. |
| `skills/` | Project-local skills — e.g. `new-viz-app` (spin up an app). |

Data-flow spine: **`data/` → `apps/` + `research/` → `results/`.** Reuse across apps is the test
of a correct boundary — shared logic belongs in `packages/`, not copied per app.

## Stack

- **3D:** react-three-fiber / Three.js (VTK.js when an app is volume/field-centric; deck.gl for geospatial-at-scale).
- **2D viz:** Observable Plot (uPlot for dense/streaming).
- **Sim / compute:** Python `core/` (NumPy/SciPy; JAX when autodiff/GPU) served via FastAPI; client-side only when interaction latency demands it.
- **Shell / build:** Vite + React + TypeScript, **pnpm workspaces** monorepo.
- **Reproducibility spine:** each app's numeric `core/` is pure (imports numpy, not web/DB) and is imported by **both** the FastAPI API and a Jupyter notebook — the notebook is the reproducible record, the app is the interactive face of the same functions.

## Add an app

Invoke the `new-viz-app` skill (`skills/new-viz-app/SKILL.md`) — it stamps `apps/_template/`,
fills placeholders, and registers the app in `apps/README.md`.

## Status (2026-11-05)

Seeded. Structure + per-app template in place; no apps built yet. Registry UUID pending (see
`.project-intelligence/REGISTRY-PENDING.md`). The field's definition is operator-authored and
intentionally blank in `docs/CHARTER.md` until Liz fills it.
