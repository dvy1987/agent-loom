# Create Agent Prompt — Full Worked Examples

Skill: `create-agent-prompt` | Load when producing output for this workflow.

## Example 1 — From skill workflow

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

## Example 2 — Typical invocation

**Input:** "Run `create-agent-prompt` for [concrete task]"

**Output:**
```
Invoked `create-agent-prompt`.
Step 1: Gather Context
Step 2: Write Role Prompt
Step 3: Validate
Agent prompt created for: [agent name]
```

---

See `SKILL.md` for hard rules, gotchas, and verification checklist.
