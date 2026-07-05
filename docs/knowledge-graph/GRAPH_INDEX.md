# Project Knowledge Graph Index

Generated: 2026-07-05T04:24:06.868230+00:00
Mode: **skill-library** | Nodes: 221 | Edges: 490

**Why this mode:** skill-library label: docs/skill-graph.md + docs/SKILL-INDEX.md present → adds authoritative skill invoke edges. Still scans full repo (not skills-only).

**Scan layers:**
- skills (109 in .agents/skills)
- repo-wide source (none — no .py/.ts/.tsx/.js outside .agents/skills)
- docs (AGENTS.md, README.md, docs/**/*.md)
- memory (docs/memory, handoffs)
- packages (package.json workspaces)
- config (.agents/ROUTING.md, tsconfig, pyproject, etc.)
- top-level directories
- authoritative invokes (skill-graph.md + SKILL-INDEX.md)

EXTRACTED: 260 | INFERRED: 230

## Hub nodes
- universal-skill-creator
- validate-skills
- secure-skill
- improve-skills
- venture-exploration
- project-setup
- library-skill
- split-skill

## Communities

**experiment** (94): adversarial-hat, agent-builder, agent-launcher, agent-loom-sync, agent-system-architecture, api-and-interface-design, api-deprecation-and-migration, apply-paper-to-project, architectural-decision-log, assumption-mapping
  … +84 more
**svg** (13): app-security-hardening, browser-testing-with-devtools, ci-cd-and-automation, code-review-crsp, design-direction, design-review, design-system, frontend-design, gsap-animation, motion-animation
  … +3 more
**technical** (2): code-simplification, technical-debt-audit

## Node types

- **config**: 1
- **directory**: 3
- **doc**: 84
- **handoff**: 16
- **learning**: 2
- **memory**: 6
- **skill**: 109

See `GRAPH_REPORT.md` for surprising connections and suggested questions.

Full graph: `docs/knowledge-graph/graph.json`
Authoritative call edges: `docs/knowledge-graph/call-graph.json`
