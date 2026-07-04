# Memory Handoff — Full Worked Examples

Skill: `memory-handoff` | Load when producing output for this workflow.

## Example 1 — Typical invocation

**Input:** "Run `memory-handoff` for [concrete task]"

**Output:**
```
Invoked `memory-handoff`.
Step 1: Read `docs/memory/project-index.md` and latest `docs/memory/agent-handoffs.md` if present.
Step 2: Inspect current session context and `git status --short`.
Step 3: Summarize only durable context: done, debated, decisions, blockers, deferred items, next steps, revisit triggers.
See SKILL.md Impact Report schema.
```

## Example 2 — Success criteria

**Input:** "Use `memory-handoff` on this project"

**Output:**
```
See SKILL.md Impact Report schema.
```

---

See `SKILL.md` for hard rules, gotchas, and verification checklist.
