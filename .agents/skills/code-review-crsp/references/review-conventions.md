# Code Review Conventions (reference)

Five-axis frame, comment prefixes, change sizing, dead-code hygiene, and merge gates. Sourced from addyosmani `code-review-and-quality` + agent-loom CRSP workflow.

---

## Five-axis review (deep frame)

Evaluate **every** changed file against all five. Missing an axis is a review failure.

### 1. Correctness

- Logic errors, off-by-one, null/undefined paths
- Error handling: are failures surfaced or swallowed?
- Spec/PRD alignment — does behavior match acceptance criteria?
- Edge cases: empty input, max bounds, concurrent access
- **Tests:** do they assert behavior or implementation? Would they catch a revert?

**Questions to ask:**
- What happens if this returns null?
- What if the API is slow or returns 500?
- Does this change break an existing caller?

### 2. Readability

- Names reveal intent (`userId` not `id` in multi-entity files)
- Control flow flat — early returns over nested pyramids
- No unearned cleverness (meta-programming, dense one-liners)
- Comments explain *why*, not *what*
- File length — if a file grew 200+ lines, should it split?

### 3. Architecture

- Fits existing patterns (or documents intentional deviation)
- Appropriate abstraction — not premature interface for one impl
- Hidden coupling: globals, singletons, implicit ordering
- Dependency direction — domain should not import UI
- **Dead code:** orphans after refactor? list and ask before delete

### 4. Security

- Input validation at trust boundaries
- AuthZ: can user A act on user B's resource?
- Secrets: none in source, logs, or tests
- Injection: SQL, shell, HTML, path traversal
- Untrusted external data — same rules as `debug-and-fix` triage reference
- Cross-link `app-security-hardening` for auth/crypto/OWASP depth

### 5. Performance

- N+1 queries, unbounded `SELECT *`, missing pagination
- Sync I/O in hot paths
- Missing indexes on new query patterns
- Bundle size — accidental heavy imports
- Caching invalidation correctness

---

## Review order (mandatory)

1. Read diff scope (`git diff`, branch, or named files)
2. **Read tests first** — they reveal intent and coverage gaps
3. Read production changes with test context
4. Read upstream spec/issue if linked
5. Compile findings by severity

---

## Comment prefix system

Use exactly one prefix per finding so authors know merge requirements.

| Prefix | Merge rule | Example |
|--------|------------|---------|
| **Critical:** | **Blocks merge** — security, data loss, broken production behavior | `Critical: auth bypass — session user not checked against resource owner` |
| *(none)* | **Required** — correctness, missing tests, broken contract | `Missing 404 when profile deleted — add test` |
| **Optional:** / **Consider:** | Should fix — maintainability, minor perf | `Consider: extract shared validator from auth.ts` |
| **Nit:** | Style — author may ignore | `Nit: rename data → profile in return` |
| **FYI** | Context only — no action | `FYI: this mirrors pattern in billing v2` |

### Finding format

```
N. [axis] (severity) — [file](path#L42): one-line summary
```

Group output: Critical → High → Medium → Low.

---

## Change sizing & split strategies

| Lines changed | Guidance |
|---------------|----------|
| ~100 | Ideal — review in one pass |
| ~300 | Acceptable if one logical change |
| ~1000+ | **Request split** before deep review |

### Split patterns

1. **Refactor then feature** — behavior-neutral refactor PR first, feature second
2. **Vertical slice** — one user path per PR (schema + API + UI for one action)
3. **Mechanical vs semantic** — rename/move PR separate from logic change

When asking for split, name the cut lines: "PR1: extract `validateUserId`; PR2: add profile endpoint."

---

## Dead code hygiene (Step 4 extension)

After refactors, explicitly search:

```bash
git diff --name-only | xargs -I{} grep -l "OldFunctionName" {}
```

- List orphaned exports, unused components, stale feature flags
- **Ask author** before deleting — may be used dynamically or in unreleased branch
- Flag `// TODO remove` older than one sprint as **Optional:** cleanup

---

## AI-generated code scrutiny

Do not rubber-stamp agent-written diffs. Extra checks:

- [ ] Security axis on all auth/input paths
- [ ] Tests run by reviewer (or CI) — not "should pass"
- [ ] No hallucinated APIs — grep repo for called symbols
- [ ] Architecture fits — agents love new patterns per file

---

## Verify the verification

Before **Approve**:

- [ ] Author ran tests — or reviewer ran `[project test command]` and reports result
- [ ] All **Critical** and un-deferred **High** resolved
- [ ] Bug-fix PRs include Prove-It regression (`test-driven-development`)
- [ ] No disabled/skipped tests to green the suite

---

## Multi-model review (optional, user-triggered)

For high-risk PRs (auth, payments, migrations):

1. Complete five-axis review in current session
2. Offer: "Want a second model to review the same diff cold?"
3. Pass **diff + contract only** — not prior review conclusions (avoids anchoring)
4. Reconcile disagreements; escalate conflicts to user

Skip in CI/non-interactive — note in report: `Second opinion: skipped (non-interactive)`.

---

## Verdict templates

```markdown
## Code Review — [scope]

### Critical
(none | numbered list)

### High
...

### Medium / Low
...

---
Files reviewed: N
Issues found: critical: N, high: N, medium: N, low: N
Checks run: `npm test` — N passed, N failed
Verdict: Approve | Request changes | Comment only
```

**No issues:** State explicitly — "Reviewed N files across all five axes. No blocking issues."

---

## Cross-skill links

- **TDD:** `test-driven-development/references/tdd-patterns.md` — Prove-It on bug fixes
- **Security depth:** `app-security-hardening`
- **Adversarial:** `adversarial-hat` for architecture decisions pre-PR
- **Debug:** `debug-and-fix` — reviewer confirms regression test guards the bug path
