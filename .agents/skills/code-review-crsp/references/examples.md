# Code Review CRSP — Full Worked Examples

Enriched from SKILL.md + AO Phase 3 depth merge. See `review-conventions.md` for five-axis depth.

---

## Example 1 — Five-axis review with prefixes

**Input:** Review PR "Add user profile endpoint"

```markdown
## Code Review — branch feature/profile (4 files)

### Critical
1. security (critical) — **Critical:** [profile.ts](src/routes/profile.ts#L28) — path `userId` not checked against `req.session.userId`. Auth bypass.

### High
2. correctness (high) — [profile.ts](src/routes/profile.ts#L44) — missing 404 when profile soft-deleted.
3. completeness (high) — [profile.test.ts](tests/profile.test.ts) — no test for deleted profile case.

### Medium
4. architecture (medium) — **Consider:** duplicate `validateUserId` from auth.ts — extract shared helper.
5. performance (medium) — **Optional:** N+1 avatar fetch in list endpoint — batch query.

### Low
6. readability (low) — **Nit:** rename handler return `data` → `profile`.

### FYI
7. **FYI:** Pattern matches `billing.ts` profile shape — good consistency.

---
Files reviewed: 4
Issues found: critical: 1, high: 2, medium: 2, low: 1
Checks run: `npm test` — 2 failed (profile suite — author did not run)
Verdict: Request changes
```

---

## Example 2 — Tests-first review order

**Input:** Review 200-line diff

**Agent order:**
1. `git diff main..HEAD --stat`
2. Read `tests/profile.test.ts` first — intent: cover GET/PUT; gap: no authz test
3. Read `src/routes/profile.ts` with gaps in mind
4. Read `docs/specs/profile-feature-spec.md` FR-3 alignment

---

## Example 3 — AI-generated code scrutiny

**Input:** "LGTM?" on 400-line Copilot diff

**Output:** Do not rubber-stamp.

- [ ] Security axis: every new route checked
- [ ] Grep called symbols — `getProfileBySlug` does not exist in repo (hallucination)
- [ ] Run `npm test` — 3 failures
- [ ] Request Prove-It on claimed bug fix in commit 2

Verdict: Request changes — "AI-generated diff; 1 hallucinated import, missing authz test."

---

## Example 4 — Change sizing split

**Input:** 1,200-line PR — refactor utils + new feature

**Output:**
```
This PR mixes behavior-neutral refactor (~600 lines) with feature (~600 lines).
Please split:
- PR A: refactor only (no behavior change) — I'll review for mechanical correctness
- PR B: feature on top of merged A — target <400 lines

Cannot approve combined PR — review quality degrades past ~1000 lines.
```

---

## Example 5 — Dead code after refactor

**Input:** PR renames `UserService` → `AccountService`

**Reviewer actions:**
```bash
git diff --name-only | xargs grep -l "UserService" 2>/dev/null
```

Finding: **Optional:** `src/legacy/userService.ts` orphaned — confirm safe to delete?

---

## Example 6 — Bug fix without regression test

**Input:** PR fixes login 500, no test changes

**Finding:** correctness (high) — Bug fix must include Prove-It regression per `test-driven-development/references/tdd-patterns.md`. Request changes.

---

## Example 7 — Clean review (explicit approve)

**Input:** Small focused PR, 85 lines

```markdown
## Code Review — uncommitted (2 files)

Reviewed `auth.ts` and `auth.test.ts` across all five axes.
- Correctness: null paths covered
- Security: session check present
- Tests: authz cases included

No blocking issues.

Files reviewed: 2
Issues found: critical: 0, high: 0, medium: 0, low: 0
Checks run: `npm test` — 52 passed
Verdict: Approve
```

---

## Example 8 — Multi-model second opinion (interactive)

**Input:** User confirms second review on payment PR

1. Pass diff + contract ("must not double-charge; idempotent webhook") to fresh session
2. Reconcile: second model flags race on webhook retry → classify Valid + actionable
3. Author fixes; re-run tests

---

See `references/review-conventions.md` for axis questions, prefix table, and verify-the-verification checklist.
