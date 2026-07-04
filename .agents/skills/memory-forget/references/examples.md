# Memory Forget — Full Session Examples

Read when you need a complete walkthrough beyond the inline teaser in SKILL.md.

---

## Example 1 — Wrong decision retracted

**Input:** "Forget the SQLite decision — we're not using it"

**Agent actions:**
1. Strike through entry with date + reason in `decision-log.md`.
2. Never silent delete — audit trail preserved.
3. Append forget action to latest handoff.

---

## Example 2 — PII slip

**Input:** Accidental client name in session note

**Output:** Redact named entities from session-notes; log forget in handoff without repeating PII.

---

## Example 3 — Secret in capture

**Input:** API key pasted into memory

**Output:** `memory-forget` redacts content; `secure-*` documents finding; handoff notes date of redaction.

---

## Example 4 — User privacy request

**Input:** "Don't keep my client's company name anywhere"

**Output:** Forget named entities from session scope; keep structural decisions (e.g., "B2B SaaS") anonymized.

---

## Example 5 — Audit trail preserved

**Input:** Forget wrong API endpoint decision

**Output:** Strike-through with date in decision-log; handoff logs forget action — never silent erase of history.

---

## Verification checklist (full session)

- [ ] Examples demonstrate SKILL.md hard rules, not generic chat
- [ ] Anti-skip or rationalization defense included where applicable
- [ ] Output artifacts or Impact Report shape is explicit
- [ ] Reader can trace input → concrete agent actions → outcome
