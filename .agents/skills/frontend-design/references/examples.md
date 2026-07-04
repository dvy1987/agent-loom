# Frontend Design — Full Session Examples

Read when you need a complete walkthrough beyond the inline teaser in SKILL.md.

Full orchestration path and UI implementation patterns. See `references/ui-patterns.md` + golden-examples.

---

## Example 1 — Full orchestration (team dashboard)

**Input:** "Build team dashboard for B2B SaaS"

| Step | Action | Output |
|------|--------|--------|
| 0 | Read product-soul → stack | React + Next + Tailwind v4 + shadcn |
| 1 | `design-direction` | `.design/teams/DIRECTION.md` — "dense B2B, Linear-adjacent" |
| 2 | `design-system` | `DESIGN.md` + `tokens.css` |
| 3 | Build per `ui-patterns.md` | Container/presentation split, table + empty/loading/error |
| 4 | `design-review` | SHIP after 1 loop |
| 5 | Deliver | Impact report + file tree |

**Distinctive moves:** hairline table borders, command palette for team switch, off-white `#FAFAF7` base.

---

## Example 2 — Container/presentation (from ui-patterns.md)

**Input:** "Build team list page"

```tsx
// TeamListContainer — fetch + all four states
// TeamListView — pure props
// TeamListEmpty — primary CTA "Create team"
// TeamListSkeleton — matches row layout, aria-busy
```

Gate: all four states rendered before review.

---

## Example 3 — Optimistic toggle

**Input:** "Star a project inline"

Apply optimistic mutation pattern from `ui-patterns.md`:
- Instant UI update on click
- Rollback + toast on error
- `disabled` while pending

---

## Example 4 — Anti-skip (rationalization defense)

| Excuse | Reality |
|--------|---------|
| "Skip exploration, I know the look" | First idea = corpus mean — run design-direction |
| "Happy path is enough" | Empty/loading/error = polish; absence reads unfinished |
| "shadcn defaults look fine" | Restyle every surface via tokens |
| "Accessibility later" | Focus rings + APCA now — retrofit costs 3× |

---

## Example 5 — Fast path (single landing hero)

**Input:** "One marketing hero, not full app"

Read `one-shot-flow.md` → direction → system → build → review. Still run `anti-vibecoded-checklist.md` — hero must NOT be centered H1 + 2 CTAs unless justified.

---

## Example 6 — Refactor path (beautify existing)

**Input:** "Make settings page not look AI-generated"

1. Read existing UI + `docs/visual-direction.md` if present
2. `design-direction` for refresh (not full rebrand unless asked)
3. System diff on tokens only where needed
4. Rebuild states missing from current page (often empty/error)
5. `design-review` against "feels like [direction]"

---

## Example 7 — Keyboard-only verification

Before design-review: Tab through settings form — every control reachable, visible focus ring from `--focus-ring`, Escape closes modal.

---

## Example 8 — Error boundary placement

Wrap `/teams/[id]` segment with `FeatureErrorBoundary` per `ui-patterns.md` — nav survives partial crash.

---
