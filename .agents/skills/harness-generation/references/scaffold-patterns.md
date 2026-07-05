# Scaffold Patterns

Distilled from harnessforge, metaharness, AHE — no external URLs.

## Inspect → plan → staged write

1. **Inspect** — repo tree, manifests, existing agent files, git branch.
2. **Profile** — stack, commands, skill install path, platform (Cursor/Codex/etc.).
3. **Plan** — list `PlannedFile` entries with collision policy (refuse overwrite of user-edited).
4. **Write** — staged; update manifest sha256 after each.
5. **Verify** — manifest complete; eval stub present; **interface validation** passes.

## Interface validation (Meta-Harness)

Before sign-off on v0:
- [ ] `docs/harness/eval-interface.md` paths exist and are readable
- [ ] `docs/harness/tasks.json` schema valid (≥1 held-in, ≥1 held-out when evolution planned)
- [ ] `allowed_write_paths` non-empty and covers intended evolve surfaces
- [ ] Regression command runs (smoke — may fail tasks, must not crash harness)

Invalid harness → fix scaffold before first evolution round.

## Environment bootstrap block

Inject compact snapshot into harness docs for meta-agents (metaharness `collect_environment_bootstrap`):

```
Stack: [from pyproject/package.json]
Commands: test=[cmd] lint=[cmd] build=[cmd]
Git: branch=[name] clean=[yes/no]
Skills: [.agents/skills count] + global install [yes/no]
```

## Eval interface stub

`docs/harness/eval-interface.md` must declare:
- Regression command or script path
- Held-in vs held-out split paths
- Pass metric (pass@1 primary)
- Rollouts per task (k ≥ 2 when evolution planned)
- Minimum promotion threshold

`docs/harness/tasks.json` minimal shape:

```json
{
  "tasks": [
    {
      "id": "smoke-001",
      "file_phrase": "optional substring in repo",
      "command": "npm test -- --run path/to.test.ts",
      "split": "held-in"
    }
  ]
}
```

## Manifest drift + CI (harnessforge)

On re-run or CI `--check`:
1. Compare on-disk sha256 to manifest per component.
2. If mismatch and `status: user-edited` → skip overwrite, flag in report.
3. If mismatch and `status: generated` → require user `--force` or manual reconcile.
4. **CI:** drift on generated files → non-zero exit (do not silent overwrite).

Track `written_by` (adapter/blueprint name) per manifest entry for attribution.

## Governance defaults

- **Forbidden:** `.env*`, credentials, `node_modules/`, destructive git ops without ask.
- **allowed_write_paths:** declare explicitly in manifest — evolve agent may only edit these.
- **Verifier sandbox (AHE):** evolve agent cannot disable eval, swap models, or raise token budgets.
- **runs/ READ ONLY:** `docs/harness/runs/` — analysis only, never write during evolve.
- **Iteration-1 prompt rules:** cannot delete ORIGINAL system-prompt rules — only add/refine.
- **Explore skills:** bootstrap skills from round 1 have **no special protection** from round 2.

## Forbidden harness edits (HarnessFix)

Evolve agent must never modify:
- Benchmark data, task definitions, evaluator oracles
- Held-out validation sets or validation labels

## Merge with project-setup

When AGENTS.md exists from interview:
- Preserve: User Context, Boundaries, Session Lifecycle, Orchestration Map prose.
- Add: Harness section pointer to `docs/harness/manifest.json`, eval stub paths.
- Do not duplicate skill routing — link to Orchestration Map.

## RHO workspace shape (partial)

Optimized harness may materialize as folder with:
- Task-agnostic **instructions** (AGENTS.md harness section)
- Environment-specific **skills** (grader idiosyncrasies)
- **Executable tool scripts** where needed — not prompt-only
