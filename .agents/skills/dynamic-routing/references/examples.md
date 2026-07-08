# Dynamic Routing — Examples

## Ex.1 — Decompose after failure

**Input:** Step S2 "apply migration" failed — relation already exists

**Output:**
```markdown
## Dynamic route — add-users-table / S2

Reflection:
- Hypothesis: migration partially applied in prior run [EXTRACTED: psql error duplicate table]
- Layer: environment
- Actionability: plan revision

Route chosen: decompose

Plan delta:
| at | step_id | from | to | reason |
|----|---------|------|-----|--------|
| 2026-07-05T12:00:00Z | S2 | pending | failed | duplicate table |
| 2026-07-05T12:01:00Z | S2 | failed | revised | split into check + apply |

New steps: S2.1 verify schema state, S2.2 apply missing columns only
Resume at: **S2.1**
```

## Ex.2 — Debug handoff

**Input:** S3 API test fails with 500 — stack trace in handler

**Output:**
```markdown
Route chosen: debug handoff
Handoff: debug-and-fix — reproduce 500 on POST /users
Plan paused at S3 (in-progress). Resume structured-planning after fix verified.
```

## Ex.3 — Escalate model tier (advisory — the human switches)

**Input:** Step S4 "implement date-filter" — same unit test failed twice on the
executing mid-tier model; second "fix" edited an unrelated helper.

**Output:**
```markdown
## Dynamic route — report-filters / S4

Reflection:
- Hypothesis: task exceeds executing model's reasoning band — repeated failed
  fixes + out-of-contract edit are model-selection tripwires, not a plan flaw
  [EXTRACTED: pytest failure x2, diff touched utils/format.py outside contract]
- Layer: code (executor capability), plan structure sound
- Actionability: tier escalation per model-selection

Route chosen: escalate model tier

ANNOUNCE: switch to high-mid (Sonnet-class) for S4 only — then WAIT.
Do NOT proceed on the current model; the harness cannot switch itself.
Revert the out-of-contract edit to utils/format.py before resuming (safe-change).

Plan delta:
| at | step_id | from | to | reason |
|----|---------|------|-----|--------|
| 2026-07-08T09:00:00Z | S4 | in-progress | paused | tier escalation announced |

Resume at: **S4** (after the human confirms the model switch)
```

**Why this works:** the tripwire is external and observable (failing test +
out-of-contract diff — never the model's self-report); the route pauses and
WAITS for the human switch instead of assuming the harness can change models;
the stray edit is reverted before resuming so the bad attempt leaves no
residue; tier escalation (who executes) is kept separate from path revision
(what to do) — the plan itself was fine, so no decompose/replan was needed.
