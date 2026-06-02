# Comparison: test-driven-development vs addyosmani/test-driven-development

**Date:** 2026-06-01

| Axis | agent-loom | addyosmani | Winner |
|---|---|---|---|
| Workflow specificity | 1/2 | 2/2 | theirs |
| Hard rules | 2/2 | 2/2 | tie |
| Gotchas | 2/2 | 2/2 | tie |
| Examples | 1/2 | 2/2 | theirs |
| Verification | 1/2 | 2/2 | theirs |
| Anti-rationalization | 0/2 | 2/2 | theirs |
| **Total** | **7/12** | **12/12** | **MERGE BEST-OF-BOTH** |

## Per-axis notes

**Workflow specificity:** AO names concrete commands (`npm test -- --grep`), Prove-It Pattern, test pyramid, bisection-adjacent sizing. Ours has Red-Green-Refactor steps but fewer shell-level imperatives.

**Hard rules:** Both enforce test-before-code. Ours adds SKILL-OUTPUTS logging; AO adds "don't re-run tests on unchanged code."

**Gotchas:** Ours targets **agent failure modes** (skip Red, test the framework, giant tests). AO targets **engineering craft** (DAMP over DRY, mock preference order, state vs interaction testing). Complementary.

**Examples:** AO has multiple full TypeScript cycles (createTask, completeTask bug). Ours has one domain-specific Python walkthrough in XML — good but single-domain.

**Verification:** AO ends with a checkbox list tied to `npm test`. Ours has Impact Report prose — less gate-like.

**Anti-rationalization:** AO has full Common Rationalizations + Red Flags. Ours has none.

## Verdict: MERGE BEST-OF-BOTH

Keep our agent-specific gotchas and PRD/plan integration. Adopt AO's craft depth without bloating past 200 lines — use `references/tdd-patterns.md`.

## Recommended actions

| P | Action | Target |
|---|--------|--------|
| P1 | Add Common Rationalizations + Red Flags (6–8 rows) | `test-driven-development/SKILL.md` |
| P1 | Add **Prove-It Pattern** section (repro test before bug fix) | `test-driven-development/SKILL.md` |
| P2 | Extract to `references/tdd-patterns.md`: test pyramid, DAMP, mock preference order, state-not-interactions | new reference file |
| P2 | Verification checklist with explicit test command placeholders | `test-driven-development/SKILL.md` |
| P3 | Cross-link `browser-testing-with-devtools` when UI in scope (Phase 2 gap) | `test-driven-development/SKILL.md` |
| — | Do **not** duplicate entire AO skill body — split via `split-skill` if >200 lines | — |
