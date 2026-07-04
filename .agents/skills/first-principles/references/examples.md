# First Principles — Full Worked Examples

Skill: `first-principles` | Load when producing output for this workflow.

## Example 1 — From skill workflow

**Input:** Our SaaS onboarding takes 14 steps and users drop off at step 6. First principles this.

**Output:**
```
FUNDAMENTAL TRUTHS
1. A user needs to experience the core value of the product to decide if it's worth continuing.
2. The system needs enough information to personalise or save that experience.

CONVENTIONAL CONSTRAINTS
1. "Users must create an account before seeing value" → conventional. Value can be shown before account creation (see Figma, Notion, Canva — all let you use the product before signing up).
2. "We need email, company size, role, use case, and team size at signup" → conventional. We need zero of these to let the user experience value. We need email only to save state.
3. "Onboarding must be sequential and instructional" → conventional. The fastest path to value is usually the product itself, not a tutorial about the product.

FUNDAMENTAL TRUTHS (remaining)
- We need a way to save user state (one identifier: email or OAuth).
- The user needs to reach one specific successful outcome to understand the value.

REBUILT SOLUTION
Remove the account gate entirely. Let the user do the core action immediately (anonymously). Prompt for email only when they want to save or share their work. Eliminate all 14 steps except the one that delivers the core outcome.

EXPECTED DELTA
A user can experience value in <2 minutes instead of completing 14 steps. Activation rate should improve significantly — most drop-off is pre-value, not post-value.
```

## Example 2 — Typical invocation

**Input:** "Run `first-principles` for [concrete task]"

**Output:**
```
Invoked `first-principles`.
Step 1: Frame
Step 2: Run the Six Steps
Step 3: Deliver
First principles analysis: [problem]
```

---

See `SKILL.md` for hard rules, gotchas, and verification checklist.
