# Safe Change Demo

**Skill:** `safe-change` + `dependency-mapping`

## What it shows

Verified single edit with git snapshot and auto-revert on test failure.

## Try it

```text
Use safe-change to add a zero guard to divide() in examples/seed/calc/calc.py
```

## Expected output

- Impact report (callers: `test_calc.py`)
- Verify: `bash .agents/skills/safe-change/scripts/verify.sh examples/seed/calc` → pass
- Outcome: **KEPT**
- Suggested commit: `fix: guard divide against zero divisor`

**Before the fix:** `test_divide_by_zero_raises_explicit_message` fails (red). After the explicit guard, all tests pass (green).

## Optional — auto-revert loop

1. Deliberately break the guard (`return 0` when `b == 0`).
2. Run verify → **fail** → `git restore` on `calc.py`.
3. Re-apply the correct `raise ZeroDivisionError("divisor must be non-zero")`.

## Fixture

`examples/seed/calc/` — offline, no credentials.
