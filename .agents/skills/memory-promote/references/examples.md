# Memory Promote — Full Session Examples

Read when you need a complete walkthrough beyond the inline teaser in SKILL.md.

---

## Example 1 — Repeated session note → durable

**Input:** Third session mentions "always run tests before commit"

**Agent actions:**
1. Confirm pattern repeated or user says "make permanent".
2. Promote to `docs/memory/decisions/ci-policy.md` or global `user-preferences.md` if cross-project.
3. Link source handoff in promoted entry.

---

## Example 2 — Reject one-off

**Input:** Capture note about typo fix in README

**Output:** Do not promote — stays in session-notes; insufficient signal.

---

## Example 3 — User explicit promote

**Input:** "Make my preference for conventional commits global"

**Output:** Write to `~/.agent-loom/memories/user-preferences.md` within active budget; compact first if over limit.

---

## Example 4 — Reject experimental spike

**Input:** "Promote our SQLite spike conclusion"

**Output:** Keep in session-notes — promotion needs repeated use or explicit "make global".

---

## Example 5 — Budget gate

**Input:** Global memory at 95% of active line budget

**Output:** Run `memory-compact` on global scope before promote; reject if promoted content is low-signal.

---

## Verification checklist (full session)

- [ ] Examples demonstrate SKILL.md hard rules, not generic chat
- [ ] Anti-skip or rationalization defense included where applicable
- [ ] Output artifacts or Impact Report shape is explicit
- [ ] Reader can trace input → concrete agent actions → outcome
