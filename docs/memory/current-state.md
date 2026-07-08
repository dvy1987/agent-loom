# Current State

Last updated: 2026-07-08 (agent-loom upgrade plan, Phase 1 of 6 complete)

Twenty-one landed items across 2026-05-13 → 2026-07-08.

1.–18. *(Through Phase 3 daily-driver depth, adversarial remediation, KG v2, L3 backfill — see prior entries.)*

19. **Harness engineering suite** (2026-07-05, **uncommitted**). Three skills: `harness-generation`, `harness-evolution`, `harness-engineering`. Wired into project lifecycle (setup, orchestrator, eval, memory). ADR-0002. Proactive readiness gate for non-dev routing.

20. **Harness deep learn-from** (2026-07-05, **uncommitted**). 5 papers + 5 repos; 5 pairwise compares; INGEST-QUEUE cleared; L3 deepened (`harness-regression.md`, `harness-trajectory-mining.md`, evolution-loop, diagnosis-etclovg, scaffold-patterns). Library **109 skills**.

21. **Agent-loom upgrade plan Phase 1 — Cursor routing adapter** (2026-07-08, **uncommitted**). Plan `834ff43c-a703-4565-9b8f-2dba210002b0`, 6 phases total. `gen_host_adapters.py` generates `.cursor/rules/agent-loom-routing.mdc` + `agent-loom-skills-index.mdc` from skill frontmatter (portable, no agent-loom-only dependencies). Wired into `project-setup`/`retroactive-project-setup`/`agent-loom-sync`. Deferred #10 → PARTIAL. Full external handoff: `docs/handoffs/2026-07-08-external-agent-loom-upgrade-handoff.md`.

## Active Risks

- Large uncommitted harness batch — next session should commit when user asks.
- Harness suite not runtime-tested on a consumer project yet.
- Inferred graph edges (~84%) — `query_graph.py` authoritative-first.
- Agent-loom upgrade plan is mid-flight (1 of 6 phases) — stop-after-each-phase by user request; do not assume later phases are done.

## Immediate Next Step

1. Continue agent-loom upgrade plan Phase 2 (model-selection skill) — see external handoff doc for full spec and corrected model-tier table.
2. If user wants ship first: commit harness work + Phase 1 work (`git status` → logical commit message(s)).
3. Else: validate locally (`agentskills validate` on harness-* + patched skills) or bootstrap harness on a test project.
