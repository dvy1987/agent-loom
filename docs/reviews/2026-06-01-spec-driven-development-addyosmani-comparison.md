# Phase 3 Comparison: Spec-Driven Development

**Date:** 2026-06-01  
**Pair:** `spec-driven-development` (agent-loom) × `spec-driven-development` (addyosmani/agent-skills)  
**Snapshot:** addyosmani repo 2026-05-29 ingestion; fetched AO SKILL.md 2026-06-01  
**Scope:** Structural + content comparison. agent-loom evaluated as the **SDD suite** (orchestrator + `project-constitution`, `feature-spec`, `implementation-plan`, `spec-crosscheck`) because our orchestrator is intentionally thin.

---

## Executive Verdict

**MERGE BEST-OF-BOTH**

Keep agent-loom’s multi-skill architecture, constitution layer, `/clarify` mode, and hard `spec-crosscheck` gate. Adopt selected AO specify-phase content patterns (assumptions surfacing, success-criteria reframing, richer “when not to use” heuristics) into `feature-spec` references—not into the orchestrator body. Do **not** replace the suite with AO’s monolithic skill.

---

## Side-by-Side Shape

| Dimension | agent-loom | addyosmani |
|-----------|------------|------------|
| **Architecture** | Thin orchestrator (133 lines) → 4+ leaf skills | Single monolithic SKILL (~200 lines), all phases inline |
| **Phases** | `/constitution` → `/specify` → `/clarify` → `/plan` → `/tasks` → `/analyze` → `/implement` | SPECIFY → PLAN → TASKS → IMPLEMENT (4 phases) |
| **Constitution** | Dedicated `project-constitution` + spec cites `C-N` rules | No constitution layer; “Boundaries” live inside the spec template |
| **Spec format** | Executable FR/NFR/AC (Given/When/Then), `[NEEDS CLARIFICATION]` markers | Narrative spec template (Objective, Tech Stack, Commands, Structure, Code Style, Testing, Boundaries) |
| **Readiness gate** | `spec-crosscheck` — PASS/FAIL, six automated checks, read-only | Human review checkpoints between phases; verification checklist before implement |
| **Implement routing** | `test-driven-development` (default) | `incremental-implementation` + `test-driven-development` + `context-engineering` (skills we lack) |
| **Anti-skip defense** | `spec-crosscheck` + partial rationalization tables on leaves | Strong **Common Rationalizations** + **Red Flags** in the SDD skill itself |

---

## Six-Axis Scorecard

Scores 1–5 (5 = strongest on that axis for agent work).

| Axis | agent-loom | addyosmani | Notes |
|------|:----------:|:----------:|-------|
| **1. Workflow specificity** | 5 | 4 | Ours: explicit slash map, state detection, slug wiring, refuse out-of-order phases. AO: very detailed specify/plan/task templates but no orchestration state machine. |
| **2. Hard rules** | 5 | 3 | Ours: machine-enforced gates (no Approved with CLs, no implement without PASS). AO: “do not advance until validated” relies on human review discipline. |
| **3. Gotchas** | 4 | 4 | Ours: router-not-worker, slug discipline, `problem-to-plan` escape hatch. AO: living spec, assumption danger, scope creep red flags. |
| **4. Examples** | 3 | 5 | Ours: one orchestration example. AO: full spec template, task template, reframe example, commands/structure blocks. |
| **5. Verification** | 5 | 3 | Ours: `spec-crosscheck` six checks with `file:line` evidence. AO: pre-implement checklist (good but not traceability-aware). |
| **6. Anti-rationalization** | 3 | 5 | AO wins: dedicated rationalizations table + red flags. Ours: tables on `spec-crosscheck` / some leaves; **orchestrator has none**. |
| **Total** | **25** | **24** | Tie on substance; different strengths |

---

## What agent-loom Does Better

