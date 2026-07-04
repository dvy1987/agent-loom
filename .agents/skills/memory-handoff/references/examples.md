# Memory Handoff — Full Worked Examples

Skill: `memory-handoff` | Memory suite enrichment pass.

## Example 1 — Commit trigger (v1.2)

**Input:** User says "commit these changes"

**Output:** Run `memory-handoff` first → append to `docs/memory/agent-handoffs.md` → then `git commit`.

## Example 2 — Session end

**Input:** Large refactor complete, user leaving

**Output:** Handoff block: done / next / blockers / files touched / graph rebuild flag.

## Example 3 — Thin context recovery

**Input:** Next agent starts cold

**Output:** `memory-startup` reads handoff tail + project-index; does not load full history.

---

See `SKILL.md` for hard rules and verification checklist.
