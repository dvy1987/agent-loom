# Learn From Paper — Full Worked Examples

Skill: `learn-from-paper` | Load when producing output for this workflow.

## Example 1 — From skill workflow

**Input:** Learn from this paper: arXiv:2603.29919 (SkillReducer)

**Output:**
```
═══ Paper Credibility Report ═══
Title: SkillReducer | Credibility: 9/12 | Verdict: PASS

═══ Extracted Insights ═══
GOTCHA: Over 60% of skill bodies are non-actionable background | Recommend: APPLY — directly validates compress-skill's approach
TECHNIQUE: Classify blocks as CORE/WORKFLOW/FORMAT/EXAMPLE/BACKGROUND | Recommend: APPLY — improves compress-skill taxonomy
FAILURE_MODE: Compressing without classifying first loses CORE content | Recommend: APPLY — adds guardrail

═══ Application Plan ═══
1. IMPROVE: compress-skill — add SkillReducer taxonomy
2. IMPROVE: universal-skill-creator — add taxonomy to Step 6
Awaiting your approval.
```

## Example 2 — Typical invocation

**Input:** "Run `learn-from-paper` for [concrete task]"

**Output:**
```
Invoked `learn-from-paper`.
Step 1: Ingest the Paper
Step 2: Credibility Assessment
Step 3: Security Scan
See SKILL.md Impact Report schema.
```

---

See `SKILL.md` for hard rules, gotchas, and verification checklist.
