# Funnel Surface Map

Where experimentation pays off, where it fails, and what to default to. Used by the `experimentation` orchestrator in Step 5 (open-ended prioritisation).

Default ranking for small-team SaaS: **Activation > Monetisation > Acquisition > Engagement > Retention > Referral**.

The ranking inverts only if you already have PMF and high traffic. Most teams over-invest in landing-page tweaks and under-invest in activation.

---

## Acquisition

**Surfaces:** landing page (headline, hero, value prop, CTA), paid creative, ad copy, pricing page (entry experience), SEO snippets/metadata.

**Worth it?** Conditional. Worth it for high-volume LP/paid creative; mostly noise for SEO snippets.

| Surface | Method | Notes / failure modes |
|---|---|---|
| LP headline / value prop / CTA | A/B | Highest leverage at scale. Watch paid-channel mix — different ad sources behave differently. |
| Paid creative / offers | A/B or platform-native | Use ad platform's native experiment if budget permits. |
| Pricing page (copy, layout) | A/B | Often low signal until volume is high. |
| SEO snippets / metadata | Quasi-experiment | Indexing latency + crawler behaviour confound A/B. Don't fake A/B certainty here. |

**Failure mode:** treating LP A/B like a free win. Most LP changes are noise. Save A/B budget for activation surfaces with stronger signal.

---

## Activation ⭐ HIGHEST ROI for most small teams

**Surfaces:** signup flow, onboarding steps, sample data / templates / imports, time-to-value compression, aha-moment nudges, first-session experience, empty-state guidance.

**Worth it?** Ruthlessly. This is where most lift is hiding.

| Surface | Method | Notes / failure modes |
|---|---|---|
| Signup flow (form length, fields, social) | A/B | High volume, fast feedback. |
| Onboarding step count / sequence | A/B + Phase-2 holdout | Novelty bias — re-validate at 4 weeks. |
| Templates / sample data / imports | A/B | Big lever for time-to-value. |
| Aha-moment nudges (tooltips, prompts) | A/B | Watch tooltip fatigue — guardrail user complaints. |
| First-session content | A/B | Often the highest-leverage test in the entire product. |

**Failure mode:** measuring signup-completion as the primary metric without a downstream activation guardrail. A test that boosts signups but tanks activation is a loss, not a win.

---

## Engagement

**Surfaces:** core loop friction, notifications (timing, content, channel), recommendations / ranking, in-app prompts, search relevance.

**Worth it?** Yes — but rarely with a fixed-horizon A/B.

| Surface | Method | Notes / failure modes |
|---|---|---|
| Notification timing / copy / channel | Switchback or holdout | User fatigue interference; A/B leaks. |
| Recommendations / ranking | Holdout (long) + switchback | Cold-start contamination; long persistence effects. |
| Core loop prompts / nudges | A/B | Watch frequency cap as guardrail. |
| Search / discovery | Switchback | Shared index = interference. |

**Failure mode:** A/B testing notification copy and ignoring that treated users get fatigued differently than control. Use switchbacks or holdouts.

---

## Monetisation ⭐ SECOND-HIGHEST ROI

**Surfaces:** pricing page structure, paywall placement / framing, checkout friction, plan structure, trial vs no-trial, upgrade prompts.

**Worth it?** Yes — but with care for revenue lag and legal constraints.

| Surface | Method | Notes / failure modes |
|---|---|---|
| Pricing page copy / layout | A/B | Watch low volume. Cohort by source. |
| Paywall placement / framing | A/B | Long revenue lag — short-loop proxy + final revenue guardrail. |
| Checkout friction (steps, fields) | A/B | Cart abandonment + revenue per visit as guardrails. |
| Annual vs monthly framing | A/B | Watch downstream churn — guardrail at 30/60/90 days. |
| Actual price changes | Geo holdout / staggered | Legal/fairness constraints. Almost never a clean A/B. |

**Failure mode:** declaring a paywall test won at week 2 when the revenue lag is 4–8 weeks. Force a Phase-2 holdout for any monetisation change with delayed revenue.

---

## Retention

**Surfaces:** lifecycle email programs, win-back sequences, churn-save offers, re-engagement notifications.

**Worth it?** Yes, but the wrong method makes it useless.

| Surface | Method | Notes / failure modes |
|---|---|---|
| Lifecycle email program | Holdout (long, 4–12 weeks) | Never fixed-horizon A/B. |
| Win-back sequence | Holdout | Cohort-bound; small samples. |
| Churn-save offer | Holdout or quasi-experiment | Selection bias on who triggers the save. |
| Re-engagement push | Switchback or holdout | Fatigue interference. |

**Failure mode:** running endless tiny A/Bs on email subject lines while the program-level holdout is missing. Subject-line lift is rounding error compared to "is the program net-positive at all?".

---

## Referral

**Surfaces:** invite copy, sharing CTAs, referral incentives, share-modal flows.

**Worth it?** Usually not — until you have PMF and volume. Exception: collaborative SaaS where sharing is the core loop.

| Surface | Method | Notes |
|---|---|---|
| Invite copy / share CTA | A/B if volume | Most teams don't have the volume; test only if invites > a few thousand/week. |
| Referral incentives | A/B + revenue guardrail | Watch fraud / abuse as a guardrail. |
| Share modal flow | A/B | Same volume caveat. |

**Failure mode:** fiddling with referral copy when the underlying loop is broken. Fix the loop before optimising it.

---

## Cross-Cutting Failure Modes

- **Wrong primary metric:** optimising clicks when the real outcome is activation/revenue/retention.
- **No guardrail metric:** Airbnb famously caught a "winning" booking test that hurt review ratings — guardrails surfaced it.
- **Underpowered + claiming significance:** the most common silent failure. Force the **Directional Exploration** label instead of inflated certainty.
- **Confounding paid-channel mix:** shifts in upstream channel allocation during the test invalidate causal inference.
- **Sequential novelty re-tests:** retesting the same surface with the same idea after losing rarely produces a different result. Move on.
