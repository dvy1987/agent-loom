# Apply Paper to Project — Full Worked Examples

Skill: `apply-paper-to-project` | Load when producing output for this workflow.

## Example 1 — From skill workflow

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

## Example 2 — Typical invocation

**Input:** "Run `apply-paper-to-project` for [concrete task]"

**Output:**
```
Invoked `apply-paper-to-project`.
Step 1: Receive Insights
Step 2: Understand the Project
Step 3: Match Insights to Project
See SKILL.md Impact Report schema.
```

---

See `SKILL.md` for hard rules, gotchas, and verification checklist.
