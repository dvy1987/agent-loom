# Memory Audit — Full Worked Examples

Skill: `memory-audit` | Load when producing output for this workflow.

## Example 1 — Typical invocation

**Input:** "Run `memory-audit` for [concrete task]"

**Output:**
```
Invoked `memory-audit`.
Step 1: Read memory routing and indexes for the requested scope.
Step 2: Check target files exist and are referenced by the index.
Step 3: Check global line budgets and active total size.
See SKILL.md Impact Report schema.
```

## Example 2 — Success criteria

**Input:** "Use `memory-audit` on this project"

**Output:**
```
See SKILL.md Impact Report schema.
```

---

See `SKILL.md` for hard rules, gotchas, and verification checklist.
