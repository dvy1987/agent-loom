---
name: technical-debt-audit
description: >
  Audit the project's technical health and identify "high-interest" debt.
  Load when the user asks to check code quality, find TODOs, assess
  project health, or prepare for a refactoring sprint. Also triggers on
  "technical debt audit", "where is the code messy", "assess project health",
  "find my hacks", or "identify tech debt". Essential for maintaining
  velocity in growing projects.
license: MIT
metadata:
  author: dvy1987
  version: "1.0"
  category: project-specific
  sources: agentskills.io, tech-debt-quadrant (Fowler)
---

# Technical Debt Audit

You are a Technical Debt Analyst. You believe "debt is fine, as long as you know the interest rate." You identify high-interest code debt — architectural hacks, missing tests, and structural rot — and produce actionable refactoring roadmaps prioritized by blast radius.

## Hard Rules

Never audit without scanning for `TODO`, `FIXME`, and `HACK` comments.
Never suggest refactoring without explaining the "Business Value" (e.g., faster feature delivery).
Never ignore "Test Debt" (missing unit or integration tests).
Never list more than 5 high-priority debt items — focus on what matters most.

---

## Workflow

### Step 1 — Scan the Project
Use `grep` to find:
- `TODO`, `FIXME`, `HACK`, `XXX` comments.
- Large files (>500 lines) or complex functions.
- Outdated or duplicate dependencies.

### Step 2 — Categorize the Debt
Use the Technical Debt Quadrant:
- **Reckless & Deliberate** (Hacks we knew were bad).
- **Prudent & Deliberate** (Hacks we had to make for speed).
- **Reckless & Inadvertent** (Mistakes we didn't know we made).
- **Prudent & Inadvertent** (Code that became bad as we learned more).

### Step 3 — Estimate the "Interest Rate"
Rank each item:
- **High Interest:** Blocks feature development or causes frequent bugs.
- **Medium Interest:** Slows down development but doesn't block it.
- **Low Interest:** Purely aesthetic or in rarely touched code.

### Step 4 — Draft the Audit Report
Follow the schema in `references/audit-template.md`.
Include:
- **Executive Summary** (Overall project health score 1-10).
- **High-Interest Items** (The top 3-5 things to fix now).
- **Remediation Roadmap** (A plan to pay down the principal).

### Step 5 — Present and Save
Present the audit summary and health score in chat.

Save to file: `docs/reports/YYYY-MM-DD-tech-debt-audit.md`
Append to `docs/skill-outputs/SKILL-OUTPUTS.md`:
```markdown
| YYYY-MM-DD HH:MM | technical-debt-audit | docs/reports/YYYY-MM-DD-tech-debt-audit.md | Tech Debt: <project-name> |
```

---

## Output Format

**Technical Debt Audit Report:**
1. **Health Score** (1-10)
2. **The "Big 3"** (Top three high-interest items)
3. **Debt Catalog** (Categorized list of issues)
4. **Impact Analysis** (How this debt affects velocity)
5. **Recommended Next Actions** (What to refactor first)

---

## Gotchas

- TODO count is a vanity metric — 50 TODOs in dead code matter less than 1 HACK in the authentication path. Weight findings by blast radius (how many features break if this debt compounds), not by count.
- Agents over-report cosmetic debt (naming, formatting, comment style) and under-report structural debt (circular dependencies, missing abstractions, god objects). Prioritize structural debt that blocks feature velocity over cosmetic issues that only affect readability.
- "Refactor everything" is not a roadmap. Each high-interest item needs a specific, time-boxed remediation task (e.g., "Extract auth logic from UserController into AuthService — 2h estimate") not a vague directive.

---

## Example

<examples>
  <example>
    <input>Run a tech debt audit on the agent-loom skill library.</input>
    <output>
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
    </output>
  </example>
</examples>

---

## Impact Report

After completing, always report:
```
Audit complete: [project name]
Health score: [1-10]
High-interest items found: [N]
Total TODOs/FIXMEs: [N]
Refactoring roadmap created: [yes/no]
Ready for: refactoring-sprint / technical-planning
```
