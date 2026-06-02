# TDD Patterns (reference)

Read when implementing non-trivial logic, bug fixes, or test suite design. Sourced from addyosmani/agent-skills patterns; adapted for agent-loom.

## Prove-It Pattern (bug fixes)

1. Write a test that reproduces the bug → must **fail**
2. Implement minimal fix → test **passes**
3. Run full suite → no regressions

## Test pyramid

~80% unit (small, ms) · ~15% integration (boundaries, seconds) · ~5% E2E (critical paths only).

## State vs interaction tests

Assert **outcomes** (return values, DB state), not internal method call order — survives refactors.

## DAMP over DRY in tests

Each test should read as a standalone spec. Duplication in tests is acceptable when it aids clarity.

## Test double preference

1. Real implementation → 2. Fake (in-memory) → 3. Stub (canned data) → 4. Mock (sparingly; boundary only)

## Arrange–Act–Assert

One concept per test. Name tests as specifications: `it('rejects empty titles')`.

## Anti-patterns

| Anti-pattern | Fix |
|---|---|
| Testing framework behavior | Test your code only |
| Snapshot abuse | Review every snapshot change |
| Flaky timing tests | Deterministic assertions, isolated state |
| Mocking everything | Prefer real/fake deps |

## Browser verification

For UI changes, cross-link `browser-testing-with-devtools` when available — unit tests alone are insufficient for layout/CSS/runtime bugs.
