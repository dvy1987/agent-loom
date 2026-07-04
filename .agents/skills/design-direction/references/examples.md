# Design Direction — Full Worked Examples

Skill: `design-direction` | Enriched from SKILL.md (improve-skills pass, SKIP_RESEARCH).

## Example 1 — Step-by-step execution

**Input:** "Run `design-direction` on [concrete task]"

**Agent actions:**
1. Read product reality
2. Score the archetype palette
3. Set the posture
4. Generate 2-3 distinct directions
5. Compare side-by-side
6. Commit to one
7. Write DIRECTION.md

**Impact Report shape:**
```
Direction set: [feature]
Posture: [one line]
Directions explored: [N] (differ on: [dimensions])
Chosen: [name] — feels like [product]
Owner mode: [technical | non-technical] | chooser: [user | agent]
DIRECTION.md: .design/<feature>/DIRECTION.md
Handoff to: design-system
```

## Example 2 — Anti-skip (rationalization defense)

**Input:** Agent tries to skip a gate

| Excuse | Reality |
|---|---|
| "I already know the right look — skip exploration" | The first idea IS the corpus mean. Generate options or you converge on slop. |
| "Three color variants count as three directions" | They don't. Diverge on type, layout, motion too, or it's one direction. |
| "Owner is non-technical, just ask them to pick a vibe" | They can't. Recommend one with plain rationale; decide for them. |
| "Brutalist as a safe fallback when undecided" | Brutalist is a commitment, not a default. Only when brand already owns it. |

---

See `SKILL.md` for hard rules and verification checklist.

## Verification checklist (L3)

- [ ] Examples demonstrate SKILL.md hard rules, not generic chat
- [ ] Anti-skip or rationalization defense included where applicable
- [ ] Output artifacts or Impact Report shape is explicit
- [ ] Reader can trace input → concrete agent actions → outcome

## Suite note

See orchestrator skill and sibling references for full suite walkthrough.
- [ ] Cross-check against latest SKILL.md before shipping changes
- [ ] Cross-check against latest SKILL.md before shipping changes
