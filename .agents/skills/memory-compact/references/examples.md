# Memory Compact — Full Worked Examples

Skill: `memory-compact` | Memory suite enrichment pass.

## Example 1 — Bloated handoff log

**Input:** `agent-handoffs.md` > 200 entries

**Output:** Archive older entries to `docs/memory/archive/`; keep index of archived ranges.

## Example 2 — Duplicate notes

**Input:** Same decision captured 4 times

**Output:** Merge into single decision file; leave redirect stubs.

## Example 3 — Pre-audit

**Input:** Before `memory-audit`

**Output:** Compact first to reduce audit surface.

## Example 4 — Global budget pressure

**Input:** `~/.agent-loom/memories/` over active budget

**Output:** Archive low-signal entries; preserve decisions + provenance links.

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
