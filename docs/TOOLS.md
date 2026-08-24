# Odysseus tool reference

Full descriptions for every tool the assistant can call. The system prompt carries a one-line summary of each tool; read this file for the complete usage details (examples, parameters, caveats).

## Builtin tools

### bash

```bash
<shell command>
```
Run any shell command. Output is returned to you. Use for: installing packages, checking files, git, system info, process management, etc.
Do NOT use bash/curl for web lookup/search/latest/current requests when `web_search` or `web_fetch` is available.
NEVER use bash to create or change files — no `>`/`>>` redirects, no heredocs (`cat > f << 'EOF'`), no `tee`, `sed -i`, `awk -i`, no `python -c` that writes. To CREATE or fully rewrite a file use `write_file`; to change part of an existing file use `edit_file`. Those show a diff and are the ONLY allowed way to write files. (bash is for read-only inspection: `ls`, `cat` to READ, `grep`, `git status`/`git diff`, builds, installs.)
For LONG-running commands (package installs, pip/npm, ffmpeg, model downloads, training, builds — anything that may take more than ~20s), make the FIRST line `#!bg` to run it in the BACKGROUND. You get a job id back immediately and are automatically re-invoked with the full output when it finishes — so you never block the chat waiting. Example:
```bash
#!bg
pip install openai-whisper
```
SANDBOX LIMITS: stdin/stdout are pipes, so there is NO interactive terminal — `input()`, `curses`, `termios`, `pygame`, and `tkinter` will all fail. Don't try to RUN interactive terminal games or GUI apps here — verify syntax (`python -c "import py_compile; py_compile.compile('x.py')"`) and tell the user to run it themselves in their own terminal. For anything the USER should play/use interactively (games, UIs, demos), prefer a single self-contained HTML file with `<canvas>` + inline JS — save it via `create_document` with language="html" and tell the user to hit the Run / Preview button (▶) in the document editor toolbar; it renders inline in a sandboxed iframe so the game is playable right there. Works from any machine that can reach the Odysseus UI — no need to copy files out.
NEVER pipe multi-line Python through `python -c "..."` — shell quoting eats real newlines and `\n` arrives as literal backslash-n, which Python parses as a line-continuation error on line 1. To run multi-line code, either use the dedicated `python` tool block above, or save to a file first with a quoted HEREDOC (`cat > /tmp/x.py << 'EOF' ... EOF`) and then `python /tmp/x.py`.

**Parameters:**
- `command` (string) — The shell command to execute

Required: `command`

### python

```python
<python code>
```
Execute Python code. Use for computation, data processing, scripting. NOT for writing code for the user (use create_document for that). Same sandbox limits as bash — no TTY, no GUI, no `input()`; for anything the user should interact with, generate a single HTML file with inline JS instead.
Prefer a dedicated tool whenever one fits the job (reading, searching, or writing files); use python only for computation/processing no dedicated tool covers - not for reading or writing files.
Do NOT use Python/requests for web lookup/search/latest/current requests when `web_search` or `web_fetch` is available.

**Parameters:**
- `code` (string) — Python code to execute

Required: `code`

### web_search

```web_search
<search query>
```
Or with JSON for fresh news:
```web_search
{"query": "<your query>", "time_filter": "day"}
```
Search the web for a SINGLE quick fact/lookup mid-task. For news / "today" / "latest" queries, pass `time_filter` ("day", "week", "month", or "year"). NOT for "research X" / "do research on X" / "look into X" requests — those mean a multi-source DEEP RESEARCH job: use `trigger_research` instead (it runs in the Deep Research sidebar and produces a full report). web_search = one quick query; trigger_research = a researched report.
If this `web_search` tool section is visible, search is available. Do NOT tell the user web/search tools are unavailable.
Use this instead of `bash`, `curl`, `python`, `requests`, or scraping code for web lookup/search/latest/current requests.

**Parameters:**
- `query` (string) — Search query
- `time_filter` (string: 'day', 'week', 'month', 'year') — Optional freshness filter for news/latest/today queries

Required: `query`

### web_fetch

```web_fetch
<url or domain>
```
Fetch and read the text content of a SPECIFIC URL the user names (e.g. "check example.com", "what does this page say <url>"). A bare domain like `example.com` works (defaults to https). Use this when you already have a concrete URL. For open-ended lookups use `web_search`, and for "research X" jobs use `trigger_research`.

**Parameters:**
- `url` (string) — The URL or domain to fetch (http/https; a bare domain like example.com is fine)
- `full` (boolean) — Raise the download budget to the hard cap for large pages/files. Use only after a result reported partial content.

Required: `url`

### read_file

```read_file
<file path>
```
Read a file and return its contents.

**Parameters:**
- `path` (string) — File path to read
- `offset` (integer) — 1-based line to start reading from (optional)
- `limit` (integer) — Max number of lines to read from offset (optional)

Required: `path`

### write_file

```write_file
<file path>
<file contents>
```
Write content to a file. First line is the path, rest is the content.

**Parameters:**
- `path` (string) — File path to write to
- `content` (string) — File content to write

Required: `path`, `content`

### edit_file

```edit_file
{"path": "<file path>", "old_string": "<exact text to replace>", "new_string": "<replacement>", "replace_all": false}
```
Edit an EXISTING file by exact string replacement. PREFER this over bash (sed/echo/redirects) for changing files — it shows a before/after diff. `old_string` must match the file exactly and be unique unless `replace_all` is true. Use write_file to create a new file.

**Parameters:**
- `path` (string) — File path to edit
- `old_string` (string) — Exact text to replace (must match the file, including indentation)
- `new_string` (string) — Replacement text
- `replace_all` (boolean) — Replace all occurrences instead of requiring a unique match

Required: `path`, `old_string`, `new_string`

### apply_patch

```apply_patch
*** Begin Patch
*** Update File: <file path>
@@
 <context>
-<old line>
+<new line>
*** End Patch
```
Apply a source-code patch to real workspace files. Use this for multi-file implementation/refactor/debug work where the edits belong together. The patch is workspace-confined, exact-context based, and returns a diff. Supported sections: `*** Add File:`, `*** Update File:`, `*** Delete File:`. Do NOT use bash redirects/heredocs/sed to edit files.

**Parameters:**
- `patch_text` (string) — Patch text beginning with *** Begin Patch and ending with *** End Patch

Required: `patch_text`

### todowrite

```todowrite
{"todos":[{"content":"Inspect current code","status":"in_progress","priority":"high"},{"content":"Patch implementation","status":"pending","priority":"high"}]}
```
Maintain a structured task list for multi-step coding work. Use it when the task has several phases (inspect, edit, test, fix). Keep statuses current; only one todo should be `in_progress`.

**Parameters:**
- `todos` (array) — Current task list. Only one item should be in_progress.

Required: `todos`

### get_workspace

```get_workspace
```
Return the absolute path of the active workspace folder. File tools are CONFINED to it (paths can be RELATIVE to it); the shell starts there (cwd) but is NOT sandboxed. Call this first when the user says "the project"/"the code"/"this folder" without a path, instead of asking them. No arguments.

### create_document

```create_document
<title>
<language>
<content>
```
Create a NEW document in the editor panel. Only use when the user explicitly asks for a new file/document. If a document is already open in the editor, the user's request "fix this", "add X", "change Y", etc. refers to THAT document — use edit_document, never create_document.

**Parameters:**
- `title` (string) — Document title
- `language` (string) — Programming language or format (e.g. python, javascript, markdown, text)
- `content` (string) — The document content

Required: `title`, `content`

### edit_document

```edit_document
<<<FIND>>>
old text to find
<<<REPLACE>>>
new replacement text
<<<END>>>
```
Edit a document OPEN IN THE EDITOR PANEL — NOT a file on disk. For files on disk (home folder, project files, any real path like ~/sweden.txt) use `edit_file` instead. Find exact text and replace it. Multiple FIND/REPLACE blocks per call OK. Use for any edit smaller than a full rewrite. **If a document is open in the editor, treat it as the user's current context: don't ask which file they mean, and don't create a new one — just edit_document the active one.** Do NOT re-send the whole file with update_document for small changes.

**Parameters:**
- `edits` (array) — List of find/replace edits (first match only per edit)

Required: `edits`

### update_document

```update_document
<entire new content>
```
Replace the ENTIRE active document. ONLY use when you're genuinely rewriting more than half of it from scratch. For any smaller change, use edit_document — echoing back the whole file for a two-line edit wastes tokens and is hard to review.

**Parameters:**
- `content` (string) — Complete new document content

Required: `content`

### suggest_document

```suggest_document
<<<FIND>>>
text to comment on
<<<SUGGEST>>>
suggested replacement
<<<REASON>>>
why this change improves the code
<<<END>>>
```
Suggest changes with explanations (for review/feedback requests).

