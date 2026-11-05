# {{APP_NAME}} — architecture

Three pieces, one-way dependency: **`frontend/ → api/ → core/`**.

| Piece | Runs where | Does | Must NOT |
|---|---|---|---|
| `core/` | Python (also importable in a notebook) | The science: `Params → Result`, deterministic given (inputs, seed). | import web/DB/rendering; hold global state. |
| `api/` | FastAPI (uvicorn) | Thin transport: accept request → call core → return/stream; `/api/export` stamps provenance. | compute the science. |
| `frontend/` | Browser (Vite + React + r3f) | Render `core` results (scene/viz), drive params (controls), fetch (io), trigger export. | compute the science in the render loop or a React component. |

**The reproducibility test:** `from core.simulate import run` works in a plain notebook with zero
HTTP. If it doesn't, transport/rendering has leaked into compute.

Provenance: only explicit exports are recorded (a row in `../../docs/PROVENANCE.md` + this app's
`app.manifest.yaml` `derived`). Interactive re-solves are ephemeral.
