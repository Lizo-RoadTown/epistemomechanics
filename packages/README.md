# packages — shared code reused across apps

Logic that more than one app needs lives here, imported — never copied. Reuse across apps is the
test of a correct boundary: if a second app can't adopt a package's shape unchanged, the boundary
is drawn wrong (fix it, don't fork). The reciprocal also fails: a package so abstract no real app
fits it. Validate a package by actually using it in app #2.

| Package | Concern |
|---|---|
| `viz-core/` | Shared 3D / rendering / interaction primitives (Three.js / r3f helpers, colormaps, camera/controls, field + point-cloud renderers). |
| `sim-core/` | Shared numeric / simulation kernels usable by any app's `core/` (integrators, reductions, common models). |

Barebones: each starts as a stub README. Promote code into a package the moment the second app
would otherwise copy it.
