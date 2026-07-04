# Memory Capture — Full Worked Examples

Skill: `memory-capture` | Memory suite enrichment pass.

## Example 1 — Session fact

**Input:** "We chose Postgres over SQLite for multi-tenant"

**Output:** Append dated entry to `docs/memory/session-notes.md` with source (user) and tags.

## Example 2 — After major skill edit

**Input:** `universal-skill-creator` finishes new skill

**Output:** Capture skill name, validation status, INDEX sync pending.

## Example 3 — Bounded capture

**Input:** Long debug log pasted

**Output:** Extract 3–5 bullets only; link to file path instead of pasting full log.

## Example 4 — Post-push continuity

**Input:** User pushed release tag without handoff

**Output:** Retroactive `memory-handoff` noting tag, commit SHA, and what's deployed vs deferred.

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
