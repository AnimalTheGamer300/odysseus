# Odysseus — File Map (what does what, and who it talks to)

> **Purpose:** the per-file companion to `docs/ARCHITECTURE.md`. ARCHITECTURE.md is the
> 10,000-foot view (layers, hot paths, landmines); THIS doc is the street map — every
> backend file, one line on what it does, one line on what it interacts with. New
> IRISes read this instead of re-grepping the whole tree.
>
> Repo: `odysseus-garboGH` · Base: upstream PRs ~#4983–#5290 · Map written: 2026-08-08
>
> House rules: lean, dense, pointer-heavy. If a file changes meaning, update its line
> here in the same breath. The changelog lives in `ODYSSEUS-CHANGES.md`; the frontend
> module map lives in `static/js/MODULE_SUMMARY.md`; tool docs live in `docs/TOOLS.md`.

---

## 0. How to use this map

- **Frontend questions** → `static/js/MODULE_SUMMARY.md` (already exhaustive). This doc
  only lists the top-level static files.
- **Backend questions** → the tables below. "Interacts with" = local imports (core/src/
  routes/services) + the data files/DBs it touches.
- **"Why does X misbehave?"** → start at `data/logs/app.log`, then `ODYSSEUS-CHANGES.md`
  (it documents every known bug + fix), then ARCHITECTURE.md §5 Landmines.
- **Sibling forks:** `odysseus.old` = previous upstream base (PRs ~#2548–#2989, the
  freeze-suspect); `odysseus.dev` = vanilla upstream checkout. garbo is the LIVE fork.

---

## 1. Top-level layout

```
odysseus-garboGH/
├── app.py                  FastAPI entry — wires 46 routers, middleware, lifespan
├── launcher.py             Windows-portable GUI launcher (splash, tray, browser)
├── run.sh                  THE start script: python3.11 venv, uvicorn on 127.0.0.1:7001
├── core/                   11 py files — foundation: auth, db, models, session manager
├── src/                    144 py files — the ENGINE: agent loop, LLM core, tools, memory
├── routes/                 73 py files — HTTP layer, one module per feature area
├── services/               40 py files — external wrappers: search, TTS/STT, docs, memory, hwfit
├── mcp_servers/            standalone MCP servers (email, memory, rag, image_gen)
├── companion/              additive LAN companion bridge (/api/companion/*)
├── integrations/           claude/ + codex/ — scoped API helpers for terminal agents
├── static/                 frontend: index.html + app.js + 113 js modules + sw.js
├── scripts/                CLI family: `odysseus` dispatcher + odysseus-* subcommands
├── tests/                  758 files — the test suite
├── docs/                   markdown docs + demo videos (house convention)
├── data/                   runtime data (gitignored): app.db, memory.json, settings.json, ...
├── data2/                  STALE duplicate of data/ (not referenced by code — ignore)
├── config/                 searxng settings.yml
├── docker/  Dockerfile  docker-compose*.yml   container deployment
├── .env                    live env config (secrets — never quote contents)
└── ODYSSEUS-CHANGES.md     changelog (82KB of every change + root cause — READ IT)
```

**Entry points:** `run.sh` → `python -m uvicorn app:app --host 127.0.0.1 --port 7001`
(venv python 3.11.15). `launcher.py` for the Windows portable build only.

---

## 2. `core/` — foundation (11 files)