**Parameters:**
- `suggestions` (array) — List of suggested changes with reasons

Required: `suggestions`

### generate_image

```generate_image
<prompt>
<model>
<size>
<quality>
```
Generate an image. Line 1 = description, line 2 = model name, line 3 = WxH (e.g. 1024x1024), line 4 = quality.

### chat_with_model

- ```chat_with_model``` — Ask a DIFFERENT AI model and relay its answer. Line 1 = model name (or 'model@endpoint'), rest = your message. Use when the user says 'ask <model>', 'what does <model> think', or wants to compare/their answer from another model.

**Parameters:**
- `model` (string) — Model name (e.g. 'qwen3-32b') or model@endpoint_name
- `message` (string) — The message to send to the model

Required: `model`, `message`

### ask_teacher

- ```ask_teacher``` — Escalate a hard question to a more capable model. Line 1 = model name or 'auto', rest = the question. Use when stuck or need expert knowledge.

**Parameters:**
- `model` (string) — Teacher model name (e.g. 'claude-sonnet-4') or 'auto' for configured default
- `problem` (string) — Describe the problem or question you need help with

Required: `problem`

### list_models

- ```list_models``` — Show all available AI models across all endpoints. Use when user asks what models are available.

**Parameters:**
- `filter` (string) — Optional keyword to filter models

### manage_session

- ```manage_session``` — Rename, archive, delete, fork, switch, or `list` chats (the UI calls them 'chats'; 'session' is internal). Line 1 = action (list/switch/rename/archive/unarchive/delete/important/unimportant/truncate/fork), Line 2 = exact chat id from `list_sessions` (or `current` where supported). For delete/archive/truncate, always list first and reuse the exact id; never invent placeholder ids. `switch`/`open` returns a clickable anchor link the user can tap to open the chat — use for "open my X chat".

**Parameters:**
- `action` (string: 'rename', 'archive', 'unarchive', 'delete', 'important', 'unimportant', 'truncate', 'fork') — The action to perform
- `session_id` (string) — Exact target chat id from list_sessions, or 'current' for the active chat where supported
- `value` (string) — Action parameter: new name (rename), keep_count (truncate/fork)

Required: `action`, `session_id`

### manage_memory

- ```manage_memory``` — Manage the user's persistent memory (facts about the USER themselves, their preferences, context that persists across chats). Line 1 = action (list/add/edit/delete/search), rest = content. Use when user says 'remember this' about themselves, states identity facts like 'my name is <name>' / 'call me <name>' / 'I live in <place>', or asks about stored memories. DO NOT use for info about another person (their address, phone, email, birthday) — that goes in `manage_contact`. If the user pastes an address/phone with a name and says 'save this for <person>', use `manage_contact add` with the address arg, NOT manage_memory.

**Parameters:**
- `action` (string: 'list', 'add', 'edit', 'delete', 'search') — The action to perform
- `text` (string) — Memory text (for add/edit) or search query (for search)
- `memory_id` (string) — Memory ID (for edit/delete)
- `category` (string: 'fact', 'event', 'contact', 'preference') — Memory category (for add/list filter)

Required: `action`

### manage_skills

- ```manage_skills``` — Skill registry (SKILL.md format). Args (JSON): {"action": "list|view|view_ref|search|add|edit|patch|publish|delete", ...}. `list` returns the index of available skills (published + teacher-escalation drafts); `view name=foo` fetches the full SKILL.md; `view_ref name=foo path=...` loads a reference file under the skill directory. For `add`, provide an explicit kebab-case `name` and only report the exact returned name, because storage may normalize or dedupe it. Use this BEFORE doing domain work — there may already be a procedure (published or draft) that prescribes the correct steps. Drafts written by the teacher loop are authoritative guidance even though they're not yet published.

**Parameters:**
- `action` (string: 'list', 'view', 'view_ref', 'add', 'edit', 'patch', 'publish', 'delete', 'search') — list = name+description summary; view = full SKILL.
- `name` (string) — Skill slug/name. Required for add/view/view_ref/edit/patch/publish/delete.
- `path` (string) — Sub-path under the skill directory for view_ref (e.g. 'references/example.md').
- `description` (string) — One-line summary surfaced in the skills index (for add).
- `category` (string) — Organizational grouping like 'dev', 'email', 'system' (for add).
- `when_to_use` (string) — Trigger conditions in plain English (for add).
- `procedure` (array) — Numbered steps (for add).
- `pitfalls` (array) — Known failure modes + recovery (for add).
- `verification` (array) — How to confirm the procedure succeeded (for add).
- `tags` (array) — Keyword tags (for add).
- `platforms` (array) — Restrict to OSes (for add).
- `requires_toolsets` (array) — Hide unless these toolsets are active (for add).
- `fallback_for_toolsets` (array) — Hide when these toolsets are active (for add).
- `status` (string: 'draft', 'published') — Defaults to 'draft' on add.
- `version` (string) — Semver-ish, e.g. '1.0.0' (for add).
- `confidence` (number) — 0-1 (for add/publish).
- `content` (string) — Full SKILL.md text (for edit).
- `old_string` (string) — Exact substring to replace (for patch). Must appear exactly once.
- `new_string` (string) — Replacement text (for patch).
- `query` (string) — Search query (for search).

Required: `action`

### manage_tasks

- ```manage_tasks``` — Create and manage scheduled background tasks (recurring AI jobs). Args (JSON): {"action": "list|create|edit|delete|pause|resume|run", ...}

**Parameters:**
- `action` (string: 'list', 'create', 'edit', 'delete', 'pause', 'resume', 'run') — The action to perform
- `task_id` (string) — Task ID (for edit/delete/pause/resume/run)
- `name` (string) — Task name
- `prompt` (string) — The instruction (for task_type=llm) or the research question (for task_type=research). Required for both.
- `task_type` (string: 'llm', 'research', 'action') — llm = AI runs prompt; research = deep-research on prompt; action = built-in function
- `action_name` (string: 'tidy_sessions', 'tidy_documents', 'consolidate_memory', 'tidy_research', 'summarize_emails', 'draft_email_replies', 'extract_email_events', 'classify_events', 'learn_sender_signatures', 'test_skills', 'audit_skills', 'check_email_urgency') — Built-in action (for task_type=action)
- `trigger_type` (string: 'schedule', 'event') — schedule = time-based, event = count-based
- `schedule` (string: 'once', 'daily', 'weekly', 'monthly') — Schedule frequency (for trigger_type=schedule)
- `scheduled_time` (string) — HH:MM in UTC (for schedule triggers).
- `scheduled_day` (integer) — Day of week 0=Mon (weekly) or day of month (monthly)
- `trigger_event` (string: 'session_created', 'message_sent', 'document_created', 'memory_added', 'research_completed', 'email_received', 'skill_added') — Event name (for trigger_type=event)
- `trigger_count` (integer) — Fire every N events (for trigger_type=event)
- `output_target` (string) — Where results go.

Required: `action`

### manage_endpoints

- ```manage_endpoints``` — Add, remove, or configure AI model API endpoints. Args (JSON): {"action": "list|add|delete|enable|disable", ...}. Use when user wants to add a new AI provider.

**Parameters:**
- `action` (string: 'list', 'add', 'delete', 'enable', 'disable')
- `endpoint_id` (string) — Endpoint ID (for delete/enable/disable)
- `name` (string) — Display name (for add)
- `base_url` (string) — API base URL e.g. https://api.openai.com/v1 (for add)
- `api_key` (string) — API key (for add)

Required: `action`

### manage_mcp

- ```manage_mcp``` — Manage MCP (Model Context Protocol) tool servers — external tools that extend your capabilities. Args (JSON): {"action": "list|add|delete|reconnect|list_tools", ...}

**Parameters:**
- `action` (string: 'list', 'add', 'delete', 'enable', 'disable', 'reconnect', 'list_tools')
- `server_id` (string) — Server ID (for delete/enable/disable/reconnect)
- `name` (string) — Server name (for add)
- `command` (string) — Command to run e.g. npx (for add)
- `args` (array) — Command arguments (for add)
- `env` (object) — Environment variables (for add)

Required: `action`

### manage_webhooks

- ```manage_webhooks``` — Configure outgoing webhooks (HTTP notifications on events like chat completion). Args (JSON): {"action": "list|add|delete|enable|disable", ...}

**Parameters:**
- `action` (string: 'list', 'add', 'delete', 'enable', 'disable')
- `webhook_id` (string) — Webhook ID (for delete/enable/disable)
- `name` (string) — Webhook name (for add)
- `url` (string) — Webhook URL (for add)
- `events` (string) — Comma-separated event names (for add)

