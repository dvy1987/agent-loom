# Changelog — Agent-loom Upgrade Phase 2: Advisory Model-Tier Routing (2026-07-08)

## MINOR: Plan which model tier handles which work — you switch manually

Phase 2 of the agent-loom upgrade plan (plan `834ff43c-a703-4565-9b8f-2dba210002b0`). Distinct from `dynamic-routing` (path revision after failure) — this skill assigns cognition tiers to work *before* execution begins.

### Added
- `model-selection` — advisory model-tier planner for solo builders with multiple models. High-cognition tier understands deeply + lays foundations, then assigns each module the cheapest safe tier. One-way doors pinned high; module contracts for cheap tiers; observable escalation tripwires (same test fails 2x, 3 fix attempts, out-of-contract edits, unscoped design questions). Announces "next module → tier X" at commit boundaries — the human switches models; harnesses cannot switch mid-run. `references/model-tiers.md` (editable registry with corrected Sonnet 5 / GPT-5.4 high-mid placement) + `references/examples.md`.

### Changed
- `implementation-plan` (v1.2 → v1.3) — Step 3 now requires a `model:` tier per task via `model-selection`; below-high-mid tasks need a module contract.
- `problem-to-plan` (v1.1 → v1.2) — TODO tasks gain `model:` tier tags from `model-selection`.
- `dynamic-routing` (v1.0 → v1.1) — new **Escalate model tier** route wired to `model-selection` tripwires (advisory — announce and wait).
- `docs/SKILL-INDEX.md`, `README.md`, `AGENTS.md`, `.cursor/rules/` — synced for `model-selection` (123 skills total).

### Verified
- `wc -l` on `model-selection/SKILL.md` ≤200 lines (164).
- Loader safety (`---` at byte 0).
- L3 `references/examples.md` ≥55 lines (97).
- P2 craft / AO five-section / Red Flags pass for `model-selection`.

### Known gap (not fixed this pass)
- `docs/prd/PRD.md` and full `docs/skill-graph.md` resync — pre-existing drift (~15-20 missing skills) flagged in Phase 3; not partially patched here.
