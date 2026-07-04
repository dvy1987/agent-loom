# Experiment Readout — Full Worked Examples

Skill: `experiment-readout` | Enriched from SKILL.md (improve-skills pass, SKIP_RESEARCH).

## Example 1 — Step-by-step execution

**Input:** "Run `experiment-readout` on [concrete task]"

**Agent actions:**
1. Pre-Flight Validity Checks (Blocking)
2. Compute Primary Metric Effect
3. Compute Guardrail Metrics
4. Apply the Decision Rule
5. Novelty / Long-Term Check (Conditional)
6. Segment & Exploratory Analysis (Optional, Tagged)
7. Write the Analysis File
8. Append to Learnings

**Impact Report shape:**
```
Analysis: docs/experiments/analyses/YYYY-MM-DD-<slug>-analysis.md
Validity: SRM=[PASS/FAIL] | Exposure parity=[ok/skew] | Event rate=[stable/drift]
Sample sufficiency: [adequate / underpowered]
Primary effect: [point estimate, 95% CI, p-value or posterior]
Guardrails: [N held / N breached]
Decision: [SHIP | ITERATE | KILL | INCONCLUSIVE | SRM-FAIL]
Decision-rule match: [literal condition met]
Novelty / long-term: [check result, holdout required yes/no]
Learnings entry: [appended yes]
Downstream: [prd-writing | architectural-decision-log | reality-check | none]
```

## Example 2 — Gotcha application

**Input:** Task hits a non-obvious edge case

**Apply:**
- **SRM is the silent killer of trust.** A failed SRM invalidates everything downstream — not "with caveats", entirely. The chi-squared check runs first and is blocking. Phantom wins almost always trace to broken randomisation, not real lift.
- **"Significant" is forbidden vocabulary for Directional and Instrumentation tests.** Watch for it slipping in via stakeholder summaries; strip it from every readout that wasn't pre-declared Causal with adequate power.
- **Confidence intervals that exclude zero ≠ a "win" if a guardrail breached.** The decision rule is conjunctive — primary AND guardrails. A primary lift with a guardrail breach is KILL, not "ship with watchlist".
- **Exposure parity gaps point at instrumentation, not user behaviour.** A 5%+ gap between assigned and exposed is almost always an asynchronous render or flag-fetch-before-render issue. Investigate before reporting metrics, not after.

---

See `SKILL.md` for hard rules and verification checklist.
