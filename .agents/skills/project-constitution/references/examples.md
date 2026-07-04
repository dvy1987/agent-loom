# Project Constitution — Full Worked Examples

Skill: `project-constitution` | Load when producing output for this workflow.

## Example 1 — From skill workflow

**Input:** Set up a constitution for our SaaS app — Next.js + Postgres + Vercel.

**Output:**
```
[Interview: 4 questions — testing posture (90% on services, no UI snapshot), perf budget (LCP < 2s), GDPR (yes, EU users), DB migration policy (always reversible)]

Wrote 8 categories, 19 rules, 94 lines. Top rules:
- C-1.1 Service layer code MUST have ≥ 90% coverage (Vitest)
- C-2.2 PII fields MUST be marked in Prisma schema with `@encrypted`
- C-3.1 LCP MUST be < 2s on p75 (Vercel Analytics)
- C-7.1 Every Prisma migration MUST be backwards-compatible across one deploy

Saved to `docs/constitution.md` v1. Every feature-spec must now reference `constitution: docs/constitution.md@1`.
```

## Example 2 — Typical invocation

**Input:** "Run `project-constitution` for [concrete task]"

**Output:**
```
Invoked `project-constitution`.
Step 1: Check existing context
Step 2: Interview (max 5 questions, one at a time)
Step 3: Write the constitution
Constitution complete: v<N>
```

---

See `SKILL.md` for hard rules, gotchas, and verification checklist.
