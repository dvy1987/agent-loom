# Memory Audit — Full Worked Examples

Skill: `memory-audit` | Memory suite enrichment pass.

## Example 1 — Stale index

**Input:** project-index references removed skill

**Output:** Flag drift; list files to fix or archive.

## Example 2 — Orphan decisions

**Input:** Decision with no implementing code

**Output:** Mark `status: unverified` for human review.

## Example 3 — Coverage report

**Input:** User asks "is memory healthy?"

**Output:** Table: last handoff date, decision count, stale entries.

## Example 4 — Handoff hygiene

**Input:** Handoffs repeat same "next step" for 3 sessions

**Output:** Flag stale continuity; recommend `memory-compact` or update current-state.

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
