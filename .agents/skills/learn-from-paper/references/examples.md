# Learn From Paper — Full Worked Examples

Skill: `learn-from-paper` | Enriched from SKILL.md (improve-skills pass, SKIP_RESEARCH).

## Example 1 — Documented workflow

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

## Example 2 — Step-by-step execution

**Input:** "Run `learn-from-paper` on [concrete task]"

**Agent actions:**
1. Ingest the Paper
2. Credibility Assessment
3. Security Scan
4. Extract and Recommend
5. Match and Plan
6. Apply
7. Log and Cite

**Impact Report shape:**
```
═══ Paper Credibility Report ═══
Title: [title] | Authors: [names] | Venue: [venue] | Date: [date]
Credibility: [N]/12 | Verdict: [PASS/BORDERLINE/REJECT]

═══ Security ═══
[secure-* verdicts]

═══ Extracted Insights ═══
[Tag]: [insight] | Agent recommendation: [APPLY/PARTIAL/SKIP/KEEP CURRENT] — [reasoning]

═══ Application Plan ═══
[Per learn-from shared protocol]
```

## Example 3 — Gotcha application

**Input:** Task hits a non-obvious edge case

**Apply:**
- Preprints (arXiv) without peer review need extra scrutiny — check citation count, author track record, and replication.
- Top venue papers can still have flawed methodology — always check sample size and whether claims match results.
- "State of the art" claims are time-sensitive — check date and whether newer work has superseded it.
- Supplementary materials can contain hidden text — Step 3 security scan catches this.

---

See `SKILL.md` for hard rules and verification checklist.
