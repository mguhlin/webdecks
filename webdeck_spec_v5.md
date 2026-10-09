# Web Deck Instructions — v5 (canonical, project-neutral)

*The single source of truth for the self-contained HTML slide-deck system used across `~/Documents/vibecoding` projects.*
*Canonical location: `~/Documents/vibecoding/webdeck/`. Last revised 2026-10-09.*

Any agent (Claude Code, ChatGPT/Codex, or a human) that is asked to **build or edit a web deck / slide deck** in any vibecoding project should follow this file. It is intentionally self-contained and tool-neutral: nothing here depends on a particular assistant. The reference framework lives beside it at `webdeck/assets/deck-framework.css` and `webdeck/assets/deck-framework.js`.

> **How projects use this.** Each deck project keeps its **own copy** of the two `assets/` files (so the deck is portable and deployable on its own). To start or refresh a project, copy `webdeck/assets/deck-framework.{css,js}` into the project's `assets/` and copy `webdeck/decks/template-deck.html` as a starting deck. When you change framework *behavior*, update this file in the same change, and re-sync the copies that are meant to track it.

---

## 0. What this system is

Self-contained HTML slide decks. **No build step, no bundler, no framework, no runtime dependency beyond Google Fonts.** Each deck is a single HTML file that presents fullscreen, carries teleprompter **speaker notes**, drives a **two-monitor presenter view**, exports to **PDF**, and scales to any screen.

Everything is powered by two shared files, plus one HTML file per deck:

| File | Role |
|---|---|
| `assets/deck-framework.css` | Design system, slide layout, navigation chrome, presenter-view styles, print rules. ~410 lines. |
| `assets/deck-framework.js` | Slide navigation, notes panel, presenter window, cross-window sync, exit icon, print. ~310 lines. IIFE, no dependencies. |
| `decks/<n>-<name>.html` (or `<name>.html`) | One deck. Links the two shared files + fonts; contains only its slides and any deck-local `<style>`. |

To reuse in a new project: copy those two `assets/` files and one deck as a template, then swap the slides.

### 0.1 Per-project customization (what changes, what stays)

**Stays the same across projects** (the shared framework): the 1280×720 canvas, slide types, content blocks, navigation chrome, presenter view, notes behavior, print rules, accessibility layer, keyboard map. Do not fork these casually.

**Customize per project** (local overrides, not edits to the shared framework):
- **Palette and fonts** — the framework ships a blue-and-silver editorial reference skin (§1). Re-skin by overriding the `:root` custom properties and the Google Fonts link in the deck's own `<style>`. (Example: the `eles` project re-skins to navy `#0A3476` + gold `#FCB040` with DM Serif Display + DM Sans. See §1.1.)
- **Footer brand / facilitator / URL** — set in each slide's `.slide-footer` (§2).
- **Exit-icon target** — the shared default links to `../index.html` with a generic label; point it at the project's hub (e.g. `../framework.html`) by editing the project's copy of `deck-framework.js`.
- **Deploy flow** — per project (§13).

### 0.2 Linked vs self-contained (inlined) decks — important

A deck can include the framework two ways:
1. **Linked** (default, recommended): `<link rel="stylesheet" href="../assets/deck-framework.css">` + `<script src="../assets/deck-framework.js"></script>`. Updating the `assets/` files updates every linked deck automatically.
2. **Self-contained / inlined**: the framework CSS is pasted into a `<style>` tag and the JS into a `<script>` tag, producing one portable file (good for offline use or a generator that stamps out single files).

**Consequence:** a change to `assets/deck-framework.*` reaches **linked** decks for free, but **does not** reach **inlined** decks — those carry their own embedded copy and must be patched in the built file (or regenerated if a generator inlines the framework at build time). When you make a framework change, check for inlined decks and patch/rebuild them too.

---

## 1. Aesthetic — blue-and-silver reference skin (editorial)

Distinguished editorial meets modern brief. **Typography is the hero.** Whitespace is generous. Accents are precise hairlines and brushed silver.

### Palette (`:root` CSS custom properties)

