# Calc seed — quickstart fixture

Minimal Python package for `quickstart` and `safe-change` demos. No external deps.

## Run tests

```bash
cd examples/seed/calc
python3 -m pytest -q
```

Or from repo root (verify.sh uses the same discovery):

```bash
bash .agents/skills/safe-change/scripts/verify.sh examples/seed/calc
```

## Red → green demo

**Before fix:** `test_divide_by_zero_raises_explicit_message` **fails** — bare `a/b` raises a generic `ZeroDivisionError`, not the required message.

**After fix:** add explicit guard:

```python
if b == 0:
    raise ZeroDivisionError("divisor must be non-zero")
```

All tests pass. A sloppy guard (`return 0`) still **fails** the message assertion.

## Demo task

Ask your agent:

```text
Use safe-change to add a zero guard to divide() in examples/seed/calc/calc.py
```

Expected: impact report → edit → `verify.sh examples/seed/calc` → **KEPT**.

## Optional — see auto-revert

1. Apply a bad edit (e.g. `return 0` when `b == 0`).
2. Run `bash .agents/skills/safe-change/scripts/verify.sh examples/seed/calc` → **fail**.
3. `git restore examples/seed/calc/calc.py` → re-apply correct guard.
