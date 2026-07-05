# Harness Regression Mode

Invoked when `harness-evolution` Step 4 runs. Distinct from general LLM eval pipelines.

## Metric: pass@1 with k-rollouts (AHE)

- Run **k ≥ 2** independent rollouts per task (default k=3 under noise).
- **pass@1** = mean binary success over all k × |D| attempts — not pass@k best-of.
- Report per-split: held-in, held-out separately.

## Dual-split acceptance (Self-Harness)

Promote candidate only if **all** hold:

| Rule | Condition |
|------|-----------|
| Held-in | Δ ≥ 0 vs parent harness |
| Held-out | Δ ≥ 0 vs parent harness |
| Strict gain | max(Δ) > 0 — not tie on both splits |

**Trade-off trap:** Reject edits where held-in gains but held-out regresses (or vice versa) even if total pass count rises.

## Stochastic aggregation

When tasks are noisy:
1. Repeat full candidate evaluation (same k per task).
2. Aggregate pass counts across repeats before applying dual-split rule.
3. Single lucky rollout must not promote.

## Manifest prediction telemetry (AHE)

Track per round in `change_manifest.json`:

| Field | Use |
|-------|-----|
| `predicted_impact.fixes` | Tasks expected to pass after edit |
| `predicted_impact.risk_tasks` | Tasks expected to regress — **low trust** (~2× random) |

After eval, log precision/recall separately for fix vs regression predictions. Do **not** skip held-out gate because regressions were "predicted."

## Regression suite gate (auto-harness adapted)

| Step | Check |
|------|-------|
| 0 | File guard — no edits outside `allowed_write_paths` |
| 1 | Suite `docs/harness/suite.json` pass rate ≥ threshold |
| 2 | Full held-out pass@1 ≥ best prior in `docs/harness/results.tsv` |
| 3 | Promote newly passing held-in tasks into suite (expand coverage) |

## Pareto selection (Meta-Harness)

When optimizing multiple objectives (accuracy × context-cost × latency):
- Return **frontier** of non-dominated candidates — not single scalar winner.
- Final held-out eval on frontier points only; proposer never sees held-out results.

## Label-free fallback (RHO)

Weaker evidence path — see `harness-evolution/references/evolution-loop.md`. Prefer this harness regression mode when labeled eval exists.
