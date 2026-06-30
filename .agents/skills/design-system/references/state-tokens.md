# Tokens All The Way Down

Generic-ness lives in the ~95% of decisions a brief never specifies: every interactive
state, the neutral ramp, the exact focus ring, the white that sits on the accent. If those
tokens do not exist, the model fills them from the corpus mean and the slop wins by surface
area. Define them so the seams hold.

This complements `token-recipes.md` (per-direction starting palettes). That gives the
palette; this gives the depth.

---

## 1. Neutral ramp — 8 steps, perceptual

One ramp, eight steps, hand-set in `oklch` for perceptual evenness (a `slate-500` looks
faintly blue; `oklch` greys read grey). Steps map to roles, not raw numbers:

```
--neutral-0   surface base (off-white / off-black — never #fff/#000)
--neutral-1   raised surface (cards, inputs)
--neutral-2   sunken / hover surface
--neutral-3   subtle border / hairline
--neutral-4   strong border / divider
--neutral-5   tertiary text / disabled text
--neutral-6   secondary text
--neutral-7   primary text
```
Light mode runs 0→7 light→dark; dark mode is a **separate hand-set story**, never inverted
lightness. Most products need 5-8 greys — never the 50→950 Tailwind dump.

---

## 2. Every interactive state has a token

For every interactive surface (button, link, input, row, tab), define the full state set —
not just rest:

```
--accent              rest
--accent-hover        rest shifted ~4-6% L (or chroma) — never opacity-only
--accent-active       pressed, ~8-10% L shift, often a 1px translate in motion
--accent-disabled     desaturated + lowered L; pair with --text-on-accent-disabled
--text-on-accent      the exact foreground that sits ON the accent (APCA-checked)
--focus-ring          color
--focus-ring-opacity  e.g. 0.35–0.5
--focus-ring-width    2–3px, offset 2px
```
Repeat the rest/hover/active/disabled pattern for secondary, ghost, and destructive
variants. Hover that only changes opacity is a tell — shift lightness or chroma.

---

## 3. Focus ring is a first-class decision

- Visible, archetype-colored, `:focus-visible` only (not `:focus`, which fires on click).
- `outline: var(--focus-ring-width) solid; outline-offset: 2px;` using the ring color at
  its opacity. Never `outline: none` without a replacement.

---

## 4. Spatial / motion / elevation (depth, not decoration)

- Spacing: log-spaced (4, 8, 12, 16, 24, 32, 48, 64, 96), not linear.
- Radius: direction-driven, one scale (e.g. 4/8/12). Chip radius < card radius, declared.
- Elevation: 0-3 levels max. Prefer whitespace → 3-5% background shift → soft elevation →
  (last resort) a hairline border. A flat grey 1px box on every card is the #1 slop tell.
- Motion: 3-4 durations + named curves (real cubic-bezier), plus `prefers-reduced-motion`
  override shrinking to ≤0.01ms.

---

## 5. APCA contrast (not the legacy WCAG ratio)

APCA is perceptual and accurate on dark themes and thin type. Targets (`Lc`):
- Body text: `Lc ≥ 75`
- Large / bold text: `Lc ≥ 45`
- Non-text UI (icons, borders, focus rings): `Lc ≥ 30`

Check every text/background AND text-on-accent pair. Text over images/gradients needs a
semi-transparent overlay to guarantee `Lc`. Use the script in `design-review`
(`references/apca-contrast.md`) to measure — never eyeball.

---

## 6. Token tiers (clean lookup path for agents)

1. **Primitive** — raw values (`--oklch-...`). Implementation layer only.
2. **Semantic** — role names (`--surface-1`, `--text-primary`, `--accent`). What components use.
3. **Component** — `--button-bg`, `--input-border` referencing semantics. Lets you restyle one
   component without touching the system, and gives the agent a per-component contract.

Components consume semantic/component tokens only — never primitives, never raw hex.

---

## Self-audit before emitting
- [ ] 8-step neutral ramp, oklch, dark mode hand-set (not inverted)
- [ ] rest/hover/active/disabled + text-on-accent for every interactive variant
- [ ] focus-ring color + opacity + width, `:focus-visible`
- [ ] spacing log-spaced; ≤3 elevation; borderless-card default
- [ ] 3-4 motion durations + real curves + reduced-motion override
- [ ] every text/bg and text-on-accent pair passes APCA target
- [ ] no banned default leaked (`banned-palettes.md`)
