# {{APP_NAME}}

{{ONE_LINE}}

**Research question:** {{RESEARCH_QUESTION}}

One app in the epistemomechanics monorepo. Honors the contract
`data in → core → viz → interaction → export`, with the one-way dependency
`frontend/ → api/ → core/`.

## Run (dev)

```bash
# backend (from apps/{{APP_SLUG}}/)
python -m venv .venv && . .venv/Scripts/activate   # or source .venv/bin/activate
pip install -r requirements.txt
uvicorn api.main:app --reload --port 8000

# frontend (from apps/{{APP_SLUG}}/frontend/, via pnpm workspace at repo root)
pnpm install
pnpm --filter {{APP_SLUG}}-frontend dev
```

## Layout

- `core/` — the science. Pure Python (numpy only), deterministic given (inputs, seed). Importable
  from a notebook with zero HTTP. Tested directly in `core/tests/`.
- `api/` — thin FastAPI over `core/` (`/api/simulate`, `/api/export`). Serves `dist/` in prod.
- `frontend/` — 3D (`src/scene`) + viz (`src/viz`) + controls (`src/controls`) + io (`src/io`).
- `docs/MODEL_TO_CODE.md` — the standing "how we know this app models what it claims" doc.
- `app.manifest.yaml` — declared-vs-derived record. `data/runs/` — per-run outputs (gitignored).
