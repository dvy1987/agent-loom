# Experiment Spec Template

Use this exact structure when writing `docs/experiments/specs/YYYY-MM-DD-<slug>-spec.md`. Every section is required unless explicitly marked optional.

---

```markdown
# Experiment: <Name>

**Decision class:** Causal | Directional | Instrumentation
**Status:** Draft | Approved | Launched | Concluded
**Owner:** <name>
**Created:** YYYY-MM-DD
**Linked spec / runbook / analysis:** <paths>

---

## 1. Hypothesis

We believe **[change]** will **[direction]** **[primary metric]** for **[population]** because **[mechanism]**.

If it does, we will **[decision]**.

---

## 2. Method

- **Method:** A/B | Holdout | Switchback | Quasi-experiment | MAB
- **Why this method:** <one-line justification, reference method-selector>
- **Randomisation unit:** user | account | session | group | device
- **Exposure event:** `<event_name>` with `<properties>`
- **Population:** <cohort definition>
- **Variant allocation:** e.g. `control 50% / treatment 50%` or `treatment 90% / holdout 10%`
- **Variants:**
  - `control` — <description>
  - `treatment` — <description>

---

## 3. Metrics

| Role | Metric | Direction | MDE | Notes |
|------|--------|-----------|-----|-------|
| Primary | <metric> | ↑ or ↓ | X% relative | <definition> |
| Guardrail | <metric> | bound | — | <definition> |
| Guardrail | <metric> | bound | — | <definition> |
| Secondary (exploratory) | <metric> | — | — | <definition> |
| Counter-metric | <metric> | — | — | what would tell us we're optimising the wrong thing |

---

## 4. Sample Size & Duration

- **Baseline (primary):** X%
- **MDE:** X% relative
- **Power / alpha:** 80% / 0.05
- **Required N per arm:** ~N
- **Estimated duration:** X weeks (covers Y full weekly cycles)
- **Variance reduction:** none | CUPED | trigger-based | stratified
- **Status:** ADEQUATE-POWER | DOWNGRADED-TO-DIRECTIONAL | BLOCKED-INSUFFICIENT

---

## 5. Decision Rule (Pre-Committed)

- **Ship if:** primary +≥X% AND no guardrail breach
- **Iterate if:** directionally positive but inconclusive
- **Kill if:** primary neutral/negative OR any guardrail breach
- **Peek policy:** no peeks (default) | sequential testing | alpha-spending plan

---

## 6. Validity Threats

For each applicable threat, list the mitigation. Reference `experiment-spec/references/validity-threats.md`.

- **SRM:** chi-squared check at ramp gates and readout
- **Novelty:** <mitigation or N/A>
- **Primacy:** <mitigation or N/A>
- **Interference:** <mitigation or N/A>
- **Contamination:** <mitigation or N/A>
- **Channel-mix confound:** <mitigation or N/A>
- **Instrumentation drift:** <mitigation or N/A>
- **Multiple comparisons:** <correction strategy>
- **Selection bias:** <mitigation or N/A>
- **Long-term effect lag:** <mitigation or N/A>

---

## 7. Stakeholders & Sign-off

- **Designer:** <name>
- **Engineering owner:** <name>
- **PM/data sign-off:** <name>
- **Approved:** YYYY-MM-DD

---

## 8. Open Questions / Risks

- <bullet>
- <bullet>

---

## 9. Notes

<free-form>
```

---

## Sizing the Spec

- Keep the spec under 2 pages of rendered markdown when possible. Long specs are skipped.
- Push extended methodology and stats notes to a sibling appendix file rather than padding the spec.
- The decision rule MUST be one paragraph, not three.
