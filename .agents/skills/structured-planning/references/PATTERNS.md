# Orchestration Patterns

Distilled from Anthropic "Building Effective Agents", ReCAP (NeurIPS 2025), DyFlow, GAP, NaviAgent.

---

## Pattern 1 — Plan-ahead decomposition (ReCAP)

1. Generate the **full** subgoal list in one pass (all step ids).
2. **Commit to executing only S1** (or the first pending leaf).
3. Execute against ground truth (tool output, tests, env).
4. Record actual observation in `evidence:` field.
5. **Refine remaining steps** before continuing — do not blindly execute stale plan.

---

## Pattern 2 — Workflows vs agents (Anthropic)

| Use workflow when | Use agent loop when |
|-------------------|---------------------|
| Steps are known upfront | Path depends on intermediate results |
| Failure is rare | Tool errors need branch selection |
| Cost must be predictable | Exploration is required |

Start simple. Escalate to full plan only when triage shows multi-step or failure-prone work.

---

## Pattern 3 — Designer / executor split (DyFlow)

- **Planning phase:** define steps, preconditions, expected observations.
- **Execution phase:** one step at a time; observations feed back to planner.
- Do not replan from scratch on every step — patch the remainder.

---

## Pattern 4 — Dependency-aware graph (GAP / NaviAgent)

- Steps may depend on prior step outputs — note in `precondition:`.
- On tool failure at step Sx, **recombine** remaining plan (insert alternate path) rather than retrying the same action.
- Route failure handling to `dynamic-routing`.

---

## Pattern 5 — Checkpointing

After each `done` step:
- Persist plan file
- Run `plan_lint.py`
- If multi-agent handoff, include plan path in `memory-handoff`

---

## Deferred (future work)

- Multi-agent delegation per step
- Learned routing policies
- Parallel tool execution within independent branches
