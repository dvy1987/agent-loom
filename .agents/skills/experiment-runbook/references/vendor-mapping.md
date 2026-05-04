# Vendor Mapping

Single mapping table covering the major experimentation platforms. Use this when the spec routes to a vendor other than PostHog. The user adapts; this skill does not ship dedicated adapters per vendor.

---

## Concept Mapping Table

| Concept | PostHog | GrowthBook | Statsig | LaunchDarkly | Optimizely | Eppo |
|---|---|---|---|---|---|---|
| Experiment object | Experiment + Feature Flag | Experiment | Experiment | Flag with variations | Experiment | Experiment |
| Variant identifier | Flag variant key | Variation key | Variant ID | Variation key | Variation key | Variant key |
| Assignment unit (user) | `distinct_id` | `attributeKey` (user) | `userID` | `user.key` | `user_id` | `subjectKey` |
| Assignment unit (account/group) | `posthog.group()` | `groups` attribute | Custom unit | Context (multi-context) | audience | Subject + entity |
| Exposure event | `$feature_flag_called` (auto) or custom | `experimentViewed` | auto-logged exposure | `evaluation` event | activation event | auto-logged assignment |
| Metric source | Insight on event | Data source (warehouse) | Pulse / event | LD Experimentation | Optimizely Analytics | Warehouse-native |
| Holdout pattern | Separate flag | Holdout group | Layer + holdout | Targeting rule | Audience exclusion | Holdout assignment |
| SRM check | Manual insight or alert | Built-in | Built-in | Manual | Built-in | Built-in |
| Sample-size calculator | External | Built-in | Built-in | External | Built-in | Built-in |
| CUPED / variance reduction | Manual | None native | CUPED supported | None native | Optional | CUPED supported |
| Sequential testing | Manual | Built-in (msPRT) | Sequential available | None native | Optional | Sequential supported |

---

## Adapter-Writing Pattern

When binding a spec to a non-PostHog platform:

1. **Map every concept** in the table above; list any unmappable concepts as gaps.
2. **Identify exposure-event semantics** — the #1 source of mis-binding. Some platforms log on flag fetch, some on render. Match this to the spec's intent.
3. **Verify SRM tooling** — if the platform doesn't auto-check SRM, set up a manual chi-squared dashboard before launch.
4. **Lock assignment salt / unit** — every platform supports this differently; document the locked path explicitly.
5. **Document holdout pattern** — separate flag (PostHog, GrowthBook, LaunchDarkly), or layer/holdout primitive (Statsig, Eppo).

---

## Platform-Specific Notes

### GrowthBook
- Open-source self-hosted option with built-in Bayesian + sequential support.
- Data source connects to your warehouse (Snowflake, BigQuery, Postgres, etc.); no client-side metric calculation.
- Strong fit if you already have a warehouse; weaker if you don't.

### Statsig
- "Layer" abstraction lets you run multiple experiments on the same surface with deterministic mutual exclusion. Powerful but adds modelling complexity.
- Built-in CUPED, sequential testing, and SRM checks.

### LaunchDarkly
- Primarily a feature-flag platform; experimentation is a layer on top.
- Excellent multi-context targeting (user / account / device simultaneously).
- Weaker analytics; expect to export to a warehouse for serious readouts.

### Optimizely
- Long-standing platform with marketing-tilted UI.
- Strong stat engine (sequential by default) and built-in SRM checks.
- Pricing favours larger teams.

### Eppo
- Warehouse-native — all metric computation runs on your warehouse.
- Strong fit for teams with mature data infrastructure.
- Weaker for early-stage teams without a warehouse pipeline.

---

## When to Pick What

- **Solo / small team, PostHog already in use** → PostHog. Don't switch unless a hard constraint forces it.
- **Already running a warehouse, want stat rigour** → Eppo or GrowthBook.
- **Many concurrent experiments on shared surfaces** → Statsig (layers) or Optimizely.
- **Feature flags first, experimentation second** → LaunchDarkly + warehouse for analysis.
- **Marketing-led, low engineering touch** → Optimizely.

---

## Capability Gap Convention

If a chosen platform lacks a capability the spec requires (e.g. no built-in SRM, no CUPED), document the gap explicitly in the runbook's `Platform Capability Gaps` section, with the manual mitigation:

```markdown
## Platform Capability Gaps
- SRM: not auto-monitored. Mitigation: chi-squared insight in Metabase, alert at p<0.001.
- CUPED: not native. Mitigation: not applied; sample plan adjusted for higher variance.
```
