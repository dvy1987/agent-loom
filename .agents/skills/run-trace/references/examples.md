# Run Trace — Examples

## Ex.1 — Operational + cognitive

```jsonl
{"run_id":"2026-07-05T10:00:00Z-api","step_id":"S1","surface":"cognitive","action":"plan:commit-one","input_ref":"S1 only","output_ref":"pending","error":null,"ts":"2026-07-05T10:00:01Z"}
{"run_id":"2026-07-05T10:00:00Z-api","step_id":"S1","surface":"operational","action":"tool:Shell","input_ref":"npm test","output_ref":"exit 1","error":"3 test failures","ts":"2026-07-05T10:00:45Z"}
```

## Ex.2 — Query errors

```bash
python3 .agents/skills/run-trace/scripts/trace_query.py .agent-loom/traces/2026-07-05T10:00:00Z-api.jsonl errors
```
