# Project Knowledge Graph Index

Generated: 2026-07-05T07:19:35.386594+00:00
Mode: **skill-library** | Nodes: 237 | Edges: 515

**Why this mode:** skill-library label: docs/skill-graph.md + docs/SKILL-INDEX.md present → adds authoritative skill invoke edges. Still scans full repo (not skills-only).

**Scan layers:**
- skills (119 in .agents/skills)
- repo-wide source (examples)
- docs (AGENTS.md, README.md, docs/**/*.md)
- memory (docs/memory, handoffs)
- packages (package.json workspaces)
- config (.agents/ROUTING.md, tsconfig, pyproject, etc.)
- top-level directories
- authoritative invokes (skill-graph.md + SKILL-INDEX.md)

EXTRACTED: 272 | INFERRED: 243

## Hub nodes
- universal-skill-creator
- validate-skills
- secure-skill
- improve-skills
- project-setup
- venture-exploration
- retroactive-project-setup
- library-skill

## Communities

**deploy** (1): deploy-anywhere
**issue** (1): issue-sync
**memory** (101): adversarial-hat, agent-builder, agent-launcher, agent-loom-sync, agent-system-architecture, api-and-interface-design, api-deprecation-and-migration, apply-paper-to-project, architectural-decision-log, assumption-mapping
  … +91 more
**motion** (13): app-security-hardening, browser-testing-with-devtools, ci-cd-and-automation, code-review-crsp, design-direction, design-review, design-system, frontend-design, gsap-animation, motion-animation
  … +3 more
**pr** (1): pr-authoring
**technical** (2): code-simplification, technical-debt-audit

## Node types

- **config**: 1
- **directory**: 4
- **doc**: 86
- **handoff**: 17
- **learning**: 2
- **memory**: 6
- **module**: 2
- **skill**: 119

See `GRAPH_REPORT.md` for surprising connections and suggested questions.

Full graph: `docs/knowledge-graph/graph.json`
Authoritative call edges: `docs/knowledge-graph/call-graph.json`
