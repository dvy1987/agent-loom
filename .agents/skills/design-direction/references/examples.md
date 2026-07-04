# Design Direction — Full Session Examples

Read when you need a complete walkthrough beyond the inline teaser in SKILL.md.

---

## Example 1 — B2B settings page (3 distinct directions)

**Input:** "Design direction for our team billing settings — feels trustworthy, not playful"

**Agent actions:**
1. Read `docs/product-soul.md` + PRD — audience: finance admins, emotional goal: confidence.
2. Score archetypes — top seeds: `enterprise-trust`, `b2b-productivity`.
3. Posture: restrained, cool, classic, quiet, calm.
4. Generate 3 directions differing on type, layout, motion:
   - **Ledger** — feels like Stripe Dashboard; tabular density, mono accents
   - **Briefing** — feels like Linear; sidebar nav, generous whitespace
   - **Vault** — feels like 1Password; card stacks, strong elevation
5. Side-by-side comparison table; owner non-technical → agent recommends **Ledger** with plain rationale.
6. Write `.design/billing-settings/DIRECTION.md`; handoff to `design-system`.

---

## Example 2 — Anti-skip (three palettes ≠ three directions)

**Input:** Agent proposes light/dark/blue variants of same layout

**Response:** Block — diverge on ≥3 dimensions (type, layout, motion) or it's one direction.

---

## Example 3 — No product docs

**Input:** "Make it look modern" (no PRD)

**Agent asks ONE question:** "What is this for, who is it for, and which product should it feel closest to?"

---

## Example 4 — Reference without posture

**Input:** "Make it like Linear"

**Output:** Reference sets fit; still state posture sentence + bold move per direction — never stop at the name drop.

---

## Example 5 — Orchestrator handoff

**Input:** `frontend-design` routes here for new dashboard shell

**Output:** DIRECTION.md committed; Impact Report lists handoff to `design-system` with chosen direction name and file path.

---

## Verification checklist (full session)

- [ ] Examples demonstrate SKILL.md hard rules, not generic chat
- [ ] Anti-skip or rationalization defense included where applicable
- [ ] Output artifacts or Impact Report shape is explicit
- [ ] Reader can trace input → concrete agent actions → outcome
