# Spec-Driven Development — Full Worked Examples

Source: addyosmani/agent-skills `spec-driven-development` (2026-05-29 snapshot). Security-scanned SAFE. Adapted to agent-loom orchestrator chain.

---

## Example 1 — Full SDD chain

**Input:** "Build notification preferences"

```markdown
Route: project-constitution (if missing) → feature-spec /specify → /clarify → implementation-plan /plan → spec-crosscheck /analyze → incremental-implementation + TDD

Stop gates:
- No plan until feature-spec Approved
- No code until crosscheck PASS
- Behavior change → update spec first
```

---

## Example 2 — When NOT to use SDD

**Input:** "Fix typo in button label" / "One-line config change"

**Output:** Skip full chain — note `SDD: lightweight change`; still run tests if behavioral.

---

## Example 3 — /implement pairing

**Input:** Approved spec + plan PASS

Invoke `test-driven-development` for logic + `incremental-implementation` for vertical slices — not big-bang implementation.

---

## Example 4 — Orchestrator rationalization defense

| Excuse | Reality |
|---|---|
| "Spec is overhead for small fix" | Small fixes skip SDD; anything with FR/NFR needs spec |
| "I'll update spec after code" | Violates crosscheck; spec leads code |
