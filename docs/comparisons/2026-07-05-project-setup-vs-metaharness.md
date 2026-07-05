# Comparison: project-setup vs SuperagenticAI/metaharness (coding-tool scaffold)

**Date:** 2026-07-05  
**Repo credibility:** 9/12 PASS  
**Code verified:** `src/metaharness/core/engine.py` — FilesystemRunStore, environment bootstrap, allowed_write_paths, interface validation, pareto selection_policy

| Axis | agent-loom project-setup + harness-generation | metaharness scaffold | Winner |
|---|---|---|---|
| Non-dev interview | 2/2 | 0/2 | ours |
| Environment bootstrap block | 1/2 | 2/2 | theirs |
| Eval interface stub | 1/2 | 2/2 | theirs |
| Interface validation pre-eval | 0/2 | 2/2 | theirs |
| Filesystem artifact store | 1/2 | 2/2 | theirs |
| Pareto frontier output | 0/2 | 2/2 | theirs |
| Skill library wiring | 2/2 | 0/2 | ours |
| **Total** | **7/12** | **10/12** | **MERGE (into harness-generation)** |

## Per-axis notes

**Scaffold vs interview:** metaharness `scaffold.py` + `collect_environment_bootstrap` produce compact stack snapshot for meta-agents. agent-loom already has partial bootstrap in `scaffold-patterns.md` — needs interface-validation step before first eval.

**Engine patterns:** MetaHarnessEngine validates candidate harness **before** task eval; discards invalid harnesses without burning budget. Maps to `harness-generation` verify step.

**Filesystem store:** Prior rounds grep/cat navigable under `.metaharness/` — agent-loom mirrors as `docs/harness/runs/iteration_NNN/`.

**Pareto:** `selection_policy: pareto` returns frontier over accuracy × cost — not single scalar winner. Belongs in harness-engineering routing, not project-setup interview.

## Verdict: MERGE into harness-generation L3

project-setup Step 6c invokes `harness-generation` — metaharness patterns land there, not in interview skill body.

## Recommended actions

| P | Action | Target |
|---|--------|--------|
| P0 | Interface validation checklist before eval stub sign-off | `harness-generation/references/scaffold-patterns.md` |
| P1 | Bootstrap block fields aligned with metaharness snapshot | `scaffold-patterns.md` |
| P1 | Pareto frontier as evolution output shape | `harness-engineering/references/routing.md` |
| P2 | Confound-isolation example (structure + prompt coupling) | `harness-evolution/references/examples.md` |
| — | Do **not** embed metaharness Python engine in agent-loom | — |
