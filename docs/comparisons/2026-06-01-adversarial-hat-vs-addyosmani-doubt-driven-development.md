# Comparison: adversarial-hat vs addyosmani/doubt-driven-development

**Date:** 2026-06-01  
**Note:** Phase 1 Insight #7 already ported fresh-context + Doubt Theater into `adversarial-hat`.

| Axis | agent-loom | addyosmani | Winner |
|---|---|---|---|
| Workflow specificity | 2/2 | 2/2 | tie |
| Hard rules | 2/2 | 2/2 | tie |
| Gotchas | 2/2 | 2/2 | tie |
| Examples | 1/2 | 2/2 | theirs |
| Verification | 1/2 | 2/2 | theirs |
| Anti-rationalization | 2/2 | 2/2 | tie |
| **Total** | **10/12** | **12/12** | **MERGE BEST-OF-BOTH (extend, don't duplicate)** |

## Per-axis notes

**Workflow specificity:** AO: operational **in-flight** loop (CLAIM → EXTRACT → DOUBT → RECONCILE → STOP) for non-trivial code decisions. Ours: **document-level** three-phase red team (Diagnostic → Creative → Challenge) + fresh-context escalation.

**Hard rules:** AO defines "non-trivial" precisely; 3-cycle bound; no persona nesting. Ours: cite reasons, constructive end, stakes calibration, Doubt Theater detection.

**Gotchas:** Overlap on doubt theater, rubber-stamping reviewer, validating prompts. AO adds cross-model CLI offer every interactive cycle.

**Examples:** AO includes adversarial prompt verbatim + stdin-safe CLI shapes. Ours has report template but fewer copy-paste prompts.

**Verification:** AO has a copyable doubt-cycle checklist. Ours verification is implicit in report format.

**Anti-rationalization:** Both strong; AO table is longer; ours integrates with `deep-thinking` routing.

## Verdict: MERGE BEST-OF-BOTH — do **not** add `doubt-driven-development` skill

Would collide with `adversarial-hat` triggers ("challenge assumptions", "stress test"). Extend existing skill instead.

**Division of labour:**
- **Documents / strategy / plans** → `adversarial-hat` (existing three phases)
- **In-flight code / architecture decisions** → `adversarial-hat` Fresh-Context mode + AO CLAIM/EXTRACT/DOUBT loop
- **Post-hoc PR review** → `code-review-crsp` (complementary, per AO)

## Recommended actions

| P | Action | Target |
|---|--------|--------|
| P1 | Add **In-flight doubt loop** section with AO checklist (CLAIM→STOP) for code decisions | `adversarial-hat/SKILL.md` |
| P1 | Copyable adversarial prompt block | `adversarial-hat/references/adversarial-prompt.md` |
| P2 | Non-trivial decision definition (bullet list from AO) | `adversarial-hat/SKILL.md` |
| P2 | Cross-model offer protocol (interactive only; announce skip in CI) | `adversarial-hat/SKILL.md` Fresh-Context section |
| P2 | Interaction table: TDD RED = doubt for behavioral claims | `adversarial-hat/SKILL.md` |
| — | Do **not** create `doubt-driven-development` skill | — |
