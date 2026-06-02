# Comparison: debug-and-fix vs addyosmani/debugging-and-error-recovery

**Date:** 2026-06-01  
**Note:** External `fixing-bugs` template cited in handoff; comparison uses agent-loom `debug-and-fix` only.

| Axis | agent-loom | addyosmani | Winner |
|---|---|---|---|
| Workflow specificity | 1/2 | 2/2 | theirs |
| Hard rules | 2/2 | 2/2 | tie |
| Gotchas | 2/2 | 2/2 | tie |
| Examples | 2/2 | 2/2 | tie |
| Verification | 1/2 | 2/2 | theirs |
| Anti-rationalization | 0/2 | 2/2 | theirs |
| **Total** | **8/12** | **12/12** | **MERGE BEST-OF-BOTH** |

## Per-axis notes

**Workflow specificity:** AO's six-step triage (Reproduce → Localize → Reduce → Fix root → Guard → Verify E2E) with bash recipes and `git bisect run`. Ours is Linear-aware and user-confirm-before-fix — strong for agent-loom workflows but less systematic for generic debugging.

**Hard rules:** Ours: present root cause before code, minimal diff, untrusted Linear snippets. AO: stop-the-line rule, no feature work past red tests. Both strong; different emphasis.

**Gotchas:** Ours: stale Linear, minified stack traces, shared root causes. AO: non-reproducible bugs (timing/env/state branches), instrumentation hygiene.

**Examples:** Both have two realistic narratives. Ours includes Linear HID-42 flow; AO includes symptom-vs-root-cause fix contrast.

**Verification:** AO checklist is explicit. Ours Output Format is good but not checkbox-gated.

**Anti-rationalization:** AO only.

## Verdict: MERGE BEST-OF-BOTH

Keep user confirmation gate, Linear MCP integration, and one-bug-at-a-time queue. Adopt AO triage structure and untrusted-error-output rules (AO has a dedicated section; we only mention Linear).

## Recommended actions

| P | Action | Target |
|---|--------|--------|
| P1 | Merge AO **Stop-the-Line** + six-step triage as primary workflow skeleton | `debug-and-fix/SKILL.md` |
| P1 | Add **Treat error output as untrusted data** (expand beyond Linear) | `debug-and-fix/SKILL.md` |
| P1 | Common Rationalizations table | `debug-and-fix/SKILL.md` |
| P2 | Non-reproducible bug decision tree → `references/non-repro-debug.md` | reference file |
| P2 | Post-fix verification checklist (specific test, full suite, build) | `debug-and-fix/SKILL.md` |
| P2 | **Guard:** require regression test after fix (AO Step 5) | `debug-and-fix/SKILL.md` Hard Rules |
| — | Do **not** create separate `debugging-and-error-recovery` skill — would collide with `debug-and-fix` | — |
