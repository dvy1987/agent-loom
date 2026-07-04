# Knowledge Graph Integration

## Deployment

- **agent-loom:** skill-library mode when `docs/skill-graph.md` + `docs/SKILL-INDEX.md` exist — authoritative invoke graph layered on full-repo scan
- **Consumer projects:** application mode — same full-repo scan (skills + code + docs + memory); bootstrap via `project-setup` Step 6b
- Meta skills (`improve-skills`, `library-skill`, `validate-skills`) consume the graph in agent-loom only

## Producers (build/update)

| Event | Skill | Action |
|---|---|---|
| User asks build/update graph | `knowledge-graph` | `build_graph.py` full or `--incremental` |
| Session handoff written | `memory-handoff` | `build_graph.py --incremental` after Step 6 |
| Project bootstrap | `project-setup` Step 6b | initial `build_graph.py` if skill installed |
| Retroactive bootstrap | `retroactive-project-setup` Step 6b | initial build after memory seed |
| Skill library sync | `library-skill` Step 5b | `build_graph.py --incremental` after `skill-graph.md` rebuild |
| Cross-link repair | `cross-link-skills` Step 5b | `build_graph.py --incremental` after edits |
| Skill created | `universal-skill-creator` Step 11b | recommend incremental rebuild (via `library-skill`) |

## Consumers (query before deep scan)

| Skill | When | How |
|---|---|---|
| `memory-startup` | Step 3.5 | Read `GRAPH_INDEX.md`; enforce freshness; query if relational opener |
| `memory-recall` | Step 2.5 | `query_graph.py` for topic → memory/skill paths |
| `codebase-understanding` | Step 0 | Query graph; reuse paths; tag EXTRACTED/INFERRED |
| `context-engineering` | Tier B/C | Query touched modules + 1-hop neighbors |
| `debug-and-fix` | Step 1.5 | Query error component → related skills/files |
| `project-orchestrator` | Triage | Query goal keywords → candidate skills |
| `validate-skills` | Step 4d | `graph_health.py` when graph exists |

## Fast path

If `docs/knowledge-graph/graph.json` exists and the task is relational: **query first**. Rebuild only when inputs changed, handoff written, or library sync completed.

## Shrink guard

`build_graph.py` refuses to replace a graph with <50% prior node count unless `--force`.

## Health audit flags

`graph_health.py` reports: missing graph (P1), **skills-only-graph** (P0 — source on disk, 0 modules), dangling invoke targets (P0), orphan skills on disk (P2), stale graph vs latest handoff (P1), high inferred ratio >0.7 (P2).
