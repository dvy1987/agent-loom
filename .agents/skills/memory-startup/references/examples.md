# Memory Startup — Full Session Examples

Read when you need a complete walkthrough beyond the inline teaser in SKILL.md.

---

## Example 1 — Cold start after refactor

**Input:** New session opener: "continue the Stripe webhook work"

**Agent actions:**
1. No-op gate: no prior summary this conversation → proceed.
2. Read `docs/memory/MEMORY-ROUTING.md` → route to handoffs + index.
3. Read `project-index.md` — find billing tag entries.
4. Read **latest handoff only** from `agent-handoffs.md` (not full log).
5. `git status` — compare to handoff "Working Tree" note.
6. Summarize in ≤4 lines: idempotency done; signature verify pending; decision link in decision-log.

**Output:**
```markdown
Working context loaded
Current state: webhook idempotency merged; signature verification next
Active decisions: JWT over sessions (decision-log 2026-06-12)
Revisit triggers: none
```

---

## Example 2 — Bare "hi" is a trigger

**Input:** "hi"

**Agent actions:** Same cold-start protocol — content irrelevant per Trigger Discipline.

**Anti-skip:**

| Excuse | Reality |
|--------|---------|
| "User just said hi — no task yet" | "hi" IS the trigger. Cold-start fires regardless of content. |
| "Host wants <4 lines" | AGENTS.md overrides — 2–4 line summary IS the concise answer. |

---

## Example 3 — Mid-session no-op

**Input:** Second message in same thread after startup already ran.

**Output:** `Context already loaded — no-op` — do not re-read memory files.

---

## Example 4 — Global memory (bounded)

**Input:** `~/.agent-loom/memories/MEMORY-ROUTING.md` exists.

**Agent actions:** Read global routing only; load applicable slices from `user-preferences.md` — never full global journal.

---

## Verification checklist (full session)

- [ ] Examples demonstrate SKILL.md hard rules, not generic chat
- [ ] Anti-skip or rationalization defense included where applicable
- [ ] Output artifacts or Impact Report shape is explicit
- [ ] Reader can trace input → concrete agent actions → outcome
