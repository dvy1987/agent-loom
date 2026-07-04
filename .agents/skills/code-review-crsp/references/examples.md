# Code Review CRSP — Full Worked Examples

Source: addyosmani/agent-skills `code-review-and-quality` (2026-05-29 snapshot). Security-scanned SAFE. Mapped to agent-loom six criteria.

---

## Example 1 — Five-axis review output

**Input:** Review PR "Add user profile endpoint"

```markdown
## Review: Add user profile endpoint

### Critical
1. **[security]** `src/routes/profile.ts:28` — user ID from path not checked against session user. Fix: compare `req.params.id === req.user.id`.

### Required
2. **[correctness]** Missing 404 when profile deleted — add test.
3. **[architecture]** Validation duplicated from `auth.ts` — reuse `validateUserId` helper.

### Suggestion
4. **[performance]** N+1 on avatar fetch — batch or join.

### Nit
5. **[style]** Rename `data` → `profile` in handler return.

### Verdict: Request changes (1 Critical, 2 Required)
Tests: `npm test` — 2 failures in profile suite (not run by author — run before re-review).
```

---

## Example 2 — AI-generated code scrutiny

**Input:** "LGTM?" on 400-line agent-generated diff

**Output:** Do not rubber-stamp. Check all five axes; AI code is confident when wrong. Require evidence: tests run, security axis for auth/input paths, architecture fit.

---

## Example 3 — Change sizing

**Input:** 1,200-line PR mixing refactor + feature

**Output:** Request split — "Refactor PR first (no behavior change), then feature PR." Review each under 400 lines.

---

## Example 4 — Severity prefixes

| Prefix | Meaning |
|---|---|
| **Critical** | Must fix before merge (security, data loss) |
| **Required** | Must fix (correctness, broken tests) |
| **Suggestion** | Should fix (maintainability) |
| **Nit** | Optional style |
