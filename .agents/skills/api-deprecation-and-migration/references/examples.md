# API Deprecation and Migration — Full Worked Examples

Skill: `api-deprecation-and-migration` | addyosmani patterns, security-scanned SAFE.

---

## Example 1 — REST version sunset

**Input:** Deprecate `GET /api/v1/invoices`

**Decision:** v2 covers all fields; 12k daily v1 calls from 3 legacy partners.

**Plan:** 60-day notice → `Deprecation` + `Link` headers → partner office hours → v1 410 after traffic < 0.1% for 7 days.

**Migration guide:** Field mapping table + Postman collection.

---

## Example 2 — Feature flag removal

**Input:** Remove `legacy_checkout` after new flow stable

**Steps:** Metric shows 99.2% on new flow → email stragglers → force flag on for remaining tenants → delete branch and dead code in one release.

---

## Example 3 — Compulsory (security)

**Input:** Old auth endpoint uses weak hashing

**Output:** 30-day compulsory migration; new endpoint live; old returns 403 with migration doc after deadline; no extension without security sign-off.

---

See `SKILL.md` for hard rules and verification checklist.
