# PostHog Binding

Concrete PostHog mapping for `experiment-runbook`. Every field in this file maps a vendor-neutral spec concept to a specific PostHog construct.

PostHog's experimentation product (Experiments + Feature Flags) is the primary supported platform. This binding works on PostHog Cloud and self-hosted v1.40+.

---

## Concept Mapping

| Spec concept | PostHog construct |
|---|---|
| Experiment | Experiment (UI) backed by a Feature Flag |
| Variant | Feature flag variant key |
| Randomisation unit (user) | Person-property assignment |
| Randomisation unit (account / B2B) | Group-property assignment (`organization`, `team`) |
| Exposure event | `$feature_flag_called` event (auto) OR explicit custom event |
| Primary metric | Trends insight on the metric event, broken down by `$feature_flag_response` |
| Guardrail metric | Trends insight on the guardrail event |
| Cohort filter | Cohort attached to the flag's release condition |
| Holdout | Separate feature flag with persistent assignment, distinct from the experiment flag |

---

## Flag Configuration

```yaml
flag_key: exp_<slug>_<quarter>            # e.g. exp_lp_headline_2026q2
flag_name: <readable name>
release_condition:
  cohort: <cohort_id or filter expression>
variants:
  - key: control
    rollout_percentage: 50
    payload: {}
  - key: treatment
    rollout_percentage: 50
    payload: {}
ensure_consistent_assignment: true        # critical for SRM stability
salt: locked-on-creation                  # do not change mid-experiment
```

**Pitfall:** changing the salt or rollout percentages mid-experiment re-randomises units and silently corrupts results. Lock both at launch.

---

## Assignment

- **User-level:** assignment by `distinct_id` (or alias chain). Use `posthog.getFeatureFlag('exp_<slug>')`.
- **Group-level (B2B):** call `posthog.group('organization', '<org_id>')` before flag evaluation. Configure flag with group type.
- **Session-level:** discouraged; if needed, use a session property and document the trade-off (high variance, contamination risk).

Server-side: use the PostHog server SDK. Pass the same `distinct_id` AND any group identifiers used client-side, otherwise client and server see different variants.

---

## Exposure Event

PostHog auto-captures `$feature_flag_called` whenever a flag is evaluated. This works for client-side flag evaluations.

For server-rendered or async surfaces, the auto-event fires on flag evaluation, NOT on render. Add an explicit exposure event when render is delayed:

```javascript
// when the variant actually renders / takes effect
posthog.capture('experiment_exposed', {
  experiment_key: 'exp_lp_headline_2026q2',
  variant: variantKey,
  surface: 'landing_page'
})
```

Use the explicit event as the exposure source for SRM and analysis.

---

## Cohorts

- **Inclusion cohort:** the population eligible for the experiment (e.g. organic-only visitors, free-trial users).
- **Exclusion cohort:** internal users, bots, QA accounts. Always exclude.
- **Holdout cohort:** separate flag with persistent assignment for long-term holdout tests.

Build the inclusion cohort BEFORE the experiment launches and verify size.

---

## Dashboards

For each experiment, create a dashboard with:

1. **Primary metric trend** — broken down by `$feature_flag_response` (or `variant` from your explicit exposure event).
2. **Guardrail trends** — one per guardrail.
3. **SRM monitor** — chi-squared on exposure counts per variant, alert at p < 0.001.
4. **Exposure parity** — % of assigned units in each variant that fired the exposure event.
5. **Error / latency** — surface-specific.

PostHog's built-in Experiments view computes the primary effect, but verify SRM and exposure parity in custom insights for full trust.

---

## Holdout Pattern

For persistent treatments (lifecycle email, recommendations):

1. Create a separate flag `holdout_<area>_<year>` with 90/10 split (90% in-treatment, 10% holdout).
2. Lock salt and assignment for the full holdout window (4–12 weeks).
3. Exclude the holdout cohort from any A/B tests on the same surface during the window.
4. Analyse at the end of the window — never peek for early significance on a holdout.

---

## Common PostHog Pitfalls

- **Salt change mid-experiment** — re-randomises units, kills SRM. Always lock at launch.
- **Mismatched server / client `distinct_id`** — a logged-out client and a logged-in server can see different variants for the same human. Identify before flag evaluation.
- **Group flags without `posthog.group()` call** — flag evaluates as anonymous, never assigns the group variant.
- **Insight broken-down by anonymous `$device_id`** when the spec randomises by user — silently uses the wrong unit.
- **Auto-capture on a server surface** — `$feature_flag_called` does not fire reliably; add the explicit exposure event.
- **Reusing a flag key for a new experiment** — old assignments contaminate the new run. Always create a fresh key.
