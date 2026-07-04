# Technical Debt Audit — Full Worked Examples

Skill: `technical-debt-audit` | Enriched from SKILL.md (improve-skills pass, SKIP_RESEARCH).

## Example 1 — Documented workflow

**Input:** Run a tech debt audit on the agent-loom skill library.

**Output:**
```
**Technical Debt Audit: agent-loom**
**Date:** 2026-04-12 | **Health Score:** 7/10

**The "Big 3" (High-Interest Items):**
1. **agent-creator at 262 lines** — 62 lines over the 200-line limit. Blocks validation pipeline. Blast radius: every improve-skills run flags this as a failure. Fix: compress topology templates and consolidate examples. Effort: 30min.
2. **10 skills below 10/14 score** — missing Gotchas and Examples sections. These skills produce lower-quality agent behavior because the agent has no failure-mode awareness or output examples to pattern-match against. Fix: batch improvement pass. Effort: 2h.
3. **No automated validation in CI** — skill quality is manually checked. Regressions can slip in silently. Fix: add validate-skills as a pre-commit hook. Effort: 1h.

**Debt Catalog:**
| Item | Quadrant | Interest | Location |
|------|----------|----------|----------|
| Oversized agent-creator | Prudent/Deliberate | High | `.agents/skills/agent-creator/SKILL.md` |
| Missing structural sections | Prudent/Inadvertent | High | 10 skills (see queue) |
| No CI validation | Prudent/Inadvertent | Medium | repo root |
| Stale cross-references | Reckless/Inadvertent | Low | various SKILL.md files |

**Recommended Next Actions:**
1. Compress agent-creator (30min)
2. Run improve-skills batch on 10-skill queue (2h)
3. Add validate-skills to pre-commit (1h)

Audit complete: agent-loom
Health score: 7/10
High-interest items found: 3
Total TODOs/FIXMEs: 0
Refactoring roadmap created: yes
Ready for: improve-skills batch execution
```

## Example 2 — Step-by-step execution

**Input:** "Run `technical-debt-audit` on [concrete task]"

**Agent actions:**
1. Scan the Project
2. Categorize the Debt
3. Estimate the "Interest Rate"
4. Draft the Audit Report
5. Present and Save

## Example 3 — Gotcha application

**Input:** Task hits a non-obvious edge case

**Apply:**
- TODO count is a vanity metric — 50 TODOs in dead code matter less than 1 HACK in the authentication path. Weight findings by blast radius (how many features break if this debt compounds), not by count.
- Agents over-report cosmetic debt (naming, formatting, comment style) and under-report structural debt (circular dependencies, missing abstractions, god objects). Prioritize structural debt that blocks feature velocity over cosmetic issues that only affect readability.
- "Refactor everything" is not a roadmap. Each high-interest item needs a specific, time-boxed remediation task (e.g., "Extract auth logic from UserController into AuthService — 2h estimate") not a vague directive.
- 

---

See `SKILL.md` for hard rules and verification checklist.
