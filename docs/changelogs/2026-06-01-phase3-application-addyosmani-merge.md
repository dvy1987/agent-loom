# Changelog — Phase 3 Application (addyosmani craft merge)

**Date:** 2026-06-01  
**Type:** MINOR (skill content upgrades, no new skills)

## Summary

Applied Phase 3 comparison recommendations: merged addyosmani craft patterns into existing agent-loom skills without duplicating orchestrator architecture or adding conflicting gap skills.

## Meta-layer

- `validate-skills` — P2 flags for missing Common Rationalizations and Verification checklists on `project-specific` skills
- `universal-skill-creator` — requires both sections for new `project-specific` skills

## Skills upgraded

- `test-driven-development` — Prove-It Pattern, rationalizations, verification, `references/tdd-patterns.md`
- `debug-and-fix` — stop-the-line, triage skeleton, untrusted errors, regression-test rule
- `code-review-crsp` — five-axis review, comment prefixes, change sizing
- `implementation-plan` — vertical slices, `references/plan-schemas.md`
- `brainstorming` — HMW, Not Doing, assumptions, venture routing
- `adversarial-hat` — in-flight doubt loop, `references/adversarial-prompt.md`
- `spec-driven-development` — rationalizations, when-not-to-use heuristic
- `feature-spec` — reframe vague requirements step
- `frontend-design` — rationalizations; build-conventions patterns

## Not done (still Phase 2)

Gap skills: `source-driven-development`, `code-simplification`, `api-and-interface-design`, and remainder per `docs/comparisons/2026-06-01-SUMMARY.md`.
