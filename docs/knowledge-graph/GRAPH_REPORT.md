# Knowledge Graph Report

Generated: 2026-07-04T02:52:36.403032+00:00
Mode: skill-library | Nodes: 125 | Edges: 434

## God nodes (skill connectivity)
- universal-skill-creator
- validate-skills
- secure-skill
- improve-skills
- library-skill
- experimentation
- split-skill
- learn-from
- feature-spec
- spec-driven-development

## Surprising cross-community connections
- project-orchestrator → skill-routing (invokes: project ↔ skill)
- project-orchestrator → process-decomposer (invokes: project ↔ process)
- publish-skill → validate-skills (invokes: publish ↔ validate)
- publish-skill → improve-skills (invokes: publish ↔ improve)
- reality-check → assumption-mapping (invokes: reality ↔ assumption)
- reality-check → adversarial-hat (invokes: reality ↔ adversarial)
- split-skill → improve-skills (invokes: split ↔ improve)
- split-skill → compress-skill (invokes: split ↔ compress)

## Suggested questions
- How does project-orchestrator (project) connect to skill-routing (skill)?
- How does project-orchestrator (project) connect to process-decomposer (process)?
- How does publish-skill (publish) connect to validate-skills (validate)?
- What depends on universal-skill-creator, and what does universal-skill-creator invoke?
- What depends on validate-skills, and what does validate-skills invoke?
- What depends on secure-skill, and what does secure-skill invoke?

## Provenance
- Authoritative invokes: 170
- EXTRACTED: 218 | INFERRED: 216

Query: `python3 .agents/skills/knowledge-graph/scripts/query_graph.py path <A> <B>`
