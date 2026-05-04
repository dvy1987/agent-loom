# MDE & Duration Heuristics

Quick sample-size estimates for two-arm fixed-horizon A/B tests. Numbers assume 80% power, alpha 0.05, two-sided. For other configurations, consult a power calculator.

If baseline conversion is unknown, call `fermi` for an order-of-magnitude estimate before sizing.

---

## Two-Arm A/B — Approximate Users Per Arm

| Baseline | Relative MDE 5% | Relative MDE 10% | Relative MDE 20% |
|---|---:|---:|---:|
| 0.5% | ~1,200,000 | ~310,000 | ~78,000 |
| 1% | ~620,000 | ~155,000 | ~38,000 |
| 2% | ~310,000 | ~77,000 | ~19,000 |
| 5% | ~120,000 | ~30,000 | ~7,500 |
| 10% | ~58,000 | ~14,500 | ~3,600 |
| 20% | ~25,000 | ~6,200 | ~1,550 |
| 30% | ~14,500 | ~3,600 | ~900 |
| 50% | ~6,300 | ~1,580 | ~390 |

**Rule of thumb:** halve the MDE → quadruple the sample. Halve the baseline → roughly double the sample.

---

## Duration

- **Minimum:** one full week multiple (7 / 14 / 21 / 28 days). Captures day-of-week cycles.
- **Engagement / retention metrics:** at least 2 weeks; often 4.
- **Lifecycle / persistent treatments:** 4–12 weeks (this is a holdout, not a fixed-horizon A/B).
- **B2B with low DAU:** lean toward 28 days minimum; reconsider whether A/B is the right method.

---

## Variance-Reduction Options (only if sample is the binding constraint)

| Technique | Typical sample saving | Use when |
|---|---|---|
| CUPED (pre-period covariate) | 20–50% | Users have history; pre-period data clean |
| Trigger-based analysis | varies, often 30–70% | Treatment only affects a sub-population |
| Stratified randomisation | 5–15% | Country/plan/cohort dominates variance |

These are options, not requirements. Recommend them when sample is the binding constraint; do not block tests on their absence.

---

## Decision Tree When Power Is Short

1. Can the population be widened (e.g. include more geos / both new and existing users)? → preferred fix.
2. Can duration be extended? → second preferred. Watch for novelty/primacy windows extending into noise.
3. Can the MDE be raised honestly (i.e. the team genuinely cares about a bigger lift)? → acceptable.
4. Can a variance-reduction technique cut the required sample? → CUPED or trigger-based analysis.
5. None of the above → **downgrade to Directional Exploration** with no significance claims, OR delay until the surface has more traffic.

---

## Common Sizing Mistakes

- Using **absolute MDE** when the team meant **relative MDE** (or vice versa). State explicitly.
- Sizing on **users** when randomisation is at **session** level (or vice versa) — sample is at the unit of randomisation.
- Sizing for **30-day metrics** but only running 7 days — primary metric never matures.
- Forgetting the **peek penalty:** sequential / repeat testing requires alpha-spending which raises the required sample.
- **Multiple comparisons:** more than ~3 secondary metrics or 3+ variants without correction inflates false-positive rate.
