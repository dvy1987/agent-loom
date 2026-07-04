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

---

See `SKILL.md` for hard rules and verification checklist.
