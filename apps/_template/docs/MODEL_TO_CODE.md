# {{APP_NAME}} — model → code

The standing "how we know this app models what it claims" doc (the epistemomechanics analogue of
the Interactive-LP-GUI `CURRICULUM_TO_SOLVER.md`). Keep it honest and current; mark maturity
frankly.

| Phenomenon / claim | How `core/` models it | Key assumptions / approximations | Code (file:line) | Maturity |
|---|---|---|---|---|
| _(what this app simulates)_ | _(the equations/algorithm)_ | _(what's idealized)_ | `core/simulate.py:run` | scaffolded |

Maturity ∈ `scaffolded` · `working` · `validated` — and must match `app.manifest.yaml`
`declared.maturity`. A claim marked above `scaffolded` needs a recorded run behind it
(`derived.last_run` non-null) or the contradiction is visible by design.