Required: `action`

### manage_tokens

- ```manage_tokens``` — Generate or revoke API access tokens for external integrations. Args (JSON): {"action": "list|create|delete", ...}

**Parameters:**
- `action` (string: 'list', 'create', 'delete')
- `token_id` (string) — Token ID (for delete)
- `name` (string) — Token name (for create)

Required: `action`

### manage_documents

- ```manage_documents``` — List, read/open, delete, or tidy documents in the editor panel. Args (JSON): {"action": "list|read|delete|tidy", ...}. `list` returns rows like `[Title](#document-<id>) — lang, size, updated 5m ago` sorted MOST-RECENT FIRST; the user clicks the anchor to open. `read` (aliases: view/open/get) takes `document_id` and returns the content. When the user asks "open/show/read my notes" or "what documents do I have", use this — do NOT shell out, do NOT curl.

**Parameters:**
- `action` (string: 'list', 'delete', 'tidy')
- `document_id` (string) — Document ID (for delete)
- `search` (string) — Search query (for list)
- `language` (string) — Filter by language (for list)
- `limit` (integer) — Max results (for list, default 50)

Required: `action`

### manage_research

- ```manage_research``` — List, read/open, or delete saved DEEP RESEARCH results from the Library. Args (JSON): {"action": "list|read|delete", "id": "<id>", "search": "..."}. `list` returns rows like `[query](#research-<id>) — N sources` MOST-RECENT FIRST; the user clicks to open. `read` (aliases: open/view/get) takes `id` and returns the report text + sources. Use when the user says "open/read/find/delete my research" or "that report". This IS how you read a finished report: when the user refers to a just-completed deep-research job ("check it out", "read that report", "summarize the research") WITHOUT giving an id, call `manage_research` with `action:list` to get the most-recent id, then `action:read` with that id, and answer from the returned text. Do NOT `web_fetch`/`app_api` the `/api/research/report/{id}` URL — that endpoint renders HTML for the browser, not clean text — and do NOT start a fresh `web_search`/`trigger_research` just to read an existing report. To START new research, use trigger_research instead.

### manage_settings

- ```manage_settings``` — View/change the REAL app settings (same ones the Settings panel writes) AND turn tools on/off. Change a setting: `{"action":"set","key":"...","value":"..."}` — keys accept friendly aliases, e.g. voice→tts_voice, "search engine"→search_provider, "default model"→default_model, "teacher model"→teacher_model, "task/background model"→task_model, "image quality"→image_quality, "reminder channel"→reminder_channel (browser|email|ntfy), "agent timeout"/"max tool calls"/"token budget". Read: `{"action":"get","key":"..."}`; see all: `{"action":"list"}`; reset one: `{"action":"reset","key":"..."}`. Use this when the user asks to change ANY preference instead of making them open Settings. Secrets/API keys are read-only (tell them to set those in the panel). Tool toggles: `{"action":"disable_tool|enable_tool","tool":"shell"}` (aliases: shell/search/browser/documents/memory/skills/images/tasks/notes/calendar/email), list disabled: `{"action":"list_tools"}`.

**Parameters:**
- `action` (string: 'list', 'get', 'set', 'delete', 'disable_tool', 'enable_tool', 'list_tools')
- `key` (string) — Setting key (for get/set/delete)
- `value` (string) — Setting value (for set) — can be string, number, boolean, or object
- `tool` (string) — Tool name to disable/enable (for disable_tool/enable_tool).

Required: `action`

### manage_notes

```manage_notes
{"action": "add", "title": "<short todo>", "due_date": "<natural language or ISO datetime>"}
```
Notes, checklists, AND user reminders. Use this for "create/add/write a note", todos, checklists, and "remind me to X at <time>" — never use memory for note content. For reminders, pair a short `title` (what to do) with a `due_date` (when). `due_date` accepts natural language ("tomorrow at 1pm", "in 2 hours", "next monday 9am") or ISO ("2026-05-12T13:00:00"). Actions: `list`, `add` (title, content OR items:[{text,done}], note_type, color, label, due_date), `update`, `delete`, `toggle_item`.

**Parameters:**
- `action` (string: 'list', 'search', 'view', 'add', 'update', 'delete', 'toggle_item') — The action to perform
- `id` (string) — Note id (for update/delete/toggle_item); 8-char prefix is fine
- `query` (string) — Search text for action='search'
- `title` (string) — Note title (for add/update)
- `content` (string) — Freeform body text. Use this for note_type='note'. Do NOT use this for checklists — pass `checklist_items` instead.
- `note_type` (string: 'note', 'checklist') — 'note' = freeform text in `content`. 'checklist' = structured to-do items in `checklist_items`. Defaults to 'checklist' if checklist_items is supplied, else 'note'.
- `checklist_items` (array) — Checklist items for note_type='checklist'. Each item is {text, done}. REQUIRED for checklists — leaving this empty produces a blank note.
- `color` (string) — Optional color label (e.g. 'yellow', 'blue', 'green')
- `label` (string) — Optional category label (also used as a list filter)
- `pinned` (boolean) — Pin the note to the top
- `archived` (boolean) — For update: archive/unarchive. For list: show archived notes when true.
- `due_date` (string) — Reminder time. Accepts natural language ('tomorrow at 9am', '11pm today') or ISO 8601. Fires a notification at that time.
- `index` (integer) — Checklist item index (for toggle_item, 0-based)

Required: `action`

### list_email_accounts

- ```list_email_accounts``` — List configured email accounts. Use this before reading/sending when the user says Gmail, work mail, custom domain mail, or any non-default mailbox; pass the returned account name/email/id as `account` to email tools.

### send_email

```send_email
{"to": "recipient@example.com", "subject": "Re: Your question", "body": "Hi, ...", "account": "gmail"}
```
Send a new email via SMTP. Use `resolve_contact` first if you only have a name. If multiple email accounts exist, call `list_email_accounts` first and pass the chosen `account`.

CRITICAL — signatures: DO NOT invent a sign-off name. End the body with just `Thanks,` or similar — never type a person's name unless the user explicitly told you what to sign as. When `agent_email_confirm` is on (default), the tool returns `{pending: true, pending_id: ...}` and stages the email for the user to approve in the chat UI instead of SMTPing immediately.

**Parameters:**
- `to` (string) — Recipient email address
- `subject` (string) — Email subject line
- `body` (string) — Email body text
- `account` (string) — Optional account name/email/id from list_email_accounts, e.g. Gmail or user@example.com

Required: `to`, `subject`, `body`

### list_emails

```list_emails
{"folder": "INBOX", "max_results": 20, "unread_only": false, "account": "gmail"}
```
List recent emails from a folder, newest first, including read messages by default. Use `list_email_accounts` first when the user names a mailbox/account, then pass `account`. For "last/latest/newest email", call with `max_results: 1` and `unread_only: false`.

**Parameters:**
- `folder` (string) — IMAP folder (default: INBOX)
- `max_results` (integer) — Max emails to return (default: 20)
- `limit` (integer) — Backward-compatible alias for max_results
- `unread_only` (boolean) — Only show unread emails. Default false; set true only when the user asks for unread emails.
- `unresponded_only` (boolean) — Only show unanswered emails. Default false.
- `account` (string) — Optional account name/email/id from list_email_accounts, e.g. Gmail or user@example.com

### read_email

- ```read_email``` — Read a specific email by UID. Args (JSON): {"uid": "...", "folder": "INBOX", "account": "gmail"}. Include `account` when the UID came from a named/non-default mailbox.

**Parameters:**
- `uid` (string) — Email UID to read
- `folder` (string) — IMAP folder (default: INBOX)
- `account` (string) — Optional account name/email/id from list_email_accounts, especially when the UID came from a non-default

Required: `uid`

### reply_to_email

```reply_to_email
{"uid": "1234", "body": "Sounds good — talk Friday.", "account": "gmail"}
```
SEND a reply email immediately by UID. Do not use this for "write/draft a reply", "open a reply", or "start a reply" — those should use `ui_control` with `open_email_reply <uid> <folder> reply <body>` (or structured `body`) to open the email draft document. Only use this when the user explicitly says to send now. Never invent UID `1`. Threads automatically (In-Reply-To/References handled).

CRITICAL — signatures: DO NOT invent a sign-off name. End the body with just `Thanks,` or similar — never type a person's name unless the user explicitly told you what to sign as. When `agent_email_confirm` is on (default), the tool returns `{pending: true, pending_id: ...}` and stages the email for the user to approve in the chat UI instead of SMTPing immediately.

