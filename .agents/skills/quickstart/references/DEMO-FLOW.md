# Quickstart Demo Flow (~60s active + agent time)

## Prerequisites

- agent-loom installed (`bash install.sh`)
- Python 3.11+
- `pytest` (`pip install pytest` if needed)

## Steps

1. Open agent in agent-loom repo (or consumer project with skills installed).

2. Prompt:
   ```
   Run the agent-loom quickstart — use safe-change to add a zero guard to divide() in examples/seed/calc/calc.py
   ```

3. Agent should:
   - Run `dependency-mapping` on `divide`
   - Snapshot git state
   - Confirm **red**: `bash .agents/skills/safe-change/scripts/verify.sh examples/seed/calc` fails on `test_divide_by_zero_raises_explicit_message`
   - Add: `if b == 0: raise ZeroDivisionError("divisor must be non-zero")`
   - Re-run verify → pass → report **KEPT**

4. Confirm:
   ```bash
   cd examples/seed/calc && python3 -m pytest -q
   ```

## Idempotent re-run

If guard already exists, agent reports "already done" + green tests.

## What to say after

> You just ran the library's verified edit loop — map impact, one change, test, keep or revert.
