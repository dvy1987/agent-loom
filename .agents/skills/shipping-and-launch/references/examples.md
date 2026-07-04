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
