# {{APP_NAME}} — UX + interaction notes

- The interaction loop is **param → run → render**. Keep the latency honest: if a server round
  trip makes dragging feel dead, move that one computation client-side (typed-array JS; WebGPU
  compute only if profiled-necessary) — not the whole core.
- Dispose Three.js geometries/textures/materials when regenerating a field on parameter change,
  or a long research session leaks GPU memory.
- Feature-detect `navigator.gpu`; keep a WebGL2 render fallback.
- Keep large absolute coordinates centered/normalized before GPU upload (float32 precision);
  the authoritative float64 data stays in `core/`.
- Show what is actually happening — no fake progress, no status that isn't backed by a run.
