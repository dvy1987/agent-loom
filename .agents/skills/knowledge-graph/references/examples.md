# Knowledge Graph — Full Worked Examples

Enriched from SKILL.md v2.2 — full-repo scan, never skills-only.

## Example 1 — agent-loom (skill-library label, full repo)

**Input:** Build a knowledge graph for agent-loom.

**Stdout:**
```
Auto mode: skill-library
Why: skill-library label: ... Still scans full repo (not skills-only).
Scanning: skills (102 in .agents/skills) | repo-wide source (none) | docs (...) | ...
Node types: skill=102, doc=..., memory=...
```

## Example 2 — Consumer monorepo (Ember-shaped)

**Input:** Build graph — 102 skills + TypeScript in `lib/`, `artifacts/`, `packages/`.

**Stdout:**
```
Auto mode: application
Why: application label: 102 skills ... plus source under artifacts, lib, packages → indexing entire repository.
Scanning: skills (102) | repo-wide source (artifacts, lib, packages, ...) | ...
Node types: skill=102, module=..., package=...
```

## Example 3 — Nested package discovery

**Input:** Code only under `packages/api/src/index.ts` (no top-level `src/`).

**Output:** Module nodes for `packages/api/src/index.ts` — repo-wide `rglob`, not a fixed dir allowlist.

## Example 4 — Query path

**Input:** How does memory-handoff connect to knowledge-graph?

**Output:** `query_graph.py path memory-handoff knowledge-graph` → 1 hop via `invokes` [EXTRACTED].

## Example 5 — Coverage gate

**Input:** CI build with `--strict` on consumer repo.

**Output:** Fails with `COVERAGE FAIL` if source files exist but `module` count is 0. `graph_health.py` reports P0 `skills-only-graph`.

## Example 6 — Anti-skip

| Excuse | Reality |
|--------|---------|
| "Many skills = skills-only graph" | Repo-wide scan always runs — check `module` in node types. |
| "I'll just grep" | Grep misses invoke chains and import graphs. |
| "INFERRED edge = fact" | Read provenance before acting. |

---

See `SKILL.md` and `references/schema.md` for scan layers and node types.
