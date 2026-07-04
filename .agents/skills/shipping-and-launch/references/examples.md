# Shipping and Launch — Full Worked Examples

Skill: `shipping-and-launch` | addyosmani patterns, security-scanned SAFE.

---

## Example 1 — Feature-flagged UI release

**Input:** "Launch redesigned settings page"

**Plan:** Flag `settings_v2` off in prod. Deploy artifact. Enable 5% internal → 10% beta users → 50% → 100% over 3 days.

**Monitoring:** Client error boundary reports, settings save success rate, support tag `settings`.

**Rollback:** Flip flag off; old bundle still deployed.

---

## Example 2 — Database migration launch

**Input:** "Add `tenant_id` column to orders"

**Plan:** Expand (nullable column) → backfill job → code reads/writes new column → contract (NOT NULL) in later release.

**Rollback:** Revert app to ignore column; column stays nullable until next window.

**Checklist:** Backup verified, migration idempotent, lock time measured on staging clone.

---

## Example 3 — Deferred a11y item

**Input:** Launch blocked on one contrast issue on secondary button

**Output:** Explicit deferral: "Secondary CTA contrast 3.8:1 — fix in hotfix #482 within 48h; launch approved with banner in runbook."

---

See `SKILL.md` for hard rules and verification checklist.

---

## Example 4 — Extended pass (L3 enrichment)

## Example 5 — Anti-skip (rationalization defense)

**Input:** Agent tries to skip a gate

| Excuse | Reality |
|---|---|
| "It's a small change" | Small deploys still need rollback and error visibility. |
| "We'll add alerts after launch" | You discover outages from users instead of dashboards. |
| "Full send is faster" | One incident costs more than a canary day. |
| "Rollback is unlikely" | Plan for it anyway — Hyrum's Law applies in prod. |
| "Checklist is bureaucracy" | It's how you remember security and a11y under time pressure. |

## Example 6 — Step-by-step execution

**Input:** "Run `shipping-and-launch` on [concrete task]"

**Agent actions:**
1. Define success and risk
2. Pre-launch checklist
3. Staged rollout
4. Monitor and decide
5. Rollback or complete

## Example 7 — Gotcha application

**Apply:**
- "Green staging" with 10x less data than prod hides query issues.
- Launch without feature flags forces redeploy to rollback.
- Announcing before monitoring is wired means flying blind.
- Skipping comms strands on-call.
- 

## Verification checklist (L3)

- [ ] Examples align with SKILL.md hard rules
- [ ] Anti-skip or rationalization pattern shown
- [ ] Output shape matches Impact Report
- [ ] User can trace from input → durable artifact or chat outcome
