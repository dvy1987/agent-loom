# Route Patterns

Outcome-based branching for failed or divergent plan steps. DyFlow + GAP + NaviAgent synthesis.

---

## Alternate tool

**When:** Same goal, current tool/path blocked.

**Action:** Insert step `Sx.a` with different tool or API. Example: WebFetch 404 → Shell curl with corrected raw URL.

**Delta:** `failed → revised`; add `Sx.1` pending.

---

## Decompose

**When:** Step failed because scope too large or precondition unmet.

**Action:** Replace `Sx` with `Sx.1`, `Sx.2`, … smaller steps. Mark original `revised`.

**Example:** "Run full test suite" fails at env setup → Sx.1 install deps, Sx.2 run targeted tests.

---

## Rollback + revise

**When:** A **done** step's assumption was wrong (observation downstream contradicts it).

**Action:**
1. Mark conflicting done step `revised` in delta log (do not delete history).
2. Insert fix step before current failure.
3. Re-run from fix step.

**Example:** S1 assumed API v1 — S3 discovers v2 only → insert S1.1 migrate client.

---

## Abort

**When:** Goal infeasible (missing credentials, out-of-scope, user constraint).

**Action:** Mark remaining `pending` steps `aborted` in delta log. Escalate user with evidence.

---

## Debug handoff

**When:** `Layer: code` and hypothesis points to defect in existing codebase.

**Action:** Pause plan. Invoke `debug-and-fix`. On fix verified, resume plan at failed step with updated precondition.

---

## Transient retry (narrow exception)

**When:** Rate limit, network timeout, lock contention — **transient only**.

**Action:** Max **one** retry with backoff. Delta log must say `transient retry`. Not valid for logic errors.
