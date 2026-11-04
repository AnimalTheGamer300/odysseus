// Regression tests for the markdown formatting fixes (2026-08-06):
//   - ==highlight== → <mark>
//   - ^superscript^ → <sup>
//   - backslash escapes (\* \[ \# \$ ...) actually escape
//   - ordered/unordered lists no longer split on blank lines (loose lists)
//   - indented items nest (nested lists)
//   - task items (- [ ] / - [x]) work at any depth
//   - nested blockquotes (>>, >>>) actually nest
// Same vm-sandbox approach as markdown_codefence_placeholder_regression.mjs.
import assert from 'node:assert/strict';
import fs from 'node:fs';
import path from 'node:path';
import vm from 'node:vm';
import { fileURLToPath } from 'node:url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const markdownPath = path.join(__dirname, '..', 'static', 'js', 'markdown.js');
let src = fs.readFileSync(markdownPath, 'utf8');

src = src.replace(
  /import uiModule from '\.\/ui\.js';/,
  'const uiModule = { esc: (s) => String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/\\"/g, "&quot;") };'
);
src = src.replace(
  /import \{ splitTableRow \} from '\.\/markdown\/tableRow\.js';/,
  'const splitTableRow = (row) => row.split("|").filter((cell) => cell.trim() !== "");'
);
src = src.replace(
  /import \{ replaceEmojiShortcodes, hasEmojiShortcode \} from '\.\/emojiShortcodes\.js';/,
  'const hasEmojiShortcode = (t) => !!t && t.indexOf(":") !== -1 && /:[a-z0-9_+-]{1,40}:/i.test(t); const replaceEmojiShortcodes = (t) => t;'
);
src = src.replace(/export function /g, 'function ');
src = src.replace(/export const /g, 'const ');
src = src.replace(/export default markdownModule;?/g, '');
src += '\nthis.__mdToHtml = mdToHtml;';

class MutationObserver {
  observe() {}
  disconnect() {}
}

const sandbox = {
  console,
  URL,
  MutationObserver,
  localStorage: { getItem() { return '[]'; }, setItem() {} },
  document: {
    body: { classList: { contains() { return true; } } },
    addEventListener() {},
    querySelectorAll() { return []; },
    getElementById() { return null; },
    contains() { return true; },
    // Minimal template stub so sanitizeAllowedHtml can round-trip innerHTML
    // without a real DOM. The sanitizer's tag-stripping logic is unchanged —
    // this harness simply doesn't exercise it.
    createElement() {
      return {
        _html: '',
        set innerHTML(v) { this._html = String(v); },
        get innerHTML() { return this._html; },
        content: { querySelectorAll() { return []; } },
      };
    },
  },
  window: {
    location: { origin: 'http://localhost' },
    katex: null,
    mermaid: null,
  },
};

vm.createContext(sandbox);
vm.runInContext(src, sandbox, { filename: markdownPath });
const md = (s) => sandbox.__mdToHtml(s);

let passed = 0;
function check(name, input, expected) {
  const html = md(input);
  for (const exp of expected) {
    assert.ok(html.includes(exp), `${name}: expected ${JSON.stringify(exp)} in output for ${JSON.stringify(input)}\n--- got ---\n${html}`);
  }
  passed++;
  console.log('  ok -', name);
}
function checkNot(name, input, forbidden) {
  const html = md(input);
  for (const bad of forbidden) {
    assert.ok(!html.includes(bad), `${name}: did not expect ${JSON.stringify(bad)} in output for ${JSON.stringify(input)}\n--- got ---\n${html}`);
  }
  passed++;
  console.log('  ok -', name);
}
function checkCount(name, input, pattern, want) {
  const html = md(input);
  const got = (html.match(pattern) || []).length;
  assert.equal(got, want, `${name}: expected ${want}x ${pattern} in output for ${JSON.stringify(input)}\n--- got ---\n${html}`);
  passed++;
  console.log('  ok -', name);
}

console.log('markdown formatting fixes:');

// ── highlight / superscript ────────────────────────────────────────────────
check('highlight ==x== → <mark>', 'this is ==important==', ['<mark>important</mark>']);
check('highlight no false positive', 'a == b', ['a == b']);
check('superscript ^x^ → <sup>', 'x^2^ and ^sup^', ['x<sup>2</sup>', '<sup>sup</sup>']);
checkNot('superscript ignores lone carets', 'no ^ here', ['<sup>']);

// ── backslash escapes ───────────────────────────────────────────────────────
check('escape italic', '\\*not italic\\*', ['*not italic*']);
checkNot('escape italic no <em>', '\\*not italic\\*', ['<em>']);
check('escape link brackets', '\\[no](https://example.com)', ['[no]']);
checkNot('escape link no <a> text wrap', '\\[no](https://example.com)', ['>no</a>']);
check('escape header', '\\# not a header', ['<p># not a header</p>']);
checkNot('escape header no <h1>', '\\# not a header', ['<h1']);
check('escape dollar', 'costs \\$5', ['<p>costs $5</p>']);
check('escape backslash', 'a \\\\ b', ['<p>a \\ b</p>']);
check('escape list marker', '\\- not a list', ['<p>- not a list</p>']);
checkNot('escape list marker no <ul>', '\\- not a list', ['<ul>']);
check('escape ordered marker', '1\\. not ordered', ['<p>1. not ordered</p>']);
checkNot('escape ordered marker no <ol>', '1\\. not ordered', ['<ol>']);
check('plain backslash untouched', 'C:\\Users\\crao', ['C:\\Users\\crao']);

