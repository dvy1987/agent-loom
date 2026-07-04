# Retroactive Project Setup — Full Worked Examples

Skill: `retroactive-project-setup` | Load when producing output for this workflow.

## Example 1 — From skill workflow

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

## Example 2 — Typical invocation

**Input:** "Run `retroactive-project-setup` for [concrete task]"

**Output:**
```
Invoked `retroactive-project-setup`.
Step 1: Preconditions and Idempotency
Step 2: Read-Only Repo Survey (silent)
Step 3: Build the Inference Matrix
Retroactive setup complete: [repo]
```

---

See `SKILL.md` for hard rules, gotchas, and verification checklist.
