# Memory Decision — Full Session Examples

Read when you need a complete walkthrough beyond the inline teaser in SKILL.md.

---

## Example 1 — Auth architecture choice

**Input:** "Record why we chose JWT over server sessions"

**Agent writes to `docs/memory/decision-log.md`:**
```markdown
## 2026-07-04 - JWT over server sessions
Status: active | Confidence: high | Tags: auth, api

### Decision
Use stateless JWT access tokens + refresh rotation.

### Context
Multi-region API, no sticky sessions, mobile clients.

### Alternatives
- Server sessions: simpler revoke, needs Redis cluster
- PASETO: less ecosystem support

### Revisit triggers
- When concurrent sessions >50k or instant revoke becomes compliance requirement
```

Updates `project-index.md`. Offers ADR via `architectural-decision-log` if user wants.

---

## Example 2 — Supersede old decision

**Input:** New evidence — compliance requires instant revoke

**Output:** New entry references superseded JWT decision; old record kept with `Status: superseded`.

---

## Example 3 — Lightweight library pick

**Input:** "We picked Zod over Yup for forms"

**Output:** One paragraph in session-notes with `decision:` tag; promote later if repeated.

---

## Example 4 — Anti-skip

**Input:** "Don't bother logging — we'll remember"

**Response:** Undocumented decisions get re-debated every session. Record with revisit triggers.

---

## Verification checklist (full session)

- [ ] Examples demonstrate SKILL.md hard rules, not generic chat
- [ ] Anti-skip or rationalization defense included where applicable
- [ ] Output artifacts or Impact Report shape is explicit
- [ ] Reader can trace input → concrete agent actions → outcome
