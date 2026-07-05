# Polish Playbook

"Looks unfinished" is a state-coverage and detail problem, not a taste problem. This is the
mandatory polish layer for every build. `design-review` checks it.

---

## 1. State coverage (mandatory for every data-bearing surface)

Every surface that shows data or takes input must render ALL of:
- **Rest / populated** — the happy path
- **Loading** — skeleton matching real layout (not a spinner), `aria-busy`
- **Empty** — guidance + next action (not a blank/"No data")
- **Error** — specific, recoverable, `role="alert"`
- Interactive elements also need: **hover, active, `:focus-visible`, disabled**

See `golden-examples/states.md`. Missing any = review fail.

---

## 2. Micro-interactions (purposeful, not decorative)

- Hover: shift a real token (background L/chroma), never opacity-only, never scale-1.05 reflexively.
- Press: `active:translate-y-px` or a subtle scale-down — confirms causality.
- Focus: visible `:focus-visible` ring with offset, archetype-colored.
- Toggles/switches: animate the thumb with the `--ease-standard` curve.
- Optimistic updates on toggles/likes where rollback is feasible.
- Every transform/animation has a `motion-reduce:` escape.

## 3. The one orchestrated moment

Prefer ONE well-staggered page-load reveal (CSS `animation-delay`, 40-80ms steps) over
scattered effects. Disable under reduced-motion. See `golden-examples/composition.md`.

## 4. Motion specifics (use real values, never `ease-in-out`/`transition-all`)

| Token | Typical value | Use |
|---|---|---|
| `--dur-quick` | 80-140ms | hover, color shifts |
| `--dur-base` | 160-240ms | toggles, small moves |
| `--dur-emphasized` | 280-420ms | entrances, modals |
| `--ease-standard` | `cubic-bezier(0.2, 0, 0, 1)` | most |
| `--ease-decelerate` | `cubic-bezier(0.16, 1, 0.3, 1)` | entrances |
| spring (playful) | `cubic-bezier(0.5, 1.5, 0.5, 1)` | character moments |

Framer Motion / `motion` for React when orchestration is complex; CSS-only otherwise. Invoke `motion-animation` for Motion patterns; `gsap-animation` for scroll pin and advanced SVG plugins.

## 5. Detail pass (the 95% the brief never mentions)

- `text-balance` on headings, `text-pretty` on body; tracking tightened on large display.
- Tabular numerals (`font-variant-numeric: tabular-nums`) for tables/metrics.
- Hairline dividers via `--border-subtle`, not a grey box on every card.
- Optical alignment: icons sit on the text baseline; trailing icons not crammed.
- Consistent radius hierarchy: chip < card < modal.
- Real favicon, page `<title>`, OG tags for marketing pages.
- Selection color, scrollbar styling that matches the theme.
- `::placeholder` uses `--text-tertiary`, not default grey.

## 6. Responsive polish

- Build 375px first; `min-h-dvh` (not `min-h-screen`); safe-area insets on mobile chrome.
- Container queries for components that ship into varying widths.
- Density adapts (not just shrinks) across breakpoints.

## 7. Reduced motion (non-negotiable)

`@media (prefers-reduced-motion: reduce)` shrinks durations to ≤0.01ms and disables
transforms/parallax/auto-play. Every animated element has a `motion-reduce:` variant.

---

## Final polish gate (block delivery until all pass)
- [ ] Every data surface: loading + empty + error + populated all rendered
- [ ] Every interactive el: hover + active + focus-visible + disabled
- [ ] One orchestrated entrance; reduced-motion fully honored
- [ ] Real cubic-bezier curves + named durations (no `transition-all`/`ease-in-out`)
- [ ] Detail pass done (text-balance, tabular-nums, hairlines, placeholder, selection)
- [ ] 375px clean; touch targets ≥44px
