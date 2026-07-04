# Agent Launcher — Full Worked Examples

Skill: `agent-launcher` | Load when producing output for this workflow.

## Example 1 — From skill workflow

**Input:** Architecture: proc-2026-04-11-012 (3 parallel agents: review-agent, security-agent, debt-agent). Platform: Ampcode. setup-evaluation: PASS. All prompt files present.

**Output:**
```
Preconditions: ✓ Arch spec ✓ setup-evaluation PASS ✓ All prompts present
Platform: Ampcode (Task tool)
Manifest written: docs/agents/runs/2026-04-11-review-pipeline-manifest.md

SPAWN SUBAGENTS:
Topology: parallel

Agent: review-agent
Role prompt: docs/agents/review-agent-prompt.md
Input: docs/handoffs/task-input.md
Output to: docs/handoffs/review-agent-output.md

[repeat for each agent in architecture spec]

Run all agents concurrently via Task tool. Wait for all outputs.
```

## Example 2 — Typical invocation

**Input:** "Run `agent-launcher` for [concrete task]"

**Output:**
```
Invoked `agent-launcher`.
Step 1: Precondition Check
Step 2: Platform Check
Step 3: Read Architecture Spec
Agents launched: [N]
```

---

See `SKILL.md` for hard rules, gotchas, and verification checklist.
