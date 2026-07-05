# PR Conventions

From Agentic Refactoring empirical study (arXiv:2511.04824): **separate refactoring from behavior changes** and **state intent explicitly** in PR text.

---

## PR title

```
<type>: <imperative summary — max 72 chars>
```

Types: `feat` | `fix` | `refactor` | `test` | `docs` | `chore`

One primary intent per PR. If two intents, open two PRs.

---

## PR body template

```markdown
## Summary
[1-3 bullets — what changed, user-visible impact]

## Why
[Motivation, link to issue/spec/task]

## Blast radius
| Area | Files | Risk | Notes |
|------|-------|------|-------|
| [module] | [paths] | low/med/high | [callers/tests] |

## Verification
- Typecheck: `[command]` → [pass/fail]
- Tests: `[command]` → [pass/fail/skip]
- behaviorVerified: [true/false]

## Not in scope
- [Explicit exclusions to prevent scope creep questions]
```

---

## Commit separation rules

| Situation | Action |
|-----------|--------|
| Feature needs a small refactor first | Commit 1: `refactor:` (no behavior change). Commit 2: `feat:` |
| Formatting + logic | Commit 1: `chore: format`. Commit 2: `fix:` |
| Multiple unrelated fixes | One commit per fix, or separate PRs |

---

## Reviewer affordances

- Link `docs/specs/` or `docs/plans/` when the PR implements a planned change.
- Call out breaking changes in **Summary** first line.
- If `behaviorVerified: false`, state what manual check was done instead.
