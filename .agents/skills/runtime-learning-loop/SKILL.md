---
name: runtime-learning-loop
description: >
  Design a self-improvement loop for a shipped product's AI agents —
  production traces feed evals, evals feed improvement proposals (prompts,
  playbooks, retrieval configs), and a human approval gate promotes changes
  with rollback. Technique-agnostic: chooses per project between ACE-style
  evolving playbooks, GEPA/MIPROv2 offline optimization, or simple eval-driven
  iteration via references/techniques.md. Load when the user asks to make my
  product's agents self-improving, learn from production traces, add a
  learning loop, evolve prompts or playbooks safely, promote agent
  improvements, or GEPA-style optimization. NOT harness-evolution (that
  improves the coding agent), NOT experimentation (product A/B tests), NOT
  agent-run-retro (dev-phase manual retros — this skill is the
  production-scale continuation).
license: MIT
metadata:
  author: dvy1987
  version: "1.0"
  category: project-specific
  sources: >
    ACE arXiv:2510.04618 (ICLR 2026), GEPA arXiv:2507.19457 (ICLR 2026 oral),
    DSPy MIPROv2 docs, TextGrad Nature 2025, Contextual AI ACE production
    lessons 2026, aegis competency-gated autonomy ladder
  resources:
    references:
      - techniques.md
      - examples.md
---

# Runtime Learning Loop

You design the loop that lets a *shipped* product's agents get measurably better from their own production activity — safely. You never assume a technique (GEPA is one option, not the default); you match technique to the project's data volume, feedback quality, and budget. The user is non-technical: present proposals as consequences, not mechanisms.

## Hard Rules

Hard preconditions — refuse and route if missing: observability on the target flow (`agent-observability`) AND an eval harness with a held-out set (`eval-pipeline`). No traces + no evals = nothing to learn from and no way to know if "improvement" is real.
No promotion without human approval (Apprentice mode) until the autonomy ladder's advancement gates are met — and never skip the ladder.
Never optimize against the held-out set. It exists only to check proposals; touching it during optimization is self-deception.
Every loop ships with: declared learnable surfaces (allowlist), rollback procedure, regression monitor, budget, and kill-switch — BEFORE the first cycle runs.
Production PII never enters optimization prompts or persisted playbooks — redact at the trace layer first.
Feedback design outranks algorithm choice: a multi-criteria LLM judge (relevance, groundedness, completeness, clarity) beats a bare score, and can beat ground-truth comparison (Contextual AI 2026).

## Workflow

### Step 1 — Precondition check (hard gate)
Verify: traces flowing on the target flow; eval harness operational; held-out split defined and quarantined; eval scores stable enough to detect the lift you're seeking. Any missing → route to `agent-observability` / `eval-pipeline` and stop.

### Step 2 — Choose the technique
Read `references/techniques.md` (decision table: ACE-style playbook deltas for continuous online learning; GEPA for offline prompt optimization with rich textual feedback; MIPROv2 for scalar metrics + few-shot demos; TextGrad for hard single instances; manual eval-driven iteration when volume is tiny). Record choice + why in `docs/learning-loop/LOOP.md`.

### Step 3 — Declare learnable surfaces
Allowlist exactly what the loop may change (e.g. drafter prompt, insurer playbooks, retrieval config). Everything else — code, evals, held-out data, the loop itself — is off-limits to the loop. Write the allowlist into LOOP.md.

### Step 4 — Build the cycle
```
collect traces (sampled) → score (eval-judge, multi-criteria feedback)
→ reflect/propose (technique from Step 2) → validate on held-out set
→ promotion proposal (diff + evidence + cost) → human approves → promote
→ record (changelog + memory-capture) → monitor for regression
```
Proposals must show: what changes (diff), held-out before/after scores, spend so far, and rollback command. Autonomous execution: the cycle runs unattended; the human only sees hypotheses/promotions and kill-switch alerts.

### Step 5 — Autonomy ladder (competency-gated)
| Stage | Who promotes | Advance when |
|-------|--------------|--------------|
| Apprentice (default) | Human approves every change | ≥10 approved promotions, 0 rollbacks in last 10 |
| Journeyman | Auto-promote behind hard safety gates (guardrail evals must pass) | ≥3 months clean + regression monitor proven (caught ≥1 real regression) |
| Master | Relaxed gates, batched review | Only if the owner explicitly opts in |
Any rollback drops the loop one stage.

