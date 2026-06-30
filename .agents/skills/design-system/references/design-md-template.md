# DESIGN.md — Canonical Source-of-Truth Template

`DESIGN.md` is the ONE artifact every downstream step reads before styling anything. It
replaces the old scatter of ARCHETYPE.md / TOKENS.md / ICONS.md. Keep it tight and
machine-readable. Live at the project root (or `.design/<feature>/DESIGN.md` for scoped
work). Tokens also ship as real `tokens.css` — DESIGN.md is the human/agent contract.

Copy the structure below verbatim and fill every slot. No empty sections, no "TBD".

```markdown
# DESIGN.md — [Product]

> Single source of truth. Read this before generating or styling any UI.
> Direction: [name] — feels like [reference]. Posture: [one line].
> Stack: [e.g. React + Tailwind v4 + shadcn/ui]. Token format: [shadcn HSL vars / @theme].

## 1. Theme & Atmosphere
[2-3 sentences: mood, density, the one bold move that carries identity.]

## 2. Color (semantic roles, light + dark)
| Role | Light | Dark |
|---|---|---|
| surface-0 (base) | oklch(...) | oklch(...) |
| surface-1 (raised) | ... | ... |
| surface-2 (hover/sunken) | ... | ... |
| border-subtle | ... | ... |
| border-strong | ... | ... |
| text-primary | ... | ... |
| text-secondary | ... | ... |
| text-tertiary | ... | ... |
| accent | ... | ... |
| accent-hover | ... | ... |
| accent-active | ... | ... |
| text-on-accent | ... | ... |
| focus-ring (color / opacity) | ... | ... |
| status-success / warning / error / info | ... | ... |
Neutral ramp: 8 steps, oklch, dark hand-set (not inverted). See `state-tokens.md`.
APCA: body Lc≥75, large Lc≥45, non-text Lc≥30 — all pairs pass.

## 3. Typography
- Display: [family, weights, sizes, tracking]
- Body: [family, weights, sizes, line-height]
- Mono (if used): [family]
- Type scale: [list] · Reading column: [ch]
- Pairing rule: [one line — two families used confidently]

## 4. Spacing, Radius, Elevation, Motion
- Spacing (log): 4, 8, 12, 16, 24, 32, 48, 64, 96
- Radius: [chip < card < modal, e.g. 4 / 8 / 12]
- Elevation: [0-3 levels; borderless-card default]
- Motion: durations [instant/quick/base/emphasized] + curves [real cubic-bezier] + reduced-motion

## 5. Icons
- Strategy: [tuned-phosphor / custom-svg / system-native / mixed]
- Weight + size: [matched to type weight]; one family only. See `icon-strategies.md`.

## 6. Components (contracts for core atoms)
For each of button, input, card, nav, modal, table row:
| Component | Variants | Tokens consumed | Composition rule / use-when |
|---|---|---|---|
| Button | primary, secondary, ghost, destructive · sizes sm/md/lg | --button-* | primary = one per view; never inside a table cell |
| Card | default (borderless), interactive | --surface-1, --border-subtle | a card never contains another card |
| Input | text, select, textarea · rest/focus/error/disabled | --input-* | always paired with a <label> |
| ... | ... | ... | ... |
Every component defines rest / hover / active / focus-visible / disabled (+ loading/empty/error where it holds data).

## 7. Nevers (anti-slop guardrails)
- No Inter/Roboto as the only font; no pure #000/#fff; no slate/zinc default grey ramp.
- No purple→pink / indigo→violet gradient; no grey 1px border on every card.
- No 3-equal-column feature grid; no centered H1 + subhead + 2 CTAs default hero.
- No opacity-only hover; no `transition-all`; no Lucide default drop-in.
- [Add 2-3 product-specific nevers.]

## 8. Files
- src/styles/tokens.css  (or app/globals.css) — the live tokens
- src/styles/tokens.ts   — typed exports (optional)
```

---

## Notes
- Keep DESIGN.md under ~120 lines. Depth/rationale lives in `state-tokens.md` and the
  reference files, not here.
- If the stack is shadcn/ui, emit tokens in HSL channel format (`"240 33% 14%"`, no
  `hsl()` wrapper) so they slot into `hsl(var(--token))`. Otherwise emit `oklch()` under
  `:root` / `[data-theme="dark"]` (or Tailwind v4 `@theme`).