| File | Does | Interacts with |
|---|---|---|
| `auth.py` | Multi-user auth: bcrypt password hashing, session tokens, TOTP, roles, config persistence (AuthManager) | core/database, src/settings; read by routes/auth_routes |
| `database.py` | SQLAlchemy engine + declarative models, SQLite via `data/app.db` (env `DATABASE_URL` overrides), PRAGMA foreign_keys=ON, TimestampMixin | core/models, src/runtime_paths; **the DB every ORM route hits** |
| `models.py` | Pure data models — dataclasses: `DbSession`, `ChatMessage`, `ModelEndpoint`, `ApiToken` | nothing (side-effect-free); imported by core + src + routes |
| `session_manager.py` | **All session business logic + DB ops** — create/delete/archive/rename sessions, add/truncate/replace messages, cleanup_empty_sessions. `add_message` rolls back the in-memory append + re-raises when persistence fails — a message can never live only in memory (2026-08-08). **Progressive draft checkpoint (2026-08-08):** `create_draft`/`update_draft`/`promote_draft`/`finalize_orphan_draft` — in-flight replies checkpoint to DB-only draft rows (metadata.draft, never in memory history), promoted IN PLACE on completion (same id, no duplicate); `_db_to_session` hydration finalizes orphan drafts as stopped partials and skips live ones so context never sees half-written replies | core/database, core/models, src/constants; used by ~every route module |
| `constants.py` | Backward-compat shim → re-exports `src/constants.py` | src/constants (single source of truth) |
| `atomic_io.py` | Atomic JSON file writes (temp + rename) | used by anything writing JSON state files |
| `exceptions.py` | Custom exception classes for the app | imported across core/src/routes |
| `log_safety.py` | Keeps secrets/tokens out of log lines | used by route + engine logging paths |
| `middleware.py` | SecurityHeaders + AuthMiddleware (FastAPI/Starlette middleware) | app.py mounts it; auth via core/auth |
| `platform_compat.py` | Cross-platform helpers: safe_chmod, IS_WINDOWS, signal handling | core/database, services |
| `__init__.py` | "Chat Core" package marker | — |

---

## 3. `src/` — the engine (144 files, grouped)

### 3.1 Config & constants

| File | Does | Interacts with |
|---|---|---|
| `constants.py` | **Single source of truth** for app-wide constants: limits, dirs, defaults. `DATA_DIR` = env `ODYSSEUS_DATA_DIR` or `<root>/data` | everything imports this |
| `src/config.py` | Legacy config helpers (reads constants/env) | src/constants, data files |
| `settings.py` | Centralized settings + features: `load_settings/save_settings/get_setting`, per-user keys, feature flags | `data/settings.json`, core/auth; routes/settings consumers |
| `settings_scrub.py` | Strips secrets from settings before non-admin exposure | src/settings, routes |
| `runtime_paths.py` | Resolves app root + data dir in source vs frozen (PyInstaller) builds | src/constants, core/database |
| `request_models.py` | Pydantic request/response models | routes (FastAPI bodies) |
| `secret_storage.py` | Encrypted-ish secret storage helpers | core, routes/settings |

### 3.2 Chat pipeline (the hot path)

