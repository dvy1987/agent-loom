# Experiment Spec — Full Worked Examples

Skill: `experiment-spec` | Enriched from SKILL.md (improve-skills pass, SKIP_RESEARCH).

## Example 1 — Step-by-step execution

**Input:** "Run `experiment-spec` on [concrete task]"

**Agent actions:**
1. Frame the Hypothesis
2. Declare Decision Class
3. Choose the Method
4. Define Unit and Exposure
5. Define Metrics
6. Sample Size & Duration
7. List Validity Threats
8. Decision Rule + Peek Policy

**Impact Report shape:**
```
Spec written: docs/experiments/specs/YYYY-MM-DD-<slug>-spec.md
Decision class: [Causal | Directional | Instrumentation]
Method: [A/B | Holdout | Switchback | Quasi | MAB]
Primary metric: [name, direction, MDE]
Guardrails: [list]
Sample plan: [N per arm × duration weeks]
Decision rule: [one-liner]
Validity threats listed: [count]
Status: [READY-TO-LAUNCH | DOWNGRADED-TO-DIRECTIONAL | BLOCKED-INSUFFICIENT-POWER]
```

## Example 2 — Gotcha application

**Input:** Task hits a non-obvious edge case

**Apply:**
- **MDE is relative, not absolute.** "5% lift" almost always means 5% **relative** to baseline (4.0% → 4.2%) — not 5 percentage points (4.0% → 9.0%). Stating MDE without the unit is the #1 source of post-launch surprise about sample size.
- **The if-clause IS the spec.** A spec without "if it does, we will [decision]" is not falsifiable — it's an aspiration. Refuse to finalise until the if-clause exists.
- **Exposure event ≠ flag fetch.** The spec must define exposure as the moment the user *sees* the variant. Conflating the two means SRM checks are meaningless and the readout will silently fail.
- **Duration must cover whole-week multiples.** Day-of-week effects (e.g., weekend signups) bias short tests. Round up to 7, 14, or 21 days; a "10-day test" almost always misrepresents weekly seasonality.

---

See `SKILL.md` for hard rules and verification checklist.
