# Knowledge Graph — Full Worked Examples

Skill: `knowledge-graph` | Enriched from SKILL.md (improve-skills pass, SKIP_RESEARCH).

## Example 1 — Documented workflow

**Input:** Build a knowledge graph for this project.

**Output:**
```
Ran `build_graph.py` → mode=skill-library, 120 nodes, 412 edges (164 authoritative invokes). Hubs: universal-skill-creator, validate-skills, secure-skill. Saved to `docs/knowledge-graph/`. See `GRAPH_REPORT.md` for communities and suggested questions.
```

## Example 2 — Documented workflow

**Input:** How does memory-handoff connect to knowledge-graph?

**Output:**
```
`query_graph.py path memory-handoff knowledge-graph` → 1 hop via `invokes` [EXTRACTED, provenance: memory-handoff/SKILL.md]. Neighbors: memory-capture, agent-handoffs [recorded_in].
```

## Example 3 — Step-by-step execution

**Input:** "Run `knowledge-graph` on [concrete task]"

**Agent actions:**
1. Check existing graph
2. Build or update
3. Query
4. Health audit (optional / validate-skills hook)
5. Report

## Example 4 — Anti-skip (rationalization defense)

**Input:** Agent tries to skip a gate

| Excuse | Reality |
|---|---|
| "I'll just grep" | Grep misses invoke chains and handoff lineage. Query the graph. |
| "Graph is stale, full rebuild" | Try `--incremental` first; authoritative sources may be unchanged. |
| "INFERRED edge = fact" | Read `source_file` / `provenance` before acting. |
| "Skip graph on handoff" | Next agent loses relational context. |

---

See `SKILL.md` for hard rules and verification checklist.

---

|---|
| "I'll just grep" | Grep misses invoke chains and handoff lineage. Query the graph. |
| "Graph is stale, full rebuild" | Try `--incremental` first; authoritative sources may be unchanged. |
| "INFERRED edge = fact" | Read `source_file` / `provenance` before acting. |
| "Skip graph on handoff" | Next agent loses relational context. |

---

See `SKILL.md` for hard rules and verification checklist.
