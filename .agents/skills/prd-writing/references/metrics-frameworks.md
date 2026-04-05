# Metrics Frameworks for PRDs

Read this when the user needs help choosing or defining success metrics.
Reference the relevant framework based on the product type.

---

## AARRR (Pirate Metrics) — Best for growth-stage products

| Stage | Question | Example Metric |
|-------|----------|---------------|
| **Acquisition** | How do users find us? | Signups per channel, CAC |
| **Activation** | Do users have a good first experience? | % completing onboarding, time-to-first-value |
| **Retention** | Do users come back? | D7/D30 retention, churn rate |
| **Revenue** | Do users pay? | MRR, ARPU, conversion rate free→paid |
| **Referral** | Do users tell others? | NPS, referral rate, viral coefficient |

**When to use:** Consumer apps, SaaS products, marketplaces.

---

## HEART Framework — Best for UX-focused features

| Dimension | Question | Example Metric |
|-----------|----------|---------------|
| **Happiness** | Are users satisfied? | CSAT score, app store rating |
| **Engagement** | How often do users interact? | Sessions/week, feature usage frequency |
| **Adoption** | Are new users using the feature? | % of new users who used feature in first 7 days |
| **Retention** | Are existing users continuing to use it? | Feature retention rate at 30 days |
| **Task Success** | Can users complete their goal? | Task completion rate, error rate, time-on-task |

**When to use:** New features, redesigns, anything where user experience is the primary concern.

---

## OKRs (Objectives and Key Results) — Best for strategic initiatives

```
Objective: [Qualitative, inspiring, directional goal]
  KR1: [Measurable outcome with baseline and target]
  KR2: [Measurable outcome with baseline and target]
  KR3: [Measurable outcome with baseline and target]
```

**Example:**
```
Objective: Make our search experience best-in-class
  KR1: Increase search result click-through rate from 42% to 65%
  KR2: Reduce "no results found" rate from 18% to 5%
  KR3: Achieve search p95 latency < 200ms (currently 480ms)
```

**Rules for good KRs:**
- Measurable with a specific number
- Has a baseline (where we are now) and a target (where we're going)
- Ambitious but achievable — 70% attainment is success
- Outcome-based, not output-based ("increase retention" not "ship feature X")

**When to use:** Quarterly planning, strategic features, cross-team initiatives.

---

## North Star Metric — Best for product-wide alignment

A single metric that best captures the core value your product delivers to users.

**Formula:** One metric that, if it goes up, you're confident everything else is going right.

**Examples by product type:**

| Product Type | North Star Metric |
|-------------|-------------------|
| Social network | Daily active users |
| E-commerce | GMV (gross merchandise value) |
| SaaS productivity tool | Weekly active teams |
| Marketplace | Number of successful transactions |
| Media/content | Total time spent (if quality is high) |

**Guardrail metrics** (track alongside North Star to prevent gaming):
- If North Star is DAU: also track retention and NPS (don't inflate DAU with low-quality engagement)
- If North Star is revenue: also track churn (don't inflate revenue at the cost of customer health)

---

## Choosing the Right Framework

| Situation | Recommended Framework |
|-----------|----------------------|
| New consumer feature | HEART + AARRR Activation/Retention |
| Growth initiative | AARRR |
| Strategic company goal | OKRs |
| Improving existing UX | HEART |
| Entire product strategy | North Star + guardrails |
| Engineering/performance feature | Custom: latency, error rate, uptime |

---

## Writing Good Metrics in a PRD

**Template:**
```
| Metric | Baseline | Target | Timeframe | Measurement Method |
|--------|----------|--------|-----------|-------------------|
| [Name] | [Current value or "unknown — measure in week 1"] | [Goal] | [e.g., 90 days post-launch] | [Tool/query/event] |
```

**Rules:**
- If you don't have a baseline, explicitly say so and commit to measuring it in week 1 of the rollout
- Targets should be achievable — directional is fine, but "10x in 30 days" needs justification
- Always specify HOW the metric will be measured (Mixpanel event, SQL query, support ticket tag)
- Include at least one leading indicator (early signal) and one lagging indicator (outcome)
