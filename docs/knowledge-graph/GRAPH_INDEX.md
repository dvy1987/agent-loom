# Project Knowledge Graph Index

Generated: 2026-07-04T07:55:40.015046+00:00
Mode: **skill-library** | Nodes: 206 | Edges: 1403

**Why this mode:** skill-library label: docs/skill-graph.md + docs/SKILL-INDEX.md present → adds authoritative skill invoke edges. Still scans full repo (not skills-only).

**Scan layers:**
- skills (102 in .agents/skills)
- repo-wide source (none — no .py/.ts/.tsx/.js outside .agents/skills)
- docs (AGENTS.md, README.md, docs/**/*.md)
- memory (docs/memory, handoffs)
- packages (package.json workspaces)
- config (.agents/ROUTING.md, tsconfig, pyproject, etc.)
- top-level directories
- authoritative invokes (skill-graph.md + SKILL-INDEX.md)

EXTRACTED: 225 | INFERRED: 1178

## Hub nodes
- universal-skill-creator
- validate-skills
- improve-skills
- split-skill
- library-skill
- process-decomposer
- feature-spec
- implementation-plan

## Communities

**ci** (9): app-security-hardening, browser-testing-with-devtools, ci-cd-and-automation, design-direction, design-review, design-system, frontend-design, performance-optimization, shipping-and-launch
**code** (3): code-review-crsp, code-simplification, technical-debt-audit
**context** (1): context-engineering
**debug** (1): debug-and-fix
**project** (88): adversarial-hat, agent-builder, agent-launcher, agent-system-architecture, api-and-interface-design, api-deprecation-and-migration, apply-paper-to-project, architectural-decision-log, assumption-mapping, brainstorming
  … +78 more

## Node types

- **config**: 1
- **directory**: 2
- **doc**: 77
- **handoff**: 16
- **learning**: 2
- **memory**: 6
- **skill**: 102

See `GRAPH_REPORT.md` for surprising connections and suggested questions.

Full graph: `docs/knowledge-graph/graph.json`
Authoritative call edges: `docs/knowledge-graph/call-graph.json`
