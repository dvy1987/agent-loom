# Technical Debt Audit — Full Worked Examples

Skill: `technical-debt-audit` | Load when producing output for this workflow.

## Example 1 — From skill workflow

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

## Example 2 — Typical invocation

**Input:** "Run `technical-debt-audit` for [concrete task]"

**Output:**
```
Invoked `technical-debt-audit`.
Step 1: Scan the Project
Step 2: Categorize the Debt
Step 3: Estimate the "Interest Rate"
See SKILL.md Impact Report schema.
```

---

See `SKILL.md` for hard rules, gotchas, and verification checklist.
