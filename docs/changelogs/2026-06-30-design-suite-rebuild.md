# Changelog: Design Skill Suite Rebuild

**Date:** 2026-06-30
**Type:** Suite rebuild — 5 skills → 4 skills (2 new, 2 rewritten, 3 deprecated), 11 reference assets + 1 script
**Goal:** Fix the two confirmed failures of the old suite — output was **generic** and **unpolished** — by moving from a ban-heavy, 4-doc-ceremony process to a taste-and-example-driven chain that mirrors how v0, Lovable, Anthropic's `frontend-design`, and Google's `DESIGN.md` actually get good results.

---

## Root cause of the old suite's bad output

1. **No exploration.** `design-archetype` picked exactly ONE archetype instantly — the #1 cause of sameness. Models converge on the corpus mean unless forced to compare distinct options.
2. **Taste encoded only as "Nevers."** No golden example code. Bans tell a model what to avoid, not what good looks like.
3. **Design intent scattered** across `ARCHETYPE.md` / `RESEARCH.md` / `TOKENS.md` / `ICONS.md` — no single source of truth, so each screen re-negotiated and drifted.
4. **Polish under-specified.** The build step was one paragraph; interactive/empty/loading/error states and motion specifics were left to chance.

---

## New architecture (4 skills)

| Skill | Status | Role |
|---|---|---|
| `frontend-design` | Rewritten (v2.0) | Orchestrator + builder. Stage 0 derives stack + context from product docs. Routes direction → system → build → review. Builds from golden examples with mandatory polish + state-coverage gates. Emits ONE `DESIGN.md`. |
| `design-direction` | **NEW** | The anti-generic gate. Sets a deliberate posture, generates **2-3 genuinely distinct directions**, compares side-by-side, commits to one (agent picks for non-technical owners). Absorbs the 12-archetype catalog as a starting palette. |
| `design-system` | **NEW** (replaces `design-tokens-craft` + `icon-craft`) | Canonical `DESIGN.md` + state-level tokens (8-step oklch ramp, every interactive state, focus ring, text-on-accent, **APCA**-validated) + icon strategy + component contracts, in the stack's token format. |
| `design-review` | Rewritten (v2.0) | 11-dimension rubric incl. **state coverage**; **APCA** contrast (not legacy WCAG) via bundled `apca.mjs`; state + polish + direction-fidelity gates. |

All four SKILL.md files are ≤200 lines (150 / 132 / 148 / 142).

## Where the taste now lives (the biggest change)

- **Golden component examples** — real, excellent code: `golden-examples/components.md` (button/input/card/badge, all states), `states.md` (empty/loading/error patterns), `composition.md` (non-default hero, app shell, staggered entrance).
- **`design-md-template.md`** — the canonical single-source-of-truth format.
- **`state-tokens.md`** — tokens "all the way down": neutral ramp, every state, focus ring, APCA targets, token tiers.
- **`polish-playbook.md`** — mandatory state coverage + concrete motion values + staggered-reveal recipe.
- **`stack-selection.md`** — product type → recommended stack; shadcn-as-primitives (not a drop-in look).
- **`apca-contrast.md` + `scripts/apca.mjs`** — perceptual contrast gate (tested: #1A1A1A on #FAFAF7 = Lc 101).

## No regression — salvaged content

The 12-archetype catalog + selection rubric were preserved into `design-direction/references/`. Token recipes, typography pairings, banned palettes, icon strategies, and SVG craft rules were preserved into `design-system/references/`. The anti-vibecoded checklist + build conventions stayed in `frontend-design/references/`. Nothing was discarded.

## Deprecations (archived, recoverable)

`design-archetype`, `design-tokens-craft`, `icon-craft` → `.agents/skills/.deprecated/*-deprecated-2026-06-30/` (trigger: fully subsumed). Each has a `DEPRECATION.md` + recovery command; logged in `deprecate-skill/references/deprecation-log.md`.

## Library plumbing updated

`AGENTS.md` entry points · `docs/SKILL-INDEX.md` (4 rewritten entries) · `docs/skill-graph.md` (subgraph + edges + orchestrator line) · `README.md` (skill table, count 98→97, suite blurb) · `docs/prd/PRD.md` (design rows). `.agents/ROUTING.md` and `docs/architecture.md` had no design references.

---

## How to use

| Trigger | What runs |
|---|---|
| "build a frontend / dashboard / landing page" | Full pipeline (`frontend-design`) |
| "give me design directions / explore some looks / make it feel like Linear" | `design-direction` |
| "build a design system / design tokens / create a DESIGN.md / pick icons" | `design-system` |
| "review this UI / does this feel like X" | `design-review` |

Output structure:
```
.design/<feature>/
  DIRECTION.md   <- design-direction (chosen + rejected options)
  REVIEW.md      <- design-review verdict + findings
DESIGN.md        <- design-system (single source of truth)
src/styles/tokens.css  <- generated tokens
src/...          <- the build (from golden examples)
```
