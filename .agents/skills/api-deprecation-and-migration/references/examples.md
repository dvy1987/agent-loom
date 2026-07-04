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

---

## Example 4 — Extended pass (L3 enrichment)

## Example 5 — Anti-skip (rationalization defense)

**Input:** Agent tries to skip a gate

| Excuse | Reality |
|---|---|
| "Nobody uses the old API" | Check logs — Hyrum's Law says otherwise. |
| "Just delete it" | Forced migrations without notice become incidents. |
| "We'll support both forever" | Two systems = double security and cognitive cost. |
| "Migration guide is enough" | Tooling and deadlines drive completion. |
| "Breaking change in minor is fine" | Semver exists so clients can plan. |

## Example 6 — Step-by-step execution

**Input:** "Run `api-deprecation-and-migration` on [concrete task]"

**Agent actions:**
1. Deprecation decision
2. Announce
3. Migrate
4. Sunset
5. Remove and document

## Example 7 — Gotcha application

**Apply:**
- Announcing without migration guide guarantees support churn.
- Breaking changes in patch versions destroy trust.
- Dual-write without reconciliation causes data drift.
- "We'll remove it someday" with no metric never happens.
- 

## Verification checklist (L3)

- [ ] Examples align with SKILL.md hard rules
- [ ] Anti-skip or rationalization pattern shown
- [ ] Output shape matches Impact Report
- [ ] User can trace from input → durable artifact or chat outcome
