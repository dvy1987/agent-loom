# Validity Checks

Run these before any metric analysis. Order matters: SRM first, because if randomisation is broken, every downstream computation is suspect.

---

## 1. Sample Ratio Mismatch (SRM) — BLOCKING

**Method:** chi-squared test on observed unit counts per variant against the planned allocation.

```
expected_count_v = total_units × allocation_v
chi_sq = sum( (observed_v - expected_count_v)^2 / expected_count_v )
p = chi_sq_pvalue(chi_sq, df = num_variants - 1)
```

**Threshold:** p ≥ 0.001 sustained over the analysis window. Sustained means the SRM monitor was not flagging across the test.

**FAIL action:** stop. Do NOT compute primary or guardrail metrics. Write a diagnostic readout that names the SRM failure, suspected causes, and remediation. Common SRM causes:

- Bot/crawler traffic landing disproportionately on one variant.
- A code path that bypasses flag evaluation for one variant.
- Cookie / `distinct_id` collision causing some units to be re-randomised.
- Rendering failure on one variant causing exposure mis-firing.
- Salt change mid-experiment.
- Time-bucketing bugs (Monday users in control, Friday in treatment).

**Note:** SRM is not a stat-engine problem to solve with a different test — it is a data quality alarm. Fix it, do not "p-correct around it".

---

## 2. Exposure Parity

**Method:** `% of assigned units that actually fired the exposure event`, computed per variant.

**Threshold:** parity within ~3% across variants. Large gaps suggest the variant rendering is failing for some units.

**FAIL action:** investigate variant rendering before metric analysis. Document any unfixable gap as a validity caveat in the readout.

---

## 3. Event-Rate Stability

**Method:** time-series of primary and guardrail event rates across the test window.

**Look for:**
- Sudden drops or spikes (indicates instrumentation deploy, schema change, or outage).
- Day-of-week patterns that look different between variants.
- Mid-test changes in the absolute rate of either variant.

**FAIL action:** trim the affected window from the analysis if isolated; downgrade the test to inconclusive if drift is pervasive.

---

## 4. Sample Sufficiency

**Method:** compare actual sample to spec's planned N per arm.

**Threshold:** ≥ 90% of plan = adequate. Below that = underpowered.

**FAIL action:** downgrade Causal → Directional, or (if test still running) extend duration. Do NOT claim significance on an underpowered Causal test.

---

## 5. Novelty / Primacy Window Check

**Apply when:** spec listed novelty or primacy as a threat.

**Method:** compute primary effect for the first 24–48h, the early window (week 1), and the late window (week 2+). Compare.

**Look for:**
- Initial bump that decays = novelty effect.
- Initial dip that recovers = primacy effect.
- Stable across windows = no detected novelty/primacy.

**FAIL action:** if novelty/decay is detected, the headline result must include a confidence downgrade and a recommendation for Phase-2 holdout monitoring (4+ weeks post-ship).

---

## 6. Segment Sanity

**Method:** primary effect within key strata (mobile / desktop, country, plan, traffic source).

**Look for:**
- One segment driving the entire effect (Simpson's paradox risk).
- Effect direction flipping across segments.
- A single anomalous segment (single country, single device type).

**FAIL action:** document as a caveat. Segment-level findings are EXPLORATORY unless pre-registered.

---

## 7. Multiple-Comparisons Hygiene

**Apply when:** more than 3 secondary metrics were checked, or 3+ variants.

**Method:** apply Bonferroni or Benjamini-Hochberg correction to the family of comparisons. Do not mix corrected and uncorrected p-values in the readout.

---

## 8. Channel-Mix Stability

**Apply when:** spec listed channel-mix confound as a threat.

**Method:** compare upstream channel mix in control vs treatment populations.

**FAIL action:** stratify analysis by channel; if stratification reverses the effect direction, confound dominates and the test is inconclusive on the population question.

---

## Common Anti-Patterns

- Computing primary first, "checking" SRM only when results look weird.
- Reporting p-values from underpowered tests because the point estimate "looks like a winner".
- Quietly dropping a guardrail breach by reframing it as a "secondary metric we don't care about".
- Re-running the SRM test until it passes by chance.
- Adjusting allocation mid-test because traffic is uneven (this re-randomises and breaks comparability).
