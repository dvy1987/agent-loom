# Experiment Runbook — Full Worked Examples

Skill: `experiment-runbook` | Enriched from SKILL.md (improve-skills pass, SKIP_RESEARCH).

## Example 1 — Step-by-step execution

**Input:** "Run `experiment-runbook` on [concrete task]"

**Agent actions:**
1. Read the Spec
2. Define Platform Binding
3. Define Assignment
4. Define Exposure Event
5. Wire Dashboards & Alerts
6. Ramp Plan
7. Pre-Launch QA
8. Rollback Procedure

**Impact Report shape:**
```
Runbook written: docs/experiments/runbooks/YYYY-MM-DD-<slug>-runbook.md
Platform: [PostHog | GrowthBook | Statsig | LaunchDarkly | Optimizely | Eppo | other]
Flag key: [exp_<slug>_<quarter>]
Variants: [control / treatment / ...]
Allocation: [50/50 | 90/10 holdout | ...]
Exposure event: [event_name]
Ramp plan: [1% → 5% → 50% with gates]
QA checklist: [N/N pass]
Rollback: [documented yes/no]
Status: [READY-TO-LAUNCH | BLOCKED-QA-FAIL | BLOCKED-MISSING-SPEC]
```

## Example 2 — Gotcha application

**Input:** Task hits a non-obvious edge case

**Apply:**
- **Exposure event must fire when the variant renders, not when the flag is fetched.** Server-side renders and async surfaces commonly log exposure before the variant actually loads — this guarantees SRM noise and unanalysable results.
- **`$feature_flag_called` is PostHog's exposure event.** Capturing a custom event without `$feature_flag` and `$feature_flag_response` properties means PostHog's experiment UI cannot match exposures to assignments.
- **Person-property assignment for B2B accounts is wrong.** Use group-property (account-level) — otherwise users on the same account land in different variants and contaminate the test.
- **Salt the hash and lock it.** A drifting salt re-randomises mid-test; the same user gets different variants on different sessions, destroying causal interpretation. PostHog does this for you; verify other vendors.

---

See `SKILL.md` for hard rules and verification checklist.
