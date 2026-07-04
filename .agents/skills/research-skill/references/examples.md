# Research Skill — Full Worked Examples

Skill: `research-skill` | Load when producing output for this workflow.

## Example 1 — From skill workflow

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

## Example 2 — Typical invocation

**Input:** "Run `research-skill` for [concrete task]"

**Output:**
```
Invoked `research-skill`.
Step 1: Identify the Domain
Step 2: Search in Parallel
Step 3: Classify Findings (SkillReducer Taxonomy)
See SKILL.md Impact Report schema.
```

---

See `SKILL.md` for hard rules, gotchas, and verification checklist.
