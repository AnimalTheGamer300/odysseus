/**
 * Clickable up/down prompt-history recall beside the chat composer.
 *
 *   ↑ — walk OLDER prompts (previous user messages)
 *   ↓ — walk NEWER prompts (back toward the current draft / blank)
 *
 * All keyboard shortcuts are left completely alone — every arrow key (plain,
 * Shift+, Ctrl+, Alt+) keeps its native textarea caret/selection behavior so
 * the user can shape their message with the keyboard. The in-progress draft
 * is saved when a walk starts and restored when you walk back past the newest
 * prompt, so nothing gets obliterated.
 */

/**
 * User bubbles in the active chat surface (#chat-history), newest first, using
 * dataset.raw (same source as resend/regenerate in chat.js).
 *
 * @param {Document | Element} [root=document]
 * @returns {string[]}
 */
export function getUserMessagesFromChatHistory(root = document) {
  const chatBox =
    root && root.id === 'chat-history' && typeof root.querySelectorAll === 'function'
      ? root
      : (root.getElementById ? root.getElementById('chat-history') : null);
  if (!chatBox) return [];

  const users = chatBox.querySelectorAll('.msg-user');
  const prompts = [];
  for (let i = users.length - 1; i >= 0; i--) {
    const msg = users[i];
    const bodyEl = msg.querySelector('.body');
    const text = msg.dataset?.raw || (bodyEl ? bodyEl.textContent : '') || '';
    if (text) prompts.push(text);
  }
  return prompts;
}

/**
 * Last user bubble in the active chat surface (#chat-history).
 *
 * @param {Document | Element} [root=document]
 * @returns {string}
 */
export function getLastUserMessageFromChatHistory(root = document) {
  return getUserMessagesFromChatHistory(root)[0] || '';
}

const _CHEVRON_UP = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><polyline points="18 15 12 9 6 15"/></svg>';
const _CHEVRON_DOWN = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"/></svg>';

/**
 * Wires the ↑/↓ history buttons and the draft-preserving walk logic.
 *
 * @param {HTMLTextAreaElement} composer
 * @param {() => string|string[]} getUserMessages
 * @param {{ autoResize?: (el: HTMLTextAreaElement) => void, container?: HTMLElement }} [options]
 * @returns {boolean} true when wired (or already wired)
 */
