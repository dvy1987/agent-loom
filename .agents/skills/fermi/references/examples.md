# Fermi Estimation — Full Worked Examples

Skill: `fermi` | Enriched from SKILL.md (improve-skills pass, SKIP_RESEARCH).

## Example 1 — Documented workflow

**Input:** We're thinking of building for indie developers in India. How big is that market?

**Output:**
```
Fermi Estimate: Addressable market — indie developers in India who might pay for our product

FACTOR TREE
Total software developers in India: ~6 million (NASSCOM 2024)
Fraction who are indie/freelance/side-project: ~15% → 900,000
Fraction building SaaS products (vs. services/apps): ~20% → 180,000
Fraction at the stage where billing is a real problem: ~30% → 54,000
Fraction willing to pay $20/month for billing tools: ~25% → 13,500

CALCULATION
Initial addressable segment: ~13,500 developers

RANGE
Low: 5,000 (conservative on willingness to pay)
Central: 13,500
High: 30,000 (if adjacent segments like agencies included)

SENSE-CHECK
Indie Hackers India community: ~40,000 members. Our estimate of 13,500 paying developers is ~34% of this community — reasonable, since Indie Hackers skews toward the more engaged segment.

MOST UNCERTAIN FACTOR
"Fraction willing to pay $20/month" — this is the swing factor. At 10% it's 5,400; at 40% it's 21,600. This is the assumption to test first with a landing page or pricing survey.

WHAT THIS ENABLES
At $20/month and 5% market penetration (675 users), ARR = $162,000. This determines whether the segment justifies a dedicated product. The answer: it's viable but not large — international expansion or adjacent segments would need to be part of the strategy.
```

## Example 2 — Step-by-step execution

**Input:** "Run `fermi` on [concrete task]"

**Agent actions:**
1. Frame the Question
2. Build the Factor Tree
3. Estimate Each Factor
4. Calculate
5. Sense-Check
6. Deliver

**Impact Report shape:**
```
Fermi estimate: [question]
Factors decomposed: N
Central estimate: [number with unit]
Range: [low] – [high]
Most uncertain factor: [which one]
Decision enabled: [what this makes possible]
```

## Example 3 — Gotcha application

**Input:** Task hits a non-obvious edge case

**Apply:**
- The most uncertain factor is usually the one that changes the estimate by an order of magnitude. Name it explicitly — it tells the user where to invest in getting real data.
- Fermi estimates are not for precise budgets or legal commitments. They are for "is this worth pursuing?" decisions.
- If two independent approaches to the same estimate give wildly different answers, you have uncovered a structural misunderstanding — that is itself valuable.
- Always state what the estimate enables. "We don't have the numbers" often means "we haven't made an estimate yet." A Fermi estimate converts paralysis into a decision.

---

See `SKILL.md` for hard rules and verification checklist.
