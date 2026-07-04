# Learn From Chat — Full Worked Examples

Skill: `learn-from-chat` | Enriched from SKILL.md (improve-skills pass, SKIP_RESEARCH).

## Example 1 — Documented workflow

**Input:** During debugging, the agent discovers that compress-skill's workflow doesn't check whether moved references are actually loaded by the skill at runtime.

**Output:**
```
═══ Chat Learning ═══
Discovered: compress-skill can move content to references/ without verifying load triggers exist
Evidence: During compression, background was moved to references/background.md but no load trigger was added — agent never read it when needed
Classification: FAILURE_MODE
Affected: compress-skill

═══ Proposed Changes ═══
compress-skill:
  Section: ## Gotchas
  Change:
  + - Every file moved to `references/` must have a specific load trigger in the workflow — "see references/" is not sufficient.

Awaiting your approval to apply.
```

## Example 2 — Step-by-step execution

**Input:** "Run `learn-from-chat` on [concrete task]"

**Agent actions:**
1. Capture
2. Classify
3. Match
4. Present
5. Apply (user approval required)
6. Log

**Impact Report shape:**
```
Chat learning captured: [YYYY-MM-DD]
Discovered: [one-sentence insight]
Classification: [tag] | Generalizable: [yes/no]
Status: [IMPLEMENTED / ESCALATED / REJECTED]
Skills modified: [list] | Contradictions resolved: [N]
validate-skills: [skill]: [before] → [after]   (omit if ESCALATED)
Logged: docs/learnings/chat-learnings.md
```

## Example 3 — Gotcha application

**Input:** Task hits a non-obvious edge case

**Apply:**
- Chat context can be misleading — confirm the learning is generalizable, not project-specific, before modifying a skill.
- Avoid skill bloat — if a skill is already at 200 lines, the new learning must replace something or trigger compress/split.
- Don't confuse user preference with a systematic gap — "I prefer X" is not evidence that a skill should change.
- Multiple learnings from one chat should each be evaluated independently — don't batch-approve.

---

See `SKILL.md` for hard rules and verification checklist.
