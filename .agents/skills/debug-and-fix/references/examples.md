# Debug and Fix — Full Worked Examples

Skill: `debug-and-fix` | Enriched from SKILL.md (improve-skills pass, SKIP_RESEARCH).

## Example 1 — Documented workflow

**Input:** The login page throws a 500 error when the email field is empty.

**Output:**
```
[Searched codebase for login handler. Read `src/auth/login.ts` lines 14-30.]

**Root cause:** `login.ts:22` calls `user.findByEmail(email)` without checking for an empty string. The DB query fails on an empty parameter, throwing an unhandled exception.

Proceed with the fix?

[User confirms]

Fix applied: Added empty-string guard at `login.ts:21` — returns 400 with validation message before the DB call.

```
Root cause: Missing empty-string validation before DB query in login handler
Fix applied: src/auth/login.ts — added input guard at line 21
Verification: npm test — 47 passed, 0 failed
Remaining: none
```
```

## Example 2 — Documented workflow

**Input:** Fix HID-42 from Linear.

**Output:**
```
[Fetched HID-42: "CSV export truncates rows over 1000"]
[Read src/export/csv.ts — found hardcoded LIMIT=1000 at line 8]

**Root cause:** `csv.ts:8` sets `LIMIT = 1000` as a constant. The export query uses this as a cap rather than paginating.

Proceed with the fix?

[User confirms]

Fix applied: Replaced fixed limit with cursor-based pagination in `exportCSV()`.
Added comment on HID-42 with root cause and fix summary.

```
Root cause: Hardcoded row limit of 1000 in CSV export query
Fix applied: src/export/csv.ts — replaced fixed limit with cursor pagination
Verification: npm test — 83 passed, 0 failed
Remaining: none
```

Update HID-42 status to "Done"?
```

## Example 3 — Step-by-step execution

**Input:** "Run `debug-and-fix` on [concrete task]"

**Agent actions:**
1. Gather the Bug
2. Trace via knowledge graph (if present)
3. Triage (Multiple Bugs Only)
4. Triage (Reproduce → Localize → Reduce)
5. Apply the Fix
6. Guard and Verify
7. Update Source (If Applicable)

**Impact Report shape:**
```
Root cause: [one-sentence explanation]
Fix applied: [file(s) changed + what changed]
Verification: [test command run + result]
Remaining: [N bugs left in queue, or "none"]
```

## Example 4 — Anti-skip (rationalization defense)

**Input:** Agent tries to skip a gate

| Excuse | Reality |
|---|---|
| "I know the bug, I'll just fix it" | Unreproduced fixes often miss root cause. |
| "The test is wrong, skip it" | Verify; fix test or code — don't skip. |
| "Works on my machine" | Compare CI, config, dependencies. |
| "I'll add the test later" | Later never comes; guard now. |

## Example 5 — Gotcha application

**Input:** Task hits a non-obvious edge case

**Apply:**
- Stack traces from production may reference compiled/minified paths — always map back to source before searching.
- Linear issue descriptions can be outdated — verify every claim against the current codebase.
- A passing test suite after a fix does not mean the fix is correct — check that the test actually exercises the bug's code path.
- Multiple symptoms may share one root cause — check for shared dependencies before treating each as separate.

---

See `SKILL.md` for hard rules and verification checklist.
