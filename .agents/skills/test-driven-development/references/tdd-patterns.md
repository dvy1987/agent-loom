# TDD Patterns (reference)

Read when implementing non-trivial logic, bug fixes, or test suite design. Sourced from addyosmani/agent-skills patterns; adapted for agent-loom.

---

## Prove-It Pattern (bug fixes) — full protocol

**Rule:** No production change until a test fails for the *right reason* on current code.

### Steps

1. **Name the contract** — one sentence: "When X, system must Y."
2. **Write the repro test** — minimal input that triggers the bug; assert the contract.
3. **Run and confirm RED** — failure must match the bug (not import error, not wrong assertion).
4. **Fix root cause** — smallest production change; no drive-by refactors.
5. **Confirm GREEN** — repro test passes.
6. **Regression guard** — keep the test; add edge-case siblings if the fix was narrow.
7. **Full suite** — `[project test command]`; do not re-run identical command if nothing changed.

### Prove-It checklist

```markdown
- [ ] Test fails on main BEFORE fix
- [ ] Failure message matches reported bug (not tangential)
- [ ] Fix addresses root cause, not symptom
- [ ] Test passes after fix
- [ ] Full suite green
- [ ] Test name documents the contract permanently
```

### When the bug is intermittent

- Narrow with `it.only` / `pytest -k` / `npm test -- --grep` until deterministic.
- If still flaky: log env (Node version, TZ, race window); use fake timers or await boundaries.
- **Do not** merge a fix without a test that failed first — file a follow-up repro task if blocked.

### Prove-It vs characterization

| Situation | Approach |
|-----------|----------|
| Known bug report | Prove-It repro → fix → guard |
| Legacy code, no tests | Characterization test on current behavior → refactor → tighten assertions |
| Regression after deploy | Bisect + Prove-It on the offending commit range |

---

## Regression patterns

### 1. Golden-path guard

One test per user-visible path that broke. Name: `regression: [ticket] — [one-line contract]`.

```typescript
it('regression: HID-42 — export includes rows beyond 1000', async () => {
  const rows = await seedRows(1500);
  const csv = await exportCSV({ datasetId: rows.id });
  expect(csv.split('\n').length).toBeGreaterThan(1000);
});
```

### 2. Parameterized edge matrix

Same contract, many inputs — table-driven to avoid copy-paste suites.

```python
@pytest.mark.parametrize("email,expected_status", [
    ("", 400),
    ("not-an-email", 400),
    ("user@example.com", 200),
])
def test_login_validation(email, expected_status):
    assert client.post("/login", json={"email": email}).status_code == expected_status
```

### 3. Contract snapshot (behavior, not markup)

Snapshot **stable API responses** or **parsed structures** — never whole DOM trees without review.

### 4. Time-travel / seed regression

DB or fixture seed frozen; test asserts invariant after operation. Critical for billing, permissions, idempotency.

### 5. Bisect-assisted regression

When failure appeared between releases:

```bash
git bisect start
git bisect bad HEAD
git bisect good v1.2.0
# run targeted test each step; git bisect run npm test -- --grep "regression HID-42"
```

---

## Test pyramid

~80% unit (small, ms) · ~15% integration (boundaries, seconds) · ~5% E2E (critical paths only).

| Layer | Proves | Avoid |
|-------|--------|-------|
| Unit | Pure logic, branches, edge cases | Mocking the subject under test |
| Integration | DB, HTTP client, module boundaries | Full browser |
| E2E | Login → pay → receipt | Every button click |

**Agent rule:** If you only wrote E2E for a pure function, you tested the framework.

---

## State vs interaction tests

Assert **outcomes** (return values, DB state, HTTP status + body), not internal call order — survives refactors.

```typescript
// Bad — interaction test (breaks on refactor)
expect(mockRepo.save).toHaveBeenCalledWith({ title: 'x' });

// Good — state test
const task = await repo.findById(id);
expect(task.title).toBe('x');
```

Use interaction tests **only** at system boundaries (email sent, payment charged) with fakes.

---

## DAMP over DRY in tests

Each test should read as a standalone spec. Duplication in tests is acceptable when it aids clarity.

```typescript
// Good DAMP — reader sees full setup in one place
it('rejects duplicate slug on create', async () => {
  await createProject({ slug: 'alpha' });
  await expect(createProject({ slug: 'alpha' })).rejects.toThrow('slug taken');
});
```

---

## Test double preference

1. **Real** implementation (in-memory SQLite, testcontainers for CI)
2. **Fake** (in-memory store implementing same interface)
3. **Stub** (canned responses)
4. **Mock** (sparingly — verify calls only at boundaries: email, payments, webhooks)

---

## Arrange–Act–Assert

One concept per test. Name tests as specifications:

- `it('rejects empty titles')`
- `test_login_returns_401_for_wrong_password`

If the name needs "and", split the test.

---

## Command recipes

Replace placeholders with project commands:

```bash
# Full suite
npm test | pytest | cargo test | go test ./...

# Focus one file
npm test -- path/to/file.test.ts
pytest tests/auth/test_login.py -v

# Focus one case
npm test -- --grep "rejects empty"
pytest -k "empty_email"

# Watch mode (only while actively developing — not for verification gates)
npm test -- --watch
```

**Do not** re-run the full suite on unchanged code to "be sure."

---

## Anti-patterns

| Anti-pattern | Fix |
|---|---|
| Testing framework behavior | Test your code only |
| Snapshot abuse | Review every snapshot change |
| Flaky timing tests | Fake timers, `waitFor`, deterministic seeds |
| Mocking everything | Prefer real/fake deps |
| Green before Red on new behavior | Write failing test first |
| Bug fix without repro test | Prove-It Pattern mandatory |
| Testing a mock's own configured behavior | Assert on the code under test's reaction, not the mock — a mock "passing" proves nothing |
| Test-only methods/hooks added to production classes | Test through the real public interface; if it can't be tested that way, the design needs a seam, not a backdoor |
| Retrofitting a test onto code written first | Delete the code; rewrite from Red — a post-hoc test confirms the implementation, not the contract |

---

## Cross-skill links

- **UI/layout bugs:** `browser-testing-with-devtools` — unit tests alone miss CSS/runtime.
- **Debug workflow:** `debug-and-fix` Step 5 requires regression test after fix.
- **In-flight doubt:** `adversarial-hat` — failing repro satisfies DOUBT for behavioral claims.
- **Code review:** `code-review-crsp` — review tests first; flag missing Prove-It on bug fixes.
