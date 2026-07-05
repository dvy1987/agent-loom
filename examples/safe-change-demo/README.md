# Safe Change Demo

**Skill:** `safe-change` + `dependency-mapping`

## What it shows

Verified single edit with git snapshot and auto-revert on test failure.

## Try it

```text
Use safe-change to add a zero guard to divide() in examples/seed/calc/calc.py
```

## Expected output

- Impact report (callers: test_calc.py)
- verify: `python3 -m pytest -q` → pass
- Outcome: **KEPT**
- Suggested commit: `fix: guard divide against zero divisor`

## Fixture

`examples/seed/calc/` — offline, no credentials.
