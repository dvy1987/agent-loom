# Trace Schema

Append-only JSONL at `.agent-loom/traces/<run-id>.jsonl`. Git-ignore by default. Aligns step ids with `structured-planning` plans.

---

## Record shape

```json
{
  "run_id": "2026-07-05T10:00:00Z-fix-login",
  "step_id": "S2",
  "surface": "operational",
  "action": "tool:Shell",
  "input_ref": "npm test",
  "output_ref": "exit 1 — 3 failures",
  "error": "AssertionError: expected 200 got 500",
  "ts": "2026-07-05T10:01:23Z"
}
```

---

## Surfaces (AgentTrace model)

| Surface | Log what |
|---------|----------|
| **operational** | Tool calls, commands, exit codes, file reads/writes |
| **cognitive** | Plan decisions, reflections, route choices, hypotheses |
| **contextual** | Env facts, cwd, branch, versions (no secrets) |

---

## Append rules

1. One JSON object per line — no pretty-print in file.
2. Never block execution to log — append after step completes.
3. **No secrets** — store refs (`input_ref`, `output_ref`), not API keys or tokens.
4. Reuse `step_id` from active plan when `structured-planning` is running.
5. On error, set `error` field; still append operational record.

---

## Query

```bash
python3 .agents/skills/run-trace/scripts/trace_query.py .agent-loom/traces/<run-id>.jsonl timeline
python3 .agents/skills/run-trace/scripts/trace_query.py .agent-loom/traces/<run-id>.jsonl errors
```

---

## Git ignore

Add to consumer `.gitignore`:

```
.agent-loom/traces/
```
