# Web Deck v5

A tiny system for building **self-contained HTML slide decks**: no build step, no framework, no dependency beyond Google Fonts. A deck presents fullscreen, carries teleprompter **speaker notes**, drives a two-monitor **presenter view** (with A−/A+ notes resizing), exports to **PDF**, and reflows to read on a phone.

**Site & downloads:** https://mguhlin.github.io/webdecks/ · **License:** MIT (open — use, modify, share)

This repo is the single source of truth for the deck system across projects. Point any assistant (ChatGPT, Claude, Gemini) or human at it when building a deck.

## Get started

- **Build a deck by prompting a chatbot** → download **[`webdeck_v5_standalone.md`](webdeck_v5_standalone.md)**, upload it to the chatbot, and ask for a deck. It bundles the full spec plus the complete framework (Appendix A/B), so the chatbot can return one portable `.html` with nothing else needed.
- **Build a deck in a project** → copy `assets/deck-framework.css` + `assets/deck-framework.js` into your project's `assets/`, copy `decks/template-deck.html`, re-skin the palette/fonts in the deck's own `<style>`, and replace the slides. See the **[spec](webdeck_spec_v5.md)**.

## What's in here

| Path | What it is |
|---|---|
| [`webdeck_spec_v5.md`](webdeck_spec_v5.md) | The full specification. Read this first. |
| [`webdeck_v5_standalone.md`](webdeck_v5_standalone.md) | Self-contained edition for chatbots (spec + framework embedded). **Generated** — do not hand-edit. |
| [`assets/deck-framework.css`](assets/deck-framework.css) | Design system, layout, chrome, presenter view, print, accessibility. |
| [`assets/deck-framework.js`](assets/deck-framework.js) | Navigation, presenter window, cross-window sync, print. IIFE, no deps. |
| [`decks/template-deck.html`](decks/template-deck.html) | A starter deck. Copy and replace the slides. |
| [`build-standalone.py`](build-standalone.py) | Regenerates the standalone from the spec + framework. |
| `index.html` | The landing page served at the site above. |

## Examples — decks in the wild

Every deck below runs the current v5 framework (two-monitor presenter view with A−/A+ notes, phone reflow, PDF export).

**Flagship:**
- [The Essential Learning Expectations — Facilitator deck](https://mglearn.github.io/eles/decks/facilitator.html) (TCEA)
- [Trust, Transparency, and AI](https://mguhlin.github.io/nspa/2026/p/webdeck.html) (NSPA 2026)
- [AI for the Defense — Overview](https://mglearn.github.io/legalai/decks/0-overview.html) (TCDLA)

**TCEA Creations** — each re-skinned to its own palette:
- [Create AI-Powered Publications and Dashboards](https://mguhlin.github.io/creations/tcea/webdecks/aipower/) — navy & gold, 24 slides
- [AI as Your Instructional Design Partner](https://mguhlin.github.io/creations/tcea/webdecks/aidesign/) — navy & gold keynote, 40 slides
- [iBINGO Game Maker](https://mguhlin.github.io/creations/tcea/webdecks/ibingo/) — playful multi-color, Fredoka display
- [NSF TechAccess: AI-Ready America](https://mguhlin.github.io/creations/tcea/webdecks/nsf26/) — NSF navy & gold leadership briefing
- [LearnDash Risk Assessment and Transition Path](https://mguhlin.github.io/creations/tcea/webdecks/ldtransition/) — navy & gold executive brief
- [Newsletter AI: Copyright-Safe Curation](https://mguhlin.github.io/creations/tcea/webdecks/newsmaker-copyright/) — teal & amber editorial

## Maintaining this repo

1. Edit the spec (`webdeck_spec_v5.md`) and/or the framework (`assets/deck-framework.{css,js}`).
2. Run `python3 build-standalone.py` to regenerate `webdeck_v5_standalone.md`.
3. Commit and push. GitHub Pages redeploys `https://mguhlin.github.io/webdecks/` automatically.

When you change framework **behavior**, note it in the spec in the same change. Decks that **link** the framework pick it up automatically; **self-contained / inlined** decks embed their own copy and must be patched or rebuilt (spec §0.2).

## License

MIT — see [`LICENSE`](LICENSE). Free to use, modify, and share.
