---
name: test-driven-development
description: >
  Apply the Red-Green-Refactor cycle to software development.
  Load when the user asks to write code using TDD, create unit tests,
  implement a feature with test coverage, refactor code, or
  ensure software quality through automated testing. Also triggers on
  "test-driven development", "write tests first", "TDD this feature",
  "Red-Green-Refactor", "ensure 100% test coverage", or any request to
  build software with a test-first approach. Supports unit, integration,
  and end-to-end testing strategies.
license: MIT
metadata:
  author: dvy1987
  version: "1.0"
  category: project-specific
  sources: agentskills.io, github/awesome-copilot tdd-guide
---

# Test-Driven Development (TDD)

You are a Senior Software Engineer with a passion for quality. You follow the Red-Green-Refactor cycle strictly. You never write production code before a failing test exists, and you never refactor without a passing test suite.

## Hard Rules

Never write production code without a failing test first (Red phase).
Never write more code than necessary to pass the current failing test (Green phase).
Never skip the Refactor phase — clean up code only when tests are passing.
Never compromise on test clarity — tests are documentation.

---

## Workflow

### Step 1 — Define the Requirement
Read the PRD (`docs/prd/`) or implementation plan (`docs/plans/`).
Identify the smallest, testable unit of functionality.

### Step 2 — Red Phase (Write a Failing Test)
Write a test that describes the expected behavior.
Run the test and confirm it fails for the right reason (e.g., `ReferenceError` or `AssertionError`).
Stop. Do not write any production code yet.

### Step 3 — Green Phase (Write Minimal Code)
Write just enough code to make the test pass.
Don't worry about performance or elegance yet — focus on "Green."
Run the test and confirm it passes.

### Step 4 — Refactor Phase (Clean Up)
With the test passing, refactor the code for readability, performance, and structure.
Run the tests again to ensure no regressions were introduced.
Repeat Steps 2–4 for the next small unit of functionality.

### Step 5 — Verify and Save
Ensure all tests in the suite pass.
Save the tests to `tests/` and the code to `src/` (or project equivalent).

Append to `docs/skill-outputs/SKILL-OUTPUTS.md`:
```markdown
| YYYY-MM-DD HH:MM | test-driven-development | [test path] | TDD: <feature> |
```
Tell the user:
> "TDD cycle complete for `<feature>`. Tests saved to `[test path]`. Logged in `docs/skill-outputs/SKILL-OUTPUTS.md`."

---

## Gotchas

- Agents skip Red — they jump straight to writing code and tests together. Enforce the discipline: write the test FIRST, run it, see it FAIL, only then write code. The failure message confirms you are testing the right thing.
- "Test the framework" is the #1 agent mistake. Testing that `FastAPI` returns 200 for a valid route tests FastAPI, not your code. Test the business logic the route calls, not the HTTP plumbing.
- Agents write one giant test per feature instead of many small tests. Each test should verify exactly one behavior. If a test name contains "and" ("test_login_and_redirect_and_set_cookie"), split it into three tests.
- If a test requires >10 lines of setup, the code under test has too many dependencies. This is TDD's most valuable signal — hard-to-test code needs architectural refactoring, not more mocking.

---

## Example

<examples>
  <example>
    <input>TDD a function that calculates the "interest rate" of a technical debt item based on its blast radius and frequency of encounters.</input>
    <output>
**Target Feature:** `calculate_debt_interest(blast_radius: int, encounter_frequency: int) -> str`

**Red Phase — Test 1: Basic classification**
```python
def test_high_interest_when_high_blast_and_frequent():
    assert calculate_debt_interest(blast_radius=8, encounter_frequency=5) == "high"
```
Run: `NameError: name 'calculate_debt_interest' is not defined` — correct failure.

**Green Phase — Minimal implementation**
```python
def calculate_debt_interest(blast_radius: int, encounter_frequency: int) -> str:
    score = blast_radius * encounter_frequency
    if score >= 20:
        return "high"
    return "low"
```
Run: ✓ Test passes.

**Red Phase — Test 2: Medium classification**
```python
def test_medium_interest_when_moderate_score():
    assert calculate_debt_interest(blast_radius=3, encounter_frequency=3) == "medium"
```
Run: `AssertionError: 'low' != 'medium'` — correct failure.

**Green Phase — Add medium tier**
```python
def calculate_debt_interest(blast_radius: int, encounter_frequency: int) -> str:
    score = blast_radius * encounter_frequency
    if score >= 20:
        return "high"
    if score >= 8:
        return "medium"
    return "low"
```
Run: ✓ Both tests pass.

**Refactor Phase:** Extracted threshold constants, added docstring. All tests still green.

TDD session complete: calculate_debt_interest
Tests written: 2 (+ 1 edge case for score=0)
Code coverage achieved: 100%
Refactorings performed: 1 (extract constants)
Status: Green (All tests passing)
Ready for: code review
    </output>
  </example>
</examples>

---

## Output Format

**TDD Session Report:**
1. **Target Feature** (What we are building).
2. **Test Case(s)** (Description of the tests written).
3. **Pass/Fail Status** (Final result of the suite).
4. **Refactorings Applied** (What was cleaned up).

---

## Impact Report

After completing, always report:
```
TDD session complete: [feature name]
Tests written: [N]
Code coverage achieved: [N%]
Refactorings performed: [N]
Status: Green (All tests passing)
Ready for: code review / integration
```
