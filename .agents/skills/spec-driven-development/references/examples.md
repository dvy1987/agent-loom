# Spec-Driven Development — Full Worked Examples

Skill: `spec-driven-development` | Enriched from SKILL.md (improve-skills pass, SKIP_RESEARCH).

## Example 1 — Documented workflow

**Input:** Do spec-driven development for adding magic-link login.

**Output:**
```
SDD state check:
- Constitution: docs/constitution.md@2 ✓
- No spec yet for "magic-link login"

Starting at `/specify`. Routing to `feature-spec` (mode=specify).

[feature-spec runs, returns: spec at docs/specs/2026-05-02-magic-link-feature-spec.md, status: Draft, 2 CLs]

`/specify` complete. 2 clarifications open. Run `/clarify` next, or paste answers and I'll route them to `feature-spec`.
```

## Example 2 — Step-by-step execution

**Input:** "Run `spec-driven-development` on [concrete task]"

**Agent actions:**
1. Identify entry point
2. Detect current SDD state
3. Enforce phase order
4. Delegate
5. Summarize and offer next phase

**Impact Report shape:**
```
SDD orchestration: <slug>
Phases run this turn: <list>
Current artifact state:
  Constitution: <version|missing>
  Spec: <status|missing>
  Plan: <yes|no>
  Tasks: <yes|no>
  Crosscheck: <PASS|FAIL|none>
Next phase: <slash>
```

## Example 3 — Anti-skip (rationalization defense)

**Input:** Agent tries to skip a gate

| Excuse | Reality |
|---|---|
| "Too simple for a spec" | Even two-line acceptance criteria beat guessing. |
| "I'll spec after coding" | That's documentation, not specification. |
| "Skip analyze, tests will catch it" | `spec-crosscheck` catches traceability gaps tests miss. |
| "Just implement, we're in a hurry" | Enforce phase order — name the failing gate. |

## Example 4 — Gotcha application

**Input:** Task hits a non-obvious edge case

**Apply:**
- This is a router, not a worker. Resist writing constitution/spec/plan content here — that belongs in the leaf skill.
- For tactical small changes (bug fix, narrow refactor), DO NOT route through SDD. Route to `problem-to-plan`. SDD overhead is for feature-sized work.
- **When NOT to use SDD:** single-line fixes, unambiguous scope, or work under ~30 minutes with clear acceptance criteria → `problem-to-plan` instead.
- A repo can have many feature-specs in flight. Use the slug to tie spec ↔ plan ↔ tasks ↔ crosscheck. Don't mix slugs across phases.

---

See `SKILL.md` for hard rules and verification checklist.
