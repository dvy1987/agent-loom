# Launch QA Checklist

Pre-launch verification list. Block launch on ANY fail. Run the full checklist for every Causal Decision experiment; abbreviated for Directional / Instrumentation.

---

## A. Flag & Assignment

- [ ] Flag key matches the runbook spec exactly (no typos, no version drift).
- [ ] Flag is set to the correct rollout percentage for stage 1 of the ramp (typically 1%).
- [ ] Salt is locked; will not change during the experiment.
- [ ] Assignment unit (user / group / session) matches the spec.
- [ ] For known test users: flag returns the expected variants reproducibly across multiple evaluations.
- [ ] Exclusion cohort (internal, bots, QA) is correctly applied.

---

## B. Exposure Event

- [ ] Exposure event fires on actual variant render — not on flag fetch.
- [ ] Exposure event fires for **both** control and treatment (verified manually for at least one user per variant).
- [ ] Exposure event includes `experiment_key` and `variant` properties.
- [ ] Server-side surfaces: exposure event fires from the server (or explicit client-side equivalent), not just from `$feature_flag_called`.
- [ ] Exposure is deduplicated per unit per session if intent is one-per-session.

---

## C. Primary Metric

- [ ] Primary metric event is firing in both variants.
- [ ] Metric definition in the analysis platform matches the spec exactly (numerator / denominator / filters).
- [ ] Metric chart renders, broken down by variant, with non-zero counts in both variants for known test users.
- [ ] Time window aligns with planned analysis window.

---

## D. Guardrails

- [ ] Each declared guardrail metric is wired up.
- [ ] Each guardrail has a chart broken down by variant.
- [ ] Bound (e.g. "≤ +5% bounce rate") is documented in the runbook.
- [ ] Alert configured for severe guardrail breach (where the platform supports it).

---

## E. Variant Rendering

- [ ] Control variant renders the existing experience exactly.
- [ ] Treatment variant renders the spec'd change.
- [ ] No flicker / FOUC (Flash of Unstyled Content) on client-side flag evaluation.
- [ ] No layout shift causing CLS regression.
- [ ] Mobile + desktop both verified.
- [ ] Dark mode verified (if applicable).

---

## F. Data Hygiene

- [ ] Bot / crawler traffic excluded.
- [ ] Internal / employee traffic excluded.
- [ ] Multi-device users handled per spec (typically: identify before flag evaluation).
- [ ] Existing experiments on the same surface are not contaminating (Statsig: layer check; PostHog: cohort check).

---

## G. Dashboards

- [ ] Experiment dashboard exists and is linked from the runbook.
- [ ] Primary trend chart is bookmarked.
- [ ] All guardrail charts are bookmarked.
- [ ] SRM monitor is configured (chi-squared p-value alert at < 0.001 sustained).
- [ ] Exposure parity monitor (% of assigned units that exposed) is configured.

---

## H. Rollback

- [ ] Kill switch path documented (flag override route).
- [ ] Authorised rollback owners listed (oncall, PM, engineer).
- [ ] Trigger conditions for rollback documented.
- [ ] Communication plan for rollback (who tells stakeholders).

---

## I. Sign-off

- [ ] Engineering owner signed off.
- [ ] PM / data owner signed off.
- [ ] Spec is in `Approved` status.
- [ ] Runbook is in `Ready-to-Launch` status.

---

## Abbreviated Checklist for Directional / Instrumentation Tests

For Directional Exploration: A, B, C, E, F, G (skip strict guardrails and rollback rigour).
For Instrumentation Shakedown: A, B, F (focus on exposure / assignment / data hygiene only).

---

## Common Failure Modes Caught Here

- **Stale flag key from a previous test** — A1.
- **Exposure event fires on flag fetch, not render** — B1, B4.
- **Primary metric only firing in treatment** — C2 (forgot to backfill control).
- **Bot traffic dominating one variant** — F1 (causes apparent SRM and false wins).
- **Multi-tab user assigned to both variants** — F3.
- **Salt change between QA and production** — A3 (rare but devastating).
