# Comparison: eval-pipeline vs china-qijizhifeng/agentic-harness-engineering (harness regression)

**Date:** 2026-07-05  
**Repo credibility:** 10/12 PASS  
**Code verified:** `agents/evolve_agent/evolve_prompt.md` — pass@1 objective, k-rollout eval, evidence quad, runs/ read-only

| Axis | agent-loom eval-pipeline | AHE harness eval | Winner |
|---|---|---|---|
| General LLM eval stack | 2/2 | 1/2 | ours |
| Harness pass@1 + k-rollouts | 0/2 | 2/2 | theirs |
| Dual-split acceptance | 0/2 | 2/2 | theirs |
| Manifest prediction telemetry | 0/2 | 2/2 | theirs |
| Stochastic aggregation | 0/2 | 2/2 | theirs |
| Pareto multi-objective | 0/2 | 1/2 | theirs |
| CI integration patterns | 2/2 | 1/2 | ours |
| **Total** | **4/12** | **11/12** | **MERGE (harness mode)** |

## Per-axis notes

**pass@1:** AHE optimizes single-attempt success with **k≥2 rollouts per task**; pass@1 = mean binary success over k×|D|. agent-loom had one-line gotcha only — no rollout spec or aggregation rule.

**Dual-split:** Self-Harness + AHE require held-in Δ ≥ 0 AND held-out Δ ≥ 0 with strict improvement — rejects trade-off edits where one split gains and the other regresses.

**Manifest telemetry:** AHE `change_manifest` tracks predicted fixes vs regressions; fix predictions ~5× random precision, regression predictions only ~2× — `risk_tasks` are low-trust, never skip held-out gate.

**Stochastic eval:** Under noisy tasks, repeat candidate evaluation and apply acceptance to **aggregated** pass counts — single lucky rollout must not promote.

## Verdict: MERGE (harness regression mode)

Keep eval-pipeline's three-layer stack for general systems. Add dedicated **harness regression** L3 invoked when `harness-evolution` Step 4 runs.

## Recommended actions

| P | Action | Target |
|---|--------|--------|
| P0 | New L3: k-rollouts, pass@1, dual-split, stochastic aggregation, manifest P/R | `eval-pipeline/references/harness-regression.md` |
| P1 | Pointer from SKILL.md resources + gotcha on trade-off trap | `eval-pipeline/SKILL.md` |
| P1 | Pareto frontier selection when optimizing accuracy × cost | `harness-engineering/references/routing.md` |
| — | Do **not** replace general eval workflow with harness-only gates | — |
