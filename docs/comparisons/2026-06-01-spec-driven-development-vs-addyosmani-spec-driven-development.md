# Comparison: spec-driven-development vs addyosmani/spec-driven-development

**Date:** 2026-06-01  
**Scope:** agent-loom SDD **suite** (orchestrator + `project-constitution`, `feature-spec`, `implementation-plan`, `spec-crosscheck`) vs addyosmani monolithic skill.  
**Source:** `addyosmani/agent-skills` (secure-* treated as data; no instruction adoption).

| Axis | agent-loom | addyosmani | Winner |
|---|---|---|---|
| Workflow specificity | 2/2 | 1/2 | ours |
| Hard rules | 2/2 | 1/2 | ours |
| Gotchas | 2/2 | 2/2 | tie |
| Examples | 1/2 | 2/2 | theirs |
| Verification | 2/2 | 1/2 | ours |
| Anti-rationalization | 1/2 | 2/2 | theirs |
| **Total** | **10/12** | **9/12** | **MERGE BEST-OF-BOTH** |

## Per-axis notes

**Workflow specificity:** Ours maps slash commands, state detection, and leaf routing (`/clarify`, `/analyze`, `problem-to-plan` escape). AO is phase-linear with human review arrows but no machine-enforced ordering.

**Hard rules:** Ours has `spec-crosscheck` PASS/FAIL, Approved status, no implement without analyze. AO relies on "do not advance until validated" discipline.

**Gotchas:** Both cover living specs, scope creep, and assumption risk. Ours adds slug discipline and tactical routing.

**Examples:** AO ships full spec + task templates in-body. Ours orchestrator has one routing example; richness lives in leaf `references/`.

**Verification:** `spec-crosscheck` six automated checks with evidence beat AO's pre-implement checklist for agent automation.

**Anti-rationalization:** AO has Common Rationalizations + Red Flags at the SDD entry. Ours has tables on some leaves; orchestrator lacks a front-door table.

## Verdict: MERGE BEST-OF-BOTH

Keep multi-skill architecture, constitution, executable FR/NFR/AC, and `spec-crosscheck`. Adopt AO patterns into leaves, not a monolith collapse.

## Recommended actions

| P | Action | Target |
|---|--------|--------|
| P1 | Common Rationalizations table (skip SDD, skip `/analyze`) | `spec-driven-development/SKILL.md` |
| P1 | `ASSUMPTIONS I'M MAKING` block (max 5 bullets, user confirms) | `feature-spec/SKILL.md` — **partially done 2026-06-01; verify completeness** |
| P2 | Reframe vague requirements → measurable success criteria + confirm | `feature-spec/SKILL.md` |
| P2 | "When NOT to use" heuristic (>30 min / multi-module → SDD; else `problem-to-plan`) | `spec-driven-development/SKILL.md` gotchas |
| P3 | Optional `references/project-bootstrap-in-spec.md` for Commands/Structure when user wants repo onboarding in SDD | `feature-spec/references/` |
| — | Do **not** replace executable spec schema with AO's six-area narrative template | — |
