# Project Knowledge Graph Index

Generated: 2026-07-04T17:01:21.701060+00:00
Mode: **skill-library** | Nodes: 209 | Edges: 465

**Why this mode:** skill-library label: docs/skill-graph.md + docs/SKILL-INDEX.md present → adds authoritative skill invoke edges. Still scans full repo (not skills-only).

**Scan layers:**
- skills (104 in .agents/skills)
- repo-wide source (none — no .py/.ts/.tsx/.js outside .agents/skills)
- docs (AGENTS.md, README.md, docs/**/*.md)
- memory (docs/memory, handoffs)
- packages (package.json workspaces)
- config (.agents/ROUTING.md, tsconfig, pyproject, etc.)
- top-level directories
- authoritative invokes (skill-graph.md + SKILL-INDEX.md)

EXTRACTED: 241 | INFERRED: 224

## Hub nodes
- universal-skill-creator
- validate-skills
- secure-skill
- improve-skills
- venture-exploration
- library-skill
- split-skill
- feature-spec

## Communities

**code** (13): app-security-hardening, browser-testing-with-devtools, ci-cd-and-automation, code-review-crsp, code-simplification, design-direction, design-review, design-system, frontend-design, performance-optimization
  … +3 more
**debug** (91): adversarial-hat, agent-builder, agent-launcher, agent-loom-sync, agent-system-architecture, api-and-interface-design, api-deprecation-and-migration, apply-paper-to-project, architectural-decision-log, assumption-mapping
  … +81 more

## Node types

- **config**: 1
- **directory**: 3
- **doc**: 77
- **handoff**: 16
- **learning**: 2
- **memory**: 6
- **skill**: 104

See `GRAPH_REPORT.md` for surprising connections and suggested questions.

Full graph: `docs/knowledge-graph/graph.json`
Authoritative call edges: `docs/knowledge-graph/call-graph.json`
