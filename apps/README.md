# apps — the visualization + simulation applications

One folder per app. Each app is a **sub-component** of this module (it inherits the
`epistemomechanics` loom tag; it does **not** get its own project tag or its own `tapestry init`).
`apps/_template/` is the stamp — copy it to start a new app (via the `new-viz-app` skill).

## App index

Declared state only — one of `active` · `parked` · `shipped` · `dropped` (no free-text status;
self-reported status rots). Liveness/maturity is tracked per app in its `app.manifest.yaml`
(`declared.maturity` + `derived.last_run`), where a "working" claim with no recorded run shows
as a visible contradiction.

| App | One line | State | Path |
|---|---|---|---|
| _(none yet)_ | | | |

## Add an app

See `skills/new-viz-app/SKILL.md`. In short: stamp `apps/_template/` → `apps/<slug>/`, replace
placeholders, write the app's own subdir `CLAUDE.md`, add a row above, import shared code from
`packages/` rather than copying.

## The contract every app honors

```
data in  →  core (sim/compute, pure + deterministic)  →  3D/viz surface  →  interaction  →  export
```

Dependency arrow is one-way: **`frontend/ → api/ → core/`**. `core/` imports no web/DB framework,
so a notebook can run the science with zero HTTP. If it can't, rendering/transport has leaked
into compute — fix the boundary.
