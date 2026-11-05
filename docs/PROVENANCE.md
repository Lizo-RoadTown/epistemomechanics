# Provenance ledger

Append-only. **One row per run that produced a research output** (an exported figure, a result,
a dataset). Ephemeral interaction (dragging a slider, a transient re-solve) does NOT get a row —
only explicit exports/captures do. Written by each app's run wrapper **at run time** (not after):
no run, no record; a record, always complete. This is the project's documents-as-we-go spine.

Start flat (this file). Migrate to a small SQLite / Supabase run-index only when a human can no
longer scan it.

| run_id | app | git_sha | input_hash | seed | output_path | figure_path | at (UTC) |
|---|---|---|---|---|---|---|---|
| _(none yet)_ | | | | | | | |

Each run also writes its own provenance into the app's `app.manifest.yaml` `derived.last_run`
and, on export, appends to `derived.produced_figures`. A finding that cites a run references its
`run_id` here — so every claim traces back to an exact (code, inputs, seed).
