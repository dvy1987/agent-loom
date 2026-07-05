# Localization Procedure

REFLECT-style loop: diagnose → targeted replay → verify outcome flip. Pairs with `run-trace` evidence.

---

## Step 1 — Scan trace chronologically

```bash
python3 .agents/skills/run-trace/scripts/trace_query.py <trace> timeline
```

Find the **earliest** record where:
- `error` is non-null, OR
- operational `output_ref` contradicts prior cognitive `expected` for same `step_id`

That record's `step_id` is the **suspected origin** (first divergence).

---

## Step 2 — Hypothesis (evidence-bound)

```markdown
suspected_step_id: Sx
hypothesis: [one sentence citing output_ref/error]
layer: [tooling | code | plan | environment]
```

No vague "something went wrong."

---

## Step 3 — Targeted repair

| Layer | Action |
|-------|--------|
| tooling | Different tool/flags |
| code | Minimal fix via `debug-and-fix` or `safe-change` |
| plan | `dynamic-routing` revision |
| environment | Fix deps/config; replay from Sx |

---

## Step 4 — Replay from suspected step

Re-execute from `suspected_step_id` forward — not full run from S1 unless plan layer fault.

---

## Step 5 — Outcome flip

| Before | After | Verdict |
|--------|-------|---------|
| fail | pass | **Attributed** — record intervention |
| fail | fail | Wrong localization — back to Step 1 with next candidate |
| pass | pass | No fault in trace — check success criteria |

---

## Attribution record

Append to `.agent-loom/traces/<run-id>-attribution.json`:

```json
{
  "run_id": "...",
  "suspected_step_id": "S2",
  "hypothesis": "...",
  "repair": "...",
  "outcome_flip": true
}
```
