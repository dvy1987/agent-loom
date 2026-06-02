# Comparison: brainstorming + venture-exploration vs addyosmani/idea-refine

**Date:** 2026-06-01  
**Asymmetric pair:** agent-loom uses **two orchestration paths** — product/feature design (`brainstorming`) and pre-decision business (`venture-exploration` → idea-generation, business-modeling, idea-evaluation, customer-discovery).

| Axis | agent-loom | addyosmani | Winner |
|---|---|---|---|
| Workflow specificity | 2/2 | 2/2 | tie |
| Hard rules | 2/2 | 1/2 | ours |
| Gotchas | 1/2 | 2/2 | theirs |
| Examples | 1/2 | 1/2 | tie |
| Verification | 1/2 | 2/2 | theirs |
| Anti-rationalization | 1/2 | 1/2 | tie |
| **Total** | **8/12** | **9/12** | **MERGE BEST-OF-BOTH (no new skill)** |

## Per-axis notes

**Workflow specificity:** `idea-refine` is a single three-phase dialogue (diverge → converge → one-pager). Ours splits **design approval** (brainstorming with hard no-code gate, HYPOTHESIS+CONFIDENCE%) from **venture validation** (Mom Test, Lean Canvas, go/kill scoring).

**Hard rules:** Ours wins on enforceability — brainstorming's Hard Gate blocks implementation until approved design doc. AO relies on conversational discipline ("don't skip who is this for").

**Gotchas:** AO lists ideation anti-patterns (yes-machine, 20+ shallow ideas). Ours has brainstorming gotchas but not a "Not Doing" list in the design doc template.

**Examples:** AO references `examples.md` / `frameworks.md`. Ours has one brainstorming example; venture suite has structured idea cards elsewhere.

**Verification:** AO session checklist (HMW statement, assumptions, Not Doing list). Ours Impact Report is lighter.

**Anti-rationalization:** AO tone rules ("be honest, not supportive"). Ours has HYPOTHESIS+CONFIDENCE% stop condition and optional adversarial checkpoint — different mechanism, similar intent.

## Verdict: MERGE BEST-OF-BOTH — do **not** add `idea-refine` skill

`idea-refine` overlaps two existing suites. Creating it would trigger `skill-deconflict` collisions and dilute venture-exploration's business rigor.

**Routing rule:**
- Feature/product design before code → `brainstorming`
- Startup/business idea lifecycle → `venture-exploration`
- Never route business ideation to `idea-refine` clone

## Recommended actions

| P | Action | Target |
|---|--------|--------|
| P1 | Add **Not Doing (and Why)** section to design doc template | `brainstorming/SKILL.md` Output Format |
| P1 | Phase 1: restate as **How Might We** before options | `brainstorming/SKILL.md` Step 4–5 |
| P2 | Key Assumptions to Validate checklist in design doc | `brainstorming/SKILL.md` |
| P2 | Ideation anti-patterns (5–8 bullets) from AO | `brainstorming/SKILL.md` Gotchas |
| P2 | Session verification checklist (mirror AO) | `brainstorming/SKILL.md` |
| P3 | Cross-link `venture-exploration` when input smells like business idea | `brainstorming/SKILL.md` Step 1 |
| — | Do **not** create `idea-refine` skill | — |
