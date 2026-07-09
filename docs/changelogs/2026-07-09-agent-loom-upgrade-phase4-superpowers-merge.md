# Changelog — Agent-loom Upgrade Phase 4: obra/superpowers Craft Merge (2026-07-09)

## MINOR: Merge superior craft from obra/superpowers into 6 existing skills

Phase 4 of the agent-loom upgrade plan. Ran `learn-from-repo` against `obra/superpowers`: credibility gate (11/12 PASS), full `secure-*` scan of all 12 fetched `SKILL.md` files (SAFE — 0 findings), pairwise comparison against 8 agent-loom target skills, then applied the merge to the 6 skills with real gaps. `brainstorming` and `universal-skill-creator` were confirmed KEEP CURRENT (no gap — already sourced from the same upstream lineage or already superior).

### Changed

- `debug-and-fix` (v1.3 → v1.4, 200/200 lines) — added the **3-strike architecture gate**: after 3 failed fix attempts on the same bug, stop coding and discuss architecture with the user before attempt #4, instead of trying fix #4. Wired into the Stop-the-Line Rule and Common Rationalizations.
- `test-driven-development` (v1.2 → v1.3, 194/200 lines) — **delete-not-retrofit enforcement**: code written before its test must be deleted and rewritten from Red, never retrofitted with a test after the fact. Added anti-pattern citations (never assert against a mock's own behavior; never add test-only methods to production classes) with three new rows in `references/tdd-patterns.md` Anti-patterns table.
- `incremental-implementation` (v1.1 → v1.2, 150/200 lines) — **evidence-before-claims gate** in the end-to-end check: identify the exact verify command, run it fresh, and read its actual output before reporting done — never claim green from memory. Added plan-checkbox ticking guidance as slices complete.
- `code-review-crsp` (v1.2 → v1.3, 196/200 lines) — **two-pass review order**: Pass 1 spec compliance (does it do what was asked, nothing more/less), Pass 2 code quality (the five axes). Added a receiving-feedback rule — re-verify a finding against current code before applying its fix, no reflexive agreement.
- `implementation-plan` (v1.3 → v1.4, 199/200 lines) — **task right-sizing**: bite-sized enough for one test→implement→verify→commit cycle, exact file paths, written for an executor with zero prior context on the codebase. Added a **self-review** pass (coverage, no placeholders, consistent task IDs/tiers) before presenting the plan.
- `git-workflow-and-versioning` (v1.1 → v1.2, 164/200 lines) — added a **branch-finishing flow** (Step 6): verify tests green, then offer merge locally / push+PR / keep as-is / discard. Destructive cleanup (branch delete, worktree removal) requires the user to explicitly confirm the discard choice — never inferred.
- `docs/SKILL-INDEX.md` — `Last updated` bumped to 2026-07-09. No call-graph edit needed (no new triggers, outputs, or call relationships were introduced by this pass — all six changes are internal craft/enforcement additions to existing workflows).

### Verified

- `wc -l` on all 6 edited `SKILL.md` files ≤200 lines (194, 150, 196, 199, 164, 200).
- Post-application `secure-*` sweep across all 6 files + `tdd-patterns.md` reference: no injection, exfiltration, credential, escalation, supply-chain, obfuscation, hidden-content, or DoS patterns. VERDICT: SAFE.
- `check_p2_craft.py`, `check_ao_sections.py`, `check_phase3_depth.py`, `check_l3_tiers.py`, `check_red_flags_quality.py` — clean for all 6 files (no new failures introduced).

### Known gap (not fixed this pass)

- `docs/prd/PRD.md` and `docs/skill-graph.md` full resync — pre-existing drift flagged in Phase 3; unaffected by this pass since no skills were added/removed/renamed (only internal content edits within the 200-line ceiling).
