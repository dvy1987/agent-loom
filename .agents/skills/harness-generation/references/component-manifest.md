# Harness Component Manifest

Seven orthogonal components (AHE / NexAU pattern, adapted for agent-loom):

| # | Component | Typical paths | ETCLOVG layer |
|---|-----------|---------------|---------------|
| 1 | System prompt / routing | `AGENTS.md`, harness prompt section | Context |
| 2 | Tool descriptions | `docs/harness/tools.md`, MCP configs | Tooling |
| 3 | Tool implementations | scripts, MCP server defs | Tooling |
| 4 | Middleware | `docs/harness/middleware.md` (retry, compaction hooks) | Lifecycle |
| 5 | Skills | `.agents/skills/` | Context |
| 6 | Sub-agents | `docs/agents/*-prompt.md`, orchestration map | Lifecycle |
| 7 | Long-term memory | `docs/memory/`, MEMORY routing | Context |

Plus **governance** (forbidden paths, `allowed_write`) and **verification** (eval interface) as cross-cutting.

## manifest.json schema

```json
{
  "harness_version": "v0",
  "created": "2026-07-05",
  "model_family": "optional — per-model harness lineage",
  "components": [
    {
      "id": "prompt",
      "path": "AGENTS.md",
      "status": "generated",
      "sha256": "...",
      "allowed_write": true
    }
  ],
  "eval_interface": "docs/harness/eval-interface.md",
  "held_out_split": "docs/harness/splits/held-out.json",
  "allowed_write_paths": [
    "docs/harness/",
    "AGENTS.md"
  ]
}
```

## ETCLOVG quick map

| Layer | Diagnose when |
|-------|----------------|
| **E**xecution | Sandbox, env, permissions, command failures |
| **T**ooling | Wrong tool, bad schema, missing MCP |
| **C**ontext | Stale AGENTS.md, memory rot, wrong skill loaded |
| **L**ifecycle | Session start/end, handoff, hook ordering |
| **O**bservability | Missing traces, undistilled logs |
| **V**erification | Eval missing, false pass, lint/test bypass |
| **G**overnance | Forbidden path writes, scope violations |

## Drift detection

On re-run `harness-generation`:
1. Read manifest sha256 per component.
2. If on-disk hash differs and `status: user-edited` → skip overwrite, flag in report.
3. If hash differs and `status: generated` → offer `--force` regenerate (document only; user approves).
