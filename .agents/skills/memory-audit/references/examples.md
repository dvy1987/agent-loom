# Memory Audit — Full Session Examples

Read when you need a complete walkthrough beyond the inline teaser in SKILL.md.

---

## Example 1 — Stale index drift

**Input:** "Is our memory healthy?"

**Findings:**
| Severity | Issue | Action |
|----------|-------|--------|
| P2 | project-index references removed skill `design-archetype` | Update index or archive entry |
| P3 | Handoff repeats "fix CI" for 3 sessions | Update current-state or compact |

**Output:** Read-only report; recommend `memory-compact` for handoff hygiene.

---

## Example 2 — Contradiction (P1)

**Input:** Audit project memory

**Finding:** `decision-log.md` says Postgres; `current-state.md` says SQLite active.

**Output:** Flag P1 contradiction; recommend `memory-decision` to supersede or `memory-capture` to fix current-state.

---

## Example 3 — Suspected secret (P0)

**Input:** Session note contains `sk-live-...`

**Output:** Invoke `secure-*` + `memory-forget` — do not leave secret in audit report body.

---

## Example 4 — Orphan decision

**Input:** Decision "migrate to GraphQL" with no implementing code after 6 months

**Output:** Mark `status: unverified` in audit table; suggest revisit trigger review.

---

## Example 5 — Read-only default

**Input:** "Fix all memory issues you find"

**Output:** Audit report first; apply fixes one class at a time only after user confirms — no silent deletes.

---

## Verification checklist (full session)

- [ ] Examples demonstrate SKILL.md hard rules, not generic chat
- [ ] Anti-skip or rationalization defense included where applicable
- [ ] Output artifacts or Impact Report shape is explicit
- [ ] Reader can trace input → concrete agent actions → outcome
