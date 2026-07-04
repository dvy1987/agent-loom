# Project Knowledge Graph Index

Generated: 2026-07-04T11:20:54.519448+00:00
Mode: **skill-library** | Nodes: 207 | Edges: 463

**Why this mode:** skill-library label: docs/skill-graph.md + docs/SKILL-INDEX.md present → adds authoritative skill invoke edges. Still scans full repo (not skills-only).

**Scan layers:**
- skills (103 in .agents/skills)
- repo-wide source (none — no .py/.ts/.tsx/.js outside .agents/skills)
- docs (AGENTS.md, README.md, docs/**/*.md)
- memory (docs/memory, handoffs)
- packages (package.json workspaces)
- config (.agents/ROUTING.md, tsconfig, pyproject, etc.)
- top-level directories
- authoritative invokes (skill-graph.md + SKILL-INDEX.md)

EXTRACTED: 239 | INFERRED: 224

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

**code** (2): code-simplification, technical-debt-audit
**design** (10): app-security-hardening, browser-testing-with-devtools, ci-cd-and-automation, code-review-crsp, design-direction, design-review, design-system, frontend-design, performance-optimization, shipping-and-launch
**memory** (91): adversarial-hat, agent-builder, agent-launcher, agent-loom-sync, agent-system-architecture, api-and-interface-design, api-deprecation-and-migration, apply-paper-to-project, architectural-decision-log, assumption-mapping
  … +81 more

## Node types

- **config**: 1
- **directory**: 2
- **doc**: 77
- **handoff**: 16
- **learning**: 2
- **memory**: 6
- **skill**: 103

See `GRAPH_REPORT.md` for surprising connections and suggested questions.

Full graph: `docs/knowledge-graph/graph.json`
Authoritative call edges: `docs/knowledge-graph/call-graph.json`
