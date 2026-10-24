# core/session_manager.py
"""
Session management — all session business logic and DB operations.

This is the single place that handles:
- Loading/saving sessions to database
- Adding messages to sessions
- Session lifecycle (create, archive, delete)
"""

import json
import uuid
import logging
import time
from datetime import datetime, timezone, timedelta
from typing import Dict, Optional

from sqlalchemy import func

from .database import Session as DbSession, ChatMessage as DbChatMessage, Document as DbDocument, SessionLocal, utcnow_naive
from .models import Session, ChatMessage
from src.attachment_refs import persistable_message_content
from src.upload_handler import reserve_message_upload_references
from sqlalchemy.exc import OperationalError

# Re-export singleton accessors from models for convenience
from .models import set_session_manager_instance, get_session_manager_instance

logger = logging.getLogger(__name__)


# ── Draft-write lock retry ──────────────────────────────────────────────────
# Draft checkpoints sit on the hot path (every ~4s per streaming agent) and
# the row write is idempotent, so a transient SQLite 'database is locked'
# should wait-and-retry instead of killing the whole stream (the agent_run
# dies with sqlite3.OperationalError when a checkpoint commit collides with
# another session's write). WAL + busy_timeout (core/database.py) make real
# contention rare; this is the belt-and-suspenders so a rare collision never
# takes down a live reply.
_DRAFT_LOCK_RETRIES = 4
_DRAFT_LOCK_BASE_DELAY = 0.1  # 0.1/0.2/0.4s backoff — invisible on a 4s cadence


def _commit_draft_with_retry(operation, what: str):
    """Run `operation(db)` retrying on SQLite write-lock contention.

    Each attempt gets a fresh session so a poisoned connection is never
    reused. Non-lock errors propagate immediately. Re-raises the last error
    if contention outlasts the retry budget.
    """
    last_exc = None
    for attempt in range(_DRAFT_LOCK_RETRIES):
        db = SessionLocal()
        try:
            return operation(db)
        except OperationalError as e:
            db.rollback()
            last_exc = e
            if "locked" not in str(e).lower():
                raise
            if attempt < _DRAFT_LOCK_RETRIES - 1:
                logger.warning(
                    "Draft %s hit DB lock (attempt %d/%d): %s",
                    what, attempt + 1, _DRAFT_LOCK_RETRIES, e,
                )
                time.sleep(_DRAFT_LOCK_BASE_DELAY * (2 ** attempt))
        finally:
            db.close()
    raise last_exc


def _message_timestamp_iso(value: Optional[datetime]) -> Optional[str]:
    """Return a stable ISO timestamp for chat message metadata."""
    if not value:
        return None
    if value.tzinfo is None:
        value = value.replace(tzinfo=timezone.utc)
    return value.isoformat().replace("+00:00", "Z")


def _parse_msg_content(raw):
    """Parse message content from DB — deserialises JSON arrays back to lists
    (multimodal content with image/audio attachments)."""
    if isinstance(raw, list):
        return raw
    if isinstance(raw, str) and raw.startswith('[{') and '"type"' in raw:
        try:
            parsed = json.loads(raw)
            # Only treat as serialized multimodal content when EVERY element is
            # a dict whose "type" is a recognized content-block kind. Otherwise a
            # plain text message that merely *looks* like a JSON array of objects
            # (e.g. a user pasting an API schema/sample with a "type" field) was
            # silently parsed back into a list, destroying the original string.
            _BLOCK_TYPES = {
                "text", "image", "image_url", "audio", "input_audio",
                "input_image", "document", "file",
            }
            if (isinstance(parsed, list) and parsed
                    and all(isinstance(p, dict) and p.get("type") in _BLOCK_TYPES
                            for p in parsed)):
                return parsed
        except (json.JSONDecodeError, ValueError):
            pass
    return raw


