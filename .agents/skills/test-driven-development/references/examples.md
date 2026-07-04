# Test-Driven Development — Full Session Examples

Read when you need a complete walkthrough beyond the inline teaser in SKILL.md.

Prove-It, regression, and RED-GREEN-REFACTOR walkthroughs. Deep patterns: `references/tdd-patterns.md`.

---

## Example 1 — RED-GREEN-REFACTOR (new behavior)

**Input:** "Add task creation to TaskService"

**RED — failing test first:**
```typescript
it('creates a task with title and default status', async () => {
  const task = await taskService.createTask({ title: 'Buy groceries' });
  expect(task.id).toBeDefined();
  expect(task.title).toBe('Buy groceries');
  expect(task.status).toBe('pending');
  expect(task.createdAt).toBeInstanceOf(Date);
});
```
Run: `npm test -- taskService.test.ts` → **FAIL** (`createTask is not a function`).

**GREEN — minimal implementation** until test passes.

**REFACTOR** — extract `generateId()`, shared types; re-run suite after each step.

---

## Example 2 — Prove-It Pattern (bug fix, full cycle)

**Input:** "Completing a task doesn't set completedAt"

**Step 1 — contract:** "When a task is completed, `completedAt` is set and status is `completed`."

**Step 2 — reproduction test (must FAIL on main):**
```typescript
it('regression: completeTask sets completedAt', async () => {
  const task = await taskService.createTask({ title: 'Test' });
  const completed = await taskService.completeTask(task.id);
  expect(completed.status).toBe('completed');
  expect(completed.completedAt).toBeInstanceOf(Date); // fails: undefined
});
```
Run: `npm test -- --grep "completedAt"` → **FAIL** (`expected Date, got undefined`).

**Step 3 — fix root cause** in `completeTask` (not a wrapper that hides the field).

**Step 4 — test PASSES**; run `npm test` full suite.

**Step 5 — add sibling edge case:**
```typescript
it('completeTask is idempotent for already-completed tasks', async () => {
  const task = await taskService.createTask({ title: 'Done' });
  const first = await taskService.completeTask(task.id);
  const second = await taskService.completeTask(task.id);
  expect(second.completedAt).toEqual(first.completedAt);
});
```

---

## Example 3 — Prove-It on Python / pytest

**Input:** "CSV export truncates at 1000 rows"

```python
def test_regression_export_includes_all_rows(db_session):
    seed_projects(db_session, count=1500)
    csv = export_projects_csv()
    assert csv.count("\n") >= 1500  # fails at 1000 on main
```

Run: `pytest tests/export/test_csv.py::test_regression_export_includes_all_rows -v`

---

## Example 4 — Parameterized regression matrix

**Input:** "Login validation broken for edge emails"

```typescript
describe('login validation regression', () => {
  it.each([
    ['', 400, 'empty email'],
    ['not-an-email', 400, 'malformed'],
    ['user@example.com', 200, 'valid'],
  ])('%s → %i (%s)', async (email, status) => {
    const res = await request(app).post('/login').send({ email, password: 'x' });
    expect(res.status).toBe(status);
  });
});
```

---

## Example 5 — Subagent separation (complex bug)

**Input:** "Fix flaky checkout total"

**Main agent:** Spawn subagent — "Write a test reproducing: total doubles when coupon applied twice. Must fail on current code."

**Main agent:** Confirm failure → implement fix → confirm pass → `npm test`.

Separation keeps the test independent of the fix implementation.

---

## Example 6 — Bisect + Prove-It

**Input:** "Export broke sometime after v2.1"

```bash
git bisect start
git bisect bad HEAD
git bisect good v2.1.0
git bisect run npm test -- --grep "regression export"
```

Once bisect names the commit, write Prove-It test on main that fails without the fix cherry-pick.

---

## Example 7 — When NOT to use TDD

**Input:** "Fix typo in README" / "Update CI env var name in docs"

**Output:** No behavioral change → skip TDD; note in Impact Report: `TDD: not applicable (non-behavioral)`.

---

## Example 8 — Review gate (pairs with code-review-crsp)

**Input:** PR fixes login 500 without new test

**Output:** Request changes — "Bug fix must include Prove-It regression per `test-driven-development/references/tdd-patterns.md`."
---

## Verification checklist (full session)

- [ ] Examples demonstrate SKILL.md hard rules, not generic chat
- [ ] Deep reference file cited and used (patterns / triage / conventions / schemas / prompts / ui-patterns)
- [ ] Reader can trace input → concrete agent actions → durable outcome
- [ ] Cross-skill links honored (TDD↔debug↔review, design suite chain)