**Parameters:**
- `uid` (string) — Exact UID of the email to reply to from list_emails/read_email; never invent UID 1
- `body` (string) — Reply body text
- `folder` (string) — IMAP folder (default: INBOX)
- `account` (string) — Optional account name/email/id from list_email_accounts, especially when the UID came from a non-default mailbox

Required: `uid`, `body`

### bulk_email

```bulk_email
{"action": "delete", "uids": ["10997", "10998"], "folder": "INBOX", "account": "Gmail"}
```
Bulk delete/archive/mark emails. Use this for "delete all those" after listing emails. Pass the exact UIDs and the same account from the list result, then report only the tool result.

**Parameters:**
- `action` (string: 'mark_read', 'mark_unread', 'archive', 'delete', 'junk') — Bulk action to perform
- `uids` (array) — UIDs from the latest list_emails result
- `all_unread` (boolean) — Operate on all unread messages in folder instead of explicit UIDs
- `folder` (string) — IMAP folder (default: INBOX)
- `permanent` (boolean) — For delete: hard-delete instead of moving to Trash
- `account` (string) — Account name/email/id from list_email_accounts, e.g. Gmail or user@example.com

Required: `action`

### delete_email

- ```delete_email``` — Delete one email by UID. Args (JSON): {"uid":"...", "folder":"INBOX", "account":"Gmail"}. For multiple messages use bulk_email.

**Parameters:**
- `uid` (string) — Email UID from list_emails/read_email
- `folder` (string) — IMAP folder (default: INBOX)
- `permanent` (boolean) — Hard-delete instead of moving to Trash
- `account` (string) — Account name/email/id from list_email_accounts

Required: `uid`

### archive_email

- ```archive_email``` — Archive one email by UID. Args (JSON): {"uid":"...", "folder":"INBOX", "account":"Gmail"}. For multiple messages use bulk_email.

**Parameters:**
- `uid` (string) — Email UID from list_emails/read_email
- `folder` (string) — IMAP folder (default: INBOX)
- `account` (string) — Account name/email/id from list_email_accounts

Required: `uid`

### mark_email_read

- ```mark_email_read``` — Mark one email read/unread. Args (JSON): {"uid":"...", "read":true, "folder":"INBOX", "account":"Gmail"}. For multiple messages use bulk_email.

**Parameters:**
- `uid` (string) — Email UID from list_emails/read_email
- `folder` (string) — IMAP folder (default: INBOX)
- `read` (boolean) — True marks read; false marks unread
- `account` (string) — Account name/email/id from list_email_accounts

Required: `uid`

### resolve_contact

- ```resolve_contact``` — Look up a contact's email by name. Searches CardDAV address book + sent email history. Args (JSON): {"name": "..."}. Use BEFORE send_email when the user gives only a name.

**Parameters:**
- `name` (string) — Person's name to search for

Required: `name`

### manage_contact

- ```manage_contact``` — Create/update/delete/list CardDAV contacts. Args (JSON): {"action": "list|add|update|delete", "name": "...", "email": "...", "phones": [...], "address": "...", "uid": "..."}. Use for info about another person: email, phone, postal address. For 'save this for <person>' / address paste / phone next to a name, use this — NOT manage_memory. Do NOT use for user identity facts ('my name is X'); those are manage_memory. For update/delete, call action=list first for the uid.

**Parameters:**
- `action` (string: 'list', 'add', 'update', 'delete') — list = show all contacts (with uids); add = create; update = edit by uid; delete = remove by uid.
- `uid` (string) — Contact UID (required for update/delete; get it from action=list).
- `name` (string) — Contact's display name (for add/update).
- `email` (string) — Single email address (convenience for add, or the primary email for update). Optional when phone or address is provided.
- `emails` (array) — Full list of email addresses (first is primary).
- `phones` (array) — Full list of phone numbers. Valid for add/update.
- `address` (string) — Postal/mailing address as a single human-readable string.

Required: `action`

### manage_calendar

```manage_calendar
{"action": "create_event", "summary": "<event title>", "dtstart": "<natural language or ISO datetime>"}
```
Calendar event management (CalDAV). Actions: `list_events`, `create_event`, `update_event`, `delete_event`, `list_calendars`. For `list_events`: {action: "list_events", start: "YYYY-MM-DDT00:00:00", end: "YYYY-MM-DDT00:00:00", calendar?}; resolve month/week phrases yourself from the Current date and time context and do not pass a loose `query` field. Prefer `start`/`end`; start_time/end_time, start_date/end_date, and from/to aliases are accepted. For `create_event`: {summary, dtstart, dtend?, duration?, calendar?, location?, description?, reminder_minutes?, rrule?}. For `update_event`: {uid, summary?, dtstart?, dtend?, all_day?, location?, description?, event_type?, importance?, rrule?}. Pass `rrule: ""` to remove recurrence and make a repeating event a single event. `dtstart` accepts natural language ("tomorrow at 1pm", "in 2 hours", "next monday 9am") or ISO ("2026-05-12T13:00:00"). If `dtend` omitted, defaults to dtstart+1h (or +1d when `all_day: true`). For a RECURRING event pass `rrule` as an iCalendar RRULE string, e.g. `"FREQ=WEEKLY;BYDAY=MO"` (every Monday), `"FREQ=DAILY;COUNT=10"`, or `"FREQ=MONTHLY;BYMONTHDAY=1"` — create ONE event with the rrule, do not loop creating many events. Do not pass `rrule` for "next Wednesday only", "just this once", or any single occurrence. If the user asks for a reminder/alarm before the event, pass `reminder_minutes` as an integer; do not write reminder text into the event description and do NOT also call `manage_notes` for the same reminder because calendar reminders are routed through Notes automatically. `calendar` accepts a name ("Main") or short-id prefix.

**Parameters:**
- `action` (string: 'list_events', 'create_event', 'update_event', 'delete_event', 'list_calendars') — Action to perform
- `summary` (string) — Event title (for create/update)
- `dtstart` (string) — Start ISO datetime, or YYYY-MM-DD if all_day
- `dtend` (string) — End ISO datetime; defaults to +1h (or +1 day for all_day)
- `all_day` (boolean) — Whether this is an all-day event
- `description` (string) — Event description / notes
- `location` (string) — Event location
- `uid` (string) — Event UID (for update/delete)
- `calendar_href` (string) — Specific calendar URL (optional; defaults to first calendar)
- `calendar` (string) — Filter list_events by calendar name or href
- `start` (string) — list_events range start (ISO datetime). Use this for month/week requests after resolving the date range; do not pass a loose query string. Prefer start; backend also accepts start_time, start_date, range_start, from, dtstart, since.
- `end` (string) — list_events range end (ISO datetime). Use this for month/week requests after resolving the date range; defaults to +14 days only when no range is requested. Prefer end; backend also accepts end_time, end_date, range_end, to, dtend, until.
- `event_type` (string) — Tag / category for the event. Common values: work, personal, health, travel, meal, social, admin, other. Aliases accepted: tag, category, type.
- `importance` (string: 'low', 'normal', 'high', 'critical') — Priority level (defaults to 'normal')
- `reminder_minutes` (integer) — For create_event: create an Odysseus reminder this many minutes before the event, e.g. 5 for 'reminder 5 min before'.
- `rrule` (string) — Recurrence rule in iCalendar RRULE format, e.g. 'FREQ=WEEKLY;BYDAY=MO' for weekly on Monday. Use with create_event or update_event. For update_event, pass an explicit empty string to remove recurrence and make the event single-occurrence.

Required: `action`

### create_session

- ```create_session``` — Create a new chat. Line 1 = chat name, line 2 = model name. Use for background/parallel work.

**Parameters:**
- `name` (string) — Name for the new chat
- `model` (string) — Model name or model@endpoint_name

Required: `name`, `model`

### list_sessions

- ```list_sessions``` — List chats sorted MOST-RECENT FIRST (the UI calls them 'chats') with clickable chat-title links. Output includes a relative "last active" timestamp per row, so the first row is the user's most recent chat. Content = optional filter keyword (matches chat name). When answering, preserve the `[title](#session-id)` links exactly; do not convert them into plain text.

**Parameters:**
- `filter` (string) — Optional keyword to filter chats by name

### send_to_session

- ```send_to_session``` — Send a message to another session. Line 1 = session_id, rest = message. Use for orchestrating work across sessions.

**Parameters:**
- `session_id` (string) — The id of the chat to send the message to
- `message` (string) — The message to send

Required: `session_id`, `message`

### search_chats

- ```search_chats``` — Search past session transcripts for direct conversation evidence. Use when user asks 'did we discuss X?', 'find the conversation about Y', or when prior chat context is more appropriate than persistent memory.

**Parameters:**
- `query` (string) — Search keyword(s) to find in past conversations

Required: `query`

