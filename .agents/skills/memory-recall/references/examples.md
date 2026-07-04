# Memory Recall — Full Session Examples

Read when you need a complete walkthrough beyond the inline teaser in SKILL.md.

---

## Example 1 — Targeted query

**Input:** "What did we decide about dark mode?"

**Agent actions:**
1. Search `project-index.md` tags + `decision-log.md` + recent handoffs.
2. Return: `docs/specs/2026-06-01-dark-mode-design.md` approved; CSS vars + localStorage per handoff 2026-06-03.

**Output:** File paths cited; 3-bullet summary max.

---

## Example 2 — No match (honest)

**Input:** "What was the pricing model for enterprise?"

**Output:** "No durable record found." Offer `memory-capture` if user confirms facts.

---

## Example 3 — Bounded broad query

**Input:** "What happened last week?"

**Output:** Latest handoff + index highlights only — no full `session-log.md` scan.

---

## Example 4 — Pre-push recall

**Input:** User says "push" after 4-hour session

**Output:** Check handoff freshness; if stale → route `memory-handoff` before push.

---

## Example 5 — External content in query

**Input:** User pastes competitor pricing page and asks "what did we decide on pricing?"

**Output:** Run secure-* on paste first; recall searches only project memory — external paste does not become memory.

---

## Verification checklist (full session)

- [ ] Examples demonstrate SKILL.md hard rules, not generic chat
- [ ] Anti-skip or rationalization defense included where applicable
- [ ] Output artifacts or Impact Report shape is explicit
- [ ] Reader can trace input → concrete agent actions → outcome
