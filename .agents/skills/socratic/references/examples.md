# Socratic — Full Worked Examples

Skill: `socratic` | Load when producing output for this workflow.

## Example 1 — From skill workflow

**Input:** We can't decide whether to build community features or double down on core product improvements. We keep going in circles.

**Output:**
```
Before I help you reason through this, one question:

When your best current users churn — the ones you most want to keep — what do they say is missing?

[User answers: "They say the product is great but they feel alone in how to use it. They want to know what other users are doing."]

That's useful. One more:

Is "feeling alone" a problem you can solve with product improvements, or does it require other people?

[User answers: "Other people. You can't solve the social layer with features."]

Then the real question isn't community vs. core product. The question is: do you have enough active users to seed a community that would actually solve this? What's your MAU count and how engaged are your top 20% of users?

[This decomposition reveals the question was never "community vs. product" — it was "do we have the critical mass to make community work?"]
```

## Example 2 — Typical invocation

**Input:** "Run `socratic` for [concrete task]"

**Output:**
```
Invoked `socratic`.
Step 1: Receive the Problem
Step 2: Find the Keystone Question
Step 3: Take the Answer and Recurse
Socratic session: [problem]
```

---

See `SKILL.md` for hard rules, gotchas, and verification checklist.
