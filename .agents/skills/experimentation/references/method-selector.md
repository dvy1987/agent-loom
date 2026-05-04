# Method Selector

Decision tree for choosing the experiment method. Used by `experimentation` orchestrator and `experiment-spec`.

The default mistake is treating every product question as a fixed-horizon A/B test. It isn't. Match the method to the surface, the unit, and the time horizon.

---

## Decision Tree

### 1. Is the treatment persistent (lives across user sessions, hard to "turn off" cleanly)?
- Lifecycle email programs, notifications, recommendations, ranking changes, model swaps → **Holdout** (5–10% of users kept on the pre-change experience for 4–12 weeks).
- Reason: persistent treatments produce delayed and compounding effects that fixed-horizon A/Bs miss.

### 2. Is there interference between units (one user's treatment affects another's outcome)?
- Marketplaces (buyer/seller), feeds with shared inventory, scheduling/dispatch, social ranking → **Switchback** (alternate treatment on/off across time windows for the whole population) or **cluster-randomised** by region/group.
- Reason: user-level randomisation leaks treatment to the control through shared state.

### 3. Is randomisation impossible or unethical?
- Pricing changes that legally must apply uniformly, geo-required compliance, tiny B2B segments → **Quasi-experiment** (difference-in-differences, synthetic control, regression discontinuity, interrupted time series).
- Reason: better than no test; never claim full causality, label the design honestly.

### 4. Do you have very high traffic AND a short reward loop AND many candidate variants?
- Headline/creative on a homepage with millions of views, ad creative selection → **Multi-armed bandit** (Thompson sampling or epsilon-greedy).
- Reason: bandits converge faster than A/B when reward signal is fast and clean. They do NOT replace A/B for ship/kill decisions because they hide variant performance over time.

### 5. Default — fixed-horizon A/B
- Standard product changes, UI/copy, onboarding flows, paywall variants, checkout, single-page changes.
- Run for full week multiples (capture day-of-week cycles). 1–4 weeks typical.

---

## Common Surface → Method Defaults

| Surface | Default | Notes |
|---|---|---|
| Landing page (headline, hero, CTA) | A/B | Watch paid-channel mix confound |
| Onboarding flow | A/B | Watch novelty effect — add a Phase 2 holdout window |
| Pricing page (copy, layout) | A/B | Per-cohort segmentation often needed |
| Pricing change (actual price) | Geo holdout / staggered | Legal/ethical constraints common |
| Paywall placement / framing | A/B | Long revenue lag — define short-loop proxy + final revenue guardrail |
| Checkout friction | A/B | Cart abandonment as guardrail |
| Lifecycle email program | Holdout | 4–12 week observation, never fixed-horizon A/B |
| Push / notification timing | Switchback or holdout | User fatigue interference |
| Recommendations / ranking | Holdout + switchback | Cold-start contamination |
| Feed personalisation | Switchback | Shared inventory interference |
| SEO / metadata | Quasi-experiment | Indexing latency + crawler confounding |
| Referral / share copy | A/B if volume; otherwise skip | Low-leverage at small scale |
| AI feature quality (latency / cost / accuracy) | Offline eval THEN A/B | Use `eval-output` first, then live |

---

## Sample-Size & Duration Heuristics

| Baseline conversion | Relative MDE | Approx users per arm |
|---|---|---|
| 1% | 10% | ~150,000 |
| 1% | 20% | ~38,000 |
| 5% | 10% | ~30,000 |
| 5% | 20% | ~7,500 |
| 20% | 10% | ~6,200 |
| 20% | 20% | ~1,550 |

Numbers are 80% power, alpha 0.05, two-sided. Halve the MDE → quadruple the sample. If the rough baseline is unknown, call `fermi`.

Duration must be at least one full weekly cycle for any user-facing surface. Two cycles for engagement / retention metrics. Lifecycle holdouts: 4–12 weeks.

---

## Variance-Reduction Options (apply only if sample is tight)

- **CUPED** — pre-period covariate adjustment. Big win when users have history. Worthwhile if it lifts power equivalent to 20–50% more sample.
- **Stratified randomisation** — by country/plan/cohort when those segments dominate variance.
- **Trigger-based analysis** — restrict to users who actually saw the treatment surface, not the whole population.

These are optional. Do not require them — recommend them when sample is the binding constraint.

---

## Stopping Rules

- **Default:** fixed horizon, no peeking, decision at end of pre-declared duration.
- **Sequential testing / alpha-spending:** required if the user wants valid early stops. Otherwise the test runs full duration even if it "looks significant" early.
- **Rapid kill:** allowed for severe guardrail breach (error rate spike, revenue collapse) — never for "looks like a winner".

---

## Quick Anti-Patterns

- A/B testing a lifecycle email — guarantees novelty-biased false wins.
- Bandits for ship/kill decisions — hides true variant performance.
- 3-day test on a B2B SaaS — sample never accumulates.
- "Stat sig at day 4, ship it" — peeking without alpha-spending = inflated false-positive rate.
- 12 secondary metrics with no correction — somebody's going to look "significant" by chance.
- Holdout reused across multiple experiments — contamination across treatments.
