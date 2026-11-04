# Odysseus call-graph & architecture reference

Purpose: so a future session (human or AI) can see **where every function is
defined and who calls it** before changing anything — instead of discovering
the hard way that `src/llm_core.py::foo()` is also called from
`routes/chat_routes.py` and `src/agent_loop.py`.

## What's here

| File | Contents |
|---|---|
| `INDEX.md` | stats, layout, top hub functions |
| `py/<module>.md` | per Python module: defs + call sites (file:line) |
| `js/<module>.md` | per JS module: defs + call sites |
| `http-endpoints.md` | all FastAPI routes → handler → JS fetch callers |
| `module-deps-python.md` | py import edges + reverse dependents |
| `module-deps-js.md` | js import edges + reverse dependents |
| `dead-code.md` | defs with no static callers (candidates, not proof) |
| `external-calls.md` | most-called names that aren't defined locally |
| `../ARCHITECTURE.md` | human-readable architecture overview |

## Scope & exclusions

In scope: `app.py`, `launcher.py`, `core/`, `routes/`, `services/`, `src/`,
`mcp_servers/`, `scripts/`, `companion/`, `integrations/`, `tests/`,
`static/app.js`, `static/sw.js`, `static/js/`.

Excluded: `data/`, `data2/`, `venv/`, `chroma*/`, `backups/`, `.backups/`,
`.merge*`, `static/lib|fonts|icons` (vendored), `website/` (marketing site),
`*.bak*` / `*.restored*` / `*.py1` scratch copies, `__pycache__`.

## Caveats (read before trusting)

- Python defs/calls are AST-accurate. JS defs/calls are **regex-based** —
  method detection is approximate; treat as a hunting aid, not gospel.
- Call sites match by **name only** — `obj.foo()` matches any `foo`. Overloads
  across classes will merge. Check the `obj` hint in the raw JSON.
- Dynamic dispatch is invisible: `getattr`, decorator registries, FastAPI
  route handlers, `window.*` globals, string-based event names.
- Route paths get the file's first `APIRouter(prefix=...)`; routers built with
  unusual patterns may show unprefixed paths.

## Regenerating

```bash
python3 /run/media/crao/BTnvme/LLM/Sandbox/trace_odysseus.py   # -> odysseus-trace.json
python3 /run/media/crao/BTnvme/LLM/Sandbox/gen_docs.py          # -> docs/call-graph/*
```
