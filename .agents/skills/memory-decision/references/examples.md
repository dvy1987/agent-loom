# Memory Decision — Full Worked Examples

Skill: `memory-decision` | Memory suite enrichment pass.

## Example 1 — ADR-style record

**Input:** "Why JWT over sessions?"

**Output:** Write `docs/memory/decisions/YYYY-MM-DD-jwt-auth.md` — context, decision, consequences.

## Example 2 — Reversal

**Input:** New evidence contradicts old decision

**Output:** New decision file references superseded ADR; do not delete old record.

## Example 3 — Lightweight

**Input:** Small trade-off (library pick)

**Output:** One paragraph in session-notes with `decision:` tag for later promotion.

## Example 4 — Revisit trigger

**Input:** Decision assumed stable for 6 months

**Output:** Add `revisit: when traffic 10x` to decision file; `memory-recall` surfaces it on scale discussions.

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
