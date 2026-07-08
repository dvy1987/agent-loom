---
name: shipping-and-launch
description: >
  Ship production changes safely — pre-launch checklist, staged rollout, monitoring,
  rollback plan, and post-deploy verification. Load when deploying to production,
  releasing a feature, migrating data, or opening beta access. Also triggers on
  "shipping and launch", "pre-launch checklist", "production deploy", "rollout plan",
  "rollback strategy". Complements generate-changelog for release notes. Not for
  local-only dev work.
license: MIT
metadata:
  author: dvy1987
  version: "1.0"
  category: project-specific
  sources: addyosmani/agent-skills shipping-and-launch (11/12, 2026-05-29)
---

# Shipping and Launch

You deploy **reversibly, observably, and incrementally**. Every launch has a checklist, monitoring, and a rollback path before traffic moves.

## Hard Rules

- **No deploy without a rollback plan** documented before production traffic.
- **Feature flags** decouple deploy from release when risk is non-trivial.
- **Monitor the first hour** — health, errors, latency, critical user flow.
- Security, performance, and a11y gates must pass or be explicitly waived with owner sign-off.
- Invoke `generate-changelog` for user-visible releases when appropriate.

---

## Workflow

### Step 1 — Pre-launch checklist

Confirm each area (mark N/A with reason):

| Area | Minimum bar |
|------|-------------|
| Code quality | Tests green, lint/types clean, review done |
| Security | No secrets in repo, authZ on sensitive paths, headers/CORS sane |
| Performance | No known regressions on hot paths; budgets met if configured |
| Accessibility | Keyboard + screen reader on changed UI; contrast OK |
| Infrastructure | Env vars, migrations ready, health check, logging/alerts live |
| Documentation | Changelog, API docs, ADRs for architectural changes |

### Step 2 — Rollback plan (before deploy)

```markdown
## Rollback — [release]

Triggers: error rate >2× baseline | p95 +50% | data integrity issue
Steps: 1) disable flag OR revert deploy 2) verify health 3) notify team
DB: [migration reversible? data cleanup?]
Time: flag <1m | redeploy <5m | DB <15m
```

### Step 3 — Staged rollout

```
staging full test → prod deploy (flag OFF) → internal enable →
canary 5% → 25% → 50% → 100% (monitor each step)
```

**Advance thresholds:** error within 10% of baseline; p95 within 20%. **Roll back** if error >2× or p95 >+50%.

### Step 4 — Deploy and monitor

First hour:

1. Health endpoint 200
2. Error dashboard — no new error types
3. Latency dashboard — no regression
4. Manual critical path smoke test
5. Logs flowing; rollback mechanism verified

### Step 5 — Post-launch

- Monitor 24–48h through canary stages
- Remove feature flag + dead code within ~2 weeks of 100% rollout
- Update changelog/README if user-facing (`generate-changelog`)

---

## Feature Flag Rules

- Every flag has an **owner** and **expiration date**
- Test **on and off** in CI when feasible
- Do not nest flags (combinatorial explosion)
- Default new code path **off** until canary

---

## Gotchas

- Staging parity is never perfect — production data and traffic differ.
- Friday-afternoon deploys need stronger justification.
- "Works in staging" without prod monitoring is incomplete.
- Big-bang releases without flags lack a kill switch.

---

## Common Rationalizations

| Excuse | Reality |
|--------|---------|
| "Staging passed, prod will be fine" | Prod has different data, traffic, and edge cases — monitor after deploy. |
| "We don't need feature flags" | Even simple changes benefit from a kill switch. |
| "Monitoring is overhead" | You discover outages from users instead of dashboards. |
| "We'll add monitoring later" | Add before launch — you can't debug what you can't see. |
| "Rolling back is failure" | Shipping broken code is the failure; rollback is responsible engineering. |

---

## Output Format

```markdown
## Shipping plan — [release]

Checklist: [pass/waived items]
Rollout: [stages + flag name]
Rollback: [triggers + steps]
Monitoring: [dashboards/alerts]
Post-launch: [owner + window]
```

---

## Examples

<examples>
  <example>
    <input>"Ship the new task-sharing feature to production."</input>
    <output>
Deploy behind `taskSharing` flag (off). Rollback: disable flag. Canary 5% → monitor errors/latency 24h → ramp. Pre-launch: tests, authZ on share endpoints, changelog via generate-changelog.
    </output>
  </example>
</examples>

---

## Verification

- [ ] Pre-launch checklist completed (waivers documented)
- [ ] Rollback plan written before production deploy
- [ ] Feature flag or incremental rollout path defined for risky changes
- [ ] Monitoring dashboards/alerts confirmed live
- [ ] First-hour post-deploy checks completed and recorded

---

## Prune Log
Last pruned: 2026-06-29
- No prunes — content verified current

## Impact Report

```
Release: [name] | Rollout: [staged/flag/big-bang]
Rollback ready: [yes/no] | First-hour checks: [pass/fail]
Flag cleanup date: [if applicable]
```
