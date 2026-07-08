# Knowledge Graph Report

Generated: 2026-07-08T08:38:53.632244+00:00
Mode: skill-library | Nodes: 707 | Edges: 562

**Why this mode:** skill-library label: docs/skill-graph.md + docs/SKILL-INDEX.md present → adds authoritative skill invoke edges. Still scans full repo (not skills-only).

## God nodes (skills + modules)
- universal-skill-creator
- validate-skills
- secure-skill
- improve-skills
- project-setup
- retroactive-project-setup
- library-skill
- venture-exploration
- memory-capture
- experimentation

## Surprising cross-community connections
- agent-builder → harness-generation (invokes: agent ↔ harness)
- agent-builder → setup-evaluation (invokes: agent ↔ setup)
- agent-loom-sync → validate-skills (invokes: agent ↔ validate)
- apply-paper-to-project → learn-from-paper (invokes: apply ↔ learn)
- architectural-decision-log → memory-decision (invokes: architectural ↔ memory)
- brainstorming → feature-spec (invokes: core ↔ feature)
- brainstorming → venture-exploration (invokes: core ↔ venture)
- business-modeling → venture-exploration (invokes: business ↔ venture)

## Suggested questions
- How does agent-builder (agent) connect to harness-generation (harness)?
- How does agent-builder (agent) connect to setup-evaluation (setup)?
- How does agent-loom-sync (agent) connect to validate-skills (validate)?
- What depends on universal-skill-creator, and what does universal-skill-creator invoke?
- What depends on validate-skills, and what does validate-skills invoke?
- What depends on secure-skill, and what does secure-skill invoke?

## Provenance
- Authoritative invokes: 256
- EXTRACTED: 291 | INFERRED: 271

Query: `python3 .agents/skills/knowledge-graph/scripts/query_graph.py path <A> <B>`
