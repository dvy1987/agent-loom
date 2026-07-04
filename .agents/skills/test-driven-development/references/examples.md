# TDD — Full Worked Examples

Source: addyosmani/agent-skills `test-driven-development` (2026-05-29 snapshot). Security-scanned SAFE. Adapted for agent-loom (no external URLs).

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
Run tests → **FAIL** (function missing).

**GREEN — minimal implementation** until test passes.

**REFACTOR** — extract `generateId()`, shared types; re-run suite after each step.

---

## Example 2 — Prove-It Pattern (bug fix)

**Input:** "Completing a task doesn't set completedAt"

**Step 1 — reproduction test (must FAIL):**
```typescript
it('sets completedAt when task is completed', async () => {
  const task = await taskService.createTask({ title: 'Test' });
  const completed = await taskService.completeTask(task.id);
  expect(completed.status).toBe('completed');
  expect(completed.completedAt).toBeInstanceOf(Date); // fails → bug confirmed
});
```

**Step 2 — fix root cause** (not symptom).

**Step 3 — test PASSES; run full suite** — do not re-run identical command unless code changed.

---

## Example 3 — Subagent separation (complex bug)

**Input:** "Fix flaky checkout total"

**Main agent:** Spawn subagent — "Write a test reproducing: [bug]. Must fail on current code."

**Main agent:** Confirm failure → implement fix → confirm pass → full suite.

Separation keeps the test independent of the fix implementation.

---

## Example 4 — When NOT to use TDD

**Input:** "Fix typo in README" / "Update CI env var name in docs"

**Output:** No behavioral change → skip TDD; note in Impact Report: `TDD: not applicable (non-behavioral)`.
