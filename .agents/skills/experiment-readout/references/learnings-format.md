# Learnings Format

The cumulative learnings log lives at `docs/experiments/learnings.md`. Every readout — wins, losses, inconclusives, SRM-fails — appends one entry. This is the long-term knowledge base that prevents the team from rerunning the same bad test six weeks later.

---

## File Header (one-time bootstrap)

```markdown
# Experiment Learnings Log

Cumulative learnings from every experiment run on this product.
One entry per readout. Required regardless of decision.

Most recent first.

---
```

---

## Entry Format

```markdown
## YYYY-MM-DD — <Experiment Name>

**Decision:** SHIP | ITERATE | KILL | INCONCLUSIVE | SRM-FAIL
**Decision class:** Causal | Directional | Instrumentation
**Surface:** <funnel stage / surface>
**Method:** A/B | Holdout | Switchback | Quasi | MAB

**Hypothesis:** <one-line spec hypothesis>

**Result:** <one paragraph — what actually happened, including effect magnitude with uncertainty>

**Learning:** <what we now believe more or less strongly, in plain language>

**Confidence:** HIGH | MEDIUM | LOW
- HIGH: Causal, adequately powered, validity-clean.
- MEDIUM: Causal but with one validity caveat, OR Directional positive across multiple windows.
- LOW: Directional underpowered, OR validity issues that limit interpretation.

**Surprise:** <if applicable — what was unexpected and why>

**Implication for next tests:** <one or two sentences>

**Links:** spec / runbook / analysis paths.

---
```

---

## Worked Examples

### Example 1 — Win

```markdown
## 2026-05-15 — LP Headline Test (benefit-led vs feature-led)

**Decision:** SHIP
**Decision class:** Causal
**Surface:** Acquisition / landing page
**Method:** A/B (14-day fixed-horizon)

**Hypothesis:** Replacing the LP headline with a benefit-led variant lifts signup-rate by ≥5% relative for organic visitors.

**Result:** Signup-rate +4.2% relative (95% CI: +0.8% to +7.6%, p=0.014). Bounce neutral. Day-7 activation +1.8% (no harm).

**Learning:** On organic LP traffic, naming the outcome (benefit) outperforms naming the feature for first-touch users. Effect was stable across both weeks; no novelty decay detected.

**Confidence:** HIGH

**Surprise:** Mobile users showed roughly 2x the lift of desktop users (exploratory). Worth a follow-up test.

**Implication for next tests:** Default new LP variants to benefit-led framing. Consider a mobile-only deeper exploration of outcome-naming density.

**Links:** specs/2026-05-01-lp-headline-spec.md · runbooks/2026-05-01-lp-headline-runbook.md · analyses/2026-05-15-lp-headline-analysis.md

---
```

### Example 2 — Inconclusive

```markdown
## 2026-04-12 — Onboarding Step-3 Removal

**Decision:** INCONCLUSIVE
**Decision class:** Directional (downgraded — sample short of plan)
**Surface:** Activation / onboarding
**Method:** A/B (10-day, ended early due to release pressure)

**Hypothesis:** Removing onboarding step 3 lifts Day-7 activation by ≥5% for free-trial users.

**Result:** Day-7 activation directionally +2.1% (CI: -1.4% to +5.6%) — wide uncertainty due to short run. No guardrail breach.

**Learning:** Direction is consistent with hypothesis but uncertainty is too wide to ship. Can't rule out null.

**Confidence:** LOW

**Implication for next tests:** Re-run for full 21-day window with adequate sample. Do not ship on this evidence alone.

**Links:** specs/2026-04-01-onboarding-step3-spec.md · runbooks/2026-04-01-onboarding-step3-runbook.md · analyses/2026-04-12-onboarding-step3-analysis.md

---
```

### Example 3 — SRM Fail

```markdown
## 2026-03-22 — Pricing Page Layout

**Decision:** SRM-FAIL
**Decision class:** Causal (planned)
**Surface:** Monetisation / pricing page
**Method:** A/B

**Hypothesis:** New pricing page layout lifts plan-selection rate by ≥3%.

**Result:** SRM detected (chi-squared p=2e-5). Bot traffic landing disproportionately on the treatment page. Metric analysis not performed.

**Learning:** Bot exclusion cohort was missing the new bot-detection rule for the variant URL. No business conclusion possible from this run.

**Confidence:** N/A

**Surprise:** Bot share differed by variant because the new variant URL was newly indexed.

**Implication for next tests:** Update bot-exclusion cohort before re-running. Verify SRM at 1% ramp before continuing.

**Links:** specs/2026-03-15-pricing-layout-spec.md · runbooks/2026-03-15-pricing-layout-runbook.md · analyses/2026-03-22-pricing-layout-analysis.md

---
```

---

## Why This Format Matters

The learnings log is the long-term ROI of an experimentation program. A team that runs 30 tests and writes nothing learns nothing. A team that runs 30 tests and appends one paragraph each accumulates institutional memory worth more than any single result.

**Keep entries short.** A long entry no one reads is worse than a short entry someone scans.