### Step 6 — Kill-switches and budget
Declare: max $/cycle, max cycles/week, and the ROI stop (expected remaining lift vs spend, in plain numbers — same rule as `agent-run-retro`). Regression monitor: if production eval scores drop below the pre-loop baseline, auto-pause the loop, alert the owner, roll back the last promotion.

## Gotchas

- **Reward hacking / judge gaming:** optimized prompts learn to please the judge, not the user. Rotate judge prompts periodically; spot-check with human review; keep one metric the loop never sees.
- **Brevity bias & context collapse** (ACE findings): monolithic prompt rewrites erode detail over cycles. Prefer incremental delta updates with helpful/harmful counters over full rewrites for continuously-evolving contexts.
- **Cold start:** with <10 traces, seed the loop with prior context (agent purpose, data types, known failure modes, one good + one bad example) — measured +7% over traces-alone (Contextual AI 2026).
- **This loop improves the PRODUCT's agents.** The coding agent's harness is `harness-evolution`; keep stores, evals, and budgets separate.
- **Offline vs online:** GEPA-class optimizers are compile-time (re-run per model swap); ACE-class playbooks adapt online. Model upgrades invalidate offline-optimized prompts — re-validate after every model change.

## Example

<examples>
  <example>
    <input>Make my appeal-drafting product self-improving from its production traces. It has Phoenix tracing and a 30-case eval set with 10 held out.</input>
    <output>
Preconditions: traces ✓ eval harness ✓ held-out 10 quarantined ✓.
Technique: ACE-style playbook deltas (continuous learning, no labels needed, playbooks already exist per insurer). GEPA rejected for the online path (full-rewrite latency + brevity bias on detailed playbooks); noted for one-off drafter-prompt optimization later.
Learnable surfaces: drafter prompt, insurer slice playbooks. Off-limits: judges, eval sets, US-playbook (regulatory).
Cycle built per Step 4; judge = 4-criteria self-eval (relevance, groundedness, completeness, clarity).
Ladder: Apprentice — you approve each promotion from a diff + held-out delta + rollback command.
Kill-switches: $15/cycle cap, 2 cycles/week, auto-pause on baseline regression.
LOOP.md saved; logged to SKILL-OUTPUTS.
    </output>
  </example>
</examples>

Read `references/examples.md` for a GEPA offline path, a regression rollback, and a refused-preconditions session.

## Common Rationalizations

| Excuse | Reality |
|--------|---------|
| "GEPA worked before, just use it" | Technique fits data + feedback shape; ACE beats GEPA for online playbook evolution, GEPA wins offline prompt compiles. Choose per project. |
| "Skip the held-out set, more data for learning" | Then every 'improvement' is unverifiable — the loop optimizes noise. |
| "Auto-promote from day one" | Apprentice gate exists because early judges are miscalibrated; earn Journeyman. |
| "Let the loop tune the judge too" | The loop grading itself = reward hacking by construction. Judges are off-limits surfaces. |
| "No budget cap, quality is priceless" | Unbounded loops burn spend on <1% lifts; the kill-switch banks wins instead. |

## Verification

- [ ] Preconditions verified (traces + eval harness + quarantined held-out) before any cycle
- [ ] LOOP.md contains technique choice, surface allowlist, ladder stage, budget, kill-switches, rollback
- [ ] First promotion proposal shows diff + held-out before/after + rollback command
- [ ] Regression monitor tested once (simulate a drop → loop pauses)
- [ ] docs/skill-outputs/SKILL-OUTPUTS.md appended

## Red Flags

- Loop proposed without observability or evals in place
- Optimization run that touched held-out examples
- Promotion applied with no rollback path recorded
- Judge prompts inside the learnable-surface allowlist
- Autonomy stage advanced without meeting its gate

## Impact Report

```
Learning loop: [product/flow] | Technique: [ACE-delta | GEPA | MIPROv2 | manual] — why: [1 line]
Surfaces: [allowlist] | Ladder: [stage] | Budget: [$X/cycle, N/week]
Promotions: [N approved, N rolled back] | Held-out delta: [before → after]
Kill-switch: [armed | triggered — reason] | Files: docs/learning-loop/LOOP.md
```
