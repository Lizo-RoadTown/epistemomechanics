# research — the doing-science surface

Where epistemomechanics findings are formed and verified. Apps are instruments; this is where
their outputs become knowledge.

| Path | What goes here |
|---|---|
| `notebooks/` | Exploratory + confirmatory analysis. Cell 1 pins the app `git_sha`, the data hash, and the `run_id` being analyzed — a notebook is re-runnable against an exact run. |
| `findings/` | Synthesized findings (`*.md`), each citing the `run_id`(s) it rests on (traceable via `docs/PROVENANCE.md`). |
| `Agent Drafts/` | Findings/analysis an agent or workflow produced, **not yet human-checked**. Agents write here, each file carrying a provenance header (generated-by, from run_id(s), from notebook, validation: PENDING). |
| `Human validated/` | Findings Liz has read, checked against the run + data, corrected, and stands behind. **Agents never write here.** |

## The integrity boundary

Only Liz promotes a draft from `Agent Drafts/` into `Human validated/`. The **diff** between the
two is the record of human judgment applied. An agent that promotes its own draft has forged the
one signal this boundary exists to produce.

## How an app result becomes a finding

1. An app run exports a figure/result and writes a row in `docs/PROVENANCE.md` (+ its own
   `app.manifest.yaml` `derived`).
2. A notebook pulls that run by `run_id` and analyzes it.
3. A draft finding is written to `Agent Drafts/findings/` with a provenance header.
4. Liz reviews, corrects, and promotes it to `Human validated/findings/`; the app's manifest
   back-references the finding id in `derived.validated_findings`.
