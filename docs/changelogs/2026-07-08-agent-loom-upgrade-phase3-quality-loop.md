# Changelog — Agent-loom Upgrade Phase 3: Agentic Quality Loop for Shipped Products (2026-07-08)

## MINOR: Three new skills instrument and improve your *shipped product's* agents

Phase 3 of the agent-loom upgrade plan (plan `834ff43c-a703-4565-9b8f-2dba210002b0`). Distinct from `harness-*` (which improve the *coding agent*) and `experimentation` (product A/B tests) — this suite is scoped to the runtime agents inside products you ship.

### Added
- `agent-observability` — plain-language tracing primer + free-tier-first backend decision table (Langfuse Cloud, Phoenix/Arize, LangSmith, Braintrust) + OTel GenAI/OpenInference instrumentation, so the backend stays swappable by config. Never proposes self-hosting on the user's laptop. `references/backends.md` + `references/examples.md`.
- `agent-run-retro` — development-phase retrospective: interviews the owner in plain language (≤5 questions), drafts ranked improvement hypotheses (impact × confidence ÷ cost), designs and runs small n=1/n=2 experiments with pre-declared success criteria, guardrails, stop conditions, and a cost/ROI kill-switch. Priority order quality > performance > cost with an explicit diminishing-returns stop. `references/examples.md`.
- `runtime-learning-loop` — technique-agnostic self-improvement loop for shipped agents (ACE-style playbook deltas, GEPA/MIPROv2 offline optimization, or manual eval-driven iteration — chosen per project, GEPA is never the default). Hard preconditions: observability + a quarantined eval held-out set. Competency-gated autonomy ladder (Apprentice → Journeyman → Master). `references/techniques.md` + `references/examples.md`.

All three: ≤200 lines, loader-safe, pass P2-craft / Red Flags / AO-section validation gates.

### Changed
- `agent-system-architecture` (v1.1 → v1.2) — Step 4 now points to `agent-observability` for tracing implementation (was a bare "design for observability" note with no follow-through).
- `setup-evaluation` (v1.4 → v1.5) — new "Product observability" check row routing agent-chain products without a tracing plan to `agent-observability` before any `runtime-learning-loop` work.
- `eval-judge` (v1.2 → v1.3), `eval-rubric-design` (v1.2 → v1.3), `eval-output` (v1.2 → v1.3), `eval-pipeline` (v1.4 → v1.5) — cross-linked to `agent-observability` / `runtime-learning-loop`: judge justifications should be stage-attributed so they're consumable as optimizer feedback; production evals run on traces; `runtime-learning-loop`'s held-out split must stay quarantined from optimization.
- `docs/SKILL-INDEX.md`, `README.md`, `AGENTS.md` — synced for the 3 new skills (122 skills total).

### Known gap (not fixed this pass)
- `docs/prd/PRD.md` and `docs/skill-graph.md` carry pre-existing drift from before this phase (missing roughly 15-20 skills added since 2026-05-20 / 2026-07-04 respectively — harness suite, safe-change family, svg/gsap/motion animation, etc.). Flagged rather than partially patched to avoid a heading/row-count lie in PRD.md's Section 4. Recommend a dedicated full `library-skill` resync session.

### Verified
- `wc -l` on all touched SKILL.md files ≤200 lines.
- Loader safety (`---` at byte 0) on all 3 new skills.
- `check_p2_craft.py`, `check_red_flags_quality.py`, `check_ao_sections.py` — zero findings for the 3 new skills.

---

## Addendum (same day) — Phase 3 completion audit: eval-suite research pass + hygiene

A completion audit against the original Phase 3 problem statement found the "is my eval suite actually good?" research pass had NOT been done (only cross-link edits), plus three post-Phase-3 hygiene gaps. All closed:

### Eval-suite targeted improve pass (with live research — the missing Phase 3 item)
- **New L3 `eval-judge/references/judge-calibration.md`** — the judge is a measurement instrument: golden dataset (30 viable / 200+ for gates; inter-rater ≥80% or fix the rubric), metric ensemble (Cohen's κ + failure-class precision/recall per dimension — raw agreement overstates judge ability by 33–41pp), JRH perturbation stress tests (label-flip / paraphrase / format / verbosity / position-swap / stochastic stability), claim-level RAG faithfulness (a generic judge missed 9/9 hallucinations), calibration loop + confidence triage, non-portability rule, evaluation-illusion warning. Sources: arXiv:2606.19544, arXiv:2603.05399 (JRH), arXiv:2601.08654 (RULERS), arXiv:2603.11027 (MERG), SAJA ACL 2026, Galtea + OpenTrain 2026.
- **`eval-judge` v1.4** — judge-calibration gate added to Step 1; PRUNED stale 2023-era "longer responses are systematically rated higher" claim (verbosity bias now <0.011 across 21 modern judges; position bias is the persistent threat and hides behind high test–retest consistency); new raw-agreement/κ gotcha.
- **`eval-rubric-design` v1.4** — evaluation-illusion gotcha (ground dimensions in domain knowledge, not generic quality words); rubric locking/versioning + extractive-evidence gotcha; inter-rater ≥80% gate.
- **`eval-pipeline` v1.6** — known-bad split extended with JRH perturbation pairs; judge-calibration gotcha upgraded to κ + failure-class recall; back to exactly 200 lines.
- **`eval-output` v1.4** — new hard rule: validate the judge itself before gating on its scores; evaluation-illusion gotcha.

### Hygiene (post-Phase-3 gaps closed)
- `.cursor/rules/*` regenerated — was stale at 119 skills, so the 3 new Phase 3 skills were invisible to Cursor routing (directly undermined problems #1 and #3). Now 122.
- `docs/SKILL-EXAMPLES-INDEX.md` regenerated (122 with L3, 0 broken); knowledge graph rebuilt (122 skill nodes).
- **Windows portability fix:** `check_p2_craft.py` and `validate_application_mode.py` crashed under cp1252 default encoding — explicit UTF-8 added. Validation gates now run on Windows consumer machines.

### Still open (pre-existing, out of Phase 3 scope)
- 12 skills from the 2026-07-05 high-leverage batch have L3 examples <55 lines; `gsap-animation`/`motion-animation` missing Red Flags. Candidates for a targeted hygiene pass.
