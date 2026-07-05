# Comparison: memory-handoff vs wbopan/retro-harness (session transcript mining)

**Date:** 2026-07-05  
**Repo credibility:** 7/12 BORDERLINE PASS  
**Code verified:** `src/rho/loop.py` — 3× solve per task, trajectory store, candidate pool serialization, mean_score acceptance

| Axis | agent-loom memory-handoff | retro-harness RHO | Winner |
|---|---|---|---|
| Human-readable continuity | 2/2 | 0/2 | ours |
| Secret / PII hygiene | 2/2 | 1/2 | ours |
| Trajectory reservoir for harness | 0/2 | 2/2 | theirs |
| Multi-rollout capture | 0/2 | 2/2 | theirs |
| Label-free harness path | 0/2 | 2/2 | theirs |
| Knowledge graph sync | 2/2 | 0/2 | ours |
| **Total** | **6/12** | **7/12** | **PARTIAL MERGE** |

## Per-axis notes

**Handoff purpose:** memory-handoff writes ≤80-line summaries for next agent — explicitly **no raw transcripts**. retro-harness stores full `Trajectory` objects for optimize/eval loops.

**RHO path:** When no labeled benchmark exists, `harness-evolution` can use DPP coreset + self-preference — needs a **trajectory reservoir** mined from past sessions. Handoffs are the ingestion surface, not the storage format.

**3× rollouts:** retro-harness `run_round` solves each task 3 times before optimize — enables self-consistency diagnostics. agent-loom should **distill** failure patterns into `docs/harness/runs/` digests, not persist raw chat logs in handoff files.

## Verdict: PARTIAL MERGE

Keep handoff brevity and no-raw-transcript rule. Add optional **harness trajectory mining** workflow: distill session failures into structured trace digests for RHO fallback.

## Recommended actions

| P | Action | Target |
|---|--------|--------|
| P0 | New L3: distill failures → trace digest for harness runs/ | `memory-handoff/references/harness-trajectory-mining.md` |
| P1 | Optional Step 9 in workflow when harness-evolution queued | `memory-handoff/SKILL.md` |
| P1 | Cross-link RHO prerequisites | `harness-evolution/references/evolution-loop.md` |
| — | Do **not** store raw transcripts in handoff files | — |
