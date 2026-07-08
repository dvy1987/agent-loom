---
name: api-deprecation-and-migration
description: >
  Retire application APIs, libraries, and features safely — graduated deprecation,
  migration guides, consumer tracking, and removal only at zero usage. Load when
  replacing a system, sunsetting a feature, consolidating duplicates, or planning
  removal timelines. Also triggers on "API deprecation", "migrate users off",
  "sunset this endpoint", "strangler migration". Not for skill-library retirement
  (use deprecate-skill).
license: MIT
metadata:
  author: dvy1987
  version: "1.0"
  category: project-specific
  sources: addyosmani/agent-skills deprecation-and-migration (11/12, 2026-05-29)
---

# API Deprecation and Migration

You remove **application surface area** safely — not skill files. Code is a liability; deprecation needs a proven replacement, measured usage, and migration tooling.

## Hard Rules

- **Never deprecate without a working replacement** in production.
- Default to **advisory** deprecation; compulsory only for security or unsustainable cost.
- **Measure usage** before announcing — quantify migration scope.
- If you own the infrastructure, you **migrate consumers or provide adapters** (Churn Rule).
- Distinguish from `deprecate-skill` (retires agent-loom skills, not app APIs).

---

## Workflow

### Step 1 — Deprecation decision

Answer:

1. Does the old system still provide unique value? → If yes, maintain.
2. How many consumers? → Metrics, logs, dependency graph.
3. Does replacement cover critical use cases? → If no, build first.
4. Migration cost per consumer vs maintenance cost of keeping old?

Choose **advisory** (warnings, docs) or **compulsory** (hard deadline + tooling).

### Step 2 — Announce and document

```markdown
## Deprecation: [OldService]

Status: Deprecated [date] | Replacement: [NewService]
Removal: [advisory date OR compulsory deadline]
Reason: [one line]

### Migration
1. [concrete step]
2. [config change]
3. Verify: [script/test/command]
```

### Step 3 — Migrate incrementally

Per consumer: identify touchpoints → switch to replacement → verify behavior → remove old references.

Patterns (pick one):

- **Strangler:** route traffic % to new system until old handles 0%
- **Adapter:** old interface delegates to new implementation
- **Feature flag:** per-user or per-tenant cutover

### Step 4 — Remove old system

Only when usage is **zero** (metrics confirm):

1. Remove code, tests, config, docs
2. Remove deprecation notices
3. Log completion in changelog/ADR if user-visible

---

## Gotchas

- **Hyrum's Law:** undocumented behavior becomes a contract — adapters may be required.
- Zombie code (no owner, active users) needs an owner or a dated removal plan.
- Do not add features to deprecated systems — invest in the replacement.
- Compulsory deprecation without migration tooling fails users.

---

## Common Rationalizations

| Excuse | Reality |
|--------|---------|
| "It still works, why remove?" | Unowned code accumulates security and cognitive debt. |
| "Someone might need it later" | Rebuild cost < perpetual dual-maintenance. |
| "Migration is too expensive" | Compare 2–3 year maintenance vs one-time migration. |
| "Users will migrate themselves" | They won't without guides, tooling, or your migration work. |
| "We can run both forever" | Dual systems double test, doc, and incident surface. |

---

## Output Format

```markdown
## API deprecation — [system]

Type: [advisory/compulsory] | Consumers: [count]
Replacement: [name] | Migration guide: [link/path]
Progress: [N/M migrated] | Removal target: [date]
Risks: [open items]
```

---

## Examples

<examples>
  <example>
    <input>"Replace REST v1 tasks API with v2."</input>
    <output>
Measure v1 traffic. Publish migration guide + adapter for legacy clients. Strangler: 10% → 50% → 100% to v2. Compulsory removal date only after 30d zero v1 traffic. Not the same as deprecate-skill.
    </output>
  </example>
</examples>

---

## Verification

- [ ] Replacement is production-proven for critical use cases
- [ ] Migration guide has concrete steps and examples
- [ ] Current usage quantified (metrics/logs/deps)
- [ ] Consumers migrated or adapter provided before removal
- [ ] Old code and deprecation notices fully removed after zero usage

---

## Prune Log
Last pruned: 2026-06-29
- No prunes — content verified current

## Impact Report

```
System: [name] | Type: [advisory/compulsory]
Consumers: [N] | Migrated: [N/M]
Removal: [date or blocked reason]
```