class SessionManager:
    """
    Manages chat sessions with database persistence.

    Usage:
        manager = SessionManager()
        session = manager.create_session(id, name, url, model)
        manager.add_message(session.id, ChatMessage("user", "hello"))
        session = manager.get_session(session_id)
    """

    def __init__(self, sessions_file: str = None):
        # sessions_file kept for backward compat, not used
        self.sessions: Dict[str, Session] = {}
        self.upload_handler = None
        self.load_sessions()

    # ------------------------------------------------------------------
    # Loading
    # ------------------------------------------------------------------

    def load_sessions(self):
        """Load recent session METADATA from the database — messages are
        hydrated on demand by `get_session`. Previously this walked every
        message of every session into RAM at boot, which on a long-running
        personal-server box could be tens of thousands of rows held forever
        in `self.sessions`.
        """
        db = SessionLocal()
        try:
            db_sessions = db.query(DbSession).filter(
                DbSession.archived == False,
                DbSession.messages.any(),
            ).order_by(DbSession.last_accessed.desc()).limit(100).all()

            # message_count is derived metadata and can drift after interrupted
            # or legacy writes. Count only the bounded discovery set so startup
            # remains metadata-only while lazy hydration sees an authoritative
            # positive count for every discovered non-empty session.
            message_counts = {}
            if db_sessions:
                message_counts = dict(
                    db.query(DbChatMessage.session_id, func.count(DbChatMessage.id))
                    .filter(DbChatMessage.session_id.in_([row.id for row in db_sessions]))
                    .filter(
                        ~func.coalesce(DbChatMessage.meta_data, "").like('%"archived": true%'),
                        ~func.coalesce(DbChatMessage.meta_data, "").like('%"archived":true%'),
                    )
                    .group_by(DbChatMessage.session_id)
                    .all()
                )

            loaded_count = 0
            for db_session in db_sessions:
                try:
                    session = self._db_to_session_meta(db_session)
                    if session is not None:
                        session.message_count = message_counts[db_session.id]
                        self.sessions[db_session.id] = session
                        loaded_count += 1
                except Exception as e:
                    logger.error(f"Error loading session {db_session.id}: {e}")
                    continue

            logger.info(f"Loaded {loaded_count} session(s) (metadata only)")

        except Exception as e:
            logger.error(f"Error loading sessions: {e}")
            self.sessions = {}
        finally:
            db.close()

    def _db_to_session_meta(self, db_session: DbSession) -> Optional[Session]:
        """Build a Session with empty history. `get_session` will hydrate
        messages from the DB on first read."""
        headers = db_session.headers
        if isinstance(headers, str):
            try:
                headers = json.loads(headers)
            except json.JSONDecodeError:
                headers = {}
        session = Session(
            id=db_session.id,
            name=db_session.name,
            endpoint_url=db_session.endpoint_url,
            model=db_session.model,
            rag=db_session.rag,
            archived=db_session.archived,
            headers=headers,
            history=[],
            owner=getattr(db_session, "owner", None),
            is_important=getattr(db_session, "is_important", False) or False,
        )
        session.message_count = getattr(db_session, "message_count", 0) or 0
        return session

    def _db_to_session(self, db_session: DbSession, db) -> Optional[Session]:
        """Convert a database session to a Session object."""
        history = []

        def _draft_ok(db_msg, meta) -> bool:
            """Draft-row policy at hydration time (2026-08-08
            draft-checkpoint audit): a live draft (an active stream is still
            checkpointing it) must NEVER enter the model's context, so it is
            skipped; an orphaned draft (no active stream — the server died
            mid-turn) is finalized to a stopped partial and kept, so the
            crashed turn survives as a visible, resumable message."""
            if not meta.get("draft"):
                return True
            try:
                from routes.chat_routes import _active_streams
                rec = _active_streams.get(db_msg.session_id)
            except Exception:
                rec = None
            if rec and rec.get("status") == "streaming":
                return False
            meta.pop("draft", None)
            meta["stopped"] = True
            try:
                self.finalize_orphan_draft(db_msg.session_id, db_msg.id)
            except Exception:
                logger.exception("Failed to finalize orphan draft %s", db_msg.id)
            return True

        # Try relationship first, then direct query
        if db_session.messages:
            for db_msg in db_session.messages:
                meta = json.loads(db_msg.meta_data) if db_msg.meta_data else {}
                if meta is None: meta = {}
                # Compaction archive (2026-10-23): flagged rows stay on disk
                # but never re-enter the live transcript or model context.
                if meta.get("archived"):
                    continue
                if not _draft_ok(db_msg, meta):
                    continue
                meta['_db_id'] = db_msg.id
                meta.setdefault('timestamp', _message_timestamp_iso(db_msg.timestamp))
                history.append(ChatMessage(
                    role=db_msg.role,
                    content=_parse_msg_content(db_msg.content),
                    metadata=meta,
                ))
        else:
            db_messages = db.query(DbChatMessage).filter(
                DbChatMessage.session_id == db_session.id
            ).filter(
                ~func.coalesce(DbChatMessage.meta_data, "").like('%"archived": true%'),
                ~func.coalesce(DbChatMessage.meta_data, "").like('%"archived":true%'),
            ).order_by(DbChatMessage.timestamp).all()

            for db_msg in db_messages:
                meta = json.loads(db_msg.meta_data) if db_msg.meta_data else {}
                if meta is None: meta = {}
                if not _draft_ok(db_msg, meta):
                    continue
                meta['_db_id'] = db_msg.id
                meta.setdefault('timestamp', _message_timestamp_iso(db_msg.timestamp))
                history.append(ChatMessage(
                    role=db_msg.role,
                    content=_parse_msg_content(db_msg.content),
                    metadata=meta,
                ))

        if not history:
            return None

        # Parse headers
        headers = db_session.headers
        if isinstance(headers, str):
            try:
                headers = json.loads(headers)
            except json.JSONDecodeError:
                headers = {}

        session = Session(
            id=db_session.id,
            name=db_session.name,
            endpoint_url=db_session.endpoint_url,
            model=db_session.model,
            rag=db_session.rag,
            archived=db_session.archived,
            headers=headers,
            history=history,
            owner=getattr(db_session, 'owner', None),
            is_important=getattr(db_session, 'is_important', False) or False,
        )

        # The rows just loaded are the whole transcript, so they — not the
        # denormalized sessions.message_count column — are the truth for this
        # cached object. get_session's hydration gate compares against this
        # number; seeding it from a drifted column would ask for a reload that
        # can never close the gap.
        session.message_count = len(history)
        return session

    # ------------------------------------------------------------------
    # Message operations
    # ------------------------------------------------------------------

    def add_message(self, session_id: str, message: ChatMessage):
        """
        Add a message to a session and persist to database.

        Updates the authoritative history list and persists through this
        manager directly so tests and temporary managers do not depend on the
        process-wide session-manager singleton.

        Persistence happens after the in-memory append, but a failed persist
        rolls the append back: a message that lives only in memory is
        invisible to refresh, undeletable by id, and desyncs the model's
        context from the DB (2026-08-08, see changelog). Real persist
        failures re-raise so callers surface them; a soft drop for an
        already-deleted session is silent.

        Args:
            session_id: Session ID
            message: ChatMessage to add
        """
        session = self.get_session(session_id)
        session.history.append(message)
        session._history = session.history
        session.message_count = len(session.history)

        try:
            persisted = self._persist_message(session_id, message)
        except Exception:
            session.history.pop()
            session._history = session.history
            session.message_count = len(session.history)
            raise

        if not persisted:
            # Session was deleted mid-flight — drop the orphaned copy too so
            # memory and DB agree.
            session.history.pop()
            session._history = session.history
            session.message_count = len(session.history)

    def _persist_message(self, session_id: str, message: ChatMessage) -> bool:
        """Persist a single message to the database.

        Returns True on success, False when the session no longer exists
        (message intentionally dropped). Raises on real persist failures so
        callers surface them instead of ghosting a memory-only message.
        """
        db = SessionLocal()
        try:
            db_session = db.query(DbSession).filter(DbSession.id == session_id).first()
            if db_session is None:
                # A stream/tool callback can outlive a session delete. Do not
                # create a chat_messages row with no parent session; also drop
                # any stale cached session so later writes fail closed too.
                self.sessions.pop(session_id, None)
                logger.warning("Dropping message for deleted session %s", session_id)
                return False

            missing_upload_id = reserve_message_upload_references(
                getattr(self, "upload_handler", None),
                getattr(db_session, "owner", None),
                message.content,
                message.metadata,
            )
            if missing_upload_id:
                raise ValueError(
                    f"Referenced upload is no longer available: {missing_upload_id}"
                )

            missing_upload_id = reserve_message_upload_references(
                getattr(self, "upload_handler", None),
                getattr(db_session, "owner", None),
                message.content,
                message.metadata,
            )
            if missing_upload_id:
                raise ValueError(
                    f"Referenced upload is no longer available: {missing_upload_id}"
                )

            msg_id = str(uuid.uuid4())
            msg_time = datetime.utcnow()
            if message.metadata is None:
                message.metadata = {}
            message.metadata.setdefault('timestamp', _message_timestamp_iso(msg_time))
            # Multimodal content may contain provider data URLs for the live
            # model call. Persist only readable text plus attachment references
            # so chat_messages/FTS do not duplicate upload bytes.
            _content = persistable_message_content(message.content, message.metadata)
            db_message = DbChatMessage(
                id=msg_id,
                session_id=session_id,
                role=message.role,
                content=_content,
                meta_data=json.dumps(message.metadata) if message.metadata else None,
                timestamp=msg_time,
            )
            db.add(db_message)

            if session_id in self.sessions:
                db_session.message_count = len(self.sessions[session_id].history)
            else:
                db_session.message_count = 0
            _now = datetime.now(timezone.utc)
            db_session.last_accessed = _now
            # Clean "last conversation" timestamp — only bumped here on a
            # real message persist, so it powers an accurate "Last active"
            # sort that ignores renames / model swaps / mere opens.
            db_session.last_message_at = _now

            db.commit()

            # Store DB ID on the in-memory message for edit/delete by ID
            message.metadata['_db_id'] = msg_id

            logger.debug(f"Persisted message to session {session_id}")
            return True

        except Exception as e:
            logger.error(f"Error persisting message: {e}")
            db.rollback()
            raise
        finally:
            db.close()

    # ── Progressive draft checkpoint (2026-08-08 draft-checkpoint audit) ──
    # While a turn streams, the in-flight reply is checkpointed every few
    # seconds into a DB-only "draft" row (metadata["draft"]=True). If the
    # process dies mid-turn the partial survives on disk; the history reader
    # finalizes orphaned drafts as stopped partials on next read. Drafts are
    # never appended to in-memory history (the model's context must never see
    # half-written replies) and are promoted IN PLACE on completion so the
    # frontend's stamped bubble keeps the same row id with no duplicate.

    def create_draft(self, session_id: str, content: str, metadata: dict) -> Optional[str]:
        """Create a checkpointed draft row for an in-flight assistant reply.

        DB-only — nothing touches in-memory history. Returns the new row id,
        or None when the session is gone (soft-drop, mirrors _persist_message).
        """
        if metadata is None:
            metadata = {}
        def _create(db):
            db_session = db.query(DbSession).filter(DbSession.id == session_id).first()
            if db_session is None:
                self.sessions.pop(session_id, None)
                logger.warning("Dropping draft for deleted session %s", session_id)
                return None
            metadata.setdefault('timestamp', _message_timestamp_iso(datetime.utcnow()))
            metadata['draft'] = True
            msg_id = str(uuid.uuid4())
            db_message = DbChatMessage(
                id=msg_id,
                session_id=session_id,
                role="assistant",
                content=persistable_message_content(content, metadata),
                meta_data=json.dumps(metadata) if metadata else None,
                timestamp=datetime.utcnow(),
            )
            db.add(db_message)
            db.commit()
            logger.debug(f"Checkpointed draft {msg_id} for session {session_id}")
            return msg_id
        try:
            return _commit_draft_with_retry(_create, "create")
        except Exception as e:
            logger.error(f"Error creating draft for session {session_id}: {e}")
            raise

    def update_draft(self, session_id: str, draft_id: str, content: str, metadata: dict) -> bool:
        """In-place content/metadata update of a draft row (throttled checkpoint).

        Only the message row is touched — session timestamps/counts are not
        bumped per checkpoint. Returns False when the row is gone (caller
        falls back to creating a fresh draft).
        """
        def _update(db):
            db_message = db.query(DbChatMessage).filter(
                DbChatMessage.id == draft_id,
                DbChatMessage.session_id == session_id,
            ).first()
            if db_message is None:
                return False
            db_message.content = persistable_message_content(content, metadata)
            db_message.meta_data = json.dumps(metadata) if metadata else None
            db.commit()
            return True
        try:
            return _commit_draft_with_retry(_update, "update")
        except Exception as e:
            logger.error(f"Error updating draft {draft_id}: {e}")
            raise

    def promote_draft(self, session_id: str, draft_id: str, message: ChatMessage) -> str:
        """Promote a checkpointed draft row to a final message.

        Updates the draft row IN PLACE (same id — the frontend already
        stamped the bubble via the draft_saved event), appends the message to
        in-memory history, and stamps metadata['_db_id'] = draft_id. Falls
        back to a fresh _persist_message when the draft row vanished (e.g.
        the session was wiped mid-turn). Returns the final row id, or '' when
        the session no longer exists.
        """
        session = self.get_session(session_id)
        db = SessionLocal()
        try:
            db_session = db.query(DbSession).filter(DbSession.id == session_id).first()
            if db_session is None:
                self.sessions.pop(session_id, None)
                logger.warning("Dropping promoted draft for deleted session %s", session_id)
                return ""
            db_message = db.query(DbChatMessage).filter(
                DbChatMessage.id == draft_id,
                DbChatMessage.session_id == session_id,
            ).first()
            if db_message is None:
                # Draft gone (session wiped mid-turn) — plain persist path.
                session.history.append(message)
                session._history = session.history
                session.message_count = len(session.history)
                self._persist_message(session_id, message)
                _meta = getattr(message, "metadata", None) or {}
                return _meta.get("_db_id", "")

            missing_upload_id = reserve_message_upload_references(
                getattr(self, "upload_handler", None),
                getattr(db_session, "owner", None),
                message.content,
                message.metadata,
            )
            if missing_upload_id:
                raise ValueError(
                    f"Referenced upload is no longer available: {missing_upload_id}"
                )

            if message.metadata is None:
                message.metadata = {}
            message.metadata.setdefault('timestamp', _message_timestamp_iso(datetime.utcnow()))
            _content = persistable_message_content(message.content, message.metadata)
            db_message.content = _content
            db_message.meta_data = json.dumps(message.metadata) if message.metadata else None
            # Keep the draft row's original timestamp — ordering is stable and
            # the turn's "first byte" time is closer to when it was received.
            _now = datetime.now(timezone.utc)
            db_session.last_accessed = _now
            db_session.last_message_at = _now
            if session_id in self.sessions:
                db_session.message_count = len(self.sessions[session_id].history) + 1
            else:
                db_session.message_count = (db_session.message_count or 0) + 1
            db.commit()

            message.metadata['_db_id'] = draft_id
            session.history.append(message)
            session._history = session.history
            session.message_count = len(session.history)
            logger.debug(f"Promoted draft {draft_id} for session {session_id}")
            return draft_id
        except Exception as e:
            logger.error(f"Error promoting draft {draft_id}: {e}")
            db.rollback()
            raise
        finally:
            db.close()

    def finalize_orphan_draft(self, session_id: str, draft_id: str) -> bool:
        """Turn an orphaned draft row into a stopped partial.

        Called lazily by the history reader when a draft row has no active
        stream — i.e. the server died mid-turn and the checkpoint is all that
        survives. Drops the draft flag and marks it stopped so it renders as
        a resumable "[Message interrupted]" partial instead of vanishing or
        masquerading as a finished reply. Returns False when the row is gone.
        """
        db = SessionLocal()
        try:
            db_message = db.query(DbChatMessage).filter(
                DbChatMessage.id == draft_id,
                DbChatMessage.session_id == session_id,
            ).first()
            if db_message is None:
                return False
            try:
                meta = json.loads(db_message.meta_data) if db_message.meta_data else {}
            except (TypeError, ValueError):
                meta = {}
            if not isinstance(meta, dict):
                meta = {}
            meta.pop("draft", None)
            meta["stopped"] = True
            db_message.meta_data = json.dumps(meta) if meta else None
            db.commit()
            return True
        except Exception as e:
            logger.error(f"Error finalizing orphan draft {draft_id}: {e}")
            db.rollback()
            raise
        finally:
            db.close()

    def truncate_messages(self, session_id: str, keep_count: int) -> bool:
        """Truncate session history, keeping only the first `keep_count` messages."""
        session = self.get_session(session_id)

        if keep_count < 0:
            return False

        db = SessionLocal()
        try:
            db_messages = db.query(DbChatMessage).filter(
                DbChatMessage.session_id == session_id
            ).order_by(DbChatMessage.timestamp).all()

            deleted = 0
            for msg in db_messages[keep_count:]:
                db.delete(msg)
                deleted += 1

            db_session = db.query(DbSession).filter(DbSession.id == session_id).first()
            if db_session:
                # keep_count can exceed the real message total (e.g. the AI tool
                # defaults to keep_count=10 on a short session); message_count must
                # track the rows that actually remain, not the requested cap.
                db_session.message_count = min(keep_count, len(db_messages))
                db_session.updated_at = datetime.now(timezone.utc)

            db.commit()

            # Update in-memory
            session.history = session.history[:keep_count]
            session._history = session.history

            if deleted:
                logger.info(
                    "Truncated session %s to %d messages (deleted %d rows from tail: indices %d-%d)",
                    session_id, keep_count, deleted, keep_count, len(db_messages) - 1,
                )
            else:
                logger.info(f"Truncated session {session_id} to {keep_count} messages (no rows deleted)")
            return True

        except Exception as e:
            logger.error(f"Error truncating session: {e}")
            db.rollback()
            return False
        finally:
            db.close()

    def replace_messages(self, session_id: str, messages: list) -> bool:
        """Replace a session's persisted and in-memory history atomically."""
        session = self.get_session(session_id)
        db = SessionLocal()
        try:
            db_session = db.query(DbSession).filter(DbSession.id == session_id).first()
            if db_session is None:
                logger.warning("Cannot replace history for missing session %s", session_id)
                return False

            # Reserve every incoming attachment before removing any durable
            # message row. reserve_upload() shares the upload lifecycle lock
            # with cleanup, so an upload cannot be deleted between this
            # ownership check/access touch and the replacement transaction.
            # A failed reservation must leave the existing transcript intact.
            for message in messages:
                missing_upload_id = reserve_message_upload_references(
                    getattr(self, "upload_handler", None),
                    getattr(db_session, "owner", None),
                    message.content,
                    message.metadata,
                )
                if missing_upload_id:
                    raise ValueError(
                        f"Referenced upload is no longer available: {missing_upload_id}"
                    )

            # ------------------------------------------------------------------
            # Reconcile, don't incinerate (2026-10-23 compaction reform):
            # rows the incoming history no longer references are ARCHIVED in
            # place — flagged, never deleted — so compaction stays reversible
            # and the transcript remains whole on disk. Rows still referenced
            # via metadata._db_id keep their original ids and timestamps
            # instead of being churned through delete + re-insert.
            # ------------------------------------------------------------------
            existing_rows = {
                row.id: row
                for row in db.query(DbChatMessage)
                .filter(DbChatMessage.session_id == session_id)
                .all()
            }
            kept_ids = set()
            for message in messages:
                mid = (message.metadata or {}).get("_db_id") if isinstance(message.metadata, dict) else None
                if mid and mid in existing_rows:
                    kept_ids.add(mid)

            now = datetime.now(timezone.utc)
            archived_count = 0
            for row_id, row in existing_rows.items():
                if row_id in kept_ids:
                    continue
                try:
                    meta = json.loads(row.meta_data) if row.meta_data else {}
                except Exception:
                    meta = {}
                if not isinstance(meta, dict):
                    meta = {}
                if meta.get("archived"):
                    continue  # already archived by an earlier pass
                meta["archived"] = True
                meta["archived_at"] = now.isoformat()
                meta["archived_by"] = "replace_messages"
                row.meta_data = json.dumps(meta, ensure_ascii=False)
                archived_count += 1

            for i, message in enumerate(messages):
                mid = (message.metadata or {}).get("_db_id") if isinstance(message.metadata, dict) else None
                if mid and mid in existing_rows:
                    # Already persisted: keep the original row untouched
                    # (id, timestamp, content and metadata all survive).
                    continue
                msg_id = str(uuid.uuid4())
                ts = now + timedelta(microseconds=i)
                if isinstance(message.metadata, dict) and message.metadata.get("timestamp"):
                    try:
                        _ts = datetime.fromisoformat(
                            str(message.metadata["timestamp"]).replace("Z", "+00:00")
                        )
                        if _ts.tzinfo is not None:
                            _ts = _ts.astimezone(timezone.utc).replace(tzinfo=None)
                        ts = _ts
                    except Exception:
                        pass
                db_message = DbChatMessage(
                    id=msg_id,
                    session_id=session_id,
                    role=message.role,
                    # Mirrors _persist_message: keep raw media bytes out of the
                    # persisted transcript and search index.
                    content=persistable_message_content(message.content, message.metadata),
                    meta_data=json.dumps(message.metadata) if message.metadata else None,
                    timestamp=ts,
                )
                db.add(db_message)
                if message.metadata is None:
                    message.metadata = {}
                message.metadata["_db_id"] = msg_id

            db_session.message_count = len(messages)
            db_session.updated_at = now
            db_session.last_accessed = now
            db_session.last_message_at = now

            db.commit()
            session.history = list(messages)
            session._history = session.history
            session.message_count = len(messages)
            logger.info(
                "Replaced session %s history with %d messages (archived %d rows)",
                session_id, len(messages), archived_count,
            )
            return True
        except Exception as e:
            logger.error("Error replacing session history: %s", e)
            db.rollback()
            return False
        finally:
            db.close()

    # ------------------------------------------------------------------
    # Session CRUD
    # ------------------------------------------------------------------

    def get_session(self, session_id: str) -> Session:
        """Get a session by ID, loading complete DB history when needed.

        Sessions seeded by ``load_sessions`` start with empty history, and a
        cached session can also become partially stale. Refresh metadata first,
        then hydrate whenever the cached transcript is short of the stored rows.
        Model-send routes enter through this method before building context,
        while paginated display history reads SQLite directly.

        The gate compares against ``sync_session_metadata``'s reconciled count
        (the real ``chat_messages`` total), never the denormalized column, so a
        hydrate always closes the gap and the next read is a cache hit.
        """
        if session_id not in self.sessions:
            self._load_session_from_db(session_id)

        # Keep model/endpoint metadata fresh. Endpoint deletion can clear the
        # DB row while a session object is still cached in RAM. Refreshing first
        # also exposes the authoritative message count before completeness is
        # checked.
        self.sync_session_metadata(session_id)

        cached = self.sessions[session_id]
        cached_count = len(cached.history or [])
        stored_count = int(getattr(cached, "message_count", 0) or 0)
        if cached_count < stored_count:
            self._load_session_from_db(session_id)

        # Update last_accessed
        self._touch_session(session_id)

        return self.sessions[session_id]

    def sync_session_metadata(self, session_id: str) -> bool:
        """Refresh non-message session fields from the DB into the cached object.

        ``message_count`` is reconciled against the real ``chat_messages`` rows
        rather than copied from the denormalized ``sessions.message_count``
        column. That column drifts in normal operation — ``_persist_message``
        swallows a failed insert but ``add_message`` has already appended in
        memory, so the next successful persist writes rows+1, and a persist for
        an uncached session writes 0. Hydration keys off this number: a
        drifted-high column would reload the whole transcript on every warm
        read, and a drifted-low one would leave the model a truncated one.
        """
        session = self.sessions.get(session_id)
        if session is None:
            return False
        db = SessionLocal()
        try:
            db_session = db.query(DbSession).filter(DbSession.id == session_id).first()
            if db_session is None:
                return False
            headers = db_session.headers
            if isinstance(headers, str):
                try:
                    headers = json.loads(headers)
                except json.JSONDecodeError:
                    headers = {}
            session.name = db_session.name
            session.endpoint_url = db_session.endpoint_url or ""
            session.model = db_session.model or ""
            session.headers = headers or {}
            session.rag = db_session.rag
            session.archived = db_session.archived
            session.owner = getattr(db_session, "owner", None)
            session.is_important = getattr(db_session, "is_important", False) or False
            session.message_count = (
                db.query(DbChatMessage)
                .filter(DbChatMessage.session_id == session_id)
                .filter(
                    ~func.coalesce(DbChatMessage.meta_data, "").like('%"archived": true%'),
                    ~func.coalesce(DbChatMessage.meta_data, "").like('%"archived":true%'),
                )
                .count()
            )
            return True
        except Exception as e:
            logger.error(f"Error syncing session metadata {session_id}: {e}")
            return False
        finally:
            db.close()

    def _load_session_from_db(self, session_id: str):
        """Hydrate a single session (with messages) from the database."""
        db = SessionLocal()
        try:
            db_session = db.query(DbSession).filter(DbSession.id == session_id).first()
            if db_session is None:
                raise KeyError(f"Session {session_id} not found")

            session = self._db_to_session(db_session, db)
            if session:
                self.sessions[session_id] = session
            else:
                # No messages — fall back to metadata-only entry so callers
                # don't crash on KeyError for empty sessions.
                meta = self._db_to_session_meta(db_session)
                if meta is None:
                    raise KeyError(f"Session {session_id} could not be loaded")
                self.sessions[session_id] = meta

        except KeyError:
            raise
        except Exception as e:
            logger.error(f"Error loading session {session_id}: {e}")
            raise
        finally:
            db.close()

    def _touch_session(self, session_id: str):
        """Update last_accessed timestamp."""
        db = SessionLocal()
        try:
            db_session = db.query(DbSession).filter(DbSession.id == session_id).first()
            if db_session:
                db_session.last_accessed = datetime.now(timezone.utc)
                db.commit()
        except Exception as e:
            logger.error(f"Error updating last_accessed: {e}")
            db.rollback()
        finally:
            db.close()

    def create_session(
        self,
        session_id: str,
        name: str,
        endpoint_url: str,
        model: str,
        rag: bool = False,
        owner: str = None
    ) -> Session:
        """Create a new session and save to database."""
        db = SessionLocal()
        try:
            db_session = DbSession(
                id=session_id,
                name=name,
                endpoint_url=endpoint_url,
                model=model,
                rag=rag,
                headers={},
                owner=owner,
                created_at=datetime.now(timezone.utc),
                updated_at=datetime.now(timezone.utc)
            )
            db.add(db_session)
            db.commit()

            session = Session(
                id=session_id,
                name=name,
                endpoint_url=endpoint_url,
                model=model,
                rag=rag,
                headers={},
                owner=owner,
            )

            self.sessions[session_id] = session
            return session

        except Exception as e:
            db.rollback()
            logger.error(f"Error creating session: {e}")
            raise
        finally:
            db.close()

    def delete_session(self, session_id: str) -> bool:
        """Permanently delete a session and all its messages."""
        db = SessionLocal()
        try:
            try:
                from src.session_image_cleanup import cleanup_session_images
                cleanup_session_images(session_id, db=db)
            except Exception as e:
                logger.warning(f"Image cleanup failed while deleting session {session_id}: {e}")

            # Detach documents so they survive as orphans in the library
            db.query(DbDocument).filter(DbDocument.session_id == session_id).update(
                {DbDocument.session_id: None}, synchronize_session=False
            )

            # Delete messages
            db.query(DbChatMessage).filter(DbChatMessage.session_id == session_id).delete()

            # Delete session
            db_session = db.query(DbSession).filter(DbSession.id == session_id).first()
            if db_session:
                db.delete(db_session)

            # Drop the in-memory copy even when there is no DB row. A "ghost"
            # session lives only here (never persisted, or its row was removed
            # out-of-band); without this it can never be cleared and keeps
            # 404ing on every operation (issue #1044).
            removed_in_memory = self.sessions.pop(session_id, None) is not None

            if db_session or removed_in_memory:
                # Commit the document-detach / message-delete above (a no-op when
                # the ghost had no rows) together with the session delete.
                db.commit()
                logger.info(f"Deleted session {session_id}")
                return True
            return False

        except Exception as e:
            logger.error(f"Error deleting session: {e}")
            db.rollback()
            return False
        finally:
            db.close()

    # ------------------------------------------------------------------
    # Session updates
    # ------------------------------------------------------------------

    def update_session_name(self, session_id: str, name: str):
        """Update session name."""
        if session_id not in self.sessions:
            return

        db = SessionLocal()
        try:
            db_session = db.query(DbSession).filter(DbSession.id == session_id).first()
            if db_session:
                db_session.name = name
                db_session.updated_at = datetime.now(timezone.utc)
                db.commit()
                self.sessions[session_id].name = name
        except Exception as e:
            db.rollback()
            logger.error(f"Error updating session name: {e}")
            raise
        finally:
            db.close()

    def archive_session(self, session_id: str):
        """Archive a session."""
        if session_id not in self.sessions:
            return

        db = SessionLocal()
        try:
            db_session = db.query(DbSession).filter(DbSession.id == session_id).first()
            if db_session:
                db_session.archived = True
                db_session.updated_at = datetime.now(timezone.utc)
                db.commit()
                self.sessions[session_id].archived = True
        except Exception as e:
            db.rollback()
            logger.error(f"Error archiving session: {e}")
            raise
        finally:
            db.close()

    def mark_important(self, session_id: str, important: bool = True):
        """Mark session as important."""
        db = SessionLocal()
        try:
            db_session = db.query(DbSession).filter(DbSession.id == session_id).first()
            if db_session:
                db_session.is_important = important
                db_session.updated_at = datetime.now(timezone.utc)
                db.commit()

                if session_id in self.sessions:
                    self.sessions[session_id].is_important = important
            else:
                raise KeyError(f"Session {session_id} not found")
        except Exception as e:
            db.rollback()
            logger.error(f"Error marking session important: {e}")
            raise
        finally:
            db.close()

    # ------------------------------------------------------------------
    # Queries
    # ------------------------------------------------------------------

    def get_sessions_for_user(self, username: Optional[str] = None) -> Dict[str, Session]:
        """Return sessions for a specific user (or all if username is None)."""
        if username is None:
            return self.sessions
        return {
            sid: s for sid, s in self.sessions.items()
            if s.owner == username
        }

    def save_sessions(self):
        """No-op for DB compatibility."""

    def ensure_task_session(self, session_id: str, name: str, endpoint_url: str, model: str, owner: str = None, task: object = None) -> Session:
        """Create a task session if it doesn't exist, or return the existing one.

        Unlike create_session, this checks the cache first and does NOT
        overwrite an existing in-memory session. The task scheduler must
        use this instead of direct dict assignment.
        """
        if session_id in self.sessions:
            return self.sessions[session_id]

        session = self.create_session(session_id, name, endpoint_url, model, owner=owner)
        if task is not None:
            task.session_id = session_id
        return session

    # ------------------------------------------------------------------
    # Cleanup
    # ------------------------------------------------------------------

    def cleanup_empty_sessions(self, auto_archive_days: int = 30, min_age_hours: int = 1) -> dict:
        """Clean up empty and old sessions.

        Args:
            auto_archive_days: Age in days before non-important sessions are archived.
            min_age_hours: Minimum age in hours before an empty session can be deleted.
                          Prevents deleting sessions that were just created.
        """
        db = SessionLocal()
        stats = {'deleted_empty': 0, 'archived_old': 0, 'total_checked': 0}

        try:
            all_sessions = db.query(DbSession).all()
            cutoff_date = utcnow_naive() - timedelta(days=auto_archive_days)
            min_age = utcnow_naive() - timedelta(hours=min_age_hours)

            for db_session in all_sessions:
                stats['total_checked'] += 1

                # Delete empty sessions only if older than min_age_hours
                if db_session.message_count == 0:
                    if db_session.created_at is not None:
                        created = db_session.created_at
                        if created.tzinfo is None:
                            created = created.replace(tzinfo=timezone.utc)
                        if created > min_age:
                            continue  # Too young to delete
                    if db_session.id in self.sessions:
                        del self.sessions[db_session.id]
                    db.delete(db_session)
                    stats['deleted_empty'] += 1

                # Archive old sessions
                elif (not db_session.archived and
                      db_session.last_accessed and
                      db_session.last_accessed < cutoff_date and
                      db_session.message_count > 0 and
                      not getattr(db_session, 'is_important', False)):
                    db_session.archived = True
                    stats['archived_old'] += 1

            db.commit()
            logger.info(f"Cleanup: {stats['deleted_empty']} deleted, {stats['archived_old']} archived")

        except Exception as e:
            logger.error(f"Cleanup error: {e}")
            db.rollback()
            raise
        finally:
            db.close()

        return stats
