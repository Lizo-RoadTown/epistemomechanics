# ⚠ Project Registry registration PENDING

`project-context.json` carries a **placeholder** `project_id`
(`PENDING-registry-unreachable-2026-11-05`), not a real UUID.

**Why:** at launch (2026-11-05) no Project Registry was reachable (`TAPESTRY_REGISTRY_URL` unset;
the deployed registry is not yet stood up). `tapestry init` mints the UUID via the registry and
refuses to write a fake one (`init.py:682`), so this project was scaffolded locally with the UUID
left pending — same gated state as IAKM (`fall-2026-class-repos-...-observer-gated-2026-08-29`,
IAKM's own `REGISTRY-PENDING.md`).

**Consequence:** the self-observer (Stop-hook) **skips** this project until a real 36-char UUID is
in `project-context.json`. Memory, telemetry, and the discipline hooks all work regardless — only
the observer's candidate-emission is gated.

**To complete (one step, when a registry is reachable):**

```bash
export TAPESTRY_REGISTRY_URL="https://<your-live-project-registry>"
cd /path/to/epistemomechanics
python -m tapestry_cli init --slug epistemomechanics \
  --name "Epistemomechanics" --description "<one-liner>"
# idempotent: GETs by-slug, POSTs if absent, overwrites the placeholder project_id
# with the real UUID. Nothing else needs redoing.
```
