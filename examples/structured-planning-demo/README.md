# Structured Planning Demo

**Skill:** `structured-planning` + `dynamic-routing`

## What it shows

Plan-ahead decomposition with stable step IDs and plan file at `.agent-loom/plans/`.

## Try it

```text
Use structured-planning to add input validation to examples/seed/calc/calc.py (validate types on add and divide)
```

## Expected output

- Plan file: `.agent-loom/plans/calc-validation.md` with S1, S2, S3
- `plan_lint.py` passes
- One step executed per cycle (commit-one)
- On test failure → `dynamic-routing` revises plan

## Fixture

`examples/seed/calc/`
