# Knowledge Graph Report

Generated: 2026-07-04T05:58:56.559707+00:00
Mode: skill-library | Nodes: 128 | Edges: 451

## God nodes (skill connectivity)
- universal-skill-creator
- validate-skills
- improve-skills
- secure-skill
- venture-exploration
- library-skill
- split-skill
- experimentation
- learn-from
- feature-spec

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
- What depends on improve-skills, and what does improve-skills invoke?

## Provenance
- Authoritative invokes: 170
- EXTRACTED: 225 | INFERRED: 226

Query: `python3 .agents/skills/knowledge-graph/scripts/query_graph.py path <A> <B>`
