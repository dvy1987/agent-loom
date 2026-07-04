# Memory Handoff — Full Worked Examples

Skill: `memory-handoff` | Memory suite enrichment pass.

## Example 1 — Commit / push trigger (v1.3)

**Input:** User says "commit these changes" or "push to origin"

**Output:** Run full handoff workflow first → append `docs/memory/agent-handoffs.md` → update current-state + project-index → incremental graph rebuild → then proceed with git commit and/or push.

## Example 2 — Commit and push together

**Input:** "commit and push when ready"

**Output:** Handoff documents working tree state and commits pending; after handoff saved, stage → commit → push. Next agent reads handoff even if push succeeds.

## Example 3 — Session end

**Input:** Large refactor complete, user leaving

**Output:** Handoff block: done / next / blockers / files touched / graph rebuild flag.

## Example 4 — Thin context recovery

**Input:** Next agent starts cold

**Output:** `memory-startup` reads handoff tail + project-index; does not load full history.

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
