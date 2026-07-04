# Research Skill — Full Worked Examples

Skill: `research-skill` | Enriched from SKILL.md (improve-skills pass, SKIP_RESEARCH).

## Example 1 — Documented workflow

**Input:** Research the domain for a sprint-retrospective skill

**Output:**
```
Research Report: sprint-retrospective
======================================
Sources consulted:
- obra/superpowers writing-plans (GitHub): skill with retrospective-adjacent patterns
- martinfowler.com/bliki/Retrospective (blog): authoritative retro formats
- HN: "What makes retrospectives actually useful" (2025 top post)

GOTCHAS:
- Teams skip action items when retrospectives run long — time-box to 60 min max and require at least 1 committed action item before closing
- "What went well" section gets skipped under time pressure — enforce it first, not last
- Remote retros need async pre-fill (sticky notes before the meeting) or participation drops below 50%

WORKFLOW PATTERNS:
- 4Ls format (Liked, Learned, Lacked, Longed For) outperforms Start/Stop/Continue for teams under 6 months old
- Action items need owner + deadline or they're never done — always capture both

FAILURE MODES:
- Retro becomes a complaint session with no actions → require 1 committed action item with owner
- Same issues raised every sprint → track recurring themes across retros, escalate blockers

EXISTING SKILLS FOUND:
- None found specifically for sprint-retrospectives

DISCARD:
- "Retrospectives improve team communication" — general knowledge, not a skill-specific gotcha
```

## Example 2 — Step-by-step execution

**Input:** "Run `research-skill` on [concrete task]"

**Agent actions:**
1. Identify the Domain
2. Search in Parallel
3. Classify Findings (SkillReducer Taxonomy)
4. Deliver Findings Report

**Impact Report shape:**
```
Research complete: [domain]
Sources consulted: N
Gotchas found: N (listed above)
Workflow patterns found: N
Existing skills found: [names or "none"]
Discarded as background: N items
Ready for: universal-skill-creator Step 3 / improve-skills Step 2c
```

## Example 3 — Gotcha application

**Input:** Task hits a non-obvious edge case

**Apply:**
- Never report background knowledge as a finding. "PRDs should have clear requirements" is training data, not a research finding.
- If no academic papers exist for the domain, that's fine — practitioner blogs and GitHub repos are often higher signal for skill-writing purposes.
- Existing skills in repos are the highest-value source — they represent tested patterns from real use.
- 

---

See `SKILL.md` for hard rules and verification checklist.