export function wireHistoryRecall(composer, getUserMessages, options = {}) {
  if (!composer) return false;
  if (composer._historyRecallWired) return true;
  composer._historyRecallWired = true;

  const { autoResize } = options;
  let recallIndex = -1;
  let applyingRecall = false;
  let lastRecalledValue = '';
  let recallHistory = [];
  let draftSlot = null;
  let olderBtn = null;
  let newerBtn = null;

  const readHistory = () => {
    const value = getUserMessages?.();
    if (Array.isArray(value)) return value.filter(Boolean);
    return value ? [value] : [];
  };
  const norm = (value) => String(value || '').replace(/\r\n/g, '\n').trimEnd();
  const debug = (...args) => {
    try {
      if (localStorage.getItem('odysseusHistoryRecallDebug') === '1') {
        console.debug('[history-recall]', ...args);
      }
    } catch (_) {}
  };

  // Where the current text sits in the history: -1 = draft/blank slot.
  const computeCurrentIndex = (history, rawCurrentValue, currentValue) => {
    if (rawCurrentValue === '') return -1;
    const idx = history.findIndex((item) => norm(item) === currentValue);
    if (idx >= 0) return idx;
    if (currentValue === norm(lastRecalledValue)) return recallIndex;
    const markedIndex = Number(composer.dataset?.odysseusRecallIndex);
    if (Number.isInteger(markedIndex) && markedIndex >= 0 && markedIndex < history.length) {
      return markedIndex;
    }
    return -1;
  };

  const apply = (index, value, history) => {
    recallIndex = index;
    if (history) recallHistory = history;
    applyingRecall = true;
    lastRecalledValue = value;
    if (index >= 0) {
      try { composer.dataset.odysseusRecallIndex = String(index); } catch (_) {}
    } else {
      try { delete composer.dataset.odysseusRecallIndex; } catch (_) {}
    }
    composer.value = value;
    try { composer.selectionStart = composer.selectionEnd = value.length; } catch (_) {}
    if (autoResize) autoResize(composer);
    updateButtons();
    setTimeout(() => { applyingRecall = false; }, 0);
  };

  const updateButtons = () => {
    const history = readHistory();
    const raw = String(composer.value || '');
    const currentIndex = computeCurrentIndex(history, raw, norm(raw));
    if (olderBtn) {
      // Older is dead with no history, or already sitting on the oldest prompt.
      olderBtn.disabled = !history.length || currentIndex === history.length - 1;
    }
    if (newerBtn) {
      // Newer is dead while sitting on the draft/blank slot.
      newerBtn.disabled = currentIndex < 0;
    }
  };

  composer.addEventListener('input', () => {
    if (applyingRecall) return;
    if (norm(composer.value) === norm(lastRecalledValue)) return;
    recallIndex = -1;
    lastRecalledValue = '';
    recallHistory = [];
    draftSlot = null;
    try { delete composer.dataset.odysseusRecallIndex; } catch (_) {}
    updateButtons();
  });

  // The core walk. direction: 'older' walks back in time (↑), 'newer' walks
  // forward toward the draft/blank slot (↓).
  const walk = (direction) => {
    const freshHistory = readHistory();
    const history = freshHistory.length ? freshHistory : recallHistory;
    if (!history.length) {
      debug('skip:no-history', { value: composer.value });
      updateButtons();
      return;
    }

    const rawCurrentValue = String(composer.value || '');
    const currentValue = norm(rawCurrentValue);
    const currentIndex = computeCurrentIndex(history, rawCurrentValue, currentValue);

    if (direction === 'older') {
      // Walking older. From the draft slot, save the in-progress draft once,
      // then start from the newest prompt.
      if (currentIndex < 0) {
        if (rawCurrentValue !== '' && rawCurrentValue !== draftSlot) {
          draftSlot = rawCurrentValue;
          debug('draft-saved', { draftSlot });
        }
        recallIndex = -1;
      }
      const nextIndex = currentIndex >= 0 ? Math.min(currentIndex + 1, history.length - 1) : 0;
      const recalled = history[nextIndex];
      if (!recalled) {
        debug('skip:no-recalled', { nextIndex });
        updateButtons();
        return;
      }
      apply(nextIndex, recalled, history);
      debug('handled-older', { nextIndex, recalled, historyLength: history.length });
      return;
    }

    // Newer: walk back toward the draft slot / blank.
    if (currentIndex < 0) {
      debug('skip:already-newest', { value: composer.value });
      updateButtons();
      return;
    }
    const nextIndex = currentIndex - 1;
    if (nextIndex < 0) {
      const restored = draftSlot !== null ? draftSlot : '';
      apply(-1, restored, history);
      debug('handled-newer-restore', { restored: restored || '(blank)' });
      return;
    }
    apply(nextIndex, history[nextIndex], history);
    debug('handled-newer', { nextIndex, historyLength: history.length });
  };

  // Build the ↑/↓ button stack. Inserted at the start of the chatbox's
  // right-side action group (next to the mode toggle / send button), or into
  // options.container when provided.
  const nav = document.createElement('div');
  nav.className = 'history-nav';
  nav.setAttribute('aria-label', 'Prompt history');

  const mkBtn = (title, aria, svg) => {
    const btn = document.createElement('button');
    btn.type = 'button';
    btn.className = 'history-nav-btn';
    btn.title = title;
    btn.setAttribute('aria-label', aria);
    btn.innerHTML = svg;
    btn.addEventListener('click', () => {
      if (composer.disabled) return; // stream active — input is locked
      try { composer.focus(); } catch (_) {}
      walk(btn === olderBtn ? 'older' : 'newer');
    });
    nav.appendChild(btn);
    return btn;
  };

  olderBtn = mkBtn('Previous prompt (older)', 'Previous prompt', _CHEVRON_UP);
  newerBtn = mkBtn('Next prompt (newer)', 'Next prompt', _CHEVRON_DOWN);

  let container = options.container || null;
  if (!container && typeof composer.closest === 'function') {
    const bar = composer.closest('.chat-input-bar');
    container = (bar && bar.querySelector ? bar.querySelector('.chat-input-right') : null) || composer.parentNode;
  }
  if (!container) container = composer.parentNode;
  if (container && typeof container.insertBefore === 'function') {
    container.insertBefore(nav, container.firstChild);
  }

  updateButtons();
  return true;
}
