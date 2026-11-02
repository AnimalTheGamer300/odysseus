# Odysseus — Architecture Reference

Generated 2026-11-01 by static analysis (`Sandbox/trace_odysseus.py` +
`Sandbox/gen_docs.py`). Companion machine-readable data lives in
[`docs/call-graph/`](call-graph/README.md) — **start there when changing code**:
it maps every function to its definition and all known call sites, every HTTP
route to its JS callers, and every module to its dependents.

## 1. What this is

Odysseus is a self-hosted AI chat/agent web app:

- **Backend:** Python 3, **FastAPI** (not Flask), served by uvicorn. Single
  process; SQLite via SQLAlchemy (`core/database.py`), ChromaDB for vectors
  (external service on port 8100, started by `run.sh` in a tmux session).
- **Frontend:** no-build SPA of native ES6 modules in `static/` (`app.js` is
  the orchestrator, `static/js/` holds feature modules, `static/index.html` is
  the shell). Vendored libs in `static/lib/` (highlight.js, katex, mermaid…).
- **LLM access:** multi-provider — OpenAI-compatible endpoints, local
  llama.cpp/LM Studio/Ollama-style servers, cloud providers — resolved in
  `src/llm_core.py` + `src/endpoint_resolver.py` + `src/model_discovery.py`.
- **Agent mode:** tool-calling loop in `src/agent_loop.py` with tool
  parsing/execution/security in `src/tool_*.py`, concrete tools in
  `src/tools/` and `src/agent_tools/`, MCP servers in `mcp_servers/`.

## 2. Size & composition (app code only)

| Area | Files | Lines (py/js/html) |
|---|---|---|
| `app.py` + `launcher.py` | 2 | 1,461 |
| `core/` | 10 | ~5,900 |
| `routes/` | ~45 | ~49,000 |
| `services/` | ~35 | ~10,600 |
| `src/` | ~100 | ~66,000 |
| `mcp_servers/` | 4 | ~3,500 |
| `static/` (app.js, sw.js, js/) | ~165 | ~170,000 (incl. vendored `lib/`) |
| `scripts/`, `companion/`, `integrations/` | ~24 | ~7,700 |
| `tests/` | ~850 | ~112,000 |

Excluded from analysis: `data/`, `data2/` (runtime data dirs), `venv/`,
`chroma*/`, `backups/`, `.backups/`, `.merge*`, `*.bak*`/`*.restored*` scratch
copies, `website/` (GitHub-Pages marketing site), `static/lib|fonts|icons`.

Static-analysis totals: **17,664 definitions** (13,006 py / 4,658 js),
**10,858 distinct called names**, **508 HTTP routes**, **1,327 JS API-URL
literals**. See `call-graph/INDEX.md`.

## 3. Entry points

- **Server:** `launcher.py` → `uvicorn.run(app, ...)` (line 149); `run.sh` /
  `re-run.sh` start ChromaDB (tmux) + SearXNG + the app. `python -m uvicorn
  app:app` also works. `app.py` builds the `FastAPI` app at module level.
- **App assembly:** `app.py` — lifespan at ~line 127, routers registered via
  `app.include_router(...)` from line 641 onward. Route modules expose
  `setup_*_routes(...)` factories (dependency injection of managers) or
  module-level `APIRouter`s (`*_router`).
- **Frontend:** `static/index.html` loads `static/app.js` (module), which
  imports all `static/js/*` feature modules and wires global listeners.
  `static/sw.js` is the service worker (cache/version tokens).
- **MCP servers:** `mcp_servers/{email,image_gen,memory,rag}_server.py`,
  managed by `src/mcp_manager.py`, exposed to the UI via `routes/mcp_routes.py`.

## 4. Directory map

| Dir | Responsibility |
|---|---|
| `app.py` | FastAPI app factory-ish module: middleware, exception handlers, static serving, router registration, page routes (`/`, `/notes`, `/calendar`, …) |
| `launcher.py` | Process launcher: env, uvicorn bind, warmups |
| `core/` | Cross-cutting: `database.py` (SQLAlchemy/SQLite), `auth.py` (AuthManager, users, API tokens), `session_manager.py` (chat sessions), `models.py`, `middleware.py` (security headers, root-path), `constants.py`, `atomic_io.py`, `exceptions.py` |
| `routes/` | One module (or subdir) per feature: `chat_routes.py`, `session_routes.py`, `memory_routes.py`, `gallery_routes.py`, `email_routes.py`, `mcp_routes.py`, `webhook_routes.py`, `task_routes.py`, … each with `setup_*_routes()` returning an `APIRouter` |
| `src/` | Business logic: `llm_core.py` (all LLM HTTP calls, streaming, caching, host health), `agent_loop.py` (`stream_agent_loop`), `chat_handler.py`/`chat_processor.py`/`chat_helpers.py`, `tool_*.py` (parsing, policy, security, approvals, execution, implementations, replay), `tools/` + `agent_tools/` (concrete tool impls), `memory*.py`, `rag_*.py`, `chroma_client.py`, `embeddings.py`, `document_processor.py`, `vision_preprocessing.py`, `upload_handler.py`, `settings.py`, `config.py`, `event_bus.py`, `bg_jobs.py`, `task_scheduler.py`, `research_handler.py`, `deep_research.py`, `mcp_manager.py`, `webhook_manager.py`, `search/`, `model_capability_readers/` |
| `services/` | Long-running/background helpers: `memory/`, `search/` (SearXNG), `shell/`, `stt/`, `tts/`, `youtube/`, `research/`, `docs/`, `faces/`, `hwfit/` |
| `mcp_servers/` | Standalone MCP servers (email, image gen, memory, RAG) |
| `static/` | SPA: `app.js` orchestrator, `js/` feature modules, `index.html` shell, `sw.js` service worker, `lib/` vendored |
| `scripts/` | One-off maintenance/migration scripts (not imported by the app) |
| `tests/` | pytest suite + some `.mjs` browser checks |
| `website/` | Marketing/docs site (separate from the app) |

