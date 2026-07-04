# Apply Paper to Project — Full Worked Examples

Skill: `apply-paper-to-project` | Enriched from SKILL.md (improve-skills pass, SKIP_RESEARCH).

## Example 1 — Documented workflow

**Input:** Apply the insights from that SkillReducer paper to my current project

**Output:**
```
═══ Project Improvement Plan (from: SkillReducer) ═══

Directly Applicable:
1. compress-skill/SKILL.md — add content classification step before compression
   (paper: 60%+ of skill content is non-actionable background)
2. universal-skill-creator/SKILL.md — add SkillReducer taxonomy to Step 6
   (paper: classify blocks as CORE/WORKFLOW/BACKGROUND before writing)

Not Applicable:
- Token counting optimization — project doesn't do runtime token management

Estimated scope: 2 files, small change
Approve? (all / select / reject)
```

## Example 2 — Step-by-step execution

**Input:** "Run `apply-paper-to-project` on [concrete task]"

**Agent actions:**
1. Receive Insights
2. Understand the Project
3. Match Insights to Project
4. Present Improvement Plan
5. Apply Changes (with user approval)
6. Document Changes

**Impact Report shape:**
```
═══ Applied Research Insights ═══
Paper: [title] ([venue], [year])
Project: [project name/path]

Changes Applied:
1. [file:line] — [what changed] — [paper evidence]
2. [file:line] — [what changed] — [paper evidence]

Deferred (architecturally relevant, needs planning):
- [area] — [recommendation]

ADR created: [path or N/A]
Tests: [passed/failed/N/A]
```

## Example 3 — Gotcha application

**Input:** Task hits a non-obvious edge case

**Apply:**
- Research findings are general — the project's specific constraints may make a technique inapplicable even if the paper proves it works in theory. Always check the project context.
- Don't over-apply. If a paper finds "technique X improves performance by 15%," but the project doesn't have a performance problem, don't apply it.
- Papers often test on specific languages/frameworks. A technique proven for Python may not translate to Go or Rust idiomatically. Adapt, don't copy.
- Never add a dependency just because a paper recommends it. Check if the project already has an equivalent.

---

See `SKILL.md` for hard rules and verification checklist.
