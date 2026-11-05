---
name: new-viz-app
description: Use when adding a new visualization/simulation application to the epistemomechanics monorepo — stamping apps/_template into apps/<slug>, filling placeholders, wiring shared packages, and registering it. Triggers: "new app", "add a viz app", "spin up a simulator", "start an epistemomechanics application".
---

# new-viz-app

Stamp a new application from `apps/_template/`. An app is a sub-component of this module — it
inherits the `epistemomechanics` loom tag and does NOT get its own `tapestry init` or project tag.

## PROBE first
- Pick a `<slug>` (kebab-case). Confirm `apps/<slug>/` does not exist.
- Know the app's ONE line: what it visualizes/simulates and the epistemomechanics question it serves.

## ACT
1. **Stamp:** `cp -r apps/_template apps/<slug>` (PowerShell: `Copy-Item -Recurse apps/_template apps/<slug>`).
2. **Fill placeholders** across the copied tree: `{{APP_NAME}}`, `{{APP_SLUG}}`, `{{ONE_LINE}}`,
   `{{RESEARCH_QUESTION}}`.
3. **Author `app.manifest.yaml` `declared{}`** honestly: `maturity: scaffolded` (never claim
   `working`/`validated` without a recorded run — the manifest makes that contradiction visible).
4. **Write `apps/<slug>/CLAUDE.md`** with app-specific rules (subsystem rules live in the subdir
   CLAUDE.md, not the root).
5. **Register** the app: add a row to `apps/README.md` (name · one-line · state=active · path).
6. **Wire shared code:** import from `packages/viz-core` / `packages/sim-core` instead of copying.

## The contract the app must honor
`data in → core (pure, deterministic, seeded) → 3D/viz surface → interaction → export`.
One-way dependency: **`frontend/ → api/ → core/`**. Keep `core/` importable from a notebook with
zero HTTP (the reproducibility test). Every exported run stamps `{git_sha, input_hash, seed}` and
appends a row to `docs/PROVENANCE.md`.

## STOP conditions
- Don't invent the app's science/doctrine — that's operator-defined (see `docs/CHARTER.md`).
- Don't put compute in the render loop or in a React component; it belongs in `core/`.

## RECORD
Note the new app in `notes`/memory (tag `epistemomechanics`) if it's a durable decision. The app
proves out when one real run goes `data → core → viz → export → one validated finding`.
