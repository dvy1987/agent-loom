# Design Review — Full Worked Examples

Skill: `design-review` | Load when producing output for this workflow.

## Example 1 — Typical invocation

**Input:** "Run `design-review` for [concrete task]"

**Output:**
```
Invoked `design-review`.
Step 1: Read inputs
Step 2: Capture screens
Step 3: APCA contrast pass (hard gate)
Review complete: [feature] | Pass: [N] | Verdict: [SHIP / REVISE]
```

## Example 2 — Success criteria

**Input:** "Use `design-review` on this project"

**Output:**
```
Review complete: [feature] | Pass: [N] | Verdict: [SHIP / REVISE]
APCA: [PASS / N pairs failed] | Ethical: [PASS/FAIL] | UX heuristics: [N fails]
State coverage: [N/3] | Direction fidelity: [N/3] | Distinctive moves: [N/3]
Findings raised: [count] | REVIEW.md written
Handoff: [back to frontend-design build / ship]
```

---

See `SKILL.md` for hard rules, gotchas, and verification checklist.
