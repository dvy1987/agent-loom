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
