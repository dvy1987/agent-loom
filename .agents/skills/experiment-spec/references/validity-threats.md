# Validity Threats

Catalogue of the failure modes that silently invalidate experiment results. List the ones relevant to the surface in the spec's `Validity Threats` section, with the planned mitigation for each.

---

## 1. Sample Ratio Mismatch (SRM)

**What:** observed traffic split deviates from the intended split (e.g. expected 50/50, observed 52/48). Signals broken randomisation, biased traffic routing, or logging failures.

**Impact:** invalidates results. SRM-positive tests routinely produce phantom wins.

**Mitigation:** chi-squared SRM check at every ramp gate and at readout. Block analysis if p-value < 0.001 sustained.

**Apply to:** every test, no exceptions.

---

## 2. Novelty Effect

**What:** users react to "new" — not "better". The lift is real but temporary.

**Impact:** initial weeks show inflated lift; effect decays or reverses long-term.

**Mitigation:**
- Phase-2 holdout window (4+ weeks post-ship) to validate persistence.
- Exclude first 24–48h of exposure from the analysis window if traffic permits.
- Larger samples to allow within-test detection of decay.

**Apply to:** redesigns, onboarding changes, prominent UI changes, gamification.

---

## 3. Primacy Effect

**What:** the inverse of novelty — users get worse before they get better because they were trained on the old experience.

**Impact:** new variant looks worse short-term but is actually better long-term.

**Mitigation:** longer test duration; segment by user tenure; planned re-evaluation window.

**Apply to:** flow restructures, shortcut removals, navigation changes.

---

## 4. Interference (SUTVA Violation)

**What:** one unit's treatment affects another unit's outcome. The Stable Unit Treatment Value Assumption fails.

**Impact:** A/B is invalid because control "leaks" treatment.

**Mitigation:**
- **Switchback** (alternate treatment on/off across time windows for the whole population).
- **Cluster-randomisation** by region/group/account.

**Apply to:** marketplaces (buyer/seller), feeds with shared inventory, scheduling/dispatch, social ranking, recommendations.

---

## 5. Contamination

**What:** units assigned to one variant are exposed to the other (shared device, shared account, multi-tab sessions, mis-routed traffic).

**Impact:** dilutes the measured effect; can flip the sign in extreme cases.

**Mitigation:** server-side assignment with deterministic hashing; consistent unit definition across surfaces; explicit handling of multi-device users.

**Apply to:** consumer SaaS with multi-device users, B2B shared accounts, public unauth flows.

---

## 6. Channel-Mix Confound

**What:** upstream traffic source allocation shifts during the test. Variant differences reflect channel mix, not treatment effect.

**Impact:** ghost wins and ghost losses.

**Mitigation:**
- Restrict population to a stable channel (e.g. organic only).
- Stratify analysis by channel.
- Watch for paid campaign launches/changes during the test window.

**Apply to:** landing pages, signup flows, anything reachable from paid channels.

---

## 7. Instrumentation Drift

**What:** event firing rate or property structure changes mid-test (deploy of unrelated code, SDK upgrade, schema change).

**Impact:** metric calculations break across the test boundary; analysis becomes unreliable.

**Mitigation:** lock instrumentation during the test; alert on event-rate anomalies; re-validate exposure event at every ramp gate.

**Apply to:** every test, especially those running across active deploy cycles.

---

## 8. Multiple Comparisons

**What:** running many secondary metrics (or many variants) inflates the false-positive rate without correction.

**Impact:** spurious "significant" findings that don't reproduce.

**Mitigation:**
- Pre-register primary + ≤3 secondaries.
- Apply Bonferroni or Benjamini-Hochberg correction for additional metrics.
- Treat all post-hoc findings as exploratory.

**Apply to:** tests with 3+ secondaries or 3+ variants.

---

## 9. Selection Bias

**What:** the population that triggers the experiment is non-random (e.g. only users who reached step 3 of onboarding see the test; their characteristics differ from the full population).

**Impact:** treatment effect doesn't generalise.

**Mitigation:** trigger-based analysis (only compare units who actually were exposed); document the exposed sub-population explicitly.

**Apply to:** mid-funnel surfaces, conditional features.

---

## 10. Long-Term Effect Lag

**What:** the metric that matters (revenue, retention, LTV) lags the test window.

**Impact:** short-loop proxy moves but headline metric doesn't follow.

**Mitigation:** declare a short-loop proxy AND a long-loop final metric; commit to a Phase-2 holdout for the long-loop validation.

**Apply to:** monetisation tests, retention tests, anything with revenue lag > test duration.

---

## How to Use This File

1. Read each section.
2. Mark the threats that apply to your surface.
3. For each marked threat, write the mitigation into the spec.
4. If a threat applies but cannot be mitigated, downgrade the test to Directional Exploration or change the method.
