# Comparison: project-setup vs jcaiagent7143-ui/harnessforge

**Date:** 2026-07-05  
**Repo credibility:** 6/12 REJECT — patterns PARTIAL only (low stars, early maturity)  
**Code verified:** `src/harness/manifest.py` — sha256 drift detection, `detect_drift()`, refuse overwrite unless `--force`

| Axis | agent-loom | harnessforge | Winner |
|---|---|---|---|
| User discovery | 2/2 | 0/2 | ours |
| Interview + context | 2/2 | 0/2 | ours |
| Deterministic scaffold speed | 0/2 | 2/2 | theirs |
| Manifest drift / CI check | 1/2 | 2/2 | theirs |
| Skill library integration | 2/2 | 1/2 | ours |
| Multi-IDE adapters | 0/2 | 2/2 | theirs |
| **Total** | **7/12** | **7/12** | **KEEP+MERGE** |

## Per-axis notes

**User discovery:** `project-setup` interviews non-dev owners (Q1–Q6), maps Orchestration Map, default-on harness bootstrap. harnessforge is CLI `init` with zero interview — fast but blind to project intent.

**Manifest drift:** harnessforge tracks every written file with sha256; `detect_drift()` exits non-zero in CI when generated files were hand-edited. agent-loom has equivalent logic in `harness-generation/references/component-manifest.md` but lacks explicit **CI exit-code** guidance.

**Deterministic scaffold:** harnessforge emits AGENTS.md, SOUL.md, TOOLS.md, MEMORY.md in ~3s from repo walker. agent-loom routes deterministic scaffold to `harness-generation` after interview — complementary, not competing.

**Skill library:** harnessforge is standalone; agent-loom wires harness into `project-orchestrator`, `memory-startup`, `skill-routing`.

## Verdict: KEEP+MERGE

Keep interview-driven `project-setup` as primary greenfield path. Adopt harnessforge **drift CI pattern** and **inspect→plan→staged write** discipline into `harness-generation` L3 (already partial).

## Recommended actions

| P | Action | Target |
|---|--------|--------|
| P1 | Add CI drift check: manifest hash mismatch → flag, do not silent overwrite | `harness-generation/references/scaffold-patterns.md` |
| P1 | Document `written_by` / `status: user-edited` collision policy | `component-manifest.md` |
| P2 | Note harnessforge as fast deterministic alternative when user skips interview | `project-setup` Step 6c one-liner |
| — | Do **not** vendor harnessforge CLI or duplicate SOUL.md blueprint set | — |
