# Comparison: implementation-plan + problem-to-plan + process-decomposer vs addyosmani/planning-and-task-breakdown

**Date:** 2026-06-01  
**Asymmetric pair:** agent-loom **three-skill pipeline** vs AO single planning skill.

| Axis | agent-loom | addyosmani | Winner |
|---|---|---|---|
| Workflow specificity | 2/2 | 2/2 | tie |
| Hard rules | 2/2 | 1/2 | ours |
| Gotchas | 2/2 | 1/2 | ours |
| Examples | 1/2 | 2/2 | theirs |
| Verification | 2/2 | 2/2 | tie |
| Anti-rationalization | 0/2 | 2/2 | theirs |
| **Total** | **9/12** | **10/12** | **KEEP OURS + MERGE patterns** |

## Per-axis notes

**Workflow specificity:** AO: plan mode → dependency graph → vertical slices → task template → checkpoints. Ours: `process-decomposer` triage (single-skill / skill-chain / agent-chain / problem-to-plan) → `implementation-plan` with FR traceability → `problem-to-plan` for tactical triple deliverable (spec + plan + TODO.md).

**Hard rules:** Ours requires Approved feature-spec, constitution C-N traceability, `spec-crosscheck` handoff — stronger for agent-loom's SDD ecosystem. AO: "human reviews plan" without machine gate.

**Gotchas:** Ours: AlphaEval synergy-blindness, process registry reuse, plan≠PRD. AO: task sizing XS–XL, "and" in title = two tasks.

**Examples:** AO ships full plan markdown template in-body. Ours references `plan-schemas.md` — less copy-paste friendly for agents.

**Verification:** Tie — AO per-task verify lines; ours `spec-crosscheck` + memory checkpoint.

**Anti-rationalization:** AO only.

## Verdict: KEEP OURS + MERGE BEST-OF-BOTH

Our decomposition model is **strictly better** for this repo's meta-orchestration goals. AO contributes task-writing craft and vertical-slice emphasis missing from terse plan steps.

## Recommended actions

| P | Action | Target |
|---|--------|--------|
| P1 | Common Rationalizations on planning | `implementation-plan/SKILL.md` |
| P1 | Embed AO **task template** (Description, AC, Verify, Dependencies, Files, Scope) | `implementation-plan/references/plan-schemas.md` |
| P2 | Explicit **vertical slice** guidance + anti-horizontal-slicing example | `implementation-plan/SKILL.md` |
| P2 | Task sizing XS–XL table from AO | `implementation-plan/references/plan-schemas.md` |
| P2 | Checkpoint blocks every 2–3 tasks | `implementation-plan/SKILL.md` Step 3 |
| P3 | `problem-to-plan` TODO tasks inherit AO verify line format | `problem-to-plan/SKILL.md` |
| — | Do **not** add `planning-and-task-breakdown` skill | — |
