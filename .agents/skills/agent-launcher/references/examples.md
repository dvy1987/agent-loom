# Agent Launcher — Full Worked Examples

Skill: `agent-launcher` | Enriched from SKILL.md (improve-skills pass, SKIP_RESEARCH).

## Example 1 — Documented workflow

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

## Example 2 — Step-by-step execution

**Input:** "Run `agent-launcher` on [concrete task]"

**Agent actions:**
1. Precondition Check
2. Platform Check
3. Read Architecture Spec
4. Write Launch Manifest
5. Spawn Instructions
6. Monitor and Hand Off

**Impact Report shape:**
```
Agents launched: [N]
Platform: Claude Code / Ampcode (Task tool native)
Topology: sequential | parallel | hierarchical
Manifest: docs/agents/runs/YYYY-MM-DD-<slug>-manifest.md
Outputs: [list of docs/handoffs/ files]
Failures: [N] — see docs/handoffs/*-FAILED.md
Next: project-orchestrator (synthesis)
```

## Example 3 — Gotcha application

**Input:** Task hits a non-obvious edge case

**Apply:**
- Parallel agents must be truly independent — if Agent B needs Agent A's
- Sequential agents must chain outputs explicitly — never assume an agent
- Prompt files must exist on disk before spawning — in-memory prompts do
- The launch manifest is the audit trail — never skip it even for two-agent runs.

---

See `SKILL.md` for hard rules and verification checklist.
