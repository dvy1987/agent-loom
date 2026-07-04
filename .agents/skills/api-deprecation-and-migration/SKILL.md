---
name: api-deprecation-and-migration
description: >
  Deprecate APIs, features, or systems safely — announce, migrate consumers,
  sunset on a timeline, and document alternatives. Load when removing an old
  API, migrating users between implementations, sunsetting a feature, or the
  user asks about deprecation policy, migration guides, or breaking changes.
  Not for deleting dead code with zero consumers (use code-simplification).
  Distinct from meta `deprecate-skill` (skill library retirement).
license: MIT
metadata:
  author: dvy1987
  version: "1.0"
  category: project-specific
  sources: addyosmani/agent-skills deprecation-and-migration (11/12, 2026-05-29)
  resources:
    references:
      - examples.md
---

# API Deprecation and Migration

Code is a liability. Deprecation removes systems that no longer earn their keep; migration moves consumers safely to replacements.

## Hard Rules

- **Replacement before removal** — working alternative with docs and migration path.
- **Default advisory** — warnings and timelines; compulsory only for security or unsustainable cost.
- **Quantify consumers** — usage metrics, client lists, or repo search before dates.
- **Hyrum's Law** — undocumented behavior will be depended on; plan for stragglers.
- **Telemetry on migration** — track who still calls deprecated surfaces.

---

## Workflow

### Step 1 — Deprecation decision

Answer: unique value remaining? consumer count? replacement ready? migration cost vs maintenance cost?

### Step 2 — Announce

Publish notice: what, why, timeline, replacement, migration guide link, contact.

### Step 3 — Migrate

Provide codemods, dual-write/read periods, feature flags, or versioned endpoints as appropriate.

### Step 4 — Sunset

After deadline: return structured errors on old surface; keep read-only tombstone period if needed.

### Step 5 — Remove and document

Delete code; update changelog; postmortem on straggler pain for next time.

---

## Advisory vs compulsory

| Type | When | Mechanism |
|------|------|-----------|
| Advisory | Stable old path, low risk | Docs + warnings + metrics |
| Compulsory | Security, blocking progress | Hard deadline + tooling + support |

---

## When NOT to use

- Internal dead code with zero callers (delete with tests)
- Retiring a skill from agent-loom library (`deprecate-skill` instead)

---

## Gotchas

- Announcing without migration guide guarantees support churn.
- Breaking changes in patch versions destroy trust.
- Dual-write without reconciliation causes data drift.
- "We'll remove it someday" with no metric never happens.

---

## Common Rationalizations

| Excuse | Reality |
|--------|---------|
| "Nobody uses the old API" | Check logs — Hyrum's Law says otherwise. |
| "Just delete it" | Forced migrations without notice become incidents. |
| "We'll support both forever" | Two systems = double security and cognitive cost. |
| "Migration guide is enough" | Tooling and deadlines drive completion. |
| "Breaking change in minor is fine" | Semver exists so clients can plan. |

---

## Output Format

```markdown
## Deprecation plan — [surface]

Consumers: [count/evidence]
Replacement: [link]
Type: [advisory/compulsory]
Timeline: [dates]
Migration: [steps/tooling]
Removal criteria: [metric or date]
```

---

## Examples

<examples>
  <example>
    <input>"Remove REST v1 `/users` in favor of v2."</input>
    <output>90-day advisory → `Sunset` header → v1 returns 410 with link; codemod for internal clients; dashboard on v1 traffic.</output>
  </example>
</examples>

---

## Verification

- [ ] Replacement documented and production-proven
- [ ] Consumer impact quantified
- [ ] Timeline and notice published
- [ ] Migration tooling or guide available
- [ ] Telemetry proves traffic at zero before code removal

---

## Red Flags

- Sunset announced without working replacement and docs
- Breaking change shipped in patch or minor version
- Dual-write path has no reconciliation or drift checks
- Deprecation timeline set without consumer usage evidence
## Impact Report

```
Surface: [name] | Consumers: [N]
Type: [advisory/compulsory] | Sunset: [date]
Migration: [ready/partial]
```
