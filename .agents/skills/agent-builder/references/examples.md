# Agent Builder — Full Worked Examples

Skill: `agent-builder` | Enriched from SKILL.md (improve-skills pass, SKIP_RESEARCH).

## Example 1 — Documented workflow

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

## Example 2 — Documented workflow

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

## Example 3 — Step-by-step execution

**Input:** "Run `agent-builder` on [concrete task]"

**Agent actions:**
1. Read Process Entry
2. Decide Structure
3. Design Multi-Agent Topology
4. Write Architecture Spec
5. Hand Off

**Impact Report shape:**
```
Architecture designed for: [task]
Structure: single-agent | multi-agent-sequential | multi-agent-parallel | multi-agent-hierarchical
Agents defined: [N]
Architecture spec: docs/architecture/YYYY-MM-DD-<slug>-arch.md
Process entry linked: [proc-ID]
Next: setup-evaluation (if agent-chain) | project-orchestrator
```

## Example 4 — Gotcha application

**Input:** Task hits a non-obvious edge case

**Apply:**
- "Single agent" is not "no agent" — a single agent still needs a role prompt and skill stack.
- Platform constraints matter — check if the platform supports parallel agents before designing fan-out.
- **Scaffold choice is a first-order performance driver.** The same model varies 11+ points across scaffolds (e.g., Opus 4.6: 64.41 on Claude Code vs 53.45 on Codex). When designing architectures, consider scaffold/platform search behavior, retry strategies, and persistence characteristics — not just model capability (AlphaEval 2026, credibility 8/12).
- **When agents work on related outputs, design cross-agent validation checkpoints.** Independent optimization across agent boundaries produces globally suboptimal results — 26% cost overruns documented in procurement tasks where agents optimized components independently instead of jointly (AlphaEval 2026, credibility 8/12).

---

See `SKILL.md` for hard rules and verification checklist.
