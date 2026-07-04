# Project Constitution — Full Worked Examples

Skill: `project-constitution` | Enriched from SKILL.md (improve-skills pass, SKIP_RESEARCH).

## Example 1 — Documented workflow

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

## Example 2 — Step-by-step execution

**Input:** "Run `project-constitution` on [concrete task]"

**Agent actions:**
1. Check existing context
2. Interview (max 5 questions, one at a time)
3. Write the constitution
4. Self-review
5. Save and notify

## Example 3 — Gotcha application

**Input:** Task hits a non-obvious edge case

**Apply:**
- Constitution rules are NOT preferences — they bend for nobody. If a team consistently waives a rule, remove it instead of letting it rot.
- Each rule must point at a single observable behavior. "Code should be clean" is not a rule. "Functions MUST be < 50 lines OR have a `# noqa: complexity` comment" is.
- Version bumps: any rule change is a major bump. Add to Amendments. Specs cite the version they were written against (e.g. `constitution: docs/constitution.md@2`).
- AGENTS.md vs constitution: AGENTS.md tells the agent HOW to work. Constitution tells the project WHAT must always be true. Don't confuse them.

---

See `SKILL.md` for hard rules and verification checklist.

## Verification checklist (L3)

- [ ] Examples demonstrate SKILL.md hard rules, not generic chat
- [ ] Anti-skip or rationalization defense included where applicable
- [ ] Output artifacts or Impact Report shape is explicit
- [ ] Reader can trace input → concrete agent actions → outcome
- [ ] Cross-check against latest SKILL.md before shipping changes
- [ ] Cross-check against latest SKILL.md before shipping changes
- [ ] Cross-check against latest SKILL.md before shipping changes
