# Harness Evolution — Examples

## Ex.1 — Accept (Tooling layer)

**Symptom:** Agent loops on `npm test` with wrong cwd.

**Diagnosis:** Execution + Tooling — primary Tooling (schema missing `working_directory`).

**Candidate:** Update `docs/harness/tools.md` + middleware default cwd.

**Regression:** held-in +2, held-out +1 → **promote v0→v1**.

---

## Ex.2 — Reject (prompt bloat)

**Symptom:** Generic failures on diverse tasks.

**Diagnosis:** Attempted 40-line AGENTS.md addition without cluster mapping.

**Regression:** held-out -3 → **reject**; log as F5 generic prompt bloat.

---

## Ex.3 — RHO fallback (no labels)

**Symptom:** Production traces only; no benchmark labels.

**Path:** Coreset 10 hard sessions → 3 rollouts each → self-preference picks candidate-1.

**Promotion:** mean_score > 0 vs baseline → promote with `evidence: label-free` flag in manifest.

**Follow-up:** User should add `eval-pipeline` labels when available.

---

## Ex.4 — Confound isolation (Meta-Harness)

**Symptom:** Combined AGENTS.md + middleware edit regressed held-out -2.

**Diagnosis:** Prompt+structure coupling — cannot attribute which class caused regression.

**Path:** Rollback both → re-propose **additive-only** AGENTS.md clause first → re-eval → then middleware in separate round.

**Result:** Middleware-only round held-out +1 → **promote**; prompt clause deferred to next cluster.

---

## Ex.5 — Repair memory reject (HarnessFix)

**Symptom:** Proposer re-suggested same tool-schema fix rejected in round 2.

**Diagnosis:** Repair memory miss — rejection reason `insufficient target improvement` not logged.

**Path:** Log reject in `docs/harness/runs/iteration_003/repair_memory.json` → proposer context includes rejected summary.

**Result:** New candidate targets different cluster → **accept**.