| File | Does | Interacts with |
|---|---|---|
| `chat_handler.py` | Handler for chat endpoint operations — builds context, calls LLM | core/models, src/chat_helpers, src/document_processor, src/youtube_handler; routes/chat_routes |
| `chat_helpers.py` | URL extraction, message/upload validation, request parsing | used by chat routes + handler |
| `chat_processor.py` | Post-processing: markdown, sanitization, thinking-block handling | src/llm_core output; frontend rendering |
| `agent_loop.py` | **The agent engine** (~5k lines): classifies intent, assembles prompts, runs tool rounds, streams, compacts context, saves messages. The `_assemble_prompt`/tool-policy core | core, routes, services, src/*; THE file IRIS edits most |
| `llm_core.py` | **LLM transport layer**: OpenAI-compat/Ollama/native calls, streaming, caching, degenerate-stream guard, Kimi/UA handling, host-death tracking | httpx, src/agent_loop; all model calls route through here |
| `model_context.py` | Model context building: endpoint resolution, capability gating, message shaping. `get_context_length` resolution order: settings override (`model_context_overrides` — user-pinned windows beat the table/endpoint) → cache → known table → endpoint /models → DEFAULT_CONTEXT (2026-08-09). `estimate_tokens` counts content + tool_calls + reasoning pass-backs (metadata.thinking/reasoning_content) | core, src/agent_loop, src/llm_core |
| `context_compactor.py` | Token-budget compaction when context exceeds limits (force_threshold_tokens); `_map_convo_split_to_history` maps the split onto `session.history` by `_db_id` so recent turns can't be dropped (2026-08-08) | core (session_manager.replace_messages), src/agent_loop |
| `context_budget.py` | Adaptive input-token budget for the agent loop (#1170) | src/agent_loop |
| `ai_interaction.py` | AI-to-AI tools shared plumbing: `_resolve_model`, session-manager singleton, dispatch_ai_tool, pipeline/debate manager | core, routes, src/agent_tools |
| `teacher_escalation.py` | Teacher-escalation loop for self-hosted models (anchored multiline failure regexes) | src/agent_loop, routes/chat_routes |
| `action_intents.py` | Lightweight routing hints for chat requests that need tools | routes/chat_routes, src/agent_loop |
| `chatgpt_subscription.py` | ChatGPT subscription / Codex backend OAuth helpers | core, routes/chatgpt_subscription_routes |
| `copilot.py` | GitHub Copilot provider support | httpx; routes/copilot_routes |

### 3.3 Tool system

| File | Does | Interacts with |
|---|---|---|
| `tool_schemas.py` | The tool schema catalog (967 lines — 39 tools after slimming) | src/agent_loop prompt assembly |
| `tool_implementations.py` | Tool handler registry facade | src/agent_tools/*, src/tools/* |
| `tool_execution.py` | Executes fenced tool blocks: parse → policy → run → transcript caps (4000-char output, 200-event cap) | src/agent_loop, src/tool_* |
| `tool_parsing.py` | Parses LLM fenced tool calls; `_ALLOW_MID_REPLY_FENCES`, trailing-fence walk-back | src/agent_loop |
| `tool_policy.py` | Per-turn tool policy composition (what's allowed this turn) | src/agent_loop, src/tool_security |
| `tool_security.py` | Server-side tool safety policy: workspace confinement, dangerous-path deny | core, src/tool_execution |
| `tool_utils.py` | Import-free helpers for tool output shaping | src/tool_* |
| `tool_index.py` | RAG-based tool selection for agent mode (currently superseded by tools_doc) | numpy, src/tool_schemas |
| `tools_doc.py` | Always-on tool documentation (RAG selection permanently disabled) | src/tool_schemas, prompt assembly |
| `builtin_actions.py` | Builtin action handlers (diff, email, sqlalchemy etc.) | core, routes, services, src |
| `agent_tools/__init__.py` | Facade for the agent-tool registry (TOOL_HANDLERS) | src/tools/*, src/agent_tools/* |
| `agent_tools/admin_tools.py` | Config/integration admin tools | core, src/settings, src/integrations |
| `agent_tools/bg_job_tools.py` | Inspect/control detached background bash jobs | src/bg_jobs, src/bg_monitor |
| `agent_tools/coding_tools.py` | Coding-domain agent tools (search/apply patches) | json/os/re |
| `agent_tools/document_tools.py` | Document CRUD agent tools | core/database, src/document_* |
| `agent_tools/filesystem_tools.py` | File read/write/edit agent tools | src/tool_security, workspace |
| `agent_tools/interaction_tools.py` | ask_user / confirm tools | src/interactive_gate |
| `agent_tools/model_interaction_tools.py` | chat_with_model / ask_teacher / list_models | src/ai_interaction, httpx |
| `agent_tools/session_tools.py` | create_session / list_sessions / send_to_session / manage_session | core/session_manager, src/ai_interaction |
| `agent_tools/subprocess_tools.py` | Subprocess/bash agent tools | src/tool_security, pty |
| `agent_tools/web_tools.py` | web_search / web_fetch agent tools | services/search, services/youtube |
| `tools/__init__.py` | Tool implementation package split by domain (slice 1, #4082/#4071) | src/tool_implementations |
| `tools/_common.py` | Shared helpers across tool domains | core, src |
| `tools/calendar.py` | Calendar-domain tool impls | routes/calendar_routes, SQLite |
| `tools/contacts.py` | Contacts-domain tool impls | routes/contacts_routes, CardDAV |
| `tools/cookbook.py` | Cookbook (model serving) tool domain | routes/cookbook_routes, serve lifecycle |
| `tools/image.py` | Image-domain tool impls | httpx, gallery |
| `tools/notes.py` | Notes-domain tool impls | routes/note_routes |
| `tools/research.py` | Research-domain tool impls | src/research_*, trigger_research |
| `tools/search.py` | Search-domain tool impls | services/search |
| `tools/system.py` | System-domain tool impls (settings, endpoints, health) | core, routes, services, src |
| `tools/vault.py` | Vault-domain tool impls | src/secret_storage, vault files |

### 3.4 Memory, skills, RAG

| File | Does | Interacts with |
|---|---|---|
| `memory.py` | Core memory store: CRUD on `data/memory.json`, extraction, search | data/memory.json; routes/memory, services/memory |
| `memory_provider.py` | Interfaces for native + external memory systems | services/memory |
| `memory_vector.py` | Vector store for memory (embeddings) | src/embeddings, data/memory_vectors |
| `embedding_lanes.py` | Embedding lane orchestration | src/embeddings |
| `embeddings.py` | fastembed + remote embedding calls | fastembed, numpy, httpx |
| `rag_manager.py` | RAG manager: index, query personal docs | src/rag_vector, services/docs, data/rag |
| `rag_singleton.py` | App-wide RAG singleton | src/rag_manager |
| `rag_vector.py` | ChromaDB/vector ops for RAG | numpy, chromadb, data/chroma |
| `chroma_client.py` | ChromaDB client wrapper | chromadb, socket |
| `index_walk.py` | Directory-walk pruning for personal-doc indexing (#5559) | src/personal_docs |
| `personal_docs.py` | Personal document ingestion pipeline | pypdf, data/personal_docs |
| `session_search.py` | Shared transcript search (UI + agent tools) | core/database, FTS |
| `topic_analyzer.py` | Conversation topic analysis (deduped from app.py) | — |

### 3.5 Documents & files

| File | Does | Interacts with |
|---|---|---|
| `document_processor.py` | PDF/OCR extraction, text handling, image VL analysis, user content building | pypdf, PIL, data/uploads |
| `document_actions.py` | Document action helpers (AI edits etc.) | core, src |
| `office_doc.py` | Auto-create Document row from Office attachment | src/document_*, routes |
| `pdf_forms.py` | PDF AcroForm field detection/extraction | fitz (PyMuPDF) |
| `pdf_form_doc.py` | Bridge extracted form fields → document editor | src/document_* |
| `pdf_runtime.py` | Optional PDF runtime dep helpers | fitz |
| `markitdown_runtime.py` | Optional markitdown doc-extraction dep helpers | markitdown |
| `upload_handler.py` | Upload processing: validation, image handling, dedupe | PIL, python-magic, data/uploads |
| `upload_limits.py` | Route-local upload size caps | fastapi |
| `attachment_refs.py` | Attachment reference helpers for chat storage + tool manifests | — |
| `generated_images.py` | Generated-image path helpers | data/generated_images |

### 3.6 Tasks, calendar, email

| File | Does | Interacts with |
|---|---|---|
| `task_scheduler.py` | Background scheduler for ScheduledTask execution (croniter) | core/database, routes/task_routes, data/scheduled_emails.db |
| `task_endpoint.py` | Resolver for background-task AI endpoints | src/constants |
| `task_action_policy.py` | Privilege policy for scheduled task actions | core, src |
| `caldav_sync.py` | CalDAV → local SQLite sync | caldav, icalendar, core/database |
| `caldav_writeback.py` | Push local calendar changes out to remote CalDAV (#800) | caldav, icalendar, core |
| `email_thread_parser.py` | Email thread parsing for summaries | bs4 |
| `reminder_personas.py` | Server-side mirror of built-in reminder characters | — |
| `assistant_log.py` | Assistant run log | data/logs |

### 3.7 Services & infra

| File | Does | Interacts with |
|---|---|---|
| `app_initializer.py` | Initialize all app components + dependencies at startup | core, services, src; called by app.py lifespan |
| `app_helpers.py` | FastAPI app helpers (static, error handlers) | fastapi, starlette |
| `auth_helpers.py` | Shared auth helpers used by all route files | core/auth |
| `event_bus.py` | Async event bus for cross-module events | core |
| `endpoint_resolver.py` | Unified endpoint resolution (LLM hosts, ports) | core, subprocess, socket |
| `model_discovery.py` | Model catalog discovery/scans | httpx, subprocess |
| `model_capabilities.py` | Canonical model capability metadata helpers | src/model_capability_readers |
| `model_capability_readers/` | Vendor readers: openai, google, ollama, lmstudio, llamacpp, openrouter, generic_openai | src/model_capabilities |
| `image_model_ids.py` | Recognize image-generation model IDs | — |
| `service_health.py` | Consolidated service health / degraded-state reporting | core, routes, httpx |
| `readiness.py` | Local-instance readiness/integrity self-check | core, sqlalchemy |
| `rate_limiter.py` | Generic in-memory sliding-window rate limiter (by IP) | — |
| `interactive_gate.py` | Foreground-activity gate for background work | routes, src |
| `bg_jobs.py` | Background job execution for the agent's bash tool | core |
| `bg_monitor.py` | Always-on monitor auto-continuing agent on bg job completion | src |
| `cleanup_service.py` | Periodic cleanup (sessions, temp files) | src |
| `session_actions.py` | Session action helpers (retitle, archive etc.) | core, src |
| `session_image_cleanup.py` | Cleanup images attached to chat sessions | core, sqlalchemy |
| `cookbook_serve_lifecycle.py` | Kills scheduler-owned serves whose time is up | core, src |
| `webhook_manager.py` | Outgoing webhooks — fires HTTP POSTs on events (HMAC-signed) | httpx, src |
| `host_docker_access.py` | Policy checks for host Docker access from a container | — |
| `tls_overrides.py` | Extended TLS trust store for private-CA LLM providers | ssl |
| `url_safety.py` | Outbound URL safety (SSRF hardening) | ipaddress, socket |
| `url_security.py` | URL validation for server-side outbound requests | — |
| `prompt_security.py` | Prompt-injection hardening helpers | — |
| `text_helpers.py` | Text-cleanup helpers across LLM-output paths | — |
| `user_time.py` | Per-request user-local time helpers | zoneinfo |
| `optional_deps.py` | Compatibility helpers for optional third-party deps | torchvision |
| `exceptions.py` | Shim → core/exceptions.py | core |
| `src/database.py` | Shim → core/database.py | core |
| `src/integrations.py` | Third-party integration registry (API budget system) | core, httpx |
| `preset_manager.py` | Character/preset manager (data/presets.json) | core, data/presets.json |
| `api_key_manager.py` | API key storage/rotation | core, data |
| `youtube_handler.py` | Compatibility wrapper → services/youtube | services/youtube |

### 3.8 Research

| File | Does | Interacts with |
|---|---|---|
| `deep_research.py` | IterResearch-style deep research engine | src, asyncio |
| `research_handler.py` | Research service integration with expandable UI | src/research_utils, routes/research |
| `research_utils.py` | Shared research utilities | src |
| `goal_based_extractor.py` | Goal-based content extraction prompt (Alibaba Tongyi style) | — |
| `visual_report.py` | Self-contained styled HTML page from research results | data/deep_research |

---

## 4. `routes/` — the HTTP layer (73 files)

**Pattern:** most top-level `routes/X_routes.py` are **backward-compat shims** that
re-export from a canonical subpackage (`routes/X/X_routes.py`) — see the "slice 2"
refactor (#4082/#4071). Canonical homes live in subdirectories.

### 4.1 Canonical route packages (the real code)

| Package | Does | Interacts with |
|---|---|---|
| `admin_wipe/admin_wipe_routes.py` | Admin Danger Zone — per-category wipes | core, src, filesystem |
| `cleanup/cleanup_routes.py` | Cleanup operations API | src |
| `compare/compare_routes.py` | Model A/B comparison | core, routes, src |
| `contacts/contacts_routes.py` | CardDAV contacts CRUD + import/export | core, src, httpx |
| `gallery/gallery_routes.py` | Photo/AI-image library + edits (upscale, rembg, inpaint) | core, src, PIL, gfpgan, basicsr |
| `gallery/gallery_helpers.py` | Gallery helpers/models | src, PIL |
| `history/history_routes.py` | **Session history, truncation, fork, topics** — canonical exact-id delete (delete-messages ~355-395, NO pair resolution — 2026-08-08); truncate supports `keep_through_id` (regenerate keeps the user row, deletes only the AI tail); merge-last-assistant removes hidden continue-handshake user rows (`_CONTINUE_HANDSHAKE_MARKERS`: user-stop / auto-recover / step-limit texts — 2026-08-08). **Draft-row policy (2026-08-08 draft-checkpoint):** `_entry_or_none`/`_finalize_or_hide_draft` — live drafts (active stream) hidden from paged history + hydration, orphan drafts (server died mid-turn) finalized to stopped partials and shown | core, routes, src |
| `memory/memory_routes.py` | Memory CRUD/search API | services, src |
| `note/note_routes.py` | Google-Keep-style notes/checklists | core, routes, src |
| `research/research_routes.py` | Research background tasks — /api/research/* | core, src |

### 4.2 Top-level route modules (live code, no shim)

| File | Does | Interacts with |
|---|---|---|
| `_validators.py` | Shared FastAPI validators | fastapi |
| `api_token_routes.py` | /api/tokens/* — API token management | core/auth, bcrypt |
| `assistant_routes.py` | Personal assistant singleton, read/write assistant config | core, src |
| `auth_routes.py` | Login, logout, signup, status, user management, 2FA | core/auth, qrcode |
| `backup_routes.py` | Export/import user data (memories, presets, settings, skills) | routes, src |
| `calendar_routes.py` | Local SQLite calendar CRUD | core, src, icalendar |
| `chat_helpers.py` | Shared chat-route helpers: context building, post-response tasks. `build_chat_context` returns `user_message_id` (persisted user row id — frontend stamps the optimistic bubble) + `reuse_last_user` mode (regenerate reuses the existing user row, no re-send — 2026-08-08). `save_assistant_response(..., draft_id=)` promotes a checkpointed draft IN PLACE instead of inserting a fresh row (2026-08-08 draft-checkpoint) | core, routes, services, src |
| `chat_routes.py` | **/api/chat, /api/chat_stream, /api/inject_context, /api/search** — the main SSE endpoint; emits `user_message_saved` (first event — stamps the optimistic user bubble) + accepts `reuse_last_user` form field (2026-08-08); `_persist_stream_partial` saves every unfinished-turn branch (disconnect / upstream error / no-[DONE] end) with reasoning preserved in metadata.thinking (2026-08-08). **Progressive draft checkpoint (2026-08-08 draft-checkpoint):** `_checkpoint_draft` + nested `_checkpoint()` in `stream_with_save` write the in-flight reply to a DB-only draft row (early create ≥150 chars, then 4s cadence), emit `draft_saved` (bubble stamps its row id early), and promote the draft on [DONE]/partial-save — same id, no duplicate | core, routes, src |
| `chatgpt_subscription_routes.py` | ChatGPT subscription device-flow setup | routes, src |
| `codex_routes.py` | Codex integration routes | core, routes, src |
| `cookbook_helpers.py` | Cookbook validators/helpers | core, src |
| `cookbook_output.py` | Cookbook task-output shaping | — |
| `cookbook_routes.py` | Model download, serve, cache scan, state sync | core, routes, services, src |
| `copilot_routes.py` | GitHub Copilot device-flow login | routes, src |
| `device_flow.py` | Shared OAuth/device-flow scaffolding | — |
| `diagnostics_routes.py` | /api/db/stats, /api/rag/stats, /api/test/youtube, /api/test-research | core, src |
| `document_helpers.py` | Pydantic models, doc serializers, owner gating | core, src |
| `document_routes.py` | Document CRUD with version history | core, routes, src |
| `editor_draft_routes.py` | Persisted gallery-editor drafts | src |
| `email_helpers.py` | Email IMAP/SMTP helpers | core, routes, src, imaplib |
| `email_pollers.py` | Email polling (inbox refresh, urgency) | core, routes, src |
| `email_routes.py` | Email inbox/triage/tags/summaries | core, routes, src, docx |
| `embedding_routes.py` | Local fastembed models + custom endpoints | core, src |
| `emoji_routes.py` | Emoji data routes | src |
| `font_routes.py` | Custom font discovery (static/fonts/custom) | fastapi |
| `hwfit_routes.py` | Hardware-fit computation | routes, services/hwfit |
| `mcp_routes.py` | MCP server management | core, src/mcp_manager |
| `model_routes.py` | Model/provider management | core, routes, src |
| `personal_routes.py` | Personal documents management | core, src |
| `prefs_routes.py` | Per-user key/value prefs (JSON-backed) | src |
| `preset_routes.py` | /api/presets + custom templates CRUD | core, src |
| `search_routes.py` | /api/search/config, /api/search | services/search |
| `session_routes.py` | **Session CRUD + PATCH /session/{sid}** (rename ~461) | core, src |
| `shell_routes.py` | User-facing command execution endpoint | core, routes, src, pty |
| `signature_routes.py` | Saved visual signatures CRUD | src |
| `skills_routes.py` | REST API for the Skills system | routes, services, src |
| `stt_routes.py` | Multi-provider STT (Whisper/API/browser) | services/stt |
| `task_routes.py` | Scheduled task CRUD | core, src, croniter |
| `tts_routes.py` | Multi-provider TTS (Kokoro/API/browser) | services/tts |
| `upload_routes.py` | File upload endpoint | core, src, PIL |
| `vault_routes.py` | Vault file management | core |
| `webhook_routes.py` | Webhook + API token + sync chat routes | core, src |
| `workspace_routes.py` | Browse server dirs to pick a tool workspace | src |

