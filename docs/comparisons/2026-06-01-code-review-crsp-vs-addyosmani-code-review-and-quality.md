# Comparison: code-review-crsp vs addyosmani/code-review-and-quality

**Date:** 2026-06-01

| Axis | agent-loom | addyosmani | Winner |
|---|---|---|---|
| Workflow specificity | 2/2 | 2/2 | tie |
| Hard rules | 2/2 | 2/2 | tie |
| Gotchas | 2/2 | 2/2 | tie |
| Examples | 2/2 | 1/2 | ours |
| Verification | 1/2 | 2/2 | theirs |
| Anti-rationalization | 0/2 | 2/2 | theirs |
| **Total** | **9/12** | **11/12** | **MERGE BEST-OF-BOTH** |

## Per-axis notes

**Workflow specificity:** Ours: git-scope detection (`diff`, `--cached`, branch). AO: five-axis review + tests-first ordering. Both imperative.

**Hard rules:** Ours: cite lines, severity classes, advisory until user approves fixes. AO: continuous-improvement approval standard, no "fix later", severity prefixes (Critical/Nit/Optional/FYI).

**Gotchas:** Ours: empty diff, rename false positives, tests that always pass. AO: dead code hygiene, change sizing (~100/300/1000 lines), dependency discipline.

**Examples:** Ours has two full review outputs with file links. AO leans on a markdown checklist template.

**Verification:** AO's review checklist + "verify the verification" step is stronger for merge gates.

**Anti-rationalization:** AO only ("LGTM without evidence", AI code needs more scrutiny).

## Verdict: MERGE BEST-OF-BOTH

Keep our explicit trigger guard ("review for context" ≠ formal review) and numbered finding format. Adopt AO's five-axis framing, comment severity prefixes, change-sizing, dead-code ask, and multi-model review pattern.

## Recommended actions

| P | Action | Target |
|---|--------|--------|
| P1 | Add **Five-Axis Review** section (correctness, readability, architecture, security, performance) | `code-review-crsp/SKILL.md` |
| P1 | Comment prefix table: Critical / Nit / Optional / FYI | `code-review-crsp/SKILL.md` |
| P1 | Common Rationalizations + Red Flags | `code-review-crsp/SKILL.md` |
| P2 | Change sizing guidelines + split strategies | `references/review-change-sizing.md` |
| P2 | Dead code hygiene: list orphans, ask before delete | `code-review-crsp/SKILL.md` Step 4 |
| P2 | "Review tests first" as explicit Step 2b | `code-review-crsp/SKILL.md` |
| P3 | Multi-model review pattern (optional, user-triggered) | `code-review-crsp/SKILL.md` |
| P2 | Cross-link `app-security-hardening` when built (Phase 2) | security axis |