| Token | Hex | Use |
|---|---|---|
| `--navy` | `#102A54` | titles, footer bar, primary accent |
| `--navy-dk` | `#0B1D33` | cover / divider backgrounds |
| `--navy-md` / steel | `#2F5F8F` | secondary emphasis, "do" column, kicker text |
| `--gold` (steel accent) | `#6F8FAF` | bullets, bars, borders — a steel-blue in the reference skin |
| `--gold-lt` (silver) | `#C8D2DC` | subtitles, light strips on dark, hover highlight |
| `--lgray` | `#F5F8FC` | card fills |
| `--mgray` / `--hair` | `#DCE3EE` / `#E2E8F2` | hairline borders |
| `--slate` | `#51617A` | captions |
| `--text` | `#1C2B44` | body text |
| `--metal` | silver gradient | accent strips, footer rule, progress bar |
| `--paper` | subtle gradient | content-slide background |

> The `--gold*` token **names** are historical; in the reference skin their **values** are blue/silver. A project may re-skin them to any palette (see §1.1). Do/do-not columns use **steel (do) vs navy (do-not)** in the reference skin — monochrome, not green/red.

### Fonts — one Google Fonts link per deck `<head>`

- Display / headings: **Fraunces** (`--font-display`).
- Body: **Libre Franklin** (`--font-body`).
- Mono / prompts: **IBM Plex Mono** (`--font-mono`).

```html
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400;0,9..144,500;0,9..144,600;1,9..144,400;1,9..144,500&family=Libre+Franklin:ital,wght@0,300;0,400;0,500;0,600;0,700;1,400&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">
```

### Type scale (on the 1280-px canvas)

Slide title Fraunces ~41 px · kicker 13 px tracked caps in steel (diamond marker + hairline rule) · lead 22 px · bullets 23 px · card heading 20 px · card body 18 px. **Keep on-slide reading text ≥ 18 px** for projector legibility (tracked micro-labels, eyebrows, pills, and the footer are the intentional exception).

**Motion:** one orchestrated entrance per slide — children of `.slide-body` rise-and-fade in sequence (softer blur-glide on covers/dividers). Respects `prefers-reduced-motion`.

### 1.1 Re-skinning per project (worked example)

Override tokens and fonts in the **deck's own `<style>`**, loaded after the framework stylesheet, so the shared file stays generic:

```css
:root{
  --navy:#0A3476; --navy-dk:#071f4a; --navy-md:#12428f; --steel:#12428f;
  --gold:#FCB040; --gold-lt:#fdd17a; --gold-dk:#b9791f;
  --mgray:#e2e7f5; --hair:#e2e7f5; --slate:#5a6680; --text:#1a1a2e;
  --metal:linear-gradient(180deg,#fdd17a 0%,#FCB040 55%,#e09a2e 100%);
  --paper:linear-gradient(174deg,#ffffff 0%,#f3f6fc 100%);
  --font-display:"DM Serif Display", Georgia, serif;
  --font-body:"DM Sans", system-ui, sans-serif;
  --font-mono:ui-monospace, Menlo, Consolas, monospace;
}
/* DM Serif Display ships one weight; pin headings to 400 to avoid faux-bold */
.slide h1,.slide h2,.slide h3,.slide h4,.slide-title,.cover h1,.divider h1{font-weight:400;}
```

Also load that project's Google Fonts link instead of the default one. Keep contrast ≥ 4.5:1 (§7).

---

## 2. The slide canvas

Every slide is a fixed **1280 × 720** (16:9) canvas. The JS scales it to the viewport, so you author at a constant size and it fits any screen. The scale is recomputed on resize. Below ~800 px wide, or at high browser zoom, the framework switches to a **reflow mode** (§7) so the deck stays readable on phones and meets WCAG reflow; on laptops and projectors it scales as one unit.

```html
<div class="deck">
  <section class="slide cover current"> … </section>   <!-- first slide gets `current` -->
  <section class="slide"> … </section>
  …
</div>
<script src="../assets/deck-framework.js"></script>
```

Each slide has three parts — **body, footer, notes**. The footer is a **sibling** of `.slide-body` (not inside it), so the framework can pin it to the bottom:

```html
<section class="slide">
  <div class="slide-body"> …visible content… </div>
  <div class="slide-footer">
    <span class="brand"><span class="star">✦</span> Brand</span>
    <span class="fac">Facilitator: Name</span>
    <span class="url">project.url</span>
  </div>
  <div class="notes"><p>…teleprompter text…</p></div>   <!-- never rendered on the slide -->
</section>
```

The framework reads `location.hash` on load, so `deck.html#4` opens on slide 4 — used for deep links **and** for screenshot verification (§10). `window.__deck.show(n)` (0-based) jumps programmatically — useful for an in-deck "jump to a section" menu (buttons calling `window.__deck.show(i)`; the framework ignores clicks on `<button>` so they do not also advance the slide).

