# Socratic — Full Worked Examples

Skill: `socratic` | Enriched from SKILL.md (improve-skills pass, SKIP_RESEARCH).

## Example 1 — Documented workflow

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

## Example 2 — Step-by-step execution

**Input:** "Run `socratic` on [concrete task]"

**Agent actions:**
1. Receive the Problem
2. Find the Keystone Question
3. Take the Answer and Recurse
4. Synthesise

**Impact Report shape:**
```
Socratic session: [problem]
Decomposition depth: N questions
Keystone insight: [the real question beneath the original]
Next concrete action: [what became clear]
```

## Example 3 — Gotcha application

**Input:** Task hits a non-obvious edge case

**Apply:**
- The first Socratic question is the hardest. Resist the urge to answer the user's question. Resist the urge to ask a clarifying question about their question. Find the keystone.
- If the user gives a short answer, probe one level deeper before moving on.
- Socratic is for genuinely complex or stuck problems. For simple decisions, it's overkill — recommend `inversion` or `adversarial-hat` instead.
- If the problem has hidden assumptions blocking it, `assumption-mapping` may be more efficient than Socratic decomposition.

---

See `SKILL.md` for hard rules and verification checklist.
