---
name: incremental-implementation
description: >
  Deliver multi-file changes in thin vertical slices — implement, test, verify,
  commit, repeat. Load when implementing a feature from a plan, building across
  more than one file, refactoring, or when tempted to land a large change in one
  pass. Also triggers on "incremental implementation", "vertical slice",
  "thin slice", "one slice at a time", "don't do it all at once". Routes
  single-file fixes to direct execution. Pairs with test-driven-development and
  git-workflow-and-versioning.
license: MIT
metadata:
  author: dvy1987
  version: "1.0"
  category: project-specific
  sources: addyosmani/agent-skills incremental-implementation (11/12, 2026-05-29)
---

# Incremental Implementation

You ship multi-file work as a sequence of small, working slices. Each slice leaves the repo buildable and tests green.

## Hard Rules

Never write more than ~100 lines without running the project's test command.
Never mix unrelated concerns in one slice (feature + refactor + deps = separate slices).
Never expand scope beyond the current task — note adjacent issues; do not fix them.
Never skip verify because "you'll test at the end."
After each slice: test → verify → commit (see `git-workflow-and-versioning`).

---

## Workflow

### Step 1 — Confirm slice plan

Read the approved plan or task. Pick **one** slice: the smallest end-to-end path (vertical slice preferred). State what's in scope and explicitly out of scope for this slice.

### Step 2 — Implement one slice

Build only that slice. Prefer the simplest thing that could work — no abstractions before the third real use case.

### Step 3 — Test and verify

Run the project's test command. Run build/typecheck/lint if the change could affect them. Do not re-run the same command on unchanged code.

### Step 4 — Commit and pick next slice

Commit with a descriptive message (`git-workflow-and-versioning`). Repeat Steps 2–4 until the task is done.

### Step 5 — End-to-end check

Full test suite, build clean, feature matches spec/plan. Report slices completed and commits made.

---

## Slicing strategies

| Strategy | When |
|----------|------|
| **Vertical slice** (default) | One complete path through stack (e.g. create → API → UI) |
| **Contract-first** | Parallel FE/BE — define API contract first, then implement each side |
| **Risk-first** | Prove the riskiest integration before surrounding code |

---

## Gotchas

- A bug in slice 1 invalidates slices 2–5 — test each slice.
- "While I'm here" refactors belong in a separate commit, not this slice.
- Feature flags beat long-lived branches for incomplete user-visible work.
- Agents that skip verify to save time usually cost more time in debugging.

---

## Common Rationalizations

| Excuse | Reality |
|--------|---------|
| "I'll test everything at the end" | Failures compound; you won't know which slice broke. |
| "Faster to do it all at once" | Until one of 500 lines is wrong and you can't bisect. |
| "Too small to commit" | Small commits are free; giant commits are expensive to revert. |
| "I'll add the feature flag later" | Incomplete features must not be user-visible without a flag. |
| "Let me run tests again for reassurance" | Re-run only after code changed since last green run. |

---

## Output Format

```markdown
## Incremental implementation — [task/slug]

Slices planned: N | Completed: N
Current slice: [name] — [in scope / out of scope]

Verification:
- Tests: [command] → [pass/fail]
- Build: [command] → [pass/fail/skip]

Commits: [list or "pending user commit policy"]

Next slice: [one line] | Done
```

---

## Examples

<examples>
  <example>
    <input>Implement task creation from the plan — DB, API, and UI.</input>
    <output>
Slice 1 only: POST /tasks + migration + minimal form. Out of scope: list/edit/delete.
After `npm test` passes → commit `feat: add task creation endpoint and form`.
Next slice: list tasks.
    </output>
  </example>
</examples>

---

## Impact Report

```
Task: [slug] | Slices: N/M | Last verify: [pass/fail]
Commits: [count] | Scope expansions noted: [count]
```
