#!/usr/bin/env python3
"""Assemble the standalone, uploadable Web Deck v5 instructions.

Combines the canonical spec with the full framework CSS/JS embedded as
Appendix A / Appendix B, producing a single file you can upload or paste
into any web chatbot. Re-run after changing the spec or the framework.

    python3 build-standalone.py   ->   webdeck_v5_standalone.md
"""
from pathlib import Path

HERE = Path(__file__).resolve().parent
spec = (HERE / "webdeck_spec_v5.md").read_text(encoding="utf-8")
css = (HERE / "assets" / "deck-framework.css").read_text(encoding="utf-8")
js = (HERE / "assets" / "deck-framework.js").read_text(encoding="utf-8")

PREAMBLE = r"""# Web Deck v5 — Standalone Instructions (for web chatbots)

This is the **self-contained** edition of the Web Deck v5 specification. Upload or paste
this *single file* into any web-based chatbot (ChatGPT, Claude, Gemini, Copilot, etc.),
then ask it to build a deck. Everything it needs is in this one document: the full
specification below, plus the **complete framework** embedded verbatim in
**Appendix A (CSS)** and **Appendix B (JavaScript)** at the end.

## How to use it with a chatbot

1. Upload (or paste) this entire file into the chat.
2. Then send a prompt like:

> Using the Web Deck v5 system fully described in the document I just gave you, build a
> **single self-contained HTML file** deck on **[TOPIC]** for **[AUDIENCE]**. Put the
> entire CSS from Appendix A inside one `<style>` tag in the `<head>`, and paste the
> entire JavaScript from Appendix B **verbatim and in full** inside one `<script>` tag
> just before `</body>` — do not abridge, summarize, or retype it. Add a Google Fonts
> link and a `:root` skin block for the palette/fonts (spec section 1.1). Follow the
> structure, class names, and on-slide writing style in the spec. Include a cover, a
> divider before each section, and content slides using the blocks where they fit. Keep
> on-slide text to short phrases and write real teleprompter speaker notes (about 100
> words, first person) in the `.notes` block of **every** slide. Give every slide a
> `.slide-footer`. Aim for about **[N]** slides. Output the complete file, ready to save
> and open in a browser.

## Reading note (standalone vs linked)

The specification below is written for the normal workflow, where a project **links**
two shared files (`assets/deck-framework.css` and `assets/deck-framework.js`). In this
**standalone** edition there are no separate files: wherever the spec says *"copy /
link `webdeck/assets/deck-framework.*`"*, the equivalent is to **paste Appendix A into a
single `<style>` tag and Appendix B into a single `<script>` tag** (just before
`</body>`), producing one portable HTML file. The framework injects its own navigation
chrome (controls, progress bar, exit icon) at runtime — you do not add those by hand.

Single-file skeleton:

```html
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Your Deck Title</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=...&display=swap" rel="stylesheet">
  <style>
    /* --- Appendix A (deck-framework.css) pasted in full --- */
    /* --- then your per-project :root skin + any deck-local one-offs (spec 1.1, 4) --- */
  </style>
</head>
<body>
  <div class="deck">
    <section class="slide cover current"> ... </section>
    <section class="slide divider"> ... </section>
    <section class="slide"> ... </section>
  </div>
  <script>
    /* --- Appendix B (deck-framework.js) pasted in full and verbatim --- */
  </script>
</body>
</html>
```

> To point the exit icon at a hub, change the `href` in the `exitLink` line inside the
> pasted Appendix B (default is `../index.html`).

---

"""

APPENDICES = (
    "\n\n---\n\n"
    "# Appendix A — `deck-framework.css` (paste into one `<style>` tag)\n\n"
    "The complete design system, layout, chrome, presenter view, print, and accessibility "
    "styles. Paste **everything between the fences** into a single `<style>` tag in the `<head>`.\n\n"
    "```css\n" + css.rstrip() + "\n```\n\n"
    "---\n\n"
    "# Appendix B — `deck-framework.js` (paste into one `<script>` tag)\n\n"
    "The complete navigation, notes panel, presenter window, cross-window sync, and print "
    "logic. No dependencies. Paste **everything between the fences** into a single `<script>` "
    "tag just before `</body>`, verbatim and in full.\n\n"
    "```javascript\n" + js.rstrip() + "\n```\n"
)

out = PREAMBLE + spec.strip() + APPENDICES
dest = HERE / "webdeck_v5_standalone.md"
dest.write_text(out, encoding="utf-8")
print(f"wrote {dest} ({len(out):,} bytes, ~{out.count(chr(10))+1} lines)")
