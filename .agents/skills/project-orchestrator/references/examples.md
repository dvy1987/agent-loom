# Project Orchestrator — Full Worked Examples

Skill: `project-orchestrator` | Enriched from SKILL.md (improve-skills pass, SKIP_RESEARCH).

## Example 1 — Documented workflow

**Input:** I want to go from this rough idea to a full implementation plan.

**Output:**
```
[Scanned: no product-soul, no specs, no PRD. Starting from scratch.]

**Orchestration Plan** — Sequential chain (4 skills):
1. `product-soul` — strategic context
2. `brainstorming` — approved design (2-3 approaches)
3. `prd-writing` — structured requirements
4. `implementation-plan` — actionable steps

Each feeds the next. ~15-20 min. Shall I start with Product Soul?
```

## Example 2 — Step-by-step execution

**Input:** "Run `project-orchestrator` on [concrete task]"

**Agent actions:**
1. Read Project State
2. Route the Request
3. Plan and Present
4. Execute (Platform-Aware)
5. Synthesise and Check for AGENTS.md Refresh
6. Execution Feedback (Learning Loop)

**Impact Report shape:**
```
Orchestration complete: [request summary]
Mode: [single / sequential / parallel]
Skills invoked: [list]
Subagents spawned: [N or "sequential"]
Next recommended phase: [phase + skill]
```

## Example 3 — Gotcha application

**Input:** Task hits a non-obvious edge case

**Apply:**
- **Don't over-orchestrate.** Single-skill requests need routing, not orchestration.
- **Subagent scope creep is the #1 failure.** Every subagent needs explicit file boundaries.
- **Read the AGENTS.md Orchestration Map first** — if `project-setup` ran, it's already customised.
- **File-based coordination is the universal fallback.** Write the plan to a file — every platform reads files.

---

See `SKILL.md` for hard rules and verification checklist.
