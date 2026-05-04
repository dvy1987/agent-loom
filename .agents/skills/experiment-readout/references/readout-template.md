# Readout Template

Use this exact structure when writing `docs/experiments/analyses/YYYY-MM-DD-<slug>-analysis.md`. Every section is required.

---

```markdown
# Readout: <Experiment Name>

**Decision class:** Causal | Directional | Instrumentation
**Decision:** SHIP | ITERATE | KILL | INCONCLUSIVE | SRM-FAIL
**Headline:** <one-sentence summary, max 25 words>
**Spec:** docs/experiments/specs/<file>.md
**Runbook:** docs/experiments/runbooks/<file>.md
**Analyst:** <name>
**Concluded:** YYYY-MM-DD

---

## 1. Validity Checks

| Check | Result | Notes |
|---|---|---|
| SRM (chi-squared) | PASS / FAIL (p=X) | <if FAIL, root cause> |
| Exposure parity | <%, %> | <gap notes> |
| Event-rate stability | stable / drift | <window affected if drift> |
| Sample sufficiency | adequate / underpowered | actual N vs plan N |
| Novelty / long-term | clean / decay observed | <window comparison> |
| Segment sanity | clean / flagged | <segments noted> |
| Multiple comparisons | correction applied / N/A | <method> |
| Channel-mix stability | stable / drift | <stratified result if needed> |

**If any check FAILED:** document the failure here and stop the readout at this section unless the failure can be cleanly handled (trimmed window, stratified analysis).

---

## 2. Primary Metric

| Variant | N | Primary metric | 95% CI |
|---|---|---|---|
| Control | N_c | x_c | [low, high] |
| Treatment | N_t | x_t | [low, high] |

- **Effect:** absolute X, relative Y%
- **Test:** <e.g. Welch's t-test / Bayesian posterior>
- **p-value or posterior:** X (Causal only — omit for Directional)
- **CI excludes 0 in spec direction:** yes / no

---

## 3. Guardrails

| Metric | Bound | Observed | Status |
|---|---|---|---|
| <metric> | ≤ +5% | +1.2% | held |
| <metric> | ≥ -3% | -0.4% | held |

If any breached: name it, name the magnitude, name whether the spec's decision rule treats it as a kill condition.

---

## 4. Decision Rule Match

Quote the spec's decision rule verbatim. Then state which condition was met:

> Spec rule: "Ship if primary +≥3% AND no guardrail breach; iterate if directional; kill if neutral/negative OR guardrail breach."

**Matched condition:** <which one>
**Decision:** SHIP | ITERATE | KILL | INCONCLUSIVE

If the team wants a decision that does not match the rule, document the rule revision and reasoning. Never silently override.

---

## 5. Exploratory Findings (Optional)

Tag every finding as `[EXPLORATORY]`. These cannot be the ship justification. They inform future hypotheses.

- `[EXPLORATORY]` Mobile users showed 2x the lift of desktop users.
- `[EXPLORATORY]` Returning users showed no effect.

---

## 6. Caveats & Validity Notes

Anything that limits the strength of the headline:
- Underpower in a segment.
- One-week run that didn't capture full novelty window.
- Holdout still pending for Phase-2 confirmation.

---

## 7. Recommendation & Next Steps

- **Recommendation:** <ship / iterate / kill / re-run with X / phase-2 holdout>
- **Phase-2 holdout required:** yes / no, until <date>
- **Downstream:** route to prd-writing / architectural-decision-log / reality-check / none

---

## 8. Learnings Entry (Mirror)

Mirror the entry that was appended to `docs/experiments/learnings.md` for traceability.
```

---

## Sizing the Readout

- Keep the readout to one rendered page when possible. Long readouts go unread.
- Push raw query output, plots, and segment tables to a sibling appendix file rather than padding the readout.
- The decision section MUST be one paragraph, not three.
