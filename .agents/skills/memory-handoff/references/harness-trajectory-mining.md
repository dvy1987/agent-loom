# Harness Trajectory Mining (RHO prerequisite)

Optional path when `harness-evolution` needs label-free improvement and no benchmark exists.

## When to run

- User reports repeated agent failures but no `docs/harness/tasks.json` labels.
- `setup-evaluation` flagged missing trajectory reservoir.
- End of session with meaningful failures worth distilling.

## Hard rules

- **Never** paste raw chat transcripts into handoff files.
- **Never** include secrets, tokens, or PII in trace digests.
- Distill to mechanism + step refs only — same hygiene as handoff template.

## Distill workflow

1. From session context, extract **failed task attempts** (not successes-only).
2. For each failure, write one HTIR-style record:

```markdown
### Trace digest — [task-id or session label]
- Verifier cause: [terminal message / tool error]
- Primary layer: [ETCLOVG]
- Step refs: [tool calls / skill skips observed]
- Mechanism: [one sentence]
```

3. Save under `docs/harness/runs/iteration_NNN/traces/distilled.md`.
4. If same mechanism appears ≥2 times → eligible for weakness cluster (Self-Harness).

## Multi-rollout capture (retro-harness pattern)

When user can re-run a failing workflow:
- Capture **3 independent attempts** on the same task when feasible.
- Enables self-consistency diagnostics in RHO path.
- Store only digests — not full rollout text.

## Handoff cross-link

In handoff `### Next Agent Should Know`, add when applicable:

```
Harness: [N] failure digests added to docs/harness/runs/ — RHO coreset candidate pool
```

## Route

After ≥5 distilled failures → `harness-engineering` → `harness-evolution` (RHO fallback in evolution-loop.md).
