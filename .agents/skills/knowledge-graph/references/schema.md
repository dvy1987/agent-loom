# Graph Schema v2

Output directory: `docs/knowledge-graph/`

## Artifacts

| File | Purpose |
|---|---|
| `graph.json` | Full graph (nodes, edges, stats, communities) |
| `call-graph.json` | Authoritative skill invoke edges only |
| `GRAPH_INDEX.md` | Human hub summary + communities |
| `GRAPH_REPORT.md` | God nodes, cross-community links, suggested questions |
| `manifest.json` | Input content hashes for incremental skip |

## Modes

| mode | trigger | node focus |
|---|---|---|
| `skill-library` | ≥10 `.agents/skills/*/SKILL.md` | skills, memory, handoffs, docs |
| `application` | fewer skills | code modules, dirs, docs, memory |

## Node types

| type | source | example |
|---|---|---|
| skill | `.agents/skills/*/SKILL.md` | `codebase-understanding` |
| memory | `docs/memory/*.md` | `agent-handoffs` |
| handoff | sections in `agent-handoffs.md` | `2026-07-03 handoff` |
| decision | `docs/memory/decision-log.md`, `docs/adr/` | ADR entries |
| learning | `docs/learnings/*.md` | `research-learnings` |
| doc | root docs | `AGENTS.md` |
| directory | top-level dirs | `docs`, `src` |
| module | source files (application mode) | `src/api/routes.py` |

## Edge relations

| relation | confidence | source |
|---|---|---|
| invokes | EXTRACTED | `docs/skill-graph.md`, SKILL-INDEX **Calls:**, explicit invoke in SKILL.md |
| requires_gate | EXTRACTED | learn-from → secure-* chain |
| orchestrates | EXTRACTED | orchestrator SKILL.md routing |
| post_apply | EXTRACTED | post-hardening chain edges |
| recorded_in | EXTRACTED | handoff section in memory file |
| references | INFERRED | backtick skill mention in body |
| mentions | INFERRED | skill name in AGENTS.md/README/handoff body |
| depends_on | INFERRED | application-mode import/path heuristic |

## Provenance priority (dedup)

1. `skill-graph.md` (mermaid)
2. `SKILL-INDEX.md` **Calls:**
3. `SKILL.md` explicit invoke
4. Handoff semantic mentions
5. Body backtick / structural inference

Higher priority wins when the same `(source, target, relation)` appears twice.

## Confidence

- **EXTRACTED** — parsed from authoritative or explicit text
- **INFERRED** — co-occurrence, backtick, or structural guess
- **AMBIGUOUS** — agent must verify before acting

Never treat INFERRED edges as hard dependencies without file read.