---

## 3. Slide types

- **Cover** — `class="slide cover"`: dark gradient, silver left rule, inset hairline frame.
  ```html
  <div class="slide-body">
    <div class="cover-eyebrow">Event name</div>
    <h1>Big Title</h1>
    <div class="subtitle">Italic subtitle</div>
    <div class="meta"><strong>Facilitator:</strong> Name<br>url</div>
  </div>
  ```
- **Divider** — `class="slide divider"`: cover-like, with an oversized ghosted `.seg-num` numeral. Either a `cover` or an opening `divider` counts as the **title slide** (§6 exit-icon rule).
  ```html
  <div class="slide-body">
    <div class="seg-num">1</div>
    <div class="divider-eyebrow">Segment One · about 20 minutes</div>
    <h1>Section Title</h1>
    <div class="subtitle">One-line summary</div>
  </div>
  ```
- **Content** — the standard slide: kicker + title, then blocks.
  ```html
  <div class="slide-body">
    <div class="slide-kicker">Small tracked label</div>
    <h2 class="slide-title">The headline</h2>
    <p class="lead">Optional lead sentence.</p>
    <!-- blocks below -->
  </div>
  ```

> **Title width:** the framework caps `.slide-title` for the reference measure; if a title wraps to two lines when it could fit on one, widen it per deck (`.slide-title{max-width:none;}`) rather than shrinking the font.

---

## 4. Content blocks (drop into `.slide-body`)

- **Bullets** — `<ul class="bullets"><li>…</li></ul>`, 3–5 diamond bullets, short phrases; `<strong>` for emphasis.
- **Cards** — `<div class="grid cols-3">` (or `cols-2`) of `<div class="card">` (add `gold` for a top-tab). Card = `<h3><span class="ico">⚖️</span>Title</h3><p>…</p>`.
- **Steps** — `<div class="steps">` of `<div class="step"><div class="n">1</div><h4>…</h4><p>…</p></div>` — numbered process.
- **Guardrail (do / do-not)** — `<div class="guardrail">` with `.guardrail-col.will` ("Do") and `.guardrail-col.willnot` ("Do not"). Keep to ~3 items per column — it overflows easily. (Facilitator-only "how to run it" guidance belongs in notes, not on a projected slide.)
- **Compare** — `<div class="compare">` with two `<div class="compare-col">` (second one `alt`).
- **Callout** — `<div class="callout"><span class="label">LABEL</span><p>Big statement</p></div>`; add `light` for a pale version.
- **Reflect** — `<div class="reflect"><span>💬</span><p><strong>Lead.</strong> Italic prompt</p></div>`.
- **Prompt** — `<div class="prompt">…</div>` — dark mono block for prompt/citation text.
- **Stats** — `<div class="stat-row">` of `<div class="stat"><div class="num">Word</div><div class="lbl">…</div></div>`.
- **Pill** — `<span class="pill time">about 20 min</span>` or `pill tag`.
- **Scenario** — `<div class="scenario"><div class="scenario-label">Your task</div><p>…</p></div>`.
- **Next-step link** — points at an activity, resource, or the next deck:
  ```html
  <div class="next-step no-advance">
    <span class="ns-label">Do this next</span>
    <a href="../activities/x.html" target="_blank" rel="noopener">Open it <span class="arrow">↗</span></a>
  </div>
  ```
  Always give it `no-advance` (so the click does not flip the slide) and `target="_blank"`.

**Deck-local one-offs** (letter grids, tier cards, two-column layouts, image frames) live in a small `<style>` block in that deck's `<head>`. Always reuse the palette variables so they stay on-brand, and register any deck-local grid/absolute art in the `.deck.reflow` rules (§7).

---

## 5. Images and photos

Author at the fixed 1280×720 scale and place with absolute positioning (hero/divider art) or in a normal-flow `<figure>` (infographics) so text and image never collide.

### 5.1 Optimize first — always WebP

Convert every source PNG/JPG to WebP before adding it. Targets: **≤ ~160 KB**, longest edge ~1100–1200 px, quality 82–88.

```bash
magick source.png -resize 1160x -quality 86 assets/name.webp
magick source.png -crop 1400x600+0+120 +repage -resize 1160x -quality 86 assets/name.webp
```

**Sourcing:** use images you have rights to. Free/CC options include Unsplash (Unsplash License — free, incl. commercial, no attribution required) and Wikimedia Commons (CC/PD). Download and host locally; don't hotlink. Record sources in an HTML comment. Always visually vet an image before using it.

