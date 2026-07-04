# Git Workflow — Full Worked Examples

Source: addyosmani gap fill + conventional commits patterns (2026-06-01).

---

## Example 1 — Atomic commit

**Input:** Diff mixes feature + unrelated format

**Output:** Split commits:
```
feat(auth): add email validation on register
style(auth): format auth routes
```

One logical change per commit.

---

## Example 2 — Conventional message

```
fix(cart): prevent negative quantity in checkout

Root cause: parseInt without bounds check.
Regression test: cart.quantity.test.ts
```

Header ≤72 chars; body explains why.

---

## Example 3 — Breaking change

```
feat(api)!: remove legacy /v1/users endpoint

BREAKING CHANGE: clients must use /v2/users
```

---

## Example 4 — Skill improvement commit

```
improve: test-driven-development — 11/14 → 13/14

- Backfill references/examples.md from addyosmani patterns (secure-* SAFE)
Sources: addyosmani/agent-skills snapshot 2026-05-29
```
