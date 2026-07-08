# Changelog — 2026-06-29 (addyosmani Phase 2 batch 3)

Significance: **MINOR** — four new daily-driver coding skills close the remaining addyosmani Phase 2 gaps.

## Added

- **`performance-optimization`** — teams with SLAs or slow pages can profile before changing code, with measure-first workflow and regression guards. Try: *"profile this slow page"* or *"fix LCP"*.
- **`shipping-and-launch`** — teams shipping to production get pre-launch checklists, staged rollout, monitoring, and rollback plans in one workflow. Try: *"pre-launch checklist"* or *"rollback strategy"*.
- **`api-deprecation-and-migration`** — engineers retiring APIs get graduated deprecation and migration guides distinct from skill-library `deprecate-skill`. Try: *"sunset this endpoint"* or *"strangler migration"*.
- **`browser-testing-with-devtools`** — UI work can be verified in a real browser via Chrome DevTools MCP (DOM, console, network, screenshots). Try: *"check console errors"* or *"browser testing with DevTools"*.

## Changed

- Library inventory **98 → 102 skills** (69 project-specific). `docs/SKILL-INDEX.md`, `README.md`, `AGENTS.md`, `docs/skill-graph.md`, and `docs/prd/PRD.md` synced via `library-skill`.

## Test plan

- [ ] `agentskills validate .agents/skills/<each-new-skill>/` passes
- [ ] Trigger phrases route correctly (no collision with `deprecate-skill` or `secure-skill`)
- [ ] `browser-testing-with-devtools` defers gracefully when chrome-devtools MCP is unavailable
