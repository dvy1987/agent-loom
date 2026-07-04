# Memory Recall — Full Worked Examples

Skill: `memory-recall` | Memory suite enrichment pass.

## Example 1 — Targeted query

**Input:** "What did we decide about dark mode?"

**Output:** Search project-index + decisions + recent handoffs; cite file paths.

## Example 2 — No match

**Input:** Query with no hits

**Output:** Say explicitly "no durable record"; offer `memory-capture` if user confirms.

## Example 3 — Bounded read

**Input:** Broad "what happened last week"

**Output:** Summarize last handoff + index highlights only — no full log scan.

## Example 4 — Pre-commit recall

**Input:** User says "push" after long session

**Output:** Recall latest handoff draft status; if stale, route to `memory-handoff` before push.

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
