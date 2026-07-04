# Incremental Implementation — Full Worked Examples

Skill: `incremental-implementation` | Enriched from SKILL.md (improve-skills pass, SKIP_RESEARCH).

## Example 1 — Documented workflow

**Input:** Implement task creation from the plan — DB, API, and UI.

**Output:**
```
Slice 1 only: POST /tasks + migration + minimal form. Out of scope: list/edit/delete.
After `npm test` passes → commit `feat: add task creation endpoint and form`.
Next slice: list tasks.
```

## Example 2 — Step-by-step execution

**Input:** "Run `incremental-implementation` on [concrete task]"

**Agent actions:**
1. Confirm slice plan
2. Implement one slice
3. Test and verify
4. Commit and pick next slice
5. End-to-end check

## Example 3 — Anti-skip (rationalization defense)

**Input:** Agent tries to skip a gate

| Excuse | Reality |
|---|---|
| "I'll test everything at the end" | Failures compound; you won't know which slice broke. |
| "Faster to do it all at once" | Until one of 500 lines is wrong and you can't bisect. |
| "Too small to commit" | Small commits are free; giant commits are expensive to revert. |
| "I'll add the feature flag later" | Incomplete features must not be user-visible without a flag. |

## Example 4 — Gotcha application

**Input:** Task hits a non-obvious edge case

**Apply:**
- A bug in slice 1 invalidates slices 2–5 — test each slice.
- "While I'm here" refactors belong in a separate commit, not this slice.
- Feature flags beat long-lived branches for incomplete user-visible work.
- Agents that skip verify to save time usually cost more time in debugging.

---

See `SKILL.md` for hard rules and verification checklist.

## Verification checklist (L3)

- [ ] Examples demonstrate SKILL.md hard rules, not generic chat
- [ ] Anti-skip or rationalization defense included where applicable
- [ ] Output artifacts or Impact Report shape is explicit
- [ ] Reader can trace input → concrete agent actions → outcome
