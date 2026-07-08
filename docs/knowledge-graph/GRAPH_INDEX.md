# Project Knowledge Graph Index

Generated: 2026-07-08T08:38:53.632244+00:00
Mode: **skill-library** | Nodes: 707 | Edges: 562

**Why this mode:** skill-library label: docs/skill-graph.md + docs/SKILL-INDEX.md present → adds authoritative skill invoke edges. Still scans full repo (not skills-only).

**Scan layers:**
- skills (123 in .agents/skills)
- repo-wide source ((root))
- docs (AGENTS.md, README.md, docs/**/*.md)
- memory (docs/memory, handoffs)
- packages (package.json workspaces)
- config (.agents/ROUTING.md, tsconfig, pyproject, etc.)
- top-level directories
- authoritative invokes (skill-graph.md + SKILL-INDEX.md)

EXTRACTED: 291 | INFERRED: 271

## Hub nodes
- universal-skill-creator
- validate-skills
- secure-skill
- improve-skills
- project-setup
- retroactive-project-setup
- library-skill
- venture-exploration

## Communities

**code** (2): code-simplification, technical-debt-audit
**deploy** (1): deploy-anywhere
**issue** (1): issue-sync
**pr** (1): pr-authoring
**svg** (118): adversarial-hat, agent-builder, agent-launcher, agent-loom-sync, agent-observability, agent-run-retro, agent-system-architecture, api-and-interface-design, api-deprecation-and-migration, app-security-hardening
  … +108 more

## Node types

- **config**: 416
- **directory**: 6
- **doc**: 96
- **handoff**: 20
- **learning**: 2
- **memory**: 7
- **module**: 36
- **package**: 1
- **skill**: 123

See `GRAPH_REPORT.md` for surprising connections and suggested questions.

Full graph: `docs/knowledge-graph/graph.json`
Authoritative call edges: `docs/knowledge-graph/call-graph.json`
