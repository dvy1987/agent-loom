# Inversion — Full Worked Examples

Skill: `inversion` | Load when producing output for this workflow.

## Example 1 — From skill workflow

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

## Example 2 — Typical invocation

**Input:** "Run `inversion` for [concrete task]"

**Output:**
```
Invoked `inversion`.
Step 1: Assess
Step 2: Ask (Maximum 2 Questions)
Step 3: Invert
Inversion complete: [problem/goal]
```

---

See `SKILL.md` for hard rules, gotchas, and verification checklist.
