# Knowledge Graph Report

Generated: 2026-07-05T07:19:35.386594+00:00
Mode: skill-library | Nodes: 237 | Edges: 515

**Why this mode:** skill-library label: docs/skill-graph.md + docs/SKILL-INDEX.md present → adds authoritative skill invoke edges. Still scans full repo (not skills-only).

## God nodes (skills + modules)
- universal-skill-creator
- validate-skills
- secure-skill
- improve-skills
- project-setup
- venture-exploration
- retroactive-project-setup
- library-skill
- split-skill
- feature-spec

## Surprising cross-community connections
- project-orchestrator → skill-routing (invokes: project ↔ skill)
- project-orchestrator → process-decomposer (invokes: project ↔ process)
- motion-animation → svg-creation (invokes: motion ↔ svg)
- publish-skill → validate-skills (invokes: publish ↔ validate)
- publish-skill → improve-skills (invokes: publish ↔ improve)
- customer-discovery → venture-exploration (invokes: customer ↔ venture)
- harness-evolution → eval-pipeline (invokes: harness ↔ eval)
- reality-check → assumption-mapping (invokes: reality ↔ assumption)

## Suggested questions
- How does project-orchestrator (project) connect to skill-routing (skill)?
- How does project-orchestrator (project) connect to process-decomposer (process)?
- How does motion-animation (motion) connect to svg-creation (svg)?
- What depends on universal-skill-creator, and what does universal-skill-creator invoke?
- What depends on validate-skills, and what does validate-skills invoke?
- What depends on secure-skill, and what does secure-skill invoke?

## Provenance
- Authoritative invokes: 240
- EXTRACTED: 272 | INFERRED: 243

Query: `python3 .agents/skills/knowledge-graph/scripts/query_graph.py path <A> <B>`
