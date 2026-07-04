# Inversion — Full Worked Examples

Skill: `inversion` | Enriched from SKILL.md (improve-skills pass, SKIP_RESEARCH).

## Example 1 — Documented workflow

**Input:** We want to increase user activation. How do we invert this?

**Output:**
```
Method 1 — Failure Inversion:
What would guarantee activation fails?
- Users don't reach the aha moment in session 1 (most common cause)
- Onboarding assumes context users don't have
- The value is real but invisible — users can't see what they gained

Check: Is the current onboarding hiding the aha moment behind setup steps?
Forward action: Move the aha moment to before account creation if possible.

Method 2 — Opposite Goal:
What would we do if we were trying to minimise activation?
- Make users fill out a long form before seeing any value
- Send a welcome email with no clear next step
- Show a feature tour of everything instead of one path to value

Check: Is any of this in the current flow?
Forward action: Audit the first 3 minutes of the user experience against this list.
```

## Example 2 — Step-by-step execution

**Input:** "Run `inversion` on [concrete task]"

**Agent actions:**
1. Assess
2. Ask (Maximum 2 Questions)
3. Invert
4. Translate to Forward Actions
5. Deliver

**Impact Report shape:**
```
Inversion complete: [problem/goal]
Method used: [Failure / Opposite Goal / Both]
Questions asked: N (max 2)
Forward actions: N
```

## Example 3 — Gotcha application

**Input:** Task hits a non-obvious edge case

**Apply:**
- Every inverted finding must translate to a concrete action. If it doesn't, it's noise.
- The most useful inversions are non-obvious. If findings are things the user already knew, push deeper.
- For richer analysis — surfacing assumptions, imagining failure scenarios, or decomposing stuck problems — `deep-thinking` orchestrates these alongside inversion.
- 

---

See `SKILL.md` for hard rules and verification checklist.
