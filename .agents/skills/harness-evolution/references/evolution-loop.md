# Evolution Loop

## Consensus loop (2026 papers + repos)

```
execute tasks → capture traces → distill digest
→ diagnose ETCLOVG layer → propose K minimal edits
→ pre-validate → regression (held-in + held-out) → promote vN+1 | reject
```

## Loop ordering (AHE)

1. **Attribute** prior round's `change_manifest` — verdict lands in next round's evidence corpus.
2. **Rollback** rejected edits before new proposals.
3. **Distill** traces — summaries alone mislead (Meta-Harness ablation: scores-only 34.6 → full traces 50.0).

## Three observability pillars (AHE)

| Pillar | Implementation in agent-loom |
|--------|------------------------------|
| Component | `docs/harness/manifest.json` — git-tracked paths |
| Experience | `docs/harness/runs/iteration_NNN/` — distilled trace digest + raw archive |
| Decision | `change_manifest.json` — predicted impact verified next round |

## change_manifest.json fields

```json
{
  "round": 1,
  "candidates": [
    {
      "id": "cand-2",
      "layer": "Tooling",
      "files": ["docs/harness/tools.md"],
      "failure_evidence": "trace ids …",
      "root_cause": "tool schema missing required field",
      "targeted_fix": "add schema validation middleware",
      "predicted_impact": { "fixes": ["task-12"], "risk_tasks": ["task-03"] }
    }
  ],
  "accepted": "cand-2"
}
```

`risk_tasks` predictions are low-trust — never skip held-out gate.

## Proposer context (Self-Harness)

Include in every proposal round:
- **Passing behaviors to preserve** — not failure-only mining.
- **Summaries of previously rejected edits** — avoid repeated dead hypotheses.
- **Compatible same-round merge** — multiple candidates passing dual-split may merge into vN+1 in one iteration.

## Pre-validation (HarnessFix)

Before expensive held-out eval:
1. Scope conformance — files ⊆ `allowed_write_paths`.
2. Forbidden-resource check — no benchmark/oracle edits.
3. Syntax/static checks on edited harness artifacts.

## Interface validation (Meta-Harness)

Validate candidate harness contract (paths exist, eval interface callable) **before** task eval — discard invalid candidates without burning budget.

## Harness repair memory (HarnessFix)

Persist accepted AND rejected repairs:

| Rejection reason | Meaning |
|------------------|---------|
| `pre-validation failure` | Scope/syntax/forbidden artifact |
| `insufficient target improvement` | Dual-split failed |
| `excessive regression` | Held-out Δ < 0 |

Prevents re-proposing dead edits.

## auto-harness gate (adapted)

| Step | Check |
|------|-------|
| 0 | File guard — tracked files outside allowlist → reject |
| 1 | Regression suite `docs/harness/suite.json` ≥ threshold |
| 2 | Full held-out pass@1 ≥ best prior in `docs/harness/results.tsv` |
| 3 | Promote newly passing held-in tasks into suite |

Anti-cheat: held-out traces never saved to proposer context.

## metaharness outcomes

Map eval results to: `keep | discard | crash | timeout | no-change | scope-violation`.
`no-change` with zero file edits → do not promote.

## Filesystem artifact store

Every round archives under `docs/harness/runs/iteration_NNN/`:
- `input/` — harness snapshot evaluated
- `evolve/` — proposed edits
- `traces/` — distilled + optional raw
- `eval/` — pass/fail per task

Proposer navigates prior rounds via grep/read — not one monolithic prompt. At scale, add list/diff helpers for frontier runs (Meta-Harness navigation tax).

## RHO label-free fallback

When no labeled eval:
1. **DPP coreset** — kernel K = diag(r̃)·S·diag(r̃), default **θ=0.7** (balance difficulty × diversity).
2. **Dual diagnostics** — self-validation (within-trajectory) + self-consistency (cross-trajectory); both required.
3. Parallel rollouts (3× per task).
4. Pairwise self-preference among harness candidates.
5. Accept only if **mean_score > 0** vs prior (strictly beats baseline on average).

**Coreset failure modes:** difficulty-only (θ=1) clusters narrow region; diversity-only (θ=0) suboptimal; both can trail random — need both axes.

**Prerequisite:** trajectory reservoir — mine via `memory-handoff/references/harness-trajectory-mining.md`.

Still log promotion in manifest — weaker evidence than verifier regression.