### pipeline

- ```pipeline``` — Run a multi-step AI pipeline. Args (JSON) with ordered steps, each specifying a model and prompt. Use for complex workflows.

**Parameters:**
- `steps` (array) — Pipeline steps in order

Required: `steps`

### ui_control

- ```ui_control``` — Control the UI: toggle tools on/off, OPEN PANELS, open email reply drafts, switch models, change themes. Commands: `toggle <name> on/off` (names: bash/shell, web/search, research, incognito, document_editor/documents), `open_panel <name>` (panels: documents, gallery, email, sessions, notes, memories/brain, skills, settings, cookbook), `open_email_reply <uid> <folder> <reply|reply-all|ai-reply> <body text>` (opens an email compose document pre-filled with body, DOES NOT send; use this for normal “write/draft a reply saying X” requests), `set_mode agent/chat`, `switch_model <name>`, `set_theme <preset>`, `create_theme <name> <bg> <fg> <panel> <border> <accent>` (optional key=val for advanced colors AND background effects: bgPattern=<none|dots|synapse|rain|constellations|perlin-flow|petals|sparkles|embers>, bgEffectColor=#RRGGBB, bgEffectIntensity=<num>, bgEffectSize=<num>, frosted=true|false). "open documents" / "open library" / "show gallery" / "open inbox" / "open notes" / "open cookbook" all map to `open_panel <name>`. Built-in theme presets: dark, light, midnight, paper, cyberpunk, retrowave, forest, ocean, ume, copper, terminal, organs, lavender, gpt, claude, cute. For any other vibe/name, use create_theme.

**Parameters:**
- `action` (string: 'toggle', 'open_panel', 'open_email_reply', 'set_mode', 'switch_model', 'set_theme', 'create_theme', 'get_toggles') — The UI action. Use set_theme for presets, create_theme to build a custom theme with any hex colors
- `name` (string) — For toggle: web, bash, research, incognito, document_editor (aliases: shell, search, deepresearch, documents). For open_panel: documents, gallery, email, sessions, notes, brain/memories, skills, settings, cookbook. For open_email_reply: email UID. For set_theme: a preset theme name. For create_theme: the custom theme name.
- `value` (string) — Value: on/off for toggle, agent/chat for set_mode, model name for switch_model, theme name for set_theme, or folder for open_email_reply
- `uid` (string) — Email UID for open_email_reply
- `folder` (string) — Email folder for open_email_reply (default INBOX)
- `mode` (string) — Reply draft mode for open_email_reply: reply, reply-all, or ai-reply
- `body` (string) — For open_email_reply: reply body to pre-fill. Required whenever the user told you what the reply should say. Opens a draft, does not send.
- `colors` (object) — For create_theme: the theme colors

Required: `action`

### ask_user

- ```ask_user``` — Ask the user a multiple-choice question when the task is genuinely ambiguous and the answer changes what you do next (pick an approach, confirm an assumption, choose a target). Args (JSON): {"question": "...", "options": [{"label": "...", "description": "..."?}, ...], "multi": false?}. 2-6 options. The user gets clickable buttons; calling this ENDS your turn and their choice comes back as your next message. Prefer sensible defaults — only ask when you truly can't proceed well without their input.

**Parameters:**
- `question` (string) — The question to ask. Be specific and self-contained.
- `options` (array) — 2-6 choices. Each is an object with a short `label` and an optional `description` explaining the trade-off.
- `multi` (boolean) — Set true ONLY when the question explicitly allows choosing more than one option. Otherwise omit it or set false. Default false.

Required: `question`, `options`

### update_plan

- ```update_plan``` — While executing an approved plan, write the plan back: tick steps done or revise them. Args (JSON): {"plan": "- [x] done step\n- [ ] next step"}. Always pass the COMPLETE checklist, not a diff. Call it after finishing each step (mark it `- [x]`) and whenever the user asks to change the plan. The user's docked plan window updates live. Does nothing if there's no active plan.

**Parameters:**
- `plan` (string) — The full updated plan as a GitHub-style markdown checklist — one step per line, `- [ ]` for pending and `-

Required: `plan`

### list_served_models

- ```list_served_models``` — Show what the Cookbook (LLM-serving subsystem) is currently running. NO args. Use this for ANY 'what's running' / 'what's serving' / 'show my cookbook' / 'is anything up' query. DO NOT shell out (`ps aux`, `docker ps`, etc.) — this tool is the source of truth. Failed serve tasks include recent logs plus diagnosis/retry suggestions; use those suggestions to call `serve_model` again with an adjusted command when appropriate.

### stop_served_model

- ```stop_served_model``` — Stop a running model server. Args (JSON): {"session_id": "<from list_served_models>"}. Use for 'kill my cookbook' / 'stop the model' / 'shut down vLLM'.

**Parameters:**
- `session_id` (string) — Tmux session ID of the server to stop

Required: `session_id`

### tail_serve_output

- ```tail_serve_output``` — Read the actual tmux stderr/traceback of a CURRENTLY failing cookbook task. Args (JSON): {"session_id": "<from list_served_models>", "tail": 150?}. **Use ONLY after** you just launched something via `serve_model` AND `list_served_models` reports YOUR new task as `crashed`/`error`. DO NOT use it on old stopped/completed download tasks (they're historical noise — won't predict whether a new launch succeeds). DO NOT call it before launching a fresh attempt. When you do call it, bump `tail` to 400+ only if the visible error references 'see root cause above'.

**Parameters:**
- `session_id` (string) — Tmux session id from list_served_models (e.g. 'serve-abc12345', 'cookbook-a1b2c3d4').
- `tail` (integer) — How many lines of pane scrollback to fetch (default 300, max 4000).

Required: `session_id`

### download_model

- ```download_model``` — Download a HuggingFace model. Args (JSON): {"repo_id": "Qwen/Qwen3-8B", "host": "user@gpu-box"?, "include": "*Q4_K_M*"?}.

**Parameters:**
- `repo_id` (string) — HuggingFace repo (e.g. 'Qwen/Qwen3-8B')
- `host` (string) — Target server — use the friendly NAME from list_cookbook_servers (e.g.
- `local` (boolean) — Force download to THIS machine (localhost) instead of the default remote server.
- `include` (string) — Glob filter for specific files (e.g. '*Q4_K_M*')

Required: `repo_id`

### serve_model

- ```serve_model``` — Start serving a model with vLLM / SGLang / llama.cpp / Ollama / MLX Image / Diffusers. Args (JSON): {"repo_id": "...", "cmd": "vllm serve <repo> --port 8000" or "python3 -m sglang.launch_server --model-path <repo> --port 30000" or "python3 scripts/mlx_image_server.py --model <repo> --port 8100" or "python3 scripts/diffusion_server.py --model <repo> --port 8100", "host": "user@gpu-box"?}. For MLX image models, use `scripts/mlx_image_server.py`; for non-MLX image/inpaint/diffusion models, use `scripts/diffusion_server.py`. Never use `mlx_lm.server` for image models. After launch, call `list_served_models`; if it returns a diagnosis with an adjusted command, retry with that command.

**Parameters:**
- `repo_id` (string) — Model repo (e.g. 'Qwen/Qwen3-8B')
- `cmd` (string) — Full serve command (e.g. 'vllm serve <repo> --port 8000 --tp 2', 'python3 -m sglang.launch_server --model-path <repo> --port 30000', for MLX image models: 'python3 scripts/mlx_image_server.py --model <repo> --port 8100', or for non-MLX image models: 'python3 scripts/diffusion_server.py --model <repo> --port 8100')
- `host` (string) — Target server — friendly NAME from list_cookbook_servers (e.g. 'gpu-box', 'workstation') or raw user@host. Omit to use the cookbook's selected default.
- `local` (boolean) — Force serve on THIS machine instead of the default remote server.

Required: `repo_id`, `cmd`

### list_downloads

- ```list_downloads``` — Show in-progress HuggingFace model downloads (filters Cookbook tasks/status to downloads only). NO args. Use for 'what's downloading' / 'show my downloads' / 'check download progress'.

### cancel_download

- ```cancel_download``` — Cancel an in-progress download. Args (JSON): {"session_id": "<from list_downloads>"}. Use for 'cancel the download' / 'kill the download'.

**Parameters:**
- `session_id` (string) — Tmux session ID from list_downloads (e.g. 'cookbook-a1b2c3d4')

Required: `session_id`

### search_hf_models

- ```search_hf_models``` — Search HuggingFace for models. Args (JSON): {"query": "qwen 8b", "limit": 10?}. Use for 'find a model for X' / 'search huggingface' / 'what models are there for Y'.

**Parameters:**
- `query` (string) — Search terms (e.g. 'Qwen 8B', 'flux', 'llama-3 instruct')
- `limit` (integer) — Max results (default 10)

### list_cached_models

- ```list_cached_models``` — List models already on disk. Args (JSON, all optional): {"host": "server-name or user@gpu-box"?, "model_dir": "/data/models,/extra"?}. Friendly Cookbook server names work. Use for 'what models do I have' / 'show cached models' / 'is X downloaded'.

**Parameters:**
- `host` (string) — Friendly Cookbook server name (e.g. 'workstation', 'gpu-box') or raw remote host (e.g. 'user@gpu-box'). Omit for local.
- `model_dir` (string) — Comma-separated additional model directories to scan beyond ~/.cache/huggingface/hub
- `ssh_port` (string) — SSH port for remote host (default 22)
- `platform` (string: 'linux', 'windows') — Remote platform

### app_api

```app_api
{"action": "call", "method": "GET", "path": "/api/cookbook/gpus"}
```
GENERIC LOOPBACK to allowed Odysseus internal endpoints. Use this whenever the user wants something the UI can do but there's NO named tool for it. Many UI buttons hit /api/* endpoints — you can hit allowed ones. Auth is handled automatically.

**Discovery first.** If you're not sure of the path, call `{"action":"endpoints","filter":"<keyword>"}` (e.g. filter='calendar' or 'gallery' or 'theme') to list available endpoints with their methods + summaries. Then call with action='call'.

**Common surfaces (use `endpoints` with filter to discover the full set per domain):**
- Calendar: `/api/calendar/events`, `/api/calendar/calendars`, `/api/calendar/events/{uid}`
- Cookbook: `/api/cookbook/gpus`, `/api/cookbook/state`, `/api/cookbook/setup`, `/api/cookbook/packages`, `/api/cookbook/hf-latest`, `/api/model/cached`. Do NOT use `app_api` for package installs, engine rebuilds, or PID signalling.
- Gallery: `/api/gallery/list`, `/api/gallery/delete`, `/api/gallery/{id}`, `/api/gallery/albums`
- Library / Documents: list all via `/api/documents/library`; docs in a session via `/api/documents/{session_id}`; a single doc via `/api/document/{id}` (singular) and its history via `/api/document/{id}/versions` (singular). Note the plural `/api/documents/...` vs singular `/api/document/{id}` split.
- Memory: `/api/memory`, `/api/memory/{id}`, `/api/memory/search`
- Notes: `/api/notes`, `/api/notes/{id}`
- Tasks: `/api/tasks`, `/api/tasks/{id}/run`, `/api/tasks/notifications`
- Sessions: `/api/sessions`, `/api/session/{id}`, `/api/session/{id}/truncate`
- Themes: `/api/prefs/themes`, `/api/prefs/custom-themes`
- Settings: `/api/settings`, `/api/prefs/{key}`
- Research: `/api/research/start`, `/api/research/tasks` (note: `/api/research/report/{id}` renders HTML — to READ a report's text use the `manage_research` tool with `action:read`, not this endpoint)
- Compare: `/api/compare/sessions`, `/api/compare/start`
- Email: use named email tools (`list_email_accounts`, `list_emails`, `read_email`, `scan_email_unsubscribes`, `unsubscribe_email`, `send_email`, `reply_to_email`). Do NOT use `/api/email/accounts`; it is owner-filtered in tool context and may falsely return empty.
- Endpoints (model providers): `/api/endpoints`, `/api/endpoints/{id}`
- Shell: do NOT use `app_api` for `/api/shell/*`; use named command tooling instead.

Body for POST/PUT/PATCH goes in `body` (object). Query params in `query` (object). Returns the parsed JSON of the response.

**When to prefer named tools over app_api:** if a named wrapper exists (list_email_accounts, list_emails, read_email, scan_email_unsubscribes, manage_calendar, manage_notes, list_served_models, etc.) USE IT — it has nicer output formatting and clearer schema. Reach for `app_api` only when there's no wrapper for what you need.

Blocked paths/routes (refused for safety): /api/auth/, /api/users/, /api/tokens/, /api/admin/, /api/shell/, /api/backup/restore, /api/email/accounts, POST /api/cookbook/packages/install, POST /api/cookbook/rebuild-engine, POST /api/cookbook/kill-pid.

**Parameters:**
- `action` (string: 'call', 'endpoints') — 'call' to hit an endpoint, 'endpoints' to list what's available
- `path` (string) — Endpoint path starting with /api/ (e.g. '/api/cookbook/gpus', '/api/gallery/list', '/api/calendar/events')
- `method` (string: 'GET', 'POST', 'PUT', 'PATCH', 'DELETE') — HTTP method (default GET)
- `body` (object) — JSON request body for POST/PUT/PATCH
- `query` (object) — Querystring params as a key-value object
- `filter` (string) — For action=endpoints: substring to filter paths/summaries (e.g. 'cookbook', 'gallery')

Required: `action`

### adopt_served_model

(No prose section; see schema below.)

**Parameters:**
- `host` (string) — Remote host in user@host form (e.g. 'user@192.0.2.10'). Omit for localhost.
- `tmux_session` (string) — Existing tmux session name (e.g. 'minimax-m27')
- `model` (string) — Model repo_id or display name (e.g. 'cyankiwi/MiniMax-M2.7-AWQ-4bit')
- `port` (integer) — Port the server is listening on (default 8000)
- `name` (string) — Optional display name (defaults to model basename)
- `add_endpoint` (boolean) — Also register as a chat endpoint (default true)

Required: `tmux_session`, `model`

### api_call

(No prose section; see schema below.)

**Parameters:**
- `integration` (string) — Integration name or ID (e.g. 'Miniflux', 'Gitea')
- `method` (string: 'GET', 'POST', 'PUT', 'PATCH', 'DELETE') — HTTP method
- `path` (string) — API endpoint path (e.g. '/v1/entries?status=unread&limit=20')
- `body` (object) — JSON request body (for POST/PUT/PATCH)

Required: `integration`, `method`, `path`

### edit_image

(No prose section; see schema below.)

**Parameters:**
- `image_id` (string) — Gallery image ID
- `action` (string: 'upscale', 'rembg', 'inpaint', 'harmonize') — Edit action
- `prompt` (string) — For inpaint: what to fill the masked area with
- `scale` (number) — For upscale: scale factor (default 2)

Required: `image_id`, `action`

### glob

(No prose section; see schema below.)

**Parameters:**
- `pattern` (string) — Glob pattern, e.g. '**/*.ts' or 'src/**/test_*.py'
- `path` (string) — Base directory (optional; defaults to the project root)

Required: `pattern`

### grep

(No prose section; see schema below.)

**Parameters:**
- `pattern` (string) — Regular expression to search for
- `path` (string) — Directory or file to search (optional; defaults to the project root)
- `glob` (string) — Only search files matching this glob, e.g. '*.py' (optional)
- `ignore_case` (boolean) — Case-insensitive match (optional)
- `max_results` (integer) — Max matches to return (optional)

Required: `pattern`

### list_cookbook_servers

(No prose section; see schema below.)

### list_serve_presets

(No prose section; see schema below.)

### ls

(No prose section; see schema below.)

**Parameters:**
- `path` (string) — Directory to list (optional; defaults to the project root)

### manage_bg_jobs

(No prose section; see schema below.)

**Parameters:**
- `action` (string: 'list', 'output', 'kill') — list | output | kill (default: list)
- `job_id` (string) — Background job id (required for output/kill; from action='list')

Required: `action`

### scan_email_unsubscribes

(No prose section; see schema below.)

**Parameters:**
- `folder` (string) — IMAP folder to scan (default: INBOX)
- `limit` (integer) — Maximum candidates to return (default: 25)
- `max_scan` (integer) — How many newest emails to inspect (default: 150)
- `account` (string) — Optional account name/email/id from list_email_accounts

### serve_preset

(No prose section; see schema below.)

**Parameters:**
- `name` (string) — Preset name (exact or case-insensitive substring of one returned by list_serve_presets)

Required: `name`

### trigger_research

(No prose section; see schema below.)

**Parameters:**
- `topic` (string) — Research question or topic

Required: `topic`

### unsubscribe_email

(No prose section; see schema below.)

**Parameters:**
- `uid` (string) — Email UID from scan_email_unsubscribes/list_emails
- `folder` (string) — IMAP folder (default: INBOX)
- `method_index` (integer) — Method index from scan_email_unsubscribes (default: 0)
- `allow_web` (boolean) — Return browser/web instructions when selected method is URL
- `account` (string) — Optional account name/email/id from list_email_accounts

Required: `uid`

## MCP tools

### Server: Built-in: Browser

#### browser_close (`mcp__builtin_browser__browser_close`)

Close the page

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {},
  "additionalProperties": false
}
```

#### browser_resize (`mcp__builtin_browser__browser_resize`)

Resize the browser window

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {
    "width": {
      "type": "number",
      "description": "Width of the browser window"
    },
    "height": {
      "type": "number",
      "description": "Height of the browser window"
    }
  },
  "required": [
    "width",
    "height"
  ],
  "additionalProperties": false
}
```