### 5.2 Placement patterns

- **Corner icon** — `<img class="slide-ico" src="…" alt="">` as the first child of `.slide-body` (floats top-right ~108 px). Only on slides whose top-right is empty.
- **Right hero with fade** — a large image bled off the right edge, masked so it dissolves into the slide (`-webkit-mask-image`/`mask-image` linear-gradient). Constrain the text column's `max-width`.
- **Divider photo** — a rounded, shadowed card floated right of divider text.
- **Image-left / words-right** — a two-column grid inside `.slide-body`.
- **Infographic figure** — a centered normal-flow `<figure>` with `max-height` so it stays on-canvas; reflows cleanly.

**Rule of thumb:** if an image leaves a big empty band, enlarge it, add a companion element, or switch to a two-column layout. Don't ship a slide that's half whitespace.

---

## 6. Navigation chrome

Injected once by the JS, fixed to the viewport (outside the scaled canvas):

- **`#progress`** — 3 px bar at the very top; width tracks position.
- **`#controls`** — top-right cluster (~62 % idle opacity, 100 % on hover): `‹` prev · counter · `›` next · 🗒 notes · 🖥 presenter · ⛶ fullscreen · ? help.
- **`#exitDeck`** — top-**left** exit-to-hub icon (a `log-out` glyph). **Hidden on the title slide** (`idx === 0`) and in print. It lives in the shared framework — do not add it per-deck; point its `href` at the project hub.

All chrome is hidden by the print stylesheet.

---

## 7. Accessibility (WCAG 2.1 AA)

**Built into the framework (automatic):**
- **Reflow mode** (1.4.10/1.4.4/1.4.12) — `fit()` toggles `.reflow` on `.deck` when `innerWidth < 800` or the fit scale drops below `0.55×`; slides become a single-column, scrollable, relative-type layout. **When you add a deck-local two-column grid or absolutely-positioned image, add its selector to the `.deck.reflow` collapse/neutralize rules** (in the deck's `<style>`) so it stacks cleanly on phones.
- **Visible focus** (2.4.7), **slide-change live region** (4.1.3), **reduced motion** (2.3.3), **non-text contrast** (1.4.11) — all handled.

**Author rules (per slide):** real text, never images of text (1.4.5); accurate `alt` (decorative = `alt=""`, 1.1.1); contrast ≥ 4.5:1 (1.4.3); don't encode meaning in color alone (1.4.1); every slide has a real heading.

**Not automatic:** screen-reader passes and RTL `lang="en"` marking — don't claim conformance without testing.

---

## 8. Speaker notes and the presenter view

**Notes.** Every slide carries `<div class="notes"><p>…</p></div>`. Hidden on the slide; surfaced two ways:

- **On the current screen** — press **S** (or **N**) to slide up a notes panel. Dismiss it the same way, with the **×** button in the panel header, or with **Esc**.
- **On a second monitor** — press **V** (or 🖥) to open a **presenter window**: current slide, next slide, notes in large type, an elapsed **timer** (click to pause; Reset button), and a clock. Put the main window on the projector, press **F** for fullscreen. The two windows stay in sync via `BroadcastChannel` + a `localStorage` fallback (same-origin). Close the presenter window with its **✕ Close** button (top bar) or **Esc** — no need to hunt for the OS window control.
- **Resizing the notes** — the presenter window's Speaker-notes panel carries **A− / A+** buttons (right of the "Speaker notes" label) to shrink or enlarge the notes text mid-talk; the **+** and **−** keys do the same. The size is clamped and **persists** across sessions via `localStorage` (key `webdeck-notes-scale`; default 20 px / scale 1.0).

**Writing the notes — teleprompter text, not stage directions:** first person, conversational; ~90–130 words per slide; cover what to say, what to watch for, and the transition. No em dashes. No meta-remarks ("say this…"). Put facilitator "how to run it" guidance here, not on the projected slide.

**Keyboard (main deck):** → / Space / PgDn next · ← / PgUp prev · Home / End first / last · **S** notes · **V** presenter · **F** fullscreen · **P** print/PDF · **?** help. Clicking the left third of a slide goes back, the rest advances (links, buttons, `.no-advance` ignored).

**Keyboard (presenter window):** → / Space / PgDn next · ← / PgUp prev · Home / End first / last · **T** reset timer · **+** / **−** enlarge / shrink the notes text.

---

## 9. Print / PDF export

Press **P** in any deck. The print stylesheet stacks every slide one-per-page at 1280 × 720, forces `print-color-adjust: exact`, resets the JS scaling transforms, and hides all chrome. "Save as PDF" gives a clean handout.

---

## 10. Verify before you ship — headless Chrome

Never trust an edit to a fixed-canvas slide by eye alone. Render it:

```bash
google-chrome --headless --disable-gpu --hide-scrollbars \
  --window-size=1280,720 --virtual-time-budget=4000 \
  --screenshot=/tmp/slide.png "file://$PWD/decks/0-overview.html#4"
```

Then open the PNG. Crop a detail with `magick /tmp/slide.png -crop 120x70+0+0 +repage /tmp/corner.png`. Check a **content slide** (element present) and the **title slide** (exit icon absent) when touching shared chrome, and render at phone width (`--window-size=380,820`) to confirm **reflow** (§7). To verify the **presenter view**, render `…/deck.html?presenter=1`.

---

## 11. Build a new deck — checklist

1. Copy `webdeck/assets/deck-framework.{css,js}` into the project's `assets/` (or confirm they're current). Copy `webdeck/decks/template-deck.html` as a starting deck.
2. Link the Google Fonts + `../assets/deck-framework.css` in `<head>`; add a deck-local `<style>` for the project skin (§1.1) and any one-offs.
   - Keep the **invisible framework attribution** in the `<head>` — the template ships it and it never renders on a slide:
     ```html
     <!-- Built with Web Deck v5 — https://mguhlin.github.io/webdecks/ · Developed by Miguel Guhlin - mguhlin.org · MIT -->
     <meta name="generator" content="Web Deck v5 (https://mguhlin.github.io/webdecks/) — developed by Miguel Guhlin - mguhlin.org">
     ```
     This credits the **framework**, not the deck. Put the deck's own owner in the footer / cover (`Facilitator: Name`), never the framework author — the framework author's name must not appear on any slide.
