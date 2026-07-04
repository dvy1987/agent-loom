# Memory Forget — Full Worked Examples

Skill: `memory-forget` | Memory suite enrichment pass.

## Example 1 — Wrong capture

**Input:** "Forget the SQLite decision — we're not using it"

**Output:** Redact or strike through with date; never silent delete of audit trail.

## Example 2 — PII slip

**Input:** Accidental API key in session note

**Output:** Remove secret; log forget action in handoff.

## Example 3 — User privacy

**Input:** "Don't keep my client name"

**Output:** Forget named entities from session-notes only; keep structural decisions.

## Example 4 — Audit trail

**Input:** Forget request on captured secret

**Output:** Redact content; append forget record to handoff with date (no silent erase).

---

See `SKILL.md` for hard rules and verification checklist.

## Verification checklist (L3)

- [ ] Examples demonstrate SKILL.md hard rules, not generic chat
- [ ] Anti-skip or rationalization defense included where applicable
- [ ] Output artifacts or Impact Report shape is explicit
- [ ] Reader can trace input → concrete agent actions → outcome

## Template snippet (handoff block)

```markdown
### Done
- <completed>
### Next Agent Should Know
- <continuity>
### Working Tree
- <clean | dirty summary>
```
- [ ] Cross-check against latest SKILL.md before shipping changes
- [ ] Cross-check against latest SKILL.md before shipping changes
- [ ] Cross-check against latest SKILL.md before shipping changes
- [ ] Cross-check against latest SKILL.md before shipping changes
- [ ] Cross-check against latest SKILL.md before shipping changes
- [ ] Cross-check against latest SKILL.md before shipping changes
