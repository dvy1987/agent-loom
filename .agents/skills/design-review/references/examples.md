# Design Review — Full Session Examples

Read when you need a complete walkthrough beyond the inline teaser in SKILL.md.

---

## Example 1 — SHIP with minor fixes

**Input:** Review billing settings built against DIRECTION.md "Ledger"

**Agent actions:**
1. Capture screens at 1440px + 375px (Playwright or user paste).
2. Run `scripts/apca.mjs` — 2 pairs fail on secondary button dark mode.
3. Ethical patterns pass; UX heuristics: empty state missing for invoice list.
4. Findings (max 8 prioritized):
   - P0: Add empty state for zero invoices
   - P1: Secondary CTA Lc 42 → target 45 (token `--muted-foreground`)
5. Write `.design/billing-settings/REVIEW.md` — Verdict: **REVISE** (2 blockers).

---

## Example 2 — APCA hard gate

**Input:** "WCAG 4.5:1 passes, ship it"

**Response:** WCAG misreads dark/thin type. Re-run APCA — body text on `bg-muted` fails Lc 68 (<75).

---

## Example 3 — State coverage gate

**Input:** Happy path looks polished

**Output:** FAIL — no loading skeleton on invoice table; no error state on payment failure.

---

## Example 4 — Direction fidelity

**Input:** Hero uses Inter; DIRECTION.md specifies GT Sectra display

**Finding:** "Swap `--font-display` per DIRECTION.md §Typography — current Inter 700 reads generic vs Ledger reference."

---

## Example 5 — Playwright capture path

**Input:** No screenshots pasted; repo has Playwright MCP

**Output:** Follow `references/playwright-flow.md` — capture login, settings, empty invoice list at 375px before scoring.

---

## Verification checklist (full session)

- [ ] Examples demonstrate SKILL.md hard rules, not generic chat
- [ ] Anti-skip or rationalization defense included where applicable
- [ ] Output artifacts or Impact Report shape is explicit
- [ ] Reader can trace input → concrete agent actions → outcome
