# Deprecated: design-archetype
Date: 2026-06-30
Reason: Fully subsumed (deprecation trigger 2) by the rebuilt design suite.
Evidence: Design Skill Suite rebuild plan (design-skills-rebuild). The old skill picked
exactly ONE archetype instantly and skipped exploring distinct directions — the #1 cause of
generic AI output. Replaced by `design-direction`, which explores 2-3 genuinely distinct
directions and commits to one. The 12-archetype catalog + selection rubric were salvaged
into `design-direction/references/` (archetypes/ + selection-rubric.md) as a starting
posture palette — no taste content lost.
Migration: use `design-direction` (it absorbs the archetype catalog as a starting palette).
Callers updated: frontend-design (SKILL + one-shot-flow), project-setup (template +
architecture-design-rigor), AGENTS.md, docs/SKILL-INDEX.md, docs/skill-graph.md, README.md.
Recovery: mv .agents/skills/.deprecated/design-archetype-deprecated-2026-06-30/ .agents/skills/design-archetype/
