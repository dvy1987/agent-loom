# Source-Driven Development — Full Worked Examples

Skill: `source-driven-development` | Load when producing output for this workflow.

## Example 1 — From skill workflow

**Input:** Add React 19 form submission with pending state.

**Output:**
```
Detect React 19.x from package.json. Fetch react.dev/useActionState.
Implement with cited comment. Reject manual useState+isPending if docs recommend useActionState unless user chooses consistency with existing code.
```

## Example 2 — Typical invocation

**Input:** "Run `source-driven-development` for [concrete task]"

**Output:**
```
Invoked `source-driven-development`.
Step 1: Detect stack and versions
Step 2: Fetch official documentation
Step 3: Implement documented patterns
Feature: [slug] | Stack: [versions]
```

---

See `SKILL.md` for hard rules, gotchas, and verification checklist.