## 5. Key end-to-end flows

### 5.1 Chat streaming (the main flow)

```
static/js/chat.js  sendMessage → fetch(`${API_BASE}/api/chat_stream`, POST form)
  → routes/chat_routes.py::chat_stream            (routes/chat_routes.py:1119)
    → src/chat_handler.py::ChatHandler.preprocess_message   (uploads, vision, memory cmds)
    → src/agent_loop.py::stream_agent_loop         (mode=agent: tool loop)
       → src/llm_core.py::*                         (httpx streaming call to provider)
       → src/tool_parsing.py / tool_execution.py::execute_tool_block
          → src/tool_implementations.py / src/tools/* / src/agent_tools/*
          → src/tool_security.py / tool_policy.py / tool_approvals.py (vetting)
    → src/llm_core.py streaming for mode=chat
  → StreamingResponse (SSE) back to chat.js → chatStream.js / chatRenderer.js render
```

JS callers of `/api/chat_stream`: `static/js/chat.js:2510`,
`static/js/group.js:855`, `static/js/compare/stream.js:243,409`,
`static/js/notes.js:4524,4595` (full list: `call-graph/http-endpoints.md`).

### 5.2 Uploads & vision

```
static/js/fileHandler.js → POST /api/upload*  → routes/upload_routes.py
  → src/upload_handler.py::UploadHandler (ids, limits, cleanup, refs)
  → src/vision_preprocessing.py::preprocess_image_for_vlm  (upscale/encode for VLM)
  → image bytes embedded in chat messages → src/llm_core.py vision call
  → src/chat_handler.py::_sync_upload_vision_to_gallery → routes/gallery_routes.py
```

### 5.3 Memory & RAG

```
routes/memory_routes.py → services/memory/* (extractor, skills, service)
  → src/memory.py::MemoryManager (SQLite) + src/memory_vector.py (Chroma)
routes/document_routes.py → src/document_processor.py → src/rag_manager.py
  → src/chroma_client.py → ChromaDB :8100
```

### 5.4 Conventions worth knowing

- **Route registration:** `setup_*_routes(deps...)` factories in `routes/`,
  wired in `app.py` via `app.include_router(...)`. Add a feature by writing a
  routes module + one `include_router` line.
- **Exception handlers:** `@app.exception_handler(...)` in `app.py:616-629`
  map `core/exceptions.py` types to JSON responses.
- **Auth:** `core/auth.py::AuthManager`; API tokens in DB (`core/database.py::ApiToken`);
  `routes/api_token_routes.py`. Frontend gets 401 → `app.js` redirects to `/login`.
- **Config:** `.env` loaded in `app.py` (`load_dotenv`), runtime paths in
  `src/runtime_paths.py`, settings in `src/settings.py`.
- **Frontend module contract:** each `static/js/*.js` exports functions; `app.js`
  exposes some on `window` for legacy reachability. See `static/js/MODULE_SUMMARY.md`.
- **Service worker:** `static/sw.js` caches assets with version tokens — bump
  when changing static files or the UI may serve stale JS.
- **Scratch copies:** the repo accumulates `*.bak-*` / `*.restored*` / `*.py1`
  files next to originals — they are NOT imported (excluded from analysis);
  don't edit them, edit the live file.

## 6. Where to look before changing something

1. `docs/call-graph/py/<module>.md` — every def in that module + **all call
   sites** (the "who else connects here" answer).
2. `docs/call-graph/module-deps-python.md` → "Reverse: dependents" — if you
   change module X, this lists every file that imports it.
3. `docs/call-graph/http-endpoints.md` — if you change a route path/handler,
   this lists the JS files that call it.
4. `docs/call-graph/dead-code.md` — defs with zero static callers. **Verify
   manually** (dynamic dispatch is invisible) before deleting.
5. `docs/call-graph/external-calls.md` — names that look called but are
   stdlib/third-party (don't chase them into the repo).

## 7. Regenerating this analysis

```bash
python3 /run/media/crao/BTnvme/LLM/Sandbox/trace_odysseus.py  # writes Sandbox/odysseus-trace.json
python3 /run/media/crao/BTnvme/LLM/Sandbox/gen_docs.py         # rewrites docs/call-graph/*
```

Caveats: Python side is AST-accurate; JS side is regex-based (approximate).
Call sites match by bare name, so same-named methods on different classes
merge — check the raw JSON's `obj` hint when in doubt.
