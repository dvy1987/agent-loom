# Model Tier Registry (editable — models change fast)

Snapshot 2026-07. **This file is data, not doctrine.** Re-verify tiers when a
provider ships a new model, and edit this file per project — the tiers are
stable, the model names rotate. Works in any repo the `.agents/` folder is
copied into; no agent-loom-only dependencies.

## Tier definitions

| Tier | What it's for | What it must NEVER do |
|------|---------------|----------------------|
| **high** (high-cognition) | Architecture, foundations, ambiguous/novel problems, one-way-door decisions, gnarly debugging, security-sensitive work, writing module contracts for lower tiers | — (top tier) |
| **high-mid** | Most feature implementation against a clear spec, compositional logic, refactors with test coverage, RAG/agent glue code | Unscoped architecture decisions |
| **mid** | Well-scoped implementation with tests as guardrails, straightforward CRUD, test writing from a contract | Multi-file design decisions, anything without tests |
| **fast/low** | Renames, boilerplate, formatting, small single-file scoped edits, mechanical transformations | Any design decision, any multi-file change, anything without a contract |

## Current registry (owner's models — edit as your access changes)

| Model | Tier | Notes |
|-------|------|-------|
| Opus 4.8 | high | Default for foundations, planning, one-way doors |
| GPT-5.5 | high | Interchangeable with Opus for high-tier work |
| Sonnet 5 | high-mid | Stronger than most users assume — most feature work lands here, not lower |
| GPT-5.4 | high-mid | Same band as Sonnet 5 |
| GLM 5.2 | mid | Well-scoped implementation with tests as guardrails |
| Cursor Composer 2.5 | fast/low | Small scoped edits, renames, boilerplate — never multi-file design |

## Task-class → tier mapping (detail)

- **Always high:** new-project foundations; DB schema; API contracts; auth
  flows; data models; dependency/framework selection; debugging that has
  resisted one fix attempt; security-sensitive code; writing specs/contracts
  and model plans themselves.
- **High-mid default:** feature implementation from an approved spec; UI with
  states; API endpoints with tests; refactors under test coverage;
  integration glue.
- **Mid:** tasks with a written contract AND existing tests; CRUD against an
  established pattern in the codebase; test-writing from acceptance criteria.
- **Fast/low:** single-file mechanical edits inside a contract; renames;
  comment/format cleanups; boilerplate replication of an existing pattern.

Production routing audits (2026) consistently find ~70% of real tasks are
mechanical/compositional — the savings are real, but only when the hard 10-30%
is correctly kept on higher tiers.

## Slotting a NEW model into a tier

Ask three questions (run one small probe task if unsure):
1. Can it hold a multi-file design in its head without dropping constraints?
   Yes → candidate for high/high-mid. No → mid or below.
2. Given a contract + failing test, does it fix the test without touching
   out-of-scope files? Yes → mid is safe. No → fast/low only.
3. Does it announce uncertainty or plough through? Models that plough through
   need tighter contracts and lower-stakes work regardless of raw capability.

Start every new model ONE tier below where you think it belongs; promote after
it has a clean track record on that class ("downgrade after proven" in
reverse). Never trust the model's own claims about its ability.

## Cost math cheat-sheet (plain language)

- Tier premium is per-call; failure cost is per-incident. One reverted module
  = undo time + redo at higher tier + your review time — usually more than the
  entire tier premium for the whole project.
- Judge by **cost per useful output**: (what you spent) ÷ (modules that
  shipped without rework).
- The savings compound with the cheap-tier share — but only the share the
  contracts and tests make safe. Pushing the share up without contracts is how
  reversals happen.
