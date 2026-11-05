# results — publishable outputs

Outputs headed for papers, talks, or the record. Each artifact is provenanced (stamped with the
`run_id` / `git_sha` that produced it; traceable via `docs/PROVENANCE.md`).

| Path | What goes here |
|---|---|
| `figures/` | Figures for papers / talks (committed; small). |
| `exports/` | Rendered artifacts, large simulation-run exports (gitignored; tracked via provenance). |

An output with no provenance row is not a result yet — it's an orphan render.
