# Harness Engineering — Examples

## Ex.1 — Bootstrap

**Input:** "Set up harness for my new Next.js app."

**Route:**
1. `project-setup` (no AGENTS.md)
2. `harness-generation` v0
3. `eval-rubric-design` — harness reliability dimensions
4. `eval-pipeline` — stub regression

---

## Ex.2 — Evolution blocked

**Input:** "Evolve the harness now."

**Check:** No `docs/harness/eval-interface.md`.

**Route:** `eval-rubric-design` → `eval-pipeline` → then `harness-evolution`.

---

## Ex.3 — Agent chain + harness

**Input:** "Build a review agent chain and make sure the harness is solid."

**Route:**
1. `harness-generation` if no manifest
2. `process-decomposer` → `agent-builder`
3. `setup-evaluation` (harness + eval checks)
4. PASS → `agent-launcher`

Harness and topology proceed in parallel only if no shared file writes conflict.
