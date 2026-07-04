# Design Review — Full Worked Examples

Skill: `design-review` | Enriched from SKILL.md (improve-skills pass, SKIP_RESEARCH).

## Example 1 — Step-by-step execution

**Input:** "Run `design-review` on [concrete task]"

**Agent actions:**
1. Read inputs
2. Capture screens
3. APCA contrast pass (hard gate)
4. Ethical patterns pass (hard gate)
5. UX heuristics pass
6. Score the rubric
7. Specific findings
8. Prioritize (max 8)

**Impact Report shape:**
```
Review complete: [feature] | Pass: [N] | Verdict: [SHIP / REVISE]
APCA: [PASS / N pairs failed] | Ethical: [PASS/FAIL] | UX heuristics: [N fails]
State coverage: [N/3] | Direction fidelity: [N/3] | Distinctive moves: [N/3]
Findings raised: [count] | REVIEW.md written
Handoff: [back to frontend-design build / ship]
```

## Example 2 — Anti-skip (rationalization defense)

**Input:** Agent tries to skip a gate

| Excuse | Reality |
|---|---|
| "WCAG 4.5:1 passes, ship it" | WCAG misreads dark/thin type. Use APCA Lc targets. |
| "Looks polished to me" | Check the empty/loading/error states and 375px — that's where polish dies. |
| "Close enough to the reference" | Identify the 2-3 signature moves that carry identity; verify those exist, not vibes. |
| "Code-only review is fine" | Drift surfaces visually. Capture screens (Playwright or pasted) or flag the gap. |

---

See `SKILL.md` for hard rules and verification checklist.
