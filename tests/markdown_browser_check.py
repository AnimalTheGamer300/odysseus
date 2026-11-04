#!/usr/bin/env python3
"""Real-browser verification of the markdown formatting fixes.

Serves the repo's static/ dir, loads the REAL style.css, evals the REAL
markdown.js (imports stubbed like the node harness) in a headless Chromium
page, and asserts:
  - new formatting renders (highlight, sup, nested lists/quotes, escapes)
  - task-check ::after now draws in var(--fg), not var(--bg)
  - the sanitizer still strips event handlers from <details>
  - the escape pass cannot smuggle raw < / > back into the DOM
"""
import json
import re
import subprocess
import sys
import time
import urllib.request

ROOT = '/run/media/crao/BTnvme/LLM/odysseus-garboGH'

# ── tiny static server ────────────────────────────────────────────────────────
import http.server
import socketserver
import os

os.chdir(ROOT)
Handler = http.server.SimpleHTTPRequestHandler
Handler.extensions_map = {'.js': 'application/javascript', '.css': 'text/css', '': 'application/octet-stream'}
with socketserver.TCPServer(('127.0.0.1', 0), Handler) as httpd:
    port = httpd.server_address[1]
    import threading
    threading.Thread(target=httpd.serve_forever, daemon=True).start()

    # wait for the server
    for _ in range(50):
        try:
            urllib.request.urlopen(f'http://127.0.0.1:{port}/static/style.css', timeout=2)
            break
        except Exception:
            time.sleep(0.1)

    # ── playwright ────────────────────────────────────────────────────────────
    from playwright.sync_api import sync_playwright

    src = open(f'{ROOT}/static/js/markdown.js', encoding='utf8').read()
    src = re.sub(r"import uiModule from '\.\/ui\.js';",
                 'const uiModule = { esc: (s) => String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/\\"/g, "&quot;") };', src)
    src = re.sub(r"import \{ splitTableRow \} from '\.\/markdown\/tableRow\.js';",
                 'const splitTableRow = (row) => row.split("|").filter((cell) => cell.trim() !== "");', src)
    src = re.sub(r"import \{ replaceEmojiShortcodes, hasEmojiShortcode \} from '\.\/emojiShortcodes\.js';",
                 'const hasEmojiShortcode = (t) => !!t && t.indexOf(":") !== -1 && /:[a-z0-9_+-]{1,40}:/i.test(t); const replaceEmojiShortcodes = (t) => t;', src)
    src = re.sub(r'export function ', 'function ', src)
    src = re.sub(r'export const ', 'const ', src)
    src = re.sub(r'export default markdownModule;?', '', src)
    src += '\nthis.__mdToHtml = mdToHtml;'

    fails = []
    def check(name, ok, detail=''):
        if ok:
            print(f'  ok - {name}')
        else:
            fails.append(name)
            print(f'  FAIL - {name} {detail}')

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.set_content(f'''<!doctype html><html><head>
<link rel="stylesheet" href="http://127.0.0.1:{port}/static/style.css">
<style>
  .theme {{ --fg: #f8f8f2; --bg: #000000; --accent: #3b82f6; --hl-function: #5b8def; --border: #333; }}
</style></head><body><div class="theme msg" id="out"></div></body></html>''')
        page.evaluate(src)

        def md(s):
            return page.evaluate('(x) => window.__mdToHtml(x)', s)

        # ── formatting renders ──
        h = md('==hi== ^up^')
        check('highlight+sup render', '<mark>hi</mark>' in h and '<sup>up</sup>' in h, h)
        h = md('- a\n  - b\n- c')
        check('nested list renders', '<ul><li>a<ul><li>b</li></ul></li><li>c</li></ul>' in h, h)
        h = md('> a\n>> b')
        check('nested quote renders', '<blockquote><p>a</p><blockquote><p>b</p></blockquote></blockquote>' in h, h)
        h = md('1. a\n\n2. b')
        check('loose ordered list one <ol>', h.count('<ol>') == 1 and '<ol><li>a</li><li>b</li></ol>' in h, h)
        h = md('\\*not italic\\*')
        check('escape works', '*not italic*' in h and '<em>' not in h, h)
        h = md('x^2^')
        check('superscript', 'x<sup>2</sup>' in h, h)
        h = md('😀 emoji')
        check('emoji svg path alive', 'class="emoji"' in h, h)
        # ── sanitizer still strips handlers inside <details> ──
        h = md('<details><img src=x onerror=alert(1)></details>')
        check('sanitizer strips onerror', 'onerror' not in h and '<details' in h and '</details>' in h, h)
        # ── escape pass cannot smuggle raw HTML ──
        h = md('\\<img src=x onerror=alert(1)>')
        # "onerror" legitimately appears as *text* inside the escaped content;
        # what matters is there's no real <img> tag (asserted next line).
        check('escaped < stays escaped', '&lt;img' in h and '&gt;' in h, h)
        check('no raw <img in output', '<img' not in h, h)
        # ── no leaked placeholders ──
        h = md('- [x] done\n\npara text ==marked== ^sup^')
        check('no placeholder leaks', '___' not in h, h)
        # ── task check ::after computed style: fg, not bg ──
        page.evaluate('''() => {
          const li = document.createElement('li');
          li.className = 'task-item task-done';
          li.innerHTML = '<span class="task-check" aria-hidden="true"></span><span class="task-text">done</span>';
          document.getElementById('out').appendChild(li);
        }''')
        style = page.evaluate('''() => {
          const el = document.querySelector('.task-check');
          const after = getComputedStyle(el, '::after');
          return { borderTopColor: after.borderTopColor, width: after.width, height: after.height };
        }''')
        check('task check border = fg (#f8f8f2)', style['borderTopColor'] == 'rgb(248, 248, 242)', json.dumps(style))
        check('task check bigger (5x9)', style['width'] == '5px' and style['height'] == '9px', json.dumps(style))
        # ── mark background visible ──
        page.evaluate('''() => {
          const m = document.createElement('mark');
          m.textContent = 'x';
          document.getElementById('out').appendChild(m);
        }''')
        bg = page.evaluate("getComputedStyle(document.querySelector('mark')).backgroundColor")
        check('mark has visible background', bg != 'rgba(0, 0, 0, 0)', bg)
        browser.close()

    print()
    if fails:
        print(f'{len(fails)} FAILURES: {fails}')
        sys.exit(1)
    print('all browser checks passed')
