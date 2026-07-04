# Agent Builder — Full Worked Examples

Skill: `agent-builder` | Load when producing output for this workflow.

## Example 1 — From skill workflow

**Input:** Design execution for process proc-2026-04-10-007 (3 sequential steps, no parallelism)

**Output:**
```
Process: 3 steps, all sequential, no specialization.
Structure: **Single agent** with ordered skill stack.

Agent: Feature Builder
- Skills: [brainstorming, prd-writing, implementation-plan]
- Tools: [Read, Write, Bash]
- Flow: brainstorming -> prd-writing -> implementation-plan (sequential)

Generating role prompt via create-agent-prompt...
Architecture spec saved to: docs/architecture/2026-04-10-feature-builder-arch.md
```

## Example 2 — From skill workflow

**Input:** Design execution for process proc-2026-04-10-012 (5 steps, 3 parallel)

**Output:**
```
Process: 5 steps, 3 can run in parallel (code-review, security-audit, debt-check).
Structure: **Multi-agent parallel fan-out**.

Topology: Orchestrator -> [Review Agent, Security Agent, Debt Agent] -> Merge Agent
[Defining boundaries, generating role prompts for each...]

Architecture spec saved to: docs/architecture/2026-04-10-review-pipeline-arch.md
Running setup-evaluation before handoff to project-orchestrator.
```

---

See `SKILL.md` for hard rules, gotchas, and verification checklist.
