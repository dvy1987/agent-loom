# Knowledge Graph Report

Generated: 2026-07-04T11:20:54.519448+00:00
Mode: skill-library | Nodes: 207 | Edges: 463

**Why this mode:** skill-library label: docs/skill-graph.md + docs/SKILL-INDEX.md present → adds authoritative skill invoke edges. Still scans full repo (not skills-only).

## God nodes (skills + modules)
- universal-skill-creator
- validate-skills
- secure-skill
- improve-skills
- venture-exploration
- library-skill
- split-skill
- feature-spec
- experimentation
- project-setup

## Surprising cross-community connections
- project-orchestrator → skill-routing (invokes: project ↔ skill)
- project-orchestrator → process-decomposer (invokes: project ↔ process)
- publish-skill → validate-skills (invokes: publish ↔ validate)
- publish-skill → improve-skills (invokes: publish ↔ improve)
- customer-discovery → venture-exploration (invokes: customer ↔ venture)
- reality-check → assumption-mapping (invokes: reality ↔ assumption)
- reality-check → adversarial-hat (invokes: reality ↔ adversarial)
- business-modeling → venture-exploration (invokes: business ↔ venture)

## Suggested questions
- How does project-orchestrator (project) connect to skill-routing (skill)?
- How does project-orchestrator (project) connect to process-decomposer (process)?
- How does publish-skill (publish) connect to validate-skills (validate)?
- What depends on universal-skill-creator, and what does universal-skill-creator invoke?
- What depends on validate-skills, and what does validate-skills invoke?
- What depends on secure-skill, and what does secure-skill invoke?

## Provenance
- Authoritative invokes: 217
- EXTRACTED: 239 | INFERRED: 224

Query: `python3 .agents/skills/knowledge-graph/scripts/query_graph.py path <A> <B>`
