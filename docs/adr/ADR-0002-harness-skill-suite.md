# ADR-0002: Harness Skill Suite (3-skill split)

**Status:** Accepted  
**Date:** 2026-07-05  
**Context:** agent-loom bootstraps projects but lacked harness generation and self-improvement loops. 2026 research (AHE, Self-Harness, HarnessFix, Meta-Harness, RHO) converges on trace-driven evolution with regression gates.

## Decision

Add three skills:

1. `harness-generation` — seed minimal v0 (manifest, eval stub, governance)
2. `harness-evolution` — improve vN→vN+1 with ETCLOVG diagnosis + regression
3. `harness-engineering` — orchestrator routing bootstrap vs evolution

## Rationale

- Generation and evolution have different triggers, prerequisites, and failure modes — merging would exceed 200 lines or blur workflows.
- `agent-builder` designs topology; harness designs scaffold files — explicit non-overlap.
- Eval harness is hard prerequisite for evolution (`reality-check` alignment).

## Out of scope

- Model weight updates (SIA harness+weights path)
- Runtime harness products (UniHarness-style execution environments)
- Embedding external URLs in skill bodies

## Consequences

- `project-setup` Step 6c offers harness bootstrap after AGENTS.md save.
- `setup-evaluation` Step 3b adds harness checks for agent-chain paths.
- `eval-pipeline` documents harness regression pass@1 gate.