// ── loose lists (blank lines no longer split) ──────────────────────────────
check('ordered contiguous', '1. a\n2. b', ['<ol><li>a</li><li>b</li></ol>']);
checkCount('ordered with blank lines = one <ol>', '1. a\n\n2. b', /<ol>/g, 1);
check('ordered with blank lines items', '1. a\n\n2. b', ['<ol><li>a</li><li>b</li></ol>']);
checkCount('unordered with blank lines = one <ul>', '- a\n\n- b', /<ul>/g, 1);
check('unordered with blank lines items', '- a\n\n- b', ['<ul><li>a</li><li>b</li></ul>']);
check('triple blank lines collapse', '- a\n\n\n- b', ['<ul><li>a</li><li>b</li></ul>']);

// ── nested lists ────────────────────────────────────────────────────────────
check('nested unordered', '- a\n  - b\n- c', ['<ul><li>a<ul><li>b</li></ul></li><li>c</li></ul>']);
check('nested ordered-under-ordered', '1. a\n   - b\n   - c\n2. d', ['<ol><li>a<ul><li>b</li><li>c</li></ul></li><li>d</li></ol>']);
check('deep nesting 3 levels', '- a\n  - b\n    - c', ['<ul><li>a<ul><li>b<ul><li>c</li></ul></li></ul></li></ul>']);
check('marker change starts new list', '- a\n1. b', ['<ul><li>a</li></ul>', '<ol><li>b</li></ol>']);
check('list then paragraph', '- a\n\npara', ['<ul><li>a</li></ul>', '<p>para</p>']);

// ── task items ──────────────────────────────────────────────────────────────
check('task item unchecked', '- [ ] todo', ['<li class="task-item"><span class="task-check" aria-hidden="true"></span><span class="task-text">todo</span></li>']);
check('task item checked', '- [x] done', ['<li class="task-item task-done">', 'task-text">done</span>']);
check('task item star marker', '* [X] cap', ['<li class="task-item task-done">', 'cap</span>']);
check('nested task item', '- [x] parent\n  - [ ] child', ['<li class="task-item task-done">', 'parent</span><ul><li class="task-item">', 'child</span></li></ul></li>']);
check('task list loose', '- [ ] a\n\n- [x] b', ['<ul><li class="task-item">', '<li class="task-item task-done">']);

// ── nested blockquotes ──────────────────────────────────────────────────────
check('nested quote >>', '> a\n>> b', ['<blockquote><p>a</p><blockquote><p>b</p></blockquote></blockquote>']);
check('triple quote >>>', '>>> deep', ['<blockquote><blockquote><blockquote><p>deep</p></blockquote></blockquote></blockquote>']);
check('mixed quote levels', '> a\n>> b\n> c', ['<blockquote><p>a</p><blockquote><p>b</p></blockquote><p>c</p></blockquote>']);
checkCount('quote loose stays one block', '> a\n\n> b', /<blockquote>/g, 1);
check('quote loose paragraphs', '> a\n\n> b', ['<blockquote><p>a</p><p>b</p></blockquote>']);
check('plain quote unchanged', '> hi', ['<blockquote><p>hi</p></blockquote>']);

// ── regressions: things that must keep working ──────────────────────────────
check('bold/italic/strike', '**b** *i* ~~s~~', ['<strong>b</strong>', '<em>i</em>', '<del>s</del>']);
check('superscript ^text^', 'x^2^', ['<sup>2</sup>']);
check('subscript ~text~', 'H~2~O', ['<sub>2</sub>']);
check('sub+sup together', 'H~2~SO~4~ and x^2^', ['<sub>2</sub>', '<sub>4</sub>', '<sup>2</sup>']);
check('escaped tilde literal', '\\~not sub\\~', ['~not sub~']);
checkNot('strike still works with sub regex', '~~gone~~', ['<sub>']);
check('link', '[x](https://example.com)', ['<a href="https://example.com/" target="_blank" rel="noopener noreferrer">x</a>']);
check('image', '![alt](https://example.com/i.png)', ['<img src="https://example.com/i.png" alt="alt"']);
check('details preserved', '<details>\ntext\n</details>', ['<details open>', 'text']);
check('table', 'a | b | c\n---|---|---\nx | y | z', ['<table']);
check('hr', '---', ['<hr>']);
check('headers', '### mid', ['<h3>mid</h3>']);
check('fenced code with backslash stays literal', '```\n\\*literal\\*\n```', ['<code data-lang="">\\*literal\\*</code>']);
checkNot('fenced code backslash not italic', '```\n\\*literal\\*\n```', ['<em>']);
check('inline code with backslash stays literal', '`\\*x\\*`', ['<code>\\*x\\*</code>']);
check('escaped char inside code resolves', '```\n\\*x\\*\n```', ['<code data-lang="">\\*x\\*</code>']);
check('empty bullet item', '- ', ['<ul><li></li></ul>']);
check('blank lines inside code preserved', '```\na\n\nb\n```', ['<code data-lang="">a\n\nb</code>']);

console.log(`\nall ${passed} checks passed`);