#### browser_console_messages (`mcp__builtin_browser__browser_console_messages`)

Returns all console messages

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {
    "level": {
      "default": "info",
      "description": "Level of the console messages to return. Each level includes the messages of more severe levels. Defaults to \"info\".",
      "type": "string",
      "enum": [
        "error",
        "warning",
        "info",
        "debug"
      ]
    },
    "all": {
      "description": "Return all console messages since the beginning of the session, not just since the last navigation. Defaults to false.",
      "type": "boolean"
    },
    "filename": {
      "description": "Filename to save the console messages to. If not provided, messages are returned as text.",
      "type": "string"
    }
  },
  "required": [
    "level"
  ],
  "additionalProperties": false
}
```

#### browser_handle_dialog (`mcp__builtin_browser__browser_handle_dialog`)

Handle a dialog

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {
    "accept": {
      "type": "boolean",
      "description": "Whether to accept the dialog."
    },
    "promptText": {
      "description": "The text of the prompt in case of a prompt dialog.",
      "type": "string"
    }
  },
  "required": [
    "accept"
  ],
  "additionalProperties": false
}
```

#### browser_evaluate (`mcp__builtin_browser__browser_evaluate`)

Evaluate JavaScript expression on page or element

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {
    "element": {
      "description": "Human-readable element description used to obtain permission to interact with the element",
      "type": "string"
    },
    "target": {
      "description": "Exact target element reference from the page snapshot, or a unique element selector",
      "type": "string"
    },
    "function": {
      "type": "string",
      "description": "() => { /* code */ } or (element) => { /* code */ } when element is provided"
    },
    "filename": {
      "description": "Filename to save the result to. If not provided, result is returned as text.",
      "type": "string"
    }
  },
  "required": [
    "function"
  ],
  "additionalProperties": false
}
```

#### browser_file_upload (`mcp__builtin_browser__browser_file_upload`)

Upload one or multiple files

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {
    "paths": {
      "description": "The absolute paths to the files to upload. Can be single file or multiple files. If omitted, file chooser is cancelled.",
      "type": "array",
      "items": {
        "type": "string"
      }
    }
  },
  "additionalProperties": false
}
```

