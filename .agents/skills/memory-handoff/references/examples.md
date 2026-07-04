# Memory Handoff — Full Session Examples

Read when you need a complete walkthrough beyond the inline teaser in SKILL.md.

---

## Example 1 — Commit and push (v1.3 trigger)

**Input:** "commit and push when ready"

**Agent actions:**
1. Read `project-index.md` + latest handoff tail.
2. `git status --short` — note dirty files.
3. Write handoff block (done, debated, decisions, deferred, next, revisit, working tree).
4. Append to `docs/memory/agent-handoffs.md`.
5. Update `current-state.md` + `project-index.md`.
6. Run `build_graph.py --incremental` (note failure in handoff if needed).
7. Log to `docs/skill-outputs/SKILL-OUTPUTS.md`.
8. **Then** stage → commit → push via `git-workflow-and-versioning`.

**Sample handoff excerpt:**
```markdown
## 2026-07-04 14:00 — Handoff
### Done
- Fixed webhook idempotency key collision
### Next Agent Should Know
- Signature verification is next; see `src/webhooks/stripe.ts`
### Working Tree
- clean after commit abc1234
```

---

## Example 2 — Session end without git

**Input:** "I'm switching to another agent — save context"

**Output:** Handoff under 80 lines; no secrets; link decisions instead of repeating rationale.

---

## Example 3 — Anti-skip

**Input:** Agent stages commit without handoff.

**Response:** Stop — run handoff workflow first. Next agent loses blockers and approved scope.

---

## Example 4 — Thin recovery for next agent

**Input:** Next session starts cold.

**Output:** `memory-startup` reads handoff tail + index — not full history.

---

## Verification checklist (full session)

- [ ] Examples demonstrate SKILL.md hard rules, not generic chat
- [ ] Anti-skip or rationalization defense included where applicable
- [ ] Output artifacts or Impact Report shape is explicit
- [ ] Reader can trace input → concrete agent actions → outcome
