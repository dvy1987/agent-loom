# Plan Schema

Plan artifacts live at `.agent-loom/plans/<task-id>.md`. Git-friendly, human-readable.

---

## File template

```markdown
# Plan — <task-id>
created_at: YYYY-MM-DDTHH:MM:SSZ
task_id: <slug>

## Steps
- **S1** — status:`pending` | goal:[text] | action:[text] | precondition:[text] | expected:[text] | evidence:[ref or empty]
- **S1.1** — status:`pending` | goal:... | action:... | precondition:... | expected:... | evidence:
- **S2** — status:`pending` | goal:... | action:... | precondition:... | expected:... | evidence:

## Plan delta log
| at | step_id | from | to | reason |
|----|---------|------|-----|--------|
| 2026-07-05T10:00:00Z | S2 | pending | failed | test timeout |
| 2026-07-05T10:05:00Z | S2 | failed | revised | split into S2.1 + S2.2 |
```

---

## Status lifecycle

```
pending → in-progress → done
pending → in-progress → failed → revised (new/replacement steps) | aborted
```

- **revised** — step superseded; delta log must explain replacement step ids.
- **aborted** — explicit stop; remaining `pending` steps marked `aborted` in delta log.

---

## Step ID rules

- Top level: `S1`, `S2`, …
- Sub-steps: `S1.1`, `S1.2`, `S2.1`
- No orphan children (parent id must exist)
- Stable across plan revisions — new work gets new ids, not reuse

---

## Lint

```bash
python3 .agents/skills/structured-planning/scripts/plan_lint.py .agent-loom/plans/<task-id>.md
```

---

## Trivial task bypass

Single-step tasks (one tool call, one file, obvious outcome) → skip formal plan. State "trivial — plan skipped" in chat. Echo Anthropic "add complexity only when it helps."
