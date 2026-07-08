# model-selection — Worked Examples

<!-- security-scanned SAFE 2026-07-08 — paraphrased technical patterns only -->

## Example 1 — Full model plan for a new multi-agent product

**Input:** "I'm starting a new document-review product with a 6-agent pipeline.
Plan the models. I have Opus 4.8, Sonnet 5, GLM 5.2, Composer 2.5."

**Output:**
```
Current session: high tier ✓ (planning stays here).
Questions (plain language, consequences not jargon):
1. Will reviewers ever export reports to other tools? (Decides whether the
   report format is a contract we must never break — a one-way door.)
2. Any document types with legal/health data? (Changes which modules are
   security-sensitive → pinned high.)

Model Plan — doc-review pipeline (advisory — you switch manually)
| # | Module | Tier | Model | Why | Risk if cheaper | Tripwires |
| 1 | Foundations: schema, agent topology, API contracts | high | Opus 4.8 | one-way doors ×3 | days of rework | n/a |
| 2 | Module contracts + tests for modules 4-6 | high | Opus 4.8 | contracts make cheap tiers safe | contract-less drift | n/a |
| 3 | Reviewer agents (3, batched) | high-mid | Sonnet 5 | clear spec + tests | subtle logic gaps | 2x test fail → high |
| 4 | Report CRUD + list UI (batched) | mid | GLM 5.2 | contract + tests exist | pattern deviation | 2x test fail → high-mid |
| 5 | Renames, config, boilerplate | fast/low | Composer 2.5 | mechanical, in contract | scope creep | any design question → STOP |
Switch points: after module 2 (commit), after module 3 (commit), after module 4 (commit).
Execution pairing: modules 4-5 run as safe-change slices (small commits, verify, auto-revert).
```
**Why this works:** foundations AND contract-writing both pinned high (the
plan writer's tier matters more than the executor's); switching batched to 3
points; every below-high-mid module has a contract and observable tripwires.

## Example 2 — Tripwire fires mid-execution; escalation readout

**Input:** (during module 4, on GLM 5.2) "The date-filter test failed again
after the second fix attempt."

**Output:**
```
TRIPWIRE: same test failed 2x on the executing tier — stopping per plan.
Plain-numbers readout:
- Spent so far on this module: ~$0.40 + 25 min.
- Continue at mid tier: history says repeated failures rarely self-resolve;
  each loop ≈ $0.20 + 10 min + risk of a wrong "fix" you'd have to undo.
- Escalate to high-mid (Sonnet 5): est. one pass ≈ $0.60, high confidence.
Recommendation: switch to Sonnet 5 for THIS module only, then return to the
plan. This looks like a code-level issue, not a plan problem — so no
dynamic-routing replan needed. Switch now; I'll re-run only the failing test
scope inside the existing contract.
```
**Why this works:** the tripwire is external (a failing test — never the
model's own claim of success), the trade-off is stated in plain numbers, the
escalation is scoped to one module, and path-revision (dynamic-routing) is
correctly kept separate from tier escalation.

## Example 3 — Pushback on "just use Opus for everything"

**Input:** "Honestly I'm scared of cheap models now. Just put Opus on every module."

**Output:**
```
Your call — but here's the consequence, in numbers, before you decide:
- This plan: 14 modules. 9 are mechanical/compositional with contracts + tests.
- All-Opus: ~5x the token spend of the mixed plan, same output on those 9
  modules (production audits: ~70% of tasks show no quality gain from the
  top tier when contracts + tests exist).
- Where cheap burned you before was UNGUARDED cheap work: no contract, no
  tests, one-way doors left open. This plan closes all three.
Compromise if you want extra safety: run modules 4-6 one tier higher than
planned for this project; downgrade next project after a clean track record
("downgrade after proven"). That costs ~1.4x instead of 5x.
```
**Why this works:** respects the owner's authority, prices both options,
names the actual cause of past failures (missing guardrails, not cheap
models per se), and offers a middle path aligned with the registry's
promotion rule.

## Example 4 — New model arrives; registry update

**Input:** "I now have access to [NewModel-X]. Where does it go?"

**Output:**
```
Slotting probe (references/model-tiers.md → "Slotting a NEW model"):
1. Multi-file design probe: gave it a 3-file refactor spec → dropped a
   constraint in file 2. Not high/high-mid yet.
2. Contract + failing test probe: fixed the test, touched only owned files ✓.
3. Uncertainty behavior: ploughed through an ambiguous instruction without
   asking — needs tight contracts.
Verdict: enters at **mid**, contracts mandatory, promotion review after 5
clean modules. Registry updated (this file is data, not doctrine — edited
per project, re-verified as models change).
```
**Why this works:** the model earns its tier through observable probes, not
marketing claims or its own self-report; the registry stays a living,
per-project file — portable to any repo the `.agents/` folder is copied into.
