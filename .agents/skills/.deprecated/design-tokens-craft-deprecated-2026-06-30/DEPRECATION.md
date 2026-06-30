# Deprecated: design-tokens-craft
Date: 2026-06-30
Reason: Fully subsumed (deprecation trigger 2) by `design-system`.
Evidence: Design Skill Suite rebuild plan. Design intent was scattered across separate
ARCHETYPE/TOKENS/ICONS docs; tokens stopped at the accent + a few greys and missed the
state-level depth (every interactive state, 8-step ramp, focus ring, text-on-accent, APCA)
where generic-ness actually lives. Merged with `icon-craft` into `design-system`, which
emits ONE canonical DESIGN.md + state-level tokens. Reference content (token-recipes,
typography-pairings, banned-palettes) salvaged into `design-system/references/`.
Migration: use `design-system` (tokens + icons + DESIGN.md + component contracts).
Callers updated: frontend-design (build-conventions), project-setup, AGENTS.md,
docs/SKILL-INDEX.md, docs/skill-graph.md, README.md.
Recovery: mv .agents/skills/.deprecated/design-tokens-craft-deprecated-2026-06-30/ .agents/skills/design-tokens-craft/
