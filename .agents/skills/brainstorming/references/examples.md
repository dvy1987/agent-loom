# Brainstorming — Full Session Examples

Read when you need a complete walkthrough beyond the inline teaser in SKILL.md.

---

## Example 1 — Feature design (dark mode)

**Input:** "I want to add dark mode to our React app"

**Phase 1 — Frame (How Might We)**
```
How Might We let users switch between light and dark themes without breaking
existing custom components or increasing bundle size significantly?
```

**Clarifying question (one at a time):**
> Do you have an existing design system or component library (Tailwind, MUI, styled-components), or are styles written manually?

**User:** "Tailwind v4 + a few custom CSS modules for charts."

**Phase 2 — Options (3 divergent approaches)**

| Option | Summary | Trade-off |
|---|---|---|
| A. CSS variables + `class="dark"` on `<html>` | Token swap at root | Fast; chart CSS modules need manual vars |
| B. Tailwind `dark:` variant only | No extra runtime | Verbose; easy to miss a component |
| C. User preference in localStorage + system sync | Best UX | More state logic; flash-of-wrong-theme risk |

**Phase 3 — Converge**
Recommend **A + C**: CSS variables for charts, Tailwind dark: for app shell, `prefers-color-scheme` default with override.

**Design doc sections produced:**
- How Might We statement
- Target user: power users who work evenings; success = readable charts in both modes
- **Not Doing:** Per-component theme props (scope creep); auto-detect without manual toggle (accessibility concern)
- Key assumptions: chart library supports CSS color vars (validate in spike)
- HYPOTHESIS: 80% of screens themable via tokens alone — CONFIDENCE: 65%

**Output path:** `docs/specs/YYYY-MM-DD-dark-mode-design.md` — **no code until user approves.**

---

## Example 2 — Route to venture-exploration

**Input:** "I'm thinking of building a SaaS for freelance invoicing"

**Step 1 detect:** Business idea, not feature design → invoke `venture-exploration` instead of continuing brainstorming.

**Handoff message:**
> This sounds like a business validation question, not a feature design session. I'll route to venture-exploration for idea cards, Lean Canvas, and Mom Test interviews. Want to continue there?

---

## Example 3 — Anti-pattern recovery

**Input:** "Just pick the best architecture and implement auth"

**Response (Hard Gate):**
> Brainstorming blocks implementation until an approved design doc exists. I can either (1) run a 10-minute design pass on auth approach options, or (2) route directly to `feature-spec` if you already have an approved spec. Which?

---

## Verification checklist (full session)

- [ ] How Might We statement is clear
- [ ] Target user and success criteria defined
- [ ] Not Doing list makes trade-offs explicit
- [ ] Key assumptions listed with validation approach
- [ ] User approved design before implementation handoff

---

## Example 4 — Venture idea (restaurant regulars) — from idea-refine

**Input:** "I want to help local restaurants compete with DoorDash"

**Phase 1 — Reframe:**
> How might we help restaurants **retain** existing customers who already order from them — instead of competing for discovery on delivery apps?

**Clarifying:** Who is the user — owner, diner, or both? What does "compete" mean — more orders, higher margin, or less platform dependency?

**User:** "Restaurant owners. Compete = keep regulars ordering direct so they skip 30% platform fees."

**Variations (sample):**
1. **SMS reorder for regulars** — owner uploads top 20 phones + usual order; one-tap confirm link.
2. **Inversion — loyalty without an app** — punch-card via SMS, not another install.
3. **Simplification — pickup-only v1** — no delivery logistics in MVP.

**Phase 3 one-pager highlights:**
- **MVP:** SMS reorder for self-identified regulars, pickup only.
- **Not Doing:** Delivery, marketplace discovery, branded apps, POS integration in v1.
- **Assumption to validate:** Regulars will reorder via SMS vs their usual app (5 restaurants × 20 regulars, 4 weeks).

---

## Example 5 — Codebase-aware feature (real-time collaboration)

**Input:** "Add real-time collaboration to our document editor"

**Context scan:** Block-based editor, REST persistence, no WebSocket layer yet.

**Clarifying:** Same-paragraph editing (Google Docs) vs different sections (Notion)? How many simultaneous users?

**User:** "2–5 people, different sections. Losing deals — buyers expect real-time."

**Variations:**
1. **Block-level locking** — `locked_by` + presence; fits existing block model.
2. **Async-first** — suggestions/comments as primary mode.
3. **Presence without co-edit** — cursors only; coordinate verbally.

**Recommendation:** Variation 1 or 3 to **close the competitive checkbox** quickly; defer character-level CRDT.

**Not Doing (Phase 3):** Offline sync, AI-mediated collab, per-character merge in v1.

---

## Example 6 — Process idea (stale retrospectives)

**Input:** "Fix our weekly retros — people dread them"

**Diagnosis:** 8 people, 3–4 talk; same WWW format; **action items pile up unchanged** — output layer is broken, not just format.

**Variations:**
1. **One action item max** — demo completion at next retro or that *is* the topic.
2. **Async retro** — written reflections; 15-min standup to agree one change.
3. **Anonymous dot-vote** — structure for quiet voices.

**Phase 3 recommendation:** Start variation 1 + anonymous submission (variation 3) — **$0 prep**, test next week.

**Not Doing:** New tools, elaborate facilitation kits, budget spend before proving follow-through works.

