# Incremental Implementation — Full Worked Examples

Source: addyosmani vertical-slice patterns via agent-loom gap fill (2026-06-01).

---

## Example 1 — Thin vertical slice

**Input:** "Implement user registration from approved plan"

**Slice 1:** API happy path only — deployable, tested, no email yet.
**Slice 2:** Validation errors.
**Slice 3:** Verification email.

Each slice: mergeable, tests green, demoable.

---

## Example 2 — vs big-bang

**Wrong:** Build all layers (DB + API + UI + email) before any test.

**Right:** POST /register works end-to-end with mock UI or curl before polish.

---

## Example 3 — Pair with TDD

Each slice starts with failing test (see `test-driven-development/references/examples.md`).

---

## Example 4 — Stop on crosscheck fail

Plan says slice 2; crosscheck FAIL on spec drift → fix spec/plan before more code.
