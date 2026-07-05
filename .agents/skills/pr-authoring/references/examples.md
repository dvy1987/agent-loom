# PR Authoring — Examples

## Ex.1 — Feature PR after safe-change

**Input:** "Write PR for the null-guard fix we just verified"

**Output:**
```markdown
## PR draft — fix: guard parseConfig against null input

**Intent:** fix — prevent crash on missing config file

### Body
## Summary
- Add null guard to `parseConfig` before property access

## Why
Fixes #142 — crash when config file missing in CI

## Blast radius
| Area | Files | Risk | Notes |
|------|-------|------|-------|
| config | lib/config.ts | low | 2 callers, 1 test |

## Verification
- Typecheck: `npm run typecheck` → pass
- Tests: `npm test` → pass
- behaviorVerified: true
```

## Ex.2 — Split refactor from feature

**Input:** "I refactored the parser and added validation — one PR?"

**Output:**
```markdown
Split into two PRs (Agentic Refactoring finding):

PR 1 — `refactor: extract parseHeader from parseConfig`
PR 2 — `feat: validate config schema on load` (depends on PR 1)

Do not combine — reviewers cannot attribute regressions.
```