**Shims (just re-export, don't edit):** `admin_wipe_routes.py`, `cleanup_routes.py`,
`compare_routes.py`, `contacts_routes.py`, `gallery_routes.py`, `gallery_helpers.py`,
`history_routes.py`, `memory_routes.py`, `note_routes.py`, `research_routes.py`.

---

## 5. `services/` — external wrappers (40 files)

| Module | Does | Interacts with |
|---|---|---|
| `docs/` | Personal document RAG service (ChromaDB) | src/rag_*, data/chroma |
| `faces/` | Face detection + embedding worker | — |
| `hwfit/` | Hardware-fit: `hardware.py` (detect), `models.py` (registry), `profiles.py` (llama.cpp serve profiles), `hf_discovery.py`, `fit.py`, `image_models.py` | core, services, subprocess |
| `memory/` | Memory service: `service.py`, `memory_extractor.py` (fact extraction), `memory_vector.py`, `skills.py` (storage), `skill_format.py` (SKILL.md parser/writer), `skill_extractor.py`, `skill_importer.py` (GitHub import) | src, routes, core |
| `research/` | Deep research service (`service.py`, `research_handler.py`) | src, data/deep_research |
| `search/` | Web search: `core.py` (orchestrators), `providers.py` (SearXNG/Brave/DDG/Google PSE/Tavily/Serper), `content.py` (fetch+PDF), `cache.py` (LRU), `query.py`, `ranking.py`, `analytics.py`, `service.py` | httpx, config/searxng |
| `shell/` | Safe command execution service | pty |
| `stt/` | Multi-provider STT (faster-whisper, API, browser) | torch, httpx |
| `tts/` | Multi-provider TTS (Kokoro, API, browser) | torch, kokoro, numpy |
| `youtube/` | YouTube transcript extraction + comments (yt-dlp, youtube_transcript_api) | — |

---

## 6. `mcp_servers/` — standalone MCP servers

| File | Does | Interacts with |
|---|---|---|
| `email_server.py` | MCP email server (IMAP/SMTP tools) | core, routes, src, mcp |
| `memory_server.py` | MCP memory server | src/memory |
| `rag_server.py` | MCP RAG server | src/rag_* |
| `image_gen_server.py` | MCP image-generation server | src, httpx |

---

## 7. `companion/` + `integrations/`

| File | Does | Interacts with |
|---|---|---|
| `companion/routes.py` | Additive LAN companion bridge — /api/companion/* | companion/pairing, core |
| `companion/pairing.py` | Pairing helpers (QR codes) | core, qrcode |
| `integrations/claude/skills/odysseus/` | Claude Code skill: `SKILL.md` + `integrations/claude/skills/odysseus/scripts/odysseus_api.py` scoped API helper | HTTP → app |
| `integrations/codex/` | Codex terminal integration: `integrations/codex/scripts/odysseus_api.py` + README | HTTP → app |

---

## 8. `scripts/` — CLI family

`scripts/odysseus` is a `git`-style dispatcher: finds `odysseus-<name>` siblings and
forwards args. Symlink it onto PATH (`ln -s $PWD/scripts/odysseus ~/.local/bin/odysseus`).

Subcommands (each a thin CLI over the matching feature): `odysseus-{backup, calendar,
contacts, cookbook, docs, gallery, logs, mail, mcp, memory, notes, personal, preset,
research, sessions, signature, skills, tasks, theme, webhook}`. Shared scaffolding in
`scripts/_lib/`. Utility scripts (not CLI): `add_hwfit_models.py`, `hf_download.py`,
`index_documents.py`, `update_database.py`, `fix_paths.py`, `pr_blocker_audit.py`,
`agent_migration_manifest.py`, `backfill_model_release_dates.py`, `import_from_vllm_recipes.py`,
`migrate_faiss_to_chroma.py`, `claim_ownerless.py`, `diffusion_server.py`, `mlx_image_server.py`,
`check-docker-*.sh`, `encode_previews.sh`, `demo_email/`.

---

## 9. `static/` — frontend (see MODULE_SUMMARY.md for the full module map)

| File | Does |
|---|---|
| `index.html` | SPA shell — loads app.js + versioned modules, DOM skeleton |
| `app.js` | Orchestrator: imports ~35 modules, bootstrap, event wiring, 401→/login |
| `sw.js` | Service worker — network-first JS/CSS, **versioned cache name** (bump on JS changes!) |
| `style.css` | All styles (incl. .old transplant caps) |
| `login.html` | Login page |
| `js/` | 113 ES modules — chat.js (the monster; consumes `user_message_saved`, exact-id delete, send-entry flag capture so pending-flow flags can't leak), sessions.js, chatRenderer.js (hides Regenerate when the response's own user message is gone), streamingRenderer.js, cookbook*.js, document.js, editor/, compare/, ... (full map in MODULE_SUMMARY.md) |
| `lib/` | Vendored libs (markdown, hljs, etc.) |
| `fonts/`, `icons/`, `manifest.json` | Assets |

**Version-token discipline:** module URLs carry `?v=...` tokens; keep index.html, app.js,
and static imports in lockstep (split-brain bug class — see ARCHITECTURE.md §5).

---

## 10. `data/` — runtime data (gitignored)

| Path | What lives there |
|---|---|
| `app.db` | **The SQLite DB** — sessions, messages, documents, tasks, users (env `DATABASE_URL` overrides) |
| `sessions.json` | Legacy session metadata (superseded by DB; still referenced by config shims) |
| `memory.json` | The AI memory store (user facts — IRIS's own memory) |
| `settings.json` | Central settings + feature flags |
| `presets.json` | Character/persona presets |
| `auth.json` | Auth state (tokens) |
| `scheduled_emails.db` | Scheduled email queue |
| `logs/` | **app.log — check FIRST on any 502/error** (+ rotated app.log.N) |
| `skills/` | Skill library (SKILL.md files) |
| `uploads/`, `personal_uploads/`, `mail-attachments/` | Uploaded files |
| `personal_docs/` | Personal document corpus for RAG |
| `rag/`, `chroma/`, `memory_vectors/`, `fastembed_cache/` | Vector/embedding stores |
| `generated_images/`, `tts_cache/`, `emoji_cache/` | Generated/cached media |
| `deep_research/` | Research job outputs |
| `agent/`, `agent_todos/`, `partials/` | Agent run state |
| `projects/` | Workspace/project folders |
| `huggingface/`, `llama.cpp/`, `llama-mirror.git/` | Model downloads/mirror |
| `server.pid` | Running server PID |

`data2/` is a **stale duplicate** (older layout, not referenced by code) — ignore it.
`logs/garbo.log` at repo root is a separate older log.

---

## 11. Key flows (short version — details in ARCHITECTURE.md §4)

1. **Send a message:** chat.js `handleChatSubmit` → POST `/api/chat_stream` (FormData;
   `reuse_last_user=true` on regenerate — reuses the existing user row). Pending-flow
   flags (continue/regen/edit) are captured + cleared at send entry so an aborted send
   can't leak them into the next one → SSE events, **first event `user_message_saved`**
   (stamps the optimistic user bubble with its DB id — delete/regen target by id) →
   chat_routes → chat_handler → agent_loop (intent classify → prompt assemble →
   llm_core stream → tool rounds) → frontend streamingRenderer.
2. **Agent tool call:** agent_loop emits fenced block → tool_parsing → tool_policy →
   tool_execution → tool_implementations → domain impl (agent_tools/* or tools/*) →
   transcript caps → next round.
3. **Memory save:** agent saves fact → src/memory → `data/memory.json` (+ vector).
4. **Research:** research_routes → research_handler → deep_research → services/research →
   visual_report → data/deep_research → frontend research panel.
5. **Session ops:** routes/session_routes + routes/history → core/session_manager →
   core/database → `data/app.db`.

---

## 12. Conventions & landmines (full list in ARCHITECTURE.md §5-7)

- **Backup before touching anything an app runs on:** `cp file file.bak-<date>`.
- **Changelog:** append every change to `ODYSSEUS-CHANGES.md`, dated, with root cause.
- **Version tokens** on JS module URLs; bump cache name in sw.js when precache changes.
- **Provider 502s ≠ app bugs** — check `data/logs/app.log` + endpoint billing first.
- **Dirty files (don't assume pristine):** `src/agent_loop.py`, `src/llm_core.py`,
  `src/model_context.py` were pre-modified before 2026-08-05.
- **`.old`'s resumeStream is the freeze suspect** — don't port it wholesale.
- **The boop counter:** boop-variants (boob/bool/boot/...) mean "continue". Canon.
