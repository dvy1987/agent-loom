# Create Agent Prompt — Full Worked Examples

Skill: `create-agent-prompt` | Enriched from SKILL.md (improve-skills pass, SKIP_RESEARCH).

## Example 1 — Documented workflow

**Input:** Create a role prompt for a "Code Review Agent" in a parallel fan-out topology that receives code diffs and produces review comments.

**Output:**
```
ROLE: Code Review Agent — reviews code diffs for correctness, conventions, and test coverage.

RESPONSIBILITIES:
- Review each diff for bugs, logic errors, and convention violations
- Check that tests exist for new functionality
- Produce structured review comments with severity (critical/warning/nit)
- Does NOT fix code, refactor, or make changes — review only

SKILLS: [code-review-crsp]
TOOLS: [Read, Grep, Bash (for running tests)]

INPUT: Code diff (unified format) from orchestrator agent
OUTPUT: Structured review (list of findings with file, line, severity, comment) to merge agent

HANDOFF PROTOCOL:
- On success: Pass review to merge agent with verdict (approve/request-changes)
- On partial: Flag files that couldn't be reviewed (e.g., binary) to orchestrator

FAILURE BEHAVIOR:
- If diff is unparseable: report to orchestrator, do not guess
- Never approve without reviewing — if unsure, request-changes with explanation
```

## Example 2 — Step-by-step execution

**Input:** "Run `create-agent-prompt` on [concrete task]"

**Agent actions:**
1. Gather Context
2. Write Role Prompt
3. Validate
4. Return

**Impact Report shape:**
```
Agent prompt created for: [agent name]
Topology role: [role in topology]
Handoff: [to whom]
Failure behavior: defined
Ready to embed in: AGENTS.md / architecture spec
```

## Example 3 — Gotcha application

**Input:** Task hits a non-obvious edge case

**Apply:**
- Role prompts are NOT system prompts — they define behavior within a topology, not global identity.
- Avoid "be helpful" or "be thorough" — these are noise. Be specific about what the agent does.
- If the agent's boundary overlaps with another agent, the topology is wrong — flag it to agent-builder.
- 

---

See `SKILL.md` for hard rules and verification checklist.
