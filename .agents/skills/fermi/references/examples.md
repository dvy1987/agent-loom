# Fermi Estimation — Full Worked Examples

Skill: `fermi` | Load when producing output for this workflow.

## Example 1 — From skill workflow

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

## Example 2 — Typical invocation

**Input:** "Run `fermi` for [concrete task]"

**Output:**
```
Invoked `fermi`.
Step 1: Frame the Question
Step 2: Build the Factor Tree
Step 3: Estimate Each Factor
Fermi estimate: [question]
```

---

See `SKILL.md` for hard rules, gotchas, and verification checklist.
