#!/usr/bin/env python3
"""Render the full markdown formatting tour through the real pipeline + real
style.css in headless Chromium and save a PNG proof to the Sandbox."""
import os
import re
import sys
import threading
import time
import urllib.request

import http.server
import socketserver

ROOT = '/run/media/crao/BTnvme/LLM/odysseus-garboGH'
OUT = '/run/media/crao/BTnvme/LLM/Sandbox/markdown-fix-demo.png'

DEMO = '''# Heading 1
## Heading 2
### Heading 3

**bold** *italic* ***both*** ~~strike~~ ==highlight== ^superscript^

`inline code` and an image: ![pic](https://picsum.photos/seed/odysseus/64/40)

1. ordered one
2. ordered two
3. ordered three

- bullet a
- bullet b
  - nested bullet one
  - nested bullet two
- bullet c

- [x] done task
- [ ] open task
  - [x] nested done under a task

> quote line
>> nested quote
>>> deep quote

| a | b | c |
|---|---|---|
| 1 | 2 | 3 |

$E = mc^2$ (KaTeX math, if the CDN loads)

Escapes: \\*not italic\\*, \\[not a link](https://example.com), \\# not a header, \\$5 not math
'''

os.chdir(ROOT)
Handler = http.server.SimpleHTTPRequestHandler
Handler.extensions_map = {'.js': 'application/javascript', '.css': 'text/css', '': 'application/octet-stream'}
with socketserver.TCPServer(('127.0.0.1', 0), Handler) as httpd:
    port = httpd.server_address[1]
    threading.Thread(target=httpd.serve_forever, daemon=True).start()
    for _ in range(50):
        try:
            urllib.request.urlopen(f'http://127.0.0.1:{port}/static/style.css', timeout=2)
            break
        except Exception:
            time.sleep(0.1)

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

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={'width': 900, 'height': 1400})
        page.set_content(f'''<!doctype html><html><head>
<link rel="stylesheet" href="http://127.0.0.1:{port}/static/style.css">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.22/dist/katex.min.css">
<script src="https://cdn.jsdelivr.net/npm/katex@0.16.22/dist/katex.min.js"></script>
<style>
  :root {{ color-scheme: dark; }}
  body {{ background: #1e1f2b; margin: 0; padding: 24px; font-family: 'Fira Code', ui-monospace, monospace; }}
  .theme {{ --fg: #e6e6ef; --bg: #1e1f2b; --accent: #7aa2f7; --hl-function: #7aa2f7; --border: #3a3b4d; color: var(--fg); font-size: 14px; line-height: 1.55; }}
  .msg {{ max-width: 820px; }}
</style></head><body><div class="theme msg" id="out"></div></body></html>''')
        # give katex a beat to load
        page.wait_for_timeout(800)
        page.evaluate(src)
        page.evaluate("(d) => { document.getElementById('out').innerHTML = window.__mdToHtml(d); }", DEMO)
        page.wait_for_timeout(400)
        os.makedirs(os.path.dirname(OUT), exist_ok=True)
        page.screenshot(path=OUT, full_page=True)
        browser.close()

print('screenshot saved:', OUT)
