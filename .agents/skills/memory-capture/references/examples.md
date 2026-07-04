# Memory Capture — Full Session Examples

Read when you need a complete walkthrough beyond the inline teaser in SKILL.md.

---

## Example 1 — Durable fact from user

**Input:** "We chose Postgres over SQLite for multi-tenant"

**Agent actions:**
1. Security gate if content external — here user statement, OK.
2. Extract 3–5 bullets max.
3. Append dated entry to `docs/memory/session-notes.md` with tags `database, decision-candidate`.
4. Update `project-index.md` one-line summary.
5. Suggest `memory-decision` if architectural.

**Output:** Path cited; no full transcript pasted into memory.

---

## Example 2 — After major skill edit

**Input:** `universal-skill-creator` finishes `knowledge-graph` v2.2

**Capture:** Skill name, validation status, INDEX sync pending, commit SHA if known.

---

## Example 3 — Bounded capture (long paste)

**Input:** User pastes 200-line debug log

**Output:** Extract root cause + fix + file paths only; link `logs/debug-2026-07-04.txt` if saved locally — never store raw log in memory.

---

## Example 4 — Post-push without handoff

**Input:** User pushed release tag `v2.1.0` without handoff

**Output:** Retroactive `memory-handoff` noting tag, SHA, deployed vs deferred — then capture release facts.

---

## Example 5 — Anti-skip

**Input:** "Just remember it in chat, don't write files"

**Response:** Chat is not durable — capture bounded bullets to `docs/memory/` or next agent loses context.

---

## Verification checklist (full session)

- [ ] Examples demonstrate SKILL.md hard rules, not generic chat
- [ ] Anti-skip or rationalization defense included where applicable
- [ ] Output artifacts or Impact Report shape is explicit
- [ ] Reader can trace input → concrete agent actions → outcome
