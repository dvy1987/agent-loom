# Idea Evaluation — Full Worked Examples

Skill: `idea-evaluation` | Enriched from SKILL.md (improve-skills pass, SKIP_RESEARCH).

## Example 1 — Documented workflow

**Input:** Evaluate this idea: an AI-powered tool that helps freelance designers send invoices and chase payments

**Output:**
```
Two questions before I evaluate:

1. What's the specific painful workaround designers use today (e.g., manual Stripe + Notion, or Bonsai/HoneyBook, or chasing in DMs)?
2. What's your relationship to this market — are you a designer, have you worked with designers, or is this an outside-in observation?
```

## Example 2 — Step-by-step execution

**Input:** "Run `idea-evaluation` on [concrete task]"

**Agent actions:**
1. Inputs
2. Sizing (always)
3. Surface hidden beliefs
4. Score the rubric
5. Apply the verdict gate
6. Next kill test
7. Apply anti-pattern audit
8. Optional adversarial pass (high-stakes only)

**Impact Report shape:**
```
Idea evaluation complete: <idea>
File saved: docs/ventures/evaluations/YYYY-MM-DD-<slug>-eval.md
Verdict: GO / ITERATE / KILL
Composite: N/55
SOM (Fermi): $X
Top unvalidated assumptions: N
Anti-pattern flags: N
Next kill test: <method, cost, timeline>
Logged to: docs/skill-outputs/SKILL-OUTPUTS.md
```

## Example 3 — Gotcha application

**Input:** Task hits a non-obvious edge case

**Apply:**
- **Composite score is not the verdict.** A 45/55 idea with no distribution wedge is still KILL. Hard gates trump arithmetic.
- **"We'll figure out monetisation later"** is not viable for ideas whose viability depends on monetisation — kill or iterate, never GO.
- **Founder-market-fit is not optional flavour.** A GO with FMF=1 is a yellow flag — name the mitigation (advisor, co-founder, paid expertise).
- **Why-now must be specific.** "AI is changing things" is not why-now. "Cost of inference dropped 100x in 18 months" is.

---

See `SKILL.md` for hard rules and verification checklist.