#### browser_drop (`mcp__builtin_browser__browser_drop`)

Drop files or MIME-typed data onto an element, as if dragged from outside the page. At least one of "paths" or "data" must be provided.

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {
    "element": {
      "description": "Human-readable element description used to obtain permission to interact with the element",
      "type": "string"
    },
    "target": {
      "type": "string",
      "description": "Exact target element reference from the page snapshot, or a unique element selector"
    },
    "paths": {
      "description": "Absolute paths to files to drop onto the element.",
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "data": {
      "description": "Data to drop, as a map of MIME type to string value (e.g. {\"text/plain\": \"hello\", \"text/uri-list\": \"https://example.com\"}).",
      "type": "object",
      "propertyNames": {
        "type": "string"
      },
      "additionalProperties": {
        "type": "string"
      }
    }
  },
  "required": [
    "target"
  ],
  "additionalProperties": false
}
```

#### browser_find (`mcp__builtin_browser__browser_find`)

Search the accessibility snapshot of the current page for text or a regular expression. Returns matching snapshot nodes with a few lines of surrounding context (like search snippets), each shown under its path from the root of the tree, which is cheaper than capturing the whole snapshot when you only need to locate an element and its ref.

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {
    "text": {
      "description": "Plain text to search for in the page snapshot (case-insensitive substring match). Provide either text or regex, not both.",
      "type": "string"
    },
    "regex": {
      "description": "Regular expression to search for in the page snapshot. Matching is case-sensitive by default; wrap the pattern in slashes to add flags, e.g. \"/error/i\" for case-insensitive. Provide either text or regex, not both.",
      "type": "string"
    }
  },
  "additionalProperties": false
}
```

#### browser_fill_form (`mcp__builtin_browser__browser_fill_form`)

Fill multiple form fields

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {
    "fields": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "element": {
            "description": "Human-readable element description used to obtain permission to interact with the element",
            "type": "string"
          },
          "target": {
            "type": "string",
            "description": "Exact target element reference from the page snapshot, or a unique element selector"
          },
          "name": {
            "type": "string",
            "description": "Human-readable field name"
          },
          "type": {
            "type": "string",
            "enum": [
              "textbox",
              "checkbox",
              "radio",
              "combobox",
              "slider"
            ],
            "description": "Type of the field"
          },
          "value": {
            "type": "string",
            "description": "Value to fill in the field. If the field is a checkbox, the value should be `true` or `false`. If the field is a combobox, the value should be the text of the option."
          }
        },
        "required": [
          "target",
          "name",
          "type",
          "value"
        ],
        "additionalProperties": false
      },
      "description": "Fields to fill in"
    }
  },
  "required": [
    "fields"
  ],
  "additionalProperties": false
}
```

#### browser_press_key (`mcp__builtin_browser__browser_press_key`)

Press a key on the keyboard

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {
    "key": {
      "type": "string",
      "description": "Name of the key to press or a character to generate, such as `ArrowLeft` or `a`"
    }
  },
  "required": [
    "key"
  ],
  "additionalProperties": false
}
```

#### browser_type (`mcp__builtin_browser__browser_type`)

Type text into editable element

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {
    "element": {
      "description": "Human-readable element description used to obtain permission to interact with the element",
      "type": "string"
    },
    "target": {
      "type": "string",
      "description": "Exact target element reference from the page snapshot, or a unique element selector"
    },
    "text": {
      "type": "string",
      "description": "Text to type into the element"
    },
    "submit": {
      "description": "Whether to submit entered text (press Enter after)",
      "type": "boolean"
    },
    "slowly": {
      "description": "Whether to type one character at a time. Useful for triggering key handlers in the page. By default entire text is filled in at once.",
      "type": "boolean"
    }
  },
  "required": [
    "target",
    "text"
  ],
  "additionalProperties": false
}
```

#### browser_mouse_move_xy (`mcp__builtin_browser__browser_mouse_move_xy`)

Move mouse to a given position

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {
    "x": {
      "type": "number",
      "description": "X coordinate"
    },
    "y": {
      "type": "number",
      "description": "Y coordinate"
    }
  },
  "required": [
    "x",
    "y"
  ],
  "additionalProperties": false
}
```

#### browser_mouse_click_xy (`mcp__builtin_browser__browser_mouse_click_xy`)

Click mouse button at a given position

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {
    "x": {
      "type": "number",
      "description": "X coordinate"
    },
    "y": {
      "type": "number",
      "description": "Y coordinate"
    },
    "button": {
      "description": "Button to click, defaults to left",
      "type": "string",
      "enum": [
        "left",
        "right",
        "middle"
      ]
    },
    "clickCount": {
      "description": "Number of clicks, defaults to 1",
      "type": "number"
    },
    "delay": {
      "description": "Time to wait between mouse down and mouse up in milliseconds, defaults to 0",
      "type": "number"
    }
  },
  "required": [
    "x",
    "y"
  ],
  "additionalProperties": false
}
```

#### browser_mouse_drag_xy (`mcp__builtin_browser__browser_mouse_drag_xy`)

Drag left mouse button to a given position

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {
    "startX": {
      "type": "number",
      "description": "Start X coordinate"
    },
    "startY": {
      "type": "number",
      "description": "Start Y coordinate"
    },
    "endX": {
      "type": "number",
      "description": "End X coordinate"
    },
    "endY": {
      "type": "number",
      "description": "End Y coordinate"
    }
  },
  "required": [
    "startX",
    "startY",
    "endX",
    "endY"
  ],
  "additionalProperties": false
}
```

#### browser_mouse_down (`mcp__builtin_browser__browser_mouse_down`)

Press mouse down

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {
    "button": {
      "description": "Button to press, defaults to left",
      "type": "string",
      "enum": [
        "left",
        "right",
        "middle"
      ]
    }
  },
  "additionalProperties": false
}
```

#### browser_mouse_up (`mcp__builtin_browser__browser_mouse_up`)

Press mouse up

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {
    "button": {
      "description": "Button to press, defaults to left",
      "type": "string",
      "enum": [
        "left",
        "right",
        "middle"
      ]
    }
  },
  "additionalProperties": false
}
```

