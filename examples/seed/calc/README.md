# Calc seed — quickstart fixture

Minimal Python package for `quickstart` and `safe-change` demos. No external deps.

## Run tests

```bash
cd examples/seed/calc
python3 -m pytest -q
```

Expected before fix: `test_divide` may pass; quickstart adds zero-guard so `divide(1,0)` raises `ZeroDivisionError` with clear behavior.

## Demo task

Ask your agent: **"Use safe-change to add a zero guard to `divide` in examples/seed/calc/calc.py"**

Expected: impact report → edit → pytest pass → kept change.