1. **Separation of concerns** — WHAT (`feature-spec`) vs HOW (`implementation-plan`) vs policy (`project-constitution`) vs audit (`spec-crosscheck`). AO mixes project bootstrap (commands, directory layout, code style) into the spec, which blurs product spec with repo onboarding.
2. **Machine-readable contracts** — FR/NFR/AC numbering, CL markers, constitution version pins — enables automated cross-check and agent planning without prose parsing.
3. **Explicit clarify loop** — `/clarify` mode; AO folds clarification into “ask until concrete” inside Specify with no structured marker discipline.
4. **Hard analyze gate** — `spec-crosscheck` PASS/FAIL is stronger than AO’s human-review arrows between phases.
5. **Ecosystem fit** — Routes tactical work to `problem-to-plan`; AO has no equivalent escape hatch beyond “single-line fixes.”

## What addyosmani Does Better

1. **Assumptions surfacing** — `ASSUMPTIONS I'M MAKING:` block before spec content; aligns with our `assumption-mapping` thinking but is operationalized in-workflow.
2. **Success-criteria reframing** — Turns vague requirements (“make it faster”) into measurable targets with explicit human confirmation loop.
3. **Rich templates in-body** — Spec and task markdown templates agents can copy without loading a reference file.
4. **Anti-rationalization at the entry skill** — Excuse → rebuttal table + red flags at the SDD front door (insight #1 pattern).
5. **“When NOT to use” time heuristic** — “>30 minutes → spec”; complements our `problem-to-plan` routing with a simpler rule-of-thumb.

## Gaps / Risks If We Adopted Theirs Whole-Cloth

- Lose constitution as a stable, versioned artifact above features.
- Lose `[NEEDS CLARIFICATION]` / Approved status machine → weaker automation.
- Lose `/analyze` traceability (FR → task mapping).
- AO **depends on skills we don’t have** (`incremental-implementation`, `context-engineering`) — adopting their Implement phase verbatim would reference dead links until Phase 2.

---

## Recommended Merges (actionable, ordered)

| Priority | Action | Target | Effort |
|----------|--------|--------|--------|
| P1 | Add **Common Rationalizations** table (5–6 rows) for skipping SDD / skipping `/analyze` | `spec-driven-development/SKILL.md` | Small (~15 lines) |
| P1 | Add **Step 2b** to `feature-spec` specify mode: optional `ASSUMPTIONS I'M MAKING` block before drafting (max 5 bullets, user must confirm or correct) | `feature-spec/SKILL.md` or `references/feature-spec-schema.md` | Small |
| P2 | Add **reframe vague requirements** micro-step to `feature-spec` discovery: translate adjectives into measurable success criteria, confirm with user | `feature-spec/SKILL.md` | Small |
| P2 | Add AO **“When NOT to use”** line to orchestrator gotchas (>30 min / multi-module / ambiguous → SDD; else `problem-to-plan`) | `spec-driven-development/SKILL.md` | Tiny |
| P3 | Optional reference file `references/project-bootstrap-in-spec.md` for Commands/Structure/Code Style sections — **only** when user wants repo onboarding inside SDD (not default feature-spec) | `feature-spec/references/` | Medium |
| Defer | Do not collapse orchestrator + leaves into one skill | — | — |

**Do not adopt:** AO’s six-area spec as the default `feature-spec` template (conflicts with WHAT-only rule and executable AC schema).

---

## Phase 2 Dependencies Surfaced

AO Implement phase explicitly calls:

- `incremental-implementation` — **GAP** (rank #1 in Phase 2 list)
- `context-engineering` — **GAP** (#8)
- `test-driven-development` — **ALIGNED** (already exists)

Until those gaps exist, keep our `/implement` → `test-driven-development` default.

---

## Next Pair

Per 2026-05-29 plan, continue Phase 3 with **pair 2: `test-driven-development`**.

---

## Sources

- agent-loom: `.agents/skills/spec-driven-development/SKILL.md` (+ leaf skills cited above)
- addyosmani: `https://github.com/addyosmani/agent-skills` → `skills/spec-driven-development/SKILL.md` (raw fetch 2026-06-01)
