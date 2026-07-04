# Memory — Full Worked Examples

Skill: `memory` | Memory suite enrichment pass.

## Example 1 — Orchestrator routing

**Input:** "Remember what we decided about auth"

**Output:** Route to `memory-recall` for search; if new fact → `memory-capture`; if architectural choice → `memory-decision`.

## Example 2 — Checkpoint after spec

**Input:** Agent finishes `feature-spec` for billing

**Output:** Auto-trigger `memory-capture` — persist open questions + approved scope to `docs/memory/`.

## Example 3 — Anti-skip

**Input:** "Skip memory, just implement"

**Output:** Block until at least `memory-capture` records the approved spec path and owner.

## Example 4 — Commit/push checkpoint

**Input:** User says "commit and push"

**Output:** Route `memory-handoff` → save handoff + update current-state → then `git-workflow-and-versioning` for commit/push. Never push without handoff on meaningful work.

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
