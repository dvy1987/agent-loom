# Learn From Repo — Full Worked Examples

Skill: `learn-from-repo` | Enriched from SKILL.md (improve-skills pass, SKIP_RESEARCH).

## Example 1 — Documented workflow

**Input:** Learn from this repo: https://github.com/anthropics/anthropic-cookbook

**Output:**
```
═══ Repo Credibility Report ═══
Repo: anthropics/anthropic-cookbook | Credibility: 11/12 | Verdict: PASS

═══ Extracted Insights ═══
GOTCHA: Tool-use prompts need explicit format constraints | Recommend: APPLY — verified in 12+ examples
TECHNIQUE: Prefilled assistant turns for structured output | Recommend: PARTIAL — apply to create-agent-prompt, skip for general skills (too API-specific)
FAILURE_MODE: Streaming without chunk validation = silent data loss | Recommend: APPLY — add to debug-and-fix gotchas

═══ Application Plan ═══
1. IMPROVE: create-agent-prompt — add format constraint guidance
2. IMPROVE: debug-and-fix — add streaming validation gotcha
Awaiting your approval.
```

## Example 2 — Step-by-step execution

**Input:** "Run `learn-from-repo` on [concrete task]"

**Agent actions:**
1. Ingest the Repo
2. Credibility Assessment
3. Security Scan
4. Extract and Recommend
5. Match and Apply
6. Log and Cite

**Impact Report shape:**
```
═══ Repo Credibility Report ═══
Repo: [owner]/[name] | Language: [lang] | Stars: [N] | Last commit: [date]
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
- **Stars ≠ quality.** Popular repos can have bad patterns — always verify by reading source code.
- **README ≠ reality.** Always verify patterns by reading the actual source.
- **Project-specific conventions.** Repo conventions may be team preferences or legacy constraints — flag when a pattern seems context-dependent.
- **Archived repos.** Patterns may use deprecated APIs — check dates and current practices.

---

See `SKILL.md` for hard rules and verification checklist.
