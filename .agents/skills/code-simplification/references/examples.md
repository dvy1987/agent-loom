# Code Simplification — Full Worked Examples

Skill: `code-simplification` | Load when producing output for this workflow.

## Example 1 — From skill workflow

**Input:** This handler has four levels of nesting after the feature landed; tests pass.

**Output:**
```
Read tests + callers. Extract guard clauses (one commit, tests green). Rename `data` → `orderPayload` (second commit). Stop — out of scope for unrelated modules.
```

## Example 2 — Typical invocation

**Input:** "Run `code-simplification` for [concrete task]"

**Output:**
```
Invoked `code-simplification`.
Step 1: Understand (Chesterton's Fence)
Step 2: Identify opportunities
Step 3: Apply incrementally
Scope: [files] | Simplifications: N | Tests: [pass/fail]
```

---

See `SKILL.md` for hard rules, gotchas, and verification checklist.
