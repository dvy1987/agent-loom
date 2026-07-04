---
name: knowledge-graph
description: >
  Build, update, and query a persistent project knowledge graph from skills,
  memory, docs, and code structure — stdlib Python only, no external tools.
  Dual-mode: skill-library (agent-loom) or application (any consumer repo).
  Load when the user asks for a knowledge graph, project map, skill
  relationships, query the graph, update the graph, or trace how components
  connect. Auto-runs on memory-handoff and project-setup bootstrap.
  Also triggers on "build the graph", "what connects to X", "map this project".
license: MIT
metadata:
  author: dvy1987
  version: "2.0"
  category: project-specific
  sources: safishamsi/graphify patterns (native stdlib impl, no pip install)
  resources:
    references:
      - schema.md
      - integration.md
      - examples.md
    scripts:
      - build_graph.py
      - query_graph.py
      - graph_health.py
---

# Knowledge Graph

You maintain a **queryable project graph** at `docs/knowledge-graph/`. Stdlib Python only — no Graphify, no pip deps, no external URLs in outputs.

## Deployment Context

| Host | Mode | Typical use |
|---|---|---|
| **agent-loom** (skill library) | `skill-library` | Map skill invoke chains, memory, handoffs |
| **Any consumer project** | `application` | Map modules, docs, memory for GRAPHIFY-style project management |

Mode auto-detects: ≥10 skills in `.agents/skills/` → `skill-library`; else `application`. Meta skills (`improve-skills`, `validate-skills`, `library-skill`) run in agent-loom; this skill installs into **any** project via `project-setup`.

## Hard Rules

- **Query before rebuild.** Relational questions → `query_graph.py` first.
- **Authoritative > inferred.** `invokes` from `docs/skill-graph.md` + `SKILL-INDEX.md` **Calls:** lines are authoritative; `references` edges are hypotheses.
- **Shrink guard.** No `--force` unless user confirms or graph is corrupt.
- **Handoff sync.** Every `memory-handoff` → `--incremental` build.
- **No secrets.** Skip `.env`, credentials, tokens by path name.

## Common Rationalizations

| Excuse | Reality |
|--------|---------|
| "I'll just grep" | Grep misses invoke chains and handoff lineage. Query the graph. |
| "Graph is stale, full rebuild" | Try `--incremental` first; authoritative sources may be unchanged. |
| "INFERRED edge = fact" | Read `source_file` / `provenance` before acting. |
| "Skip graph on handoff" | Next agent loses relational context. |
| "Need Graphify pip package" | Native stdlib scripts; patterns only, no install. |
| "Only for agent-loom" | Bootstrap in every project via `project-setup`. |

---

## Workflow

### Step 1 — Check existing graph
Read `GRAPH_INDEX.md` and `GRAPH_REPORT.md` when present.

### Step 2 — Build or update
```bash
python3 .agents/skills/knowledge-graph/scripts/build_graph.py              # full
python3 .agents/skills/knowledge-graph/scripts/build_graph.py --incremental  # handoff/default
python3 .agents/skills/knowledge-graph/scripts/build_graph.py --force       # override shrink guard
```

### Step 3 — Query
```bash
python3 .agents/skills/knowledge-graph/scripts/query_graph.py query "memory handoff connections"
python3 .agents/skills/knowledge-graph/scripts/query_graph.py path memory-handoff knowledge-graph
python3 .agents/skills/knowledge-graph/scripts/query_graph.py explain validate-skills
```
Cite `path`, `confidence`, and `provenance` for every hit.

### Step 4 — Health audit (optional / validate-skills hook)
```bash
python3 .agents/skills/knowledge-graph/scripts/graph_health.py
```

### Step 5 — Report
Summarize: mode, node/edge counts, authoritative vs inferred ratio, hub nodes, communities, top query results.

---

## Handoff Hook (mandatory for memory-handoff)

After appending to `agent-handoffs.md`:
```bash
python3 .agents/skills/knowledge-graph/scripts/build_graph.py --incremental
```
If build fails, note in handoff `### Graph` — do not block save.

---

## Output Format

```markdown
## Knowledge graph — [full | incremental | query | health]

Mode: [skill-library | application]
Stats: [N] nodes, [E] edges ([A] authoritative invokes)
Hub nodes: [top 3]
Query: "[question]" → [matches with confidence tags]
Files: graph.json, call-graph.json, GRAPH_INDEX.md, GRAPH_REPORT.md
```

---

## Verification

- [ ] `graph.json`, `GRAPH_INDEX.md`, `GRAPH_REPORT.md` exist under `docs/knowledge-graph/`
- [ ] `call-graph.json` present when mode=skill-library
- [ ] Shrink guard respected (or `--force` approved)
- [ ] Query results cite path + confidence + provenance
- [ ] Handoff hook ran `--incremental` when invoked from `memory-handoff`
- [ ] No secrets or external URLs in graph artifacts

---

Read `references/examples.md` for full worked examples.

## Reference Files

- `references/schema.md` — node/edge types, provenance priority
- `references/integration.md` — producers/consumers, project-setup bootstrap
- `scripts/build_graph.py` — full/incremental build
- `scripts/query_graph.py` — query, path, explain
- `scripts/graph_health.py` — dangling invokes, stale graph, orphan skills

---

## File Output

Append to `docs/skill-outputs/SKILL-OUTPUTS.md`:
```
| YYYY-MM-DD HH:MM | knowledge-graph | docs/knowledge-graph/ | [N] nodes, [E] edges, mode=[mode] |
```

---

## Examples

<examples>
  <example>
    <input>Build a knowledge graph for this project.</input>
    <output>
Ran `build_graph.py` → mode=skill-library, 120 nodes, 412 edges (164 authoritative invokes). Hubs: universal-skill-creator, validate-skills, secure-skill. Saved to `docs/knowledge-graph/`. See `GRAPH_REPORT.md` for communities and suggested questions.
    </output>
  </example>
  <example>
    <input>How does memory-handoff connect to knowledge-graph?</input>
    <output>
`query_graph.py path memory-handoff knowledge-graph` → 1 hop via `invokes` [EXTRACTED, provenance: memory-handoff/SKILL.md]. Neighbors: memory-capture, agent-handoffs [recorded_in].
    </output>
  </example>
</examples>

---

## Impact Report

```
Knowledge graph: [full/incremental/query/health]
Mode: [skill-library|application] | Nodes: [N] | Edges: [E]
Authoritative invokes: [A] | EXTRACTED: [E] | INFERRED: [I]
Shrink guard: [ok/refused/forced] | Handoff sync: [yes/no]
Consumers notified: [list or n/a]
```
