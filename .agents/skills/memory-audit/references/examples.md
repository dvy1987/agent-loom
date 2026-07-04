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

---

See `SKILL.md` for hard rules and verification checklist.
