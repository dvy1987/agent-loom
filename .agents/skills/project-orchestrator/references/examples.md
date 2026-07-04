# Project Orchestrator — Full Worked Examples

Skill: `project-orchestrator` | Load when producing output for this workflow.

## Example 1 — From skill workflow

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

## Example 2 — Typical invocation

**Input:** "Run `project-orchestrator` for [concrete task]"

**Output:**
```
Invoked `project-orchestrator`.
Step 1: Read Project State
Step 2: Route the Request
Step 3: Plan and Present
Orchestration complete: [request summary]
```

---

See `SKILL.md` for hard rules, gotchas, and verification checklist.
