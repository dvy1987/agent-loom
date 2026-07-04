# Code Simplification — Full Worked Examples

Skill: `code-simplification` | Enriched from SKILL.md (improve-skills pass, SKIP_RESEARCH).

## Example 1 — Documented workflow

**Input:** This handler has four levels of nesting after the feature landed; tests pass.

**Output:**
```
Read tests + callers. Extract guard clauses (one commit, tests green). Rename `data` → `orderPayload` (second commit). Stop — out of scope for unrelated modules.
```

## Example 2 — Step-by-step execution

**Input:** "Run `code-simplification` on [concrete task]"

**Agent actions:**
1. Understand (Chesterton's Fence)
2. Identify opportunities
3. Apply incrementally
4. Verify the whole

## Example 3 — Anti-skip (rationalization defense)

**Input:** Agent tries to skip a gate

| Excuse | Reality |
|---|---|
| "It works, don't touch it" | Hard-to-read working code is expensive on every future fix. |
| "Fewer lines is always simpler" | Comprehension speed matters, not line count. |
| "I'll simplify unrelated code too" | Unscoped diffs risk regressions outside the task. |
| "Types make it self-documenting" | Types show structure; names show intent. |

## Example 4 — Gotcha application

**Input:** Task hits a non-obvious edge case

**Apply:**
- Simplification that requires test changes usually changed behavior.
- Inlining a well-named helper hurts readability.
- Fewer lines ≠ simpler (nested ternaries prove this).
- Mixed refactor + feature PRs are hard to review and revert.

## Example 5 — Pattern reference (addyosmani/agent-skills)

**Source:** addyosmani snapshot 2026-05-29, security-scanned SAFE.

```
ASK BEFORE EVERY CHANGE:
→ Does this produce the same output for every input?
→ Does this maintain the same error behavior?
→ Does this preserve the same side effects and ordering?
→ Do all existing tests still pass without modification?
```

---

See `SKILL.md` for hard rules and verification checklist.
