# Adversarial Hat — Full Worked Examples

Enriched from SKILL.md + AO Phase 3 depth merge. Copy prompts from `adversarial-prompt.md`.

---

## Example 1 — Three-phase document review (product-soul)

**Input:** Adversarial hat on community feature for retention

**Phase 1 — Diagnostic:** "Community drives retention" = hypothesis, not cited for monthly B2B segment.

**Phase 2 — Creative:** Alternative — embedded help + templates may outperform community for low-frequency users.

**Phase 3 — Challenge:** Fails if founding members go quiet — no moderation playbook.

**Output:** Critical findings + WHAT WOULD NEED TO BE TRUE + STRONGEST ELEMENTS (see SKILL.md template).

---

## Example 2 — In-flight CLAIM → DOUBT (code)

**Input:** Agent about to add global singleton for cache

**CLAIM (author only — not sent to reviewer):**
```
Decision: Add CacheManager singleton in src/lib/cache.ts
Why it matters: Shared across API routes — wrong lifecycle breaks tests
Non-trivial: crosses module boundary, hidden global state
```

**EXTRACT (sent to reviewer):**
```markdown
## ARTIFACT
export class CacheManager { static instance; get(k) { ... } set(k,v) { ... } }

## CONTRACT
- Must work in serverless handlers (no stale cross-request state)
- Must not break parallel tests
- Project uses explicit DI in src/api/* pattern
```

**DOUBT:** Use code-specific prompt from `adversarial-prompt.md`

**RECONCILE:** Finding "singleton breaks serverless" → Valid + actionable → inject per-request cache instead.

---

## Example 3 — Copy-paste DOUBT prompt (plan)

**Input:** Implementation plan Phase 1 has 8 XL tasks

Paste into fresh context:

```
Adversarial review of this plan section. Assume timeline and dependencies are optimistic.
...
ARTIFACT:
[paste Phase 1 task list]

CONTRACT:
FR-1 through FR-5 from feature-spec; MVP demoable in 2 weeks
```

**Finding:** Task 4 "Build entire admin panel" = horizontal slice — split vertically.

---

## Example 4 — TDD satisfies DOUBT

**Input:** Bug fix for `completedAt` missing

1. Author writes failing Prove-It test (RED)
2. **Skip separate DOUBT loop** for behavioral claim — repro test is the doubt
3. Fix → GREEN → ship

---

## Example 5 — Cross-model offer (interactive)

After cycle 1 on payment migration:

```
Adversarial pass complete: 1 Critical (data loss on rollback), 2 Significant.
Want a second model to review the same ARTIFACT+CONTRACT cold? (y/n)
```

User: yes → spawn with file-based artifact per `adversarial-prompt.md` stdin-safe section.

---

## Example 6 — Doubt theater escalation

**Cycle 1:** 0 findings  
**Cycle 2:** 0 findings  
**Cycle 3:** Reviewer says "looks good"

**Action:** Stop. Report doubt theater. Escalate CLAIM + artifacts to user — do not loop.

---

## Example 7 — Reconcile table

| Finding | Classification | Action |
|---------|----------------|--------|
| Missing rate limit | Valid trade-off | User decides ship v1 without |
| Wrong HTTP status | Valid + actionable | Fix, re-run cycle 2 |
| "Prefer tabs over spaces" | Noise | Dismiss |

---

## Example 8 — Architecture ADR doubt

**ARTIFACT:** "We'll use event sourcing for notifications"

**CONTRACT:** Team size 2, MVP in 6 weeks, current stack Postgres + REST

**Finding (Significant):** ES ops burden exceeds team capacity — Consider outbox pattern instead.

---

## Example 9 — Fresh-context document escalation

**When:** PRD about to ship to stakeholders; 0 critical on first pass; reviewer agreed in 30 seconds

**Action:** Run Fresh-Context mode with `adversarial-prompt.md` core prompt — pass PRD section + success metrics as CONTRACT only.

---

See `references/adversarial-prompt.md` for all copy-paste prompts (code, plan, architecture, TDD, CLI shapes).
See `SKILL.md` for three-phase Diagnostic → Creative → Challenge and stop conditions.
