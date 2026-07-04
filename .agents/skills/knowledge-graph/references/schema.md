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
| `skill-library` | `docs/skill-graph.md` + `docs/SKILL-INDEX.md` present | full repo + authoritative skill invoke edges |
| `application` | default for consumer repos | full repo (skills, modules, docs, memory, dirs) |

**v2.2:** Repo-wide source walk (`rglob`) — not limited to `src/`/`lib/` allowlist. Skips only `.agents/skills/` bodies (indexed as skills) and `docs/knowledge-graph/` output.

## Node types

| type | source | example |
|---|---|---|
| skill | `.agents/skills/*/SKILL.md` | `codebase-understanding` |
| module | any `CODE_EXTENSIONS` file in repo | `packages/api/src/index.ts` |
| package | `package.json` workspaces | `@workspace/api` |
| config | `tsconfig.json`, `.agents/ROUTING.md`, etc. | `tsconfig.json` |
| memory | `docs/memory/*.md` | `agent-handoffs` |
| handoff | sections in `agent-handoffs.md` | `2026-07-03 handoff` |
| decision | `docs/memory/decision-log.md`, `docs/adr/` | ADR entries |
| learning | `docs/learnings/*.md` | `research-learnings` |
| doc | root docs | `AGENTS.md` |
| directory | top-level dirs | `docs`, `src` |

## Edge relations

| relation | confidence | source |
|---|---|---|
| invokes | EXTRACTED | `docs/skill-graph.md`, SKILL-INDEX **Calls:**, explicit invoke in SKILL.md |
| requires_gate | EXTRACTED | learn-from → secure-* chain |
| orchestrates | EXTRACTED | orchestrator SKILL.md routing |
| post_apply | EXTRACTED | post-hardening chain edges |
| recorded_in | EXTRACTED | handoff section in memory file |
| depends_on | EXTRACTED | `package.json` workspace deps |
| imports | EXTRACTED | Python/TS import resolution |
| mentions | INFERRED | skill name in docs (excludes SKILL-INDEX noise) |
| references | INFERRED | backtick file path in docs |

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
