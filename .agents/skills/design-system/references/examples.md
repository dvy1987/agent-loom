# Design System — Full Session Examples

Read when you need a complete walkthrough beyond the inline teaser in SKILL.md.

---

## Example 1 — Ledger direction → tokens

**Input:** DIRECTION.md chosen: **Ledger** (Stripe-like B2B)

**Agent actions:**
1. Seed from archetype `enterprise-trust` recipe.
2. Build 8-step neutral ramp + semantic slots (bg, fg, muted, accent) with hover/focus/disabled states.
3. Typography: display GT Sectra / body Inter; spatial 4px grid; motion 150ms ease-out.
4. APCA pass on all text pairs — fix `--secondary-foreground` on dark.
5. Icon strategy: Lucide 1.5px stroke; component contracts for Button, Table, Badge.
6. Emit `DESIGN.md` + `src/styles/tokens.css`.

**Impact Report:** 24 color slots, APCA all pass, 6 component contracts, handoff to `frontend-design`.

---

## Example 2 — Dark mode is not invert

**Input:** Agent inverts light tokens for dark

**Response:** Block — dark is hand-set per DIRECTION.md; inverted lightness reads cheap.

---

## Example 3 — Skip DESIGN.md

**Input:** "Just write the CSS variables"

**Response:** DESIGN.md is the contract — without it each screen re-negotiates and drifts.

---

## Example 4 — Accent-only palette

**Input:** "Primary blue + greys is enough"

**Response:** Slop lives in unstated states — define hover, focus, disabled, error for every semantic slot.

---

## Example 5 — shadcn HSL emit

**Input:** Stack uses shadcn + Tailwind v4

**Output:** Emit HSL tokens in `tokens.css` matching shadcn conventions; document slot mapping in DESIGN.md §Integration.

---

## Verification checklist (full session)

- [ ] Examples demonstrate SKILL.md hard rules, not generic chat
- [ ] Anti-skip or rationalization defense included where applicable
- [ ] Output artifacts or Impact Report shape is explicit
- [ ] Reader can trace input → concrete agent actions → outcome
