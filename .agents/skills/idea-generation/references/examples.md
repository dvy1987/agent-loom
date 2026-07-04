# Idea Generation — Full Worked Examples

Skill: `idea-generation` | Enriched from SKILL.md (improve-skills pass, SKIP_RESEARCH).

## Example 1 — Documented workflow

**Input:** I'm a backend engineer who's worked on payments at two fintechs. Generate 7 startup ideas for me.

**Output:**
```
Before I generate, two quick questions:

1. What's the most annoying / expensive thing you've seen in payments in the last 12 months — the "I cannot believe this is still a manual problem in 2026" moment?
2. Are you open to founder-led sales (B2B) or do you want to stay product-led / self-serve only?
```

## Example 2 — Step-by-step execution

**Input:** "Run `idea-generation` on [concrete task]"

**Agent actions:**
1. Capture founder/domain context
2. Choose 2–3 generation methods
3. Generate the batch
4. Apply anti-pattern filter
5. Force diversity check
6. Rank for next-step priority
7. Write and log

**Impact Report shape:**
```
Idea generation complete: <theme>
File saved: docs/ventures/ideas/YYYY-MM-DD-batch.md
Methods used: <list>
Candidates produced: N (struck: M)
Non-obvious count: N
Diversity: <themes>
Top 3 by rough score: <names>
Logged to: docs/skill-outputs/SKILL-OUTPUTS.md
```

## Example 3 — Gotcha application

**Input:** Task hits a non-obvious edge case

**Apply:**
- **Don't filter while generating.** Strike anti-patterns AFTER the batch exists, not during. Filtering during generation kills quantity.
- **The user's killed-but-haunting idea is often the best lead.** Probe it.
- **Schlep blindness** is real: ideas the user dismisses with "but that would be annoying / complicated / regulated / sales-heavy" are often the best, because nobody else wants the schlep either.
- **"Live in the future"** ideas need a concrete why-now or they're sci-fi.

---

See `SKILL.md` for hard rules and verification checklist.
