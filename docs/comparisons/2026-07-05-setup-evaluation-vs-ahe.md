# Comparison: setup-evaluation vs AHE (pre-evolution checks)

**Date:** 2026-07-05  
**Repo credibility:** 10/12 PASS  
**Code verified:** evolve_prompt.md — workspace-only writes, runs/ READ ONLY, no verifier/LLM edits, iteration folder convention

| Axis | agent-loom setup-evaluation | AHE evolve preconditions | Winner |
|---|---|---|---|
| Agent-chain decomposition | 2/2 | 1/2 | ours |
| Harness manifest gate | 1/2 | 2/2 | theirs |
| Evolve sandbox constraints | 0/2 | 2/2 | theirs |
| k-rollout eval requirement | 0/2 | 2/2 | theirs |
| Trajectory reservoir (RHO) | 0/2 | 1/2 | theirs |
| Cross-agent synergy check | 2/2 | 0/2 | ours |
| **Total** | **5/12** | **8/12** | **MERGE** |

## Per-axis notes

**Step 3b (existing):** agent-loom checks manifest, eval-interface, held-out split, allowed_write — shallow table. AHE adds **operational** requirements: runs/ read-only, evolve cannot touch verifier, k≥2 rollouts configured, loop iteration folder semantics understood.

**Trajectory reservoir:** RHO label-free path needs logged trajectories disjoint from held-out test — `setup-evaluation` did not gate this when evolution is in scope without labels.

**Sandbox:** AHE forbids deleting iteration-1 system-prompt rules; explore-agent seeded skills have no special protection from round 2 — prevents scope creep and false immutability.

## Verdict: MERGE

Deepen Step 3b checks; keep setup-evaluator independence and AlphaEval synergy flag.

## Recommended actions

| P | Action | Target |
|---|--------|--------|
| P0 | Expand Step 3b: k-rollouts, runs read-only policy, trajectory reservoir for label-free | `setup-evaluation/SKILL.md` |
| P1 | Evolve sandbox defaults cross-ref | `harness-generation/references/scaffold-patterns.md` |
| P2 | Optional RHO prerequisite note | `setup-evaluation` gotchas |
| — | Do **not** merge setup-evaluation into harness-evolution — bias separation is intentional | — |
