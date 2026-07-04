# Changelog — Adversarial Review Remediation (2026-07-04)

## MINOR: Library craft parity + CI self-enforcement

Closed gaps from adversarial review of addyosmani ingestion “mostly finished” claim.

### Added
- P2 craft (Common Rationalizations, Verification, Red Flags) on all 71 project-specific skills
- `.github/workflows/validate-skills.yml` — validate, line limits, P2 check, examples index, graph health
- `check_p2_craft.py`, `add_p2_craft_project.py`, `replenish_l3.py`, `validate_application_mode.py`
- `docs/comparisons/INGEST-QUEUE.md` for learn-from-repo overlap queue (Meta B4)
- L3 quality tiers in `docs/SKILL-EXAMPLES-INDEX.md` (curated / enriched / padded / standard)

### Changed
- `learn-from-repo` Step 4b — auto-queue pairwise compare on skill overlap
- `improve-skills` Step 2b — addyosmani pattern pass for project-specific (Meta B5)
- `docs/handoffs/2026-06-01-external-agent-addyosmani-handoff.md` §7 — Phase 2/3 marked COMPLETE

### Verified
- `agentskills validate` 102/102 PASS
- All SKILL.md ≤200 lines
- Application-mode knowledge-graph smoke test PASS
