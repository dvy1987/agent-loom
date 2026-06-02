# Comparison: frontend-design suite vs addyosmani/frontend-ui-engineering

**Date:** 2026-06-01  
**Asymmetric pair:** agent-loom **5 skills** (`frontend-design`, `design-archetype`, `design-tokens-craft`, `icon-craft`, `design-review`) vs AO **monolith**.

| Axis | agent-loom | addyosmani | Winner |
|---|---|---|---|
| Workflow specificity | 2/2 | 2/2 | tie |
| Hard rules | 2/2 | 1/2 | ours |
| Gotchas | 2/2 | 2/2 | tie |
| Examples | 2/2 | 2/2 | tie |
| Verification | 2/2 | 2/2 | tie |
| Anti-rationalization | 1/2 | 2/2 | theirs |
| **Total** | **11/12** | **11/12** | **KEEP OURS + MERGE patterns** |

## Per-axis notes

**Workflow specificity:** Ours: gated orchestration (archetype → tokens → icons → build → review) with fast/full/refactor paths. AO: component architecture, state management ladder, a11y patterns — excellent **implementation** recipes.

**Hard rules:** Ours bans vibecoded defaults (Inter, purple gradient, stock Lucide) with archetype justification. AO says "avoid AI aesthetic" but lacks archetype-first enforcement.

**Gotchas:** Both have AI-aesthetic tables (nearly identical intent). Ours is design-system-first; AO is React-pattern-first.

**Examples:** AO: container/presentation split, optimistic updates, skeleton loading. Ours: examples live across sub-skills + `references/`.

**Verification:** Ours `design-review` against "feels like X" claim; AO a11y + responsive breakpoint checklist. Complementary.

**Anti-rationalization:** AO table at monolith root; ours partial at orchestrator level.

## Verdict: KEEP OURS (suite) + MERGE BEST-OF-BOTH

For agent-loom's goal ("don't look vibecoded"), the **five-skill suite is the correct architecture** — it prevents agents from skipping archetype/tokens. AO content belongs in **references**, not a replacement monolith.

## Recommended actions

| P | Action | Target |
|---|--------|--------|
| P1 | Merge AO **AI aesthetic table** into anti-vibecoded checklist (dedupe with existing) | `frontend-design/references/anti-vibecoded-checklist.md` |
| P1 | Common Rationalizations on orchestrator | `frontend-design/SKILL.md` |
| P2 | Container/presentation + optimistic update patterns | `frontend-design/references/build-conventions.md` |
| P2 | AO a11y keyboard/focus/empty-state snippets where not redundant | `design-review/SKILL.md` or references |
| P3 | State management ladder (when to use context vs URL vs store) | `frontend-design/references/build-conventions.md` |
| — | Do **not** add `frontend-ui-engineering` or collapse suite | — |
