# Deprecated: icon-craft
Date: 2026-06-30
Reason: Fully subsumed (deprecation trigger 2) by `design-system`.
Evidence: Design Skill Suite rebuild plan. Icon strategy is one facet of a coherent design
system, not a standalone step — splitting it fragmented design intent across multiple docs.
Folded into `design-system` (icon strategy: one family, stroke matched to type weight).
Reference content (icon-strategies, svg-craft) salvaged into `design-system/references/`.
Migration: use `design-system` (icon strategy is Step 6 + its references).
Callers updated: frontend-design (build-conventions, one-shot-flow), project-setup,
AGENTS.md, docs/SKILL-INDEX.md, docs/skill-graph.md, README.md.
Recovery: mv .agents/skills/.deprecated/icon-craft-deprecated-2026-06-30/ .agents/skills/icon-craft/