#### browser_mouse_wheel (`mcp__builtin_browser__browser_mouse_wheel`)

Scroll mouse wheel

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {
    "deltaX": {
      "default": 0,
      "description": "X delta",
      "type": "number"
    },
    "deltaY": {
      "default": 0,
      "description": "Y delta",
      "type": "number"
    }
  },
  "required": [
    "deltaX",
    "deltaY"
  ],
  "additionalProperties": false
}
```

#### browser_navigate (`mcp__builtin_browser__browser_navigate`)

Navigate to a URL

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {
    "url": {
      "type": "string",
      "description": "The URL to navigate to"
    }
  },
  "required": [
    "url"
  ],
  "additionalProperties": false
}
```

#### browser_navigate_back (`mcp__builtin_browser__browser_navigate_back`)

Go back to the previous page in the history

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {},
  "additionalProperties": false
}
```

#### browser_network_requests (`mcp__builtin_browser__browser_network_requests`)

Returns a numbered list of network requests since loading the page. Use browser_network_request with the number to get full details.

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {
    "static": {
      "default": false,
      "description": "Whether to include successful static resources like images, fonts, scripts, etc. Defaults to false.",
      "type": "boolean"
    },
    "filter": {
      "description": "Only return requests whose URL matches this regexp (e.g. \"/api/.*user\").",
      "type": "string"
    },
    "filename": {
      "description": "Filename to save the network requests to. If not provided, requests are returned as text.",
      "type": "string"
    }
  },
  "required": [
    "static"
  ],
  "additionalProperties": false
}
```

#### browser_network_request (`mcp__builtin_browser__browser_network_request`)

Returns full details (headers and body) of a single network request, or a single part if `part` is set. Use the number from browser_network_requests.

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {
    "index": {
      "type": "integer",
      "minimum": 1,
      "maximum": 9007199254740991,
      "description": "1-based index of the request, as printed by browser_network_requests."
    },
    "part": {
      "description": "Return only this part of the request. Omit to return full details.",
      "type": "string",
      "enum": [
        "request-headers",
        "request-body",
        "response-headers",
        "response-body"
      ]
    },
    "filename": {
      "description": "Filename to save the result to. If not provided, output is returned as text.",
      "type": "string"
    }
  },
  "required": [
    "index"
  ],
  "additionalProperties": false
}
```

#### browser_run_code_unsafe (`mcp__builtin_browser__browser_run_code_unsafe`)

Run a Playwright code snippet. Unsafe: executes arbitrary JavaScript in the Playwright server process and is RCE-equivalent.

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {
    "code": {
      "description": "A JavaScript function containing Playwright code to execute. It will be invoked with a single argument, page, which you can use for any page interaction. For example: `async (page) => { await page.getByRole('button', { name: 'Submit' }).click(); return await page.title(); }`",
      "type": "string"
    },
    "filename": {
      "description": "Load code from the specified file. If both code and filename are provided, code will be ignored.",
      "type": "string"
    }
  },
  "additionalProperties": false
}
```

#### browser_take_screenshot (`mcp__builtin_browser__browser_take_screenshot`)

Take a screenshot of the current page. You can't perform actions based on the screenshot, use browser_snapshot for actions.

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {
    "element": {
      "description": "Human-readable element description used to obtain permission to interact with the element",
      "type": "string"
    },
    "target": {
      "description": "Exact target element reference from the page snapshot, or a unique element selector",
      "type": "string"
    },
    "type": {
      "description": "Image format for the screenshot. If unset, inferred from the filename extension, otherwise png.",
      "type": "string",
      "enum": [
        "png",
        "jpeg",
        "webp"
      ]
    },
    "filename": {
      "description": "File name to save the screenshot to. Defaults to `page-{timestamp}.{png|jpeg|webp}` if not specified. Prefer relative file names to stay within the output directory.",
      "type": "string"
    },
    "fullPage": {
      "description": "When true, takes a screenshot of the full scrollable page, instead of the currently visible viewport. Cannot be used with element screenshots.",
      "type": "boolean"
    },
    "scale": {
      "default": "css",
      "description": "Image resolution scale. \"css\" produces a screenshot sized in CSS pixels (smaller, consistent across devices). \"device\" produces a high-resolution screenshot using device pixels (larger, accounts for the device pixel ratio). Default is css.",
      "type": "string",
      "enum": [
        "css",
        "device"
      ]
    }
  },
  "required": [
    "scale"
  ],
  "additionalProperties": false
}
```

#### browser_snapshot (`mcp__builtin_browser__browser_snapshot`)

Capture accessibility snapshot of the current page, this is better than screenshot

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {
    "target": {
      "description": "Exact target element reference from the page snapshot, or a unique element selector",
      "type": "string"
    },
    "filename": {
      "description": "Save snapshot to markdown file instead of returning it in the response.",
      "type": "string"
    },
    "depth": {
      "description": "Limit the depth of the snapshot tree",
      "type": "number"
    },
    "boxes": {
      "description": "Include each element's bounding box as [box=x,y,width,height] in the snapshot. Coordinates are viewport-relative, in CSS pixels (Element.getBoundingClientRect)",
      "type": "boolean"
    }
  },
  "additionalProperties": false
}
```

#### browser_click (`mcp__builtin_browser__browser_click`)

Perform click on a web page

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {
    "element": {
      "description": "Human-readable element description used to obtain permission to interact with the element",
      "type": "string"
    },
    "target": {
      "type": "string",
      "description": "Exact target element reference from the page snapshot, or a unique element selector"
    },
    "doubleClick": {
      "description": "Whether to perform a double click instead of a single click",
      "type": "boolean"
    },
    "button": {
      "description": "Button to click, defaults to left",
      "type": "string",
      "enum": [
        "left",
        "right",
        "middle"
      ]
    },
    "modifiers": {
      "description": "Modifier keys to press",
      "type": "array",
      "items": {
        "type": "string",
        "enum": [
          "Alt",
          "Control",
          "ControlOrMeta",
          "Meta",
          "Shift"
        ]
      }
    }
  },
  "required": [
    "target"
  ],
  "additionalProperties": false
}
```

#### browser_drag (`mcp__builtin_browser__browser_drag`)

Perform drag and drop between two elements

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {
    "startElement": {
      "description": "Human-readable source element description used to obtain the permission to interact with the element",
      "type": "string"
    },
    "startTarget": {
      "type": "string",
      "description": "Exact target element reference from the page snapshot, or a unique element selector"
    },
    "endElement": {
      "description": "Human-readable target element description used to obtain the permission to interact with the element",
      "type": "string"
    },
    "endTarget": {
      "type": "string",
      "description": "Exact target element reference from the page snapshot, or a unique element selector"
    }
  },
  "required": [
    "startTarget",
    "endTarget"
  ],
  "additionalProperties": false
}
```

#### browser_hover (`mcp__builtin_browser__browser_hover`)

Hover over element on page

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {
    "element": {
      "description": "Human-readable element description used to obtain permission to interact with the element",
      "type": "string"
    },
    "target": {
      "type": "string",
      "description": "Exact target element reference from the page snapshot, or a unique element selector"
    }
  },
  "required": [
    "target"
  ],
  "additionalProperties": false
}
```

#### browser_select_option (`mcp__builtin_browser__browser_select_option`)

Select an option in a dropdown

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {
    "element": {
      "description": "Human-readable element description used to obtain permission to interact with the element",
      "type": "string"
    },
    "target": {
      "type": "string",
      "description": "Exact target element reference from the page snapshot, or a unique element selector"
    },
    "values": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "Array of values to select in the dropdown. This can be a single value or multiple values."
    }
  },
  "required": [
    "target",
    "values"
  ],
  "additionalProperties": false
}
```

#### browser_tabs (`mcp__builtin_browser__browser_tabs`)

List, create, close, or select a browser tab.

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {
    "action": {
      "type": "string",
      "enum": [
        "list",
        "new",
        "close",
        "select"
      ],
      "description": "Operation to perform"
    },
    "index": {
      "description": "Tab index, used for close/select. If omitted for close, current tab is closed.",
      "type": "number"
    },
    "url": {
      "description": "URL to navigate to in the new tab, used for new.",
      "type": "string"
    }
  },
  "required": [
    "action"
  ],
  "additionalProperties": false
}
```

#### browser_wait_for (`mcp__builtin_browser__browser_wait_for`)

Wait for text to appear or disappear or a specified time to pass

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {
    "time": {
      "description": "The time to wait in seconds",
      "type": "number"
    },
    "text": {
      "description": "The text to wait for",
      "type": "string"
    },
    "textGone": {
      "description": "The text to wait for to disappear",
      "type": "string"
    }
  },
  "additionalProperties": false
}
```
