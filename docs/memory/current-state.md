# Current State

Last updated: 2026-07-09 (agent-loom upgrade plan, Phases 1-4 of 6 complete, uncommitted)

Twenty-four landed items across 2026-05-13 → 2026-07-09.

1.–18. *(Through Phase 3 daily-driver depth, adversarial remediation, KG v2, L3 backfill — see prior entries.)*

19. **Harness engineering suite** (2026-07-05, **uncommitted**). Three skills: `harness-generation`, `harness-evolution`, `harness-engineering`. Wired into project lifecycle (setup, orchestrator, eval, memory). ADR-0002. Proactive readiness gate for non-dev routing.

20. **Harness deep learn-from** (2026-07-05, **uncommitted**). 5 papers + 5 repos; 5 pairwise compares; INGEST-QUEUE cleared; L3 deepened (`harness-regression.md`, `harness-trajectory-mining.md`, evolution-loop, diagnosis-etclovg, scaffold-patterns). Library **109 skills**.

21. **Agent-loom upgrade plan Phase 1 — Cursor routing adapter** (2026-07-08, **uncommitted**). Plan `834ff43c-a703-4565-9b8f-2dba210002b0`, 6 phases total. `gen_host_adapters.py` generates `.cursor/rules/agent-loom-routing.mdc` + `agent-loom-skills-index.mdc` from skill frontmatter (portable, no agent-loom-only dependencies). Wired into `project-setup`/`retroactive-project-setup`/`agent-loom-sync`. Deferred #10 → PARTIAL. Full external handoff: `docs/handoffs/2026-07-08-external-agent-loom-upgrade-handoff.md`.

22. **Agent-loom upgrade plan Phase 3 — Agentic quality loop for shipped products** (2026-07-08, committed through `4f6fc46`/`c4b67f8`, this session finished the library sync). Three new skills: `agent-observability`, `agent-run-retro`, `runtime-learning-loop` (122 skills total). Cross-linked into `agent-system-architecture` (v1.2), `setup-evaluation` (v1.5), and the eval suite. `docs/SKILL-INDEX.md`, `README.md`, `AGENTS.md` synced; changelog `docs/changelogs/2026-07-08-agent-loom-upgrade-phase3-quality-loop.md`. User explicitly asked to skip Phase 2 and do Phase 3 first — Phase 2 (model-selection) is now the next open phase. **Known gap:** `docs/prd/PRD.md` and `docs/skill-graph.md` have pre-existing drift (missing ~15-20 skills added since 2026-05-20/2026-07-04) that predates this phase — flagged, not fixed, to avoid a heading/row-count lie; needs a dedicated full `library-skill` resync session.

23. **Phase 3 completion audit — eval-suite research pass + hygiene** (2026-07-08, committed). Closed the last open Phase 3 item: `improve-skills` TARGETED pass with live research on the eval suite ("is my eval suite actually good?"). New L3 `eval-judge/references/judge-calibration.md` (judge = measurement instrument: golden set, κ + failure-class recall, JRH perturbation tests, calibration loop, non-portability, evaluation illusion — 7 sources 2026). `eval-judge` v1.4 (pruned stale 2023 verbosity-bias claim), `eval-rubric-design` v1.4, `eval-pipeline` v1.6, `eval-output` v1.4. Hygiene: Cursor rules regenerated 119→122 (the 3 new skills were invisible to Cursor routing), SKILL-EXAMPLES-INDEX + knowledge graph rebuilt, Windows cp1252 crash fixed in `check_p2_craft.py`/`validate_application_mode.py` (portability). Pre-existing open items: 12 thin L3 files + 2 missing Red Flags from the 2026-07-05 high-leverage batch.

24. **Agent-loom upgrade plan Phase 2 — model-selection** (2026-07-08, committed). New `model-selection` skill (advisory tier planning, editable `model-tiers.md` registry, module contracts, tripwires). Wired into `implementation-plan` v1.3, `problem-to-plan` v1.2, `dynamic-routing` v1.1 (Escalate-model-tier route). Library **123 skills**.

25. **Agent-loom upgrade plan Phase 4 — obra/superpowers craft merge** (2026-07-09, **uncommitted**). `learn-from-repo` on `obra/superpowers`: credibility 11/12 PASS, secure-* scan of 12 fetched SKILL.md files SAFE, pairwise comparison vs 8 agent-loom targets. Applied to all 6 skills with real gaps (`brainstorming`/`universal-skill-creator` confirmed KEEP CURRENT, no gap): `debug-and-fix` v1.4 (3-strike architecture gate, 200/200 lines — at ceiling), `test-driven-development` v1.3 (delete-not-retrofit enforcement + 3 anti-pattern rows in `tdd-patterns.md`), `incremental-implementation` v1.2 (evidence-before-claims verify gate + checkbox ticking), `code-review-crsp` v1.3 (two-pass review order + pre-fix re-verification), `implementation-plan` v1.4 (task right-sizing + plan self-review, 199/200 lines — at ceiling), `git-workflow-and-versioning` v1.2 (branch-finishing flow with confirm-before-destroy gate). Post-application secure-* sweep: SAFE, 0 findings. All craft-check scripts pass (P2/AO/Phase3/L3/red-flags). `docs/SKILL-INDEX.md` last-updated bumped; no call-graph edit needed (no new triggers/outputs/calls). Changelog: `docs/changelogs/2026-07-09-agent-loom-upgrade-phase4-superpowers-merge.md`.

## Active Risks

- Large uncommitted harness batch — next session should commit when user asks.
- Harness suite not runtime-tested on a consumer project yet.
- Inferred graph edges (~84%) — `query_graph.py` authoritative-first.
- Agent-loom upgrade plan is mid-flight (4 of 6 phases done; Phases 5-6 open) — stop-after-each-phase by user request; do not assume later phases are done.
- `docs/prd/PRD.md` and `docs/skill-graph.md` are stale relative to the live skill registry (pre-existing, not caused by Phase 3/4) — needs a dedicated full-sync session before either is treated as authoritative.
- Phase 4 changes are uncommitted — `debug-and-fix` and `implementation-plan` are now at the 200-line ceiling with zero headroom; any future edit to either requires `split-skill` immediately, not a squeeze.

## Immediate Next Step

1. Continue agent-loom upgrade plan **Phase 5/6** — see plan `834ff43c-a703-4565-9b8f-2dba210002b0` and external handoff doc.
2. Commit the Phase 4 changes (6 skill edits + tdd-patterns.md + SKILL-INDEX + changelog) when user asks.
3. Optional/deferred: dedicated `library-skill` full resync for `docs/prd/PRD.md` / `docs/skill-graph.md` drift.
4. Optional: commit the 2026-07-05 harness batch if still uncommitted elsewhere.
