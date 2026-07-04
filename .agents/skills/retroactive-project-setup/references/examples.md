# Retroactive Project Setup — Full Worked Examples

Skill: `retroactive-project-setup` | Enriched from SKILL.md (improve-skills pass, SKIP_RESEARCH).

## Example 1 — Documented workflow

**Input:** I inherited a 2-year-old Next.js + Prisma app with no AGENTS.md and no agent infra. Set up agents for it without touching code.

**Output:**
```
Working tree clean ✓ | AGENTS.md absent ✓ | docs/memory absent ✓
Survey: package.json (Next 14, Prisma 5, Tailwind), README (1 page), 12 source samples across app/, lib/, prisma/. 50 commits scanned — themes: auth refactor, billing integration, perf work.
Inference matrix: 14 HIGH (stack, commands, structure, code style), 5 LOW (auth strategy, deployment target), 3 GAP (user identity, business model, autonomy prefs).
Interview: 3 questions asked (user, business model, autonomy). Skipped 3 (already inferred).
Files created: AGENTS.md (118), docs/architecture.md (94), docs/product-soul.md (76 — PMF marked Hypothesis), docs/adr/ADR-0001-initial-backfill.md (62), 4 memory files. [INFERRED — confirm] tags: 7. Source code modified: 0.
Next: review the 7 confirm tags, stage the commit.
```

## Example 2 — Step-by-step execution

**Input:** "Run `retroactive-project-setup` on [concrete task]"

**Agent actions:**
1. Preconditions and Idempotency
2. Read-Only Repo Survey (silent)
3. Build the Inference Matrix
4. Targeted Interview (gaps only)
5. Generate Files (compose existing skills, do not duplicate)
6. Memory Bootstrap
7. Confirm, Log, Stop

**Impact Report shape:**
```
Retroactive setup: [repo name]
Mode: [single | multi (monorepo: frontend+backend)]
Repo survey: [N manifests, M source samples, K commits scanned]
Inference matrix: [HIGH: a] [LOW: b] [GAP: c]
Interview questions asked: [N / 6]
Files created:
  - AGENTS.md ([lines])
  - docs/architecture.md ([lines])
  - docs/product-soul.md ([lines])
  - docs/adr/ADR-0001-initial-backfill.md ([lines])
  - docs/memory/project-index.md
  - docs/memory/current-state.md
  - docs/memory/agent-handoffs.md (synthetic seed)
  - docs/memory/learnings.md (stub)
[INFERRED — confirm] tags: [count] across [file list]
Source code modified: 0 files
Logged to: docs/skill-outputs/SKILL-OUTPUTS.md
```

## Example 3 — Gotcha application

**Input:** Task hits a non-obvious edge case

**Apply:**
- **The write-allowlist is the safety contract.** Any deviation undermines the entire promise of the skill. If a sub-skill (e.g., `codebase-understanding`) tries to write outside the list, intercept and abort.
- **Inference confidence is asymmetric.** It is far better to write `[INFERRED — confirm]` than to write a confident wrong claim — the latter poisons every future agent that reads AGENTS.md.
- **Don't re-implement existing skills.** This is an orchestrator. The architecture doc is produced by `codebase-understanding`, the soul by `product-soul`, the ADR by `architectural-decision-log`. Re-implementing them creates drift.
- **The synthetic handoff entry must be honest.** Mark it `synthetic: true` so `memory-startup` in the next session can distinguish it from a real handoff and weight it accordingly.

---

See `SKILL.md` for hard rules and verification checklist.
