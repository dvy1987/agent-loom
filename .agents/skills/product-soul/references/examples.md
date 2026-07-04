# Product Soul — Full Worked Examples

Skill: `product-soul` | Load when producing output for this workflow.

## Example 1 — From skill workflow

**Input:** Write the product soul for a B2B SaaS tool that helps indie developers manage their Stripe billing without writing code

**Output:**
```
[Discovery complete — 3 questions per lens]

Writing docs/product-soul.md...

---
# Product Soul: [Product Name]
Version: 1.0 | Date: YYYY-MM-DD | Status: Hypothesis (PMF unconfirmed)

## The User
**Primary user:** Indie developer, 1–3 person team, building a SaaS product as a side project or early startup. Technical enough to integrate an API but context-switching constantly — billing is a day lost they don't have.
**Current behaviour:** Hand-writing Stripe webhook handlers, copying from StackOverflow, spending 6–12 hours on something they know is fragile.
**Their words:** "I just want subscriptions to work so I can focus on my actual product."

## The Business
**Model:** Usage-based SaaS. Free tier to first transaction, then per-seat or per-revenue-share.
**Year 1 must-be-true:** 500 active integrations generating >$1 in live revenue.
**Year 3 must-be-true:** Self-serve motion covers CAC; expansion revenue from teams upgrading.
**Biggest risk:** Stripe itself builds this natively.

## The Strategy
**Alternatives:** Stripe's own Billing (too complex for 1-person teams), Paddle (takes margin), roll-your-own (what we replace).
**Moat:** Deep integration with indie developer workflows — not enterprise compliance, not white-glove support. Speed to first working subscription is <30 minutes. Stripe will never optimise for this segment.
**Strategic bet:** The indie developer market is large enough and underserved enough that a focused tool outperforms a general one.

## Product-Market Fit
**Status:** Pre-PMF. 40 beta users, 12 active (30% activation).
**Signal we're watching:** Developers who complete first integration — do they return for a second project? Current rate: 4/12 (33%).
**PMF signal threshold:** >60% of activated users integrate a second project within 60 days.
**Not-PMF signal:** If users complete integration once and never return, we are a tutorial, not a product.

## GTM Distribution
**First user finds us via:** Developer Twitter/X + specific Stripe frustration searches on Google ("stripe webhooks subscription management").
**Wedge channel:** SEO on high-intent developer queries. 3 posts targeting specific Stripe pain points.
**Acquisition → Activation → Retention loop:** Search → free signup → first integration working (activation) → second project (retention signal) → team invite (expansion).

## Open Hypotheses (must be resolved before Series A framing)
- [ ] Does the indie developer segment have enough willingness to pay, or do they always find a free alternative?
- [ ] Is the Stripe-builds-this-natively risk material within 18 months?
```

## Example 2 — Typical invocation

**Input:** "Run `product-soul` for [concrete task]"

**Output:**
```
Invoked `product-soul`.
Step 1: Check for Existing Context
Step 2: Discovery Interview (Five Lenses)
Step 3: Run Inversion + Adversarial Hat (Recommended)
See SKILL.md Impact Report schema.
```

---

See `SKILL.md` for hard rules, gotchas, and verification checklist.
