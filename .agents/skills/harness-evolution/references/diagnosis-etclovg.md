# Diagnosis — ETCLOVG + HTIR

## HTIR node (HarnessFix pattern)

Each trace step becomes a node:

| Field | Content |
|-------|---------|
| `step_id` | Monotonic index |
| `action` | tool call / skill invoke / message |
| `layer` | ETCLOVG primary attribution |
| `inputs` | Provenance — what context was visible |
| `outcome` | success / fail / timeout |
| `downstream` | control-flow links |
| `harness_artifact_refs` | Prompt templates, adapters, hooks tied to step |

HTIR maps runtime steps to **implementation artifacts** — not trace summary alone.

## Attribution rules

1. **One primary layer per flaw record** — secondary layers noted but not edited in same round.
2. **Evidence required** — cite step_ids, not final pass/fail alone (FAILURE_MODE F1).
3. **Recurring flaws** — consolidate ≥2 traces with same mechanism before proposing.

## Weakness mining (Self-Harness)

Before proposing:
1. Cluster failed traces on **signature φ(r)=(cause, agent_status, mechanism)** — exact triple, not latent similarity.
2. Order clusters by **support × estimated actionability**.
3. **Addressability filter** — exclude task-specific difficulty, unstable outcomes, model-capability limits.
4. Generate one candidate edit per top-K clusters (diverse-minimal).

## Repair specification (HarnessFix)

Per flaw, write 4-field contract before editing:

| Field | Content |
|-------|---------|
| Target/scope | Layer + operator binding |
| Edit constraints | Named **forbidden artifacts** for this repair |
| Required behavior | What must change for this flaw instance |
| Validation bounds | Risk limits, max regression tolerance |

## Forbidden edit targets (HarnessFix)

Never propose edits to:
- Benchmark data or task definitions
- Evaluator oracles or held-out validation sets
- Validation labels or public benchmark APIs

Prevents "fixing" by contaminating eval.

## Scoped repair operators

| Layer | Allowed edit types |
|-------|-------------------|
| Tooling | tool schema, descriptions, middleware validation |
| Context | AGENTS.md routing, skill triggers, memory routing |
| Lifecycle | hooks, handoff protocol, session blocks |
| Observability | trace capture, distillation hooks |
| Verification | eval tasks, gates, lint hooks |
| Governance | forbidden paths, allowed_write expansion (human approve) |
| Execution | sandbox docs — not infra code without user ask |

**Multi-layer flaws:** select one **primary** operator; adjacent-layer operators become **auxiliary constraints** in same spec — not parallel unrelated edits.

Reject: runtime supervision that catches errors without fixing layer (F2).

## FAILURE_MODE table

| ID | Mode | Signal |
|----|------|--------|
| F1 | Outcome-only diagnosis | Edit without step refs |
| F2 | Supervision patch | Catches error, doesn't fix layer |
| F3 | Benchmark contamination | Oracle/task edit proposed |
| F4 | Non-addressable cluster | Model-capability limit forced into harness |
| F5 | Generic prompt bloat | No cluster mapping |
| F6 | Scoped-repair bypass | Free-form edits — **zero gain over H₀** (HarnessFix ablation) |

## Pivot rule (AHE)

If same failure class persists **2+ iterations** at one component level:
1. Rollback last edit on that component.
2. Pivot diagnosis to adjacent layer or component file.
3. Log pivot in `docs/harness/runs/` metadata.

## Confound isolation (Meta-Harness)

When structural + prompt edits regress together:
1. Hypothesis-test by **isolating edit classes** — try additive-only pivot.
2. Prompt+structure coupling is a common false-negative.