3. Open `<div class="deck">`. One `<section class="slide …">` per slide; give the **first** one `current`.
4. Start with a `cover`, use `divider` slides between segments, `content` slides between.
5. On every slide include the `.slide-footer` (sibling of `.slide-body`) and a `.notes` block.
6. Keep slides to 3–5 short bullets or one main block; push full sentences into the notes.
7. Optimize images to WebP (§5.1); place absolutely or in a `<figure>`; register deck-local grids/art in `.deck.reflow` (§7).
8. End the body with `<script src="../assets/deck-framework.js"></script>`.
9. Write teleprompter notes for **every** slide before calling it done.
10. Render each new/edited slide headless (§10) at 1280×720 **and** phone width.

### On-slide writing style

Second person · Oxford comma · spell out numbers one through ten · **no em dashes** · **no ampersands** (use "and") · **no colons in titles** · avoid hype words (empower, journey, embark, delve, unlock, elevate, discover, master).

---

## 12. Resource pages and i18n (optional)

Reader pages (hubs, activities, handouts) can use a sibling `assets/pages.css` with the same palette/fonts. A lightweight i18n engine (`data-i18n` attributes + a registered dictionary, persisted via `?lang=` + localStorage) adds a language switcher. Translate chrome; keep substantive content in its authored language unless the project says otherwise. These are project-specific; see the project's own notes.

---

## 13. Deploy workflow (per project)

Most vibecoding decks are static sites on **GitHub Pages**, deployed by pushing to the repo's default branch. General flow:

```bash
git add <files> && git commit -m "…"
git push origin main            # Pages auto-builds
# confirm live: curl -s -o /dev/null -w '%{http_code}' https://<user>.github.io/<repo>/<path>
```

Notes:
- Some repos require a specific GitHub account to push (e.g. `gh auth switch --user <name>` before the push, then switch back). Follow the project's own deploy note.
- `_site/` and similar build outputs may be gitignored; the **committed** source files are what deploy. For **generator-built, inlined** decks (§0.2), fix the generator *source* and **rebuild**, and patch any already-committed built file so the live page updates.
- After pushing, **verify the live URL** (poll until the new content appears; Pages takes ~30–90 s), and hard-refresh to clear cache.

Honor each repo's standing instructions (e.g. an `AGENTS.md` that authorizes commit/push/deploy without asking).

---

*End of v5. If you change the framework's public behavior (a keyboard binding, a chrome element, a content block, the presenter view), update this file in the same change, re-sync `webdeck/assets/`, and patch inlined decks (§0.2).*
