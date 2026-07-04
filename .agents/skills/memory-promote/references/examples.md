# Memory Promote — Full Worked Examples

Skill: `memory-promote` | Memory suite enrichment pass.

## Example 1 — Session → durable

**Input:** Repeated session note about CI policy

**Output:** Promote to `docs/memory/decisions/` or project-index bullet.

## Example 2 — Criteria

**Input:** One-off typo fix note

**Output:** Do not promote — stays in session-notes.

## Example 3 — User request

**Input:** "Make this permanent"

**Output:** Promote with date + source handoff link.

## Example 4 — Reject promotion

**Input:** Experimental spike conclusion

**Output:** Keep in session-notes; promotion requires repeated use or explicit user "make global".

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
