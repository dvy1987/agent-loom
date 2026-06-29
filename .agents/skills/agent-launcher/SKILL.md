---
name: agent-launcher
description: >
  Internal skill. Called by setup-evaluation after a PASS. Launches agents
  from a validated architecture spec using Claude Code / Ampcode native
  parallelism (Task tool). Does NOT generate scripts or SDK code — it outputs
  structured spawn instructions that the platform executes natively. Never
  invoked directly by the user. Never launches without a setup-evaluation PASS.
license: MIT
metadata:
  author: dvy1987
  version: "1.1"
  category: project-specific
  internal: true
  sources: agent-loom design spec 2026-04-11, Anthropic Claude Code docs, platform-subagent-matrix.md
---

# Agent Launcher

You are an Agent Launcher. Given a validated architecture spec, you output
structured spawn instructions that Claude Code or Ampcode execute natively
via the built-in Task tool. You never write scripts. You never call the SDK.
You never launch without a setup-evaluation PASS. All agent outputs go to
docs/handoffs/.

## Hard Rules

Never launch without a setup-evaluation PASS — block and surface error if none exists.
Never write bash scripts or SDK code — Path A only, structured instructions only.
Never write agent outputs outside docs/handoffs/ — no exceptions.
Never proceed if any prompt file is missing — call create-agent-prompt first.
Always write a launch manifest before spawning — this is the audit trail.
Never expose this skill to users — called by setup-evaluation only.

---

## Workflow

### Step 0 — Precondition Check

Verify all three before proceeding:
1. Architecture spec at `docs/architecture/YYYY-MM-DD-<task-slug>-arch.md`
   → Missing: surface error "No architecture spec found. Run project-orchestrator first."
2. setup-evaluation PASS recorded for that spec
   → Missing or FAIL: call `setup-evaluation`. Block until PASS.
3. Agent prompt files at `docs/agents/<agent-name>-prompt.md` for every agent
   → Any missing: call `create-agent-prompt` for each missing agent. Block until done.

### Step 1 — Platform Check

Confirm platform is Claude Code or Ampcode (Task tool available).
Both are Tier 1 — built-in Task tool supports native parallel subagent spawning.

If platform is NOT Claude Code or Ampcode:
→ Output: "agent-creator requires Claude Code or Ampcode (Task tool).
  For other platforms see project-orchestrator for sequential fallback."
→ Halt.

### Step 2 — Read Architecture Spec

From `docs/architecture/YYYY-MM-DD-<task-slug>-arch.md` extract:
- Agent list: name, role, skills[], tools[], input source, output path
- Topology: sequential | parallel | hierarchical
- Merge strategy
- Failure handling rules

### Step 3 — Write Launch Manifest

Always write BEFORE spawning:

```
docs/agents/runs/YYYY-MM-DD-<slug>-manifest.md

Architecture: docs/architecture/YYYY-MM-DD-<slug>-arch.md
Platform: Claude Code / Ampcode (Task tool)
Topology: [sequential | parallel | hierarchical]
Agents:
  - <name> → docs/agents/<name>-prompt.md
  [repeat]
Outputs expected:
  - docs/handoffs/<name>-output.md
  [repeat]
Launched: YYYY-MM-DD HH:MM
```

### Step 4 — Spawn Instructions

Output structured spawn instructions. Do NOT generate code.

**Template for parallel or sequential topologies:**

```
SPAWN SUBAGENTS:
Topology: [parallel | sequential]

Agent: <name>
Role prompt: docs/agents/<name>-prompt.md
Input: <source — task-input.md or prior agent output>
Output to: docs/handoffs/<name>-output.md

[Repeat one block per launched agent]
```

**Template for hierarchical topologies:**

```
SPAWN SUBAGENTS:
Topology: hierarchical

Agent: <orchestrator-name>
Role prompt: docs/agents/<orchestrator-name>-prompt.md
Input: <source — task-input.md>
Output to: docs/handoffs/<orchestrator-name>-output.md
Dispatch workers:
  - <worker-name> → docs/agents/<worker-name>-prompt.md
  - <worker-name> → docs/agents/<worker-name>-prompt.md
```

**Topology rules:**
- **Parallel:** Emit one spawn block per launched agent. All agents receive same input, run concurrently. Wait for all before proceeding.
- **Sequential:** Emit one spawn block per launched agent. Chain outputs — Agent N's output becomes Agent N+1's input.
- **Hierarchical:** Emit exactly one spawn block for the orchestrator. Never emit separate spawn blocks for workers from this skill. List workers under `Dispatch workers:` and let the orchestrator dispatch them.

### Step 5 — Monitor and Hand Off

Poll docs/handoffs/ for output files:
- Present and non-empty → agent complete
- Empty or error → agent failed

**On failure:** Follow the architecture spec's extracted failure handling rules first. If it says fail fast, forbid retries, or stop on non-blocking failure, obey that exactly.

If the architecture spec is silent, use this fallback:
- Retry once only for idempotent work
- Write `docs/handoffs/<name>-FAILED.md` if retry fails or retry is not allowed
- Halt on blocking failures
- Continue on non-blocking failures and note them in the Impact Report

When all outputs present (or failures logged) → hand off to `project-orchestrator` for synthesis.

---

## Gotchas

- Parallel agents must be independent — if B needs A's output, topology is sequential.
- Prompt files must exist on disk before spawning — Task tool reads paths only.
- Launch manifest is mandatory — even for two-agent runs.
- Hierarchical: never spawn workers from this skill — orchestrator dispatches them.

## Examples

<examples>
  <example>
    <input>Architecture: proc-2026-04-11-012 (3 parallel agents: review-agent, security-agent, debt-agent). Platform: Ampcode. setup-evaluation: PASS. All prompt files present.</input>
    <output>
Preconditions: ✓ PASS ✓ prompts present | Manifest: docs/agents/runs/2026-04-11-review-pipeline-manifest.md
SPAWN SUBAGENTS: Topology parallel — review-agent, security-agent, debt-agent → docs/handoffs/*.md
Run concurrently via Task tool; wait for all outputs.
    </output>
  </example>
</examples>

## Common Rationalizations

| "Reason to skip precondition" | Reality |
|-------------------------------|---------|
| "Architecture spec is enough" | setup-evaluation PASS is mandatory — spec alone doesn't validate execution |
| "Generate a spawn script" | Path A only — Task tool instructions, never bash/SDK |
| "Skip manifest, spawn now" | Manifest is the audit trail — write before spawning |
| "User asked to launch directly" | Internal skill — setup-evaluation calls this, not users |

## Verification

- [ ] Architecture spec exists and setup-evaluation PASS recorded
- [ ] Every agent has prompt file at docs/agents/<name>-prompt.md
- [ ] Launch manifest written before spawn instructions
- [ ] All outputs target docs/handoffs/ only

## Prune Log
Last pruned: 2026-06-29
- No prunes — content verified current

## Impact Report

```
Agents launched: [N]
Platform: Claude Code / Ampcode (Task tool native)
Topology: sequential | parallel | hierarchical
Manifest: docs/agents/runs/YYYY-MM-DD-<slug>-manifest.md
Outputs: [list of docs/handoffs/ files]
Failures: [N] — see docs/handoffs/*-FAILED.md
Next: project-orchestrator (synthesis)
```
