# Skill Routing — Full Worked Examples

Skill: `skill-routing` | Enriched from SKILL.md (improve-skills pass, SKIP_RESEARCH).

## Example 1 — Documented workflow

**Input:** User says: "Help me think through this problem"

**Output:**
```
Candidates: deep-thinking, brainstorming, socratic
Ambiguity: 5/10

Context signals:
- Project phase: specs exist, PRD exists → past design phase
- Conversation: user just finished implementation, hit a wall
- Trigger match: "think through" matches deep-thinking and brainstorming equally
- Upstream: post-implementation thinking → deep-thinking (not brainstorming, which is pre-implementation)

Routed: deep-thinking
Ambiguity: 5/10
Candidates: deep-thinking, brainstorming, socratic
Resolved by: upstream-downstream (post-implementation context)
Pre-req: met
```

## Example 2 — Step-by-step execution

**Input:** "Run `skill-routing` on [concrete task]"

**Agent actions:**
1. Discover Candidate Skills
2. Score Ambiguity (1–10)
3. Resolve Ambiguity
4. Check Pre-requisites
5. Return Routing Decision

**Impact Report shape:**
```
Routing complete: [request summary]
Skill routed: [skill-name]
Ambiguity: N/10
Candidates considered: [list]
Resolved by: [method]
Question asked: [yes — question text | no]
```

## Example 3 — Gotcha application

**Input:** Task hits a non-obvious edge case

**Apply:**
- "Review" is the most ambiguous word — "review this code" → `code-review-crsp`, "review changes for context" → not a review skill, "review the plan" → `adversarial-hat`. Always check the object being reviewed.
- "Plan" is similarly overloaded — "plan this change" → `problem-to-plan`, "plan implementation" → `implementation-plan`, "plan this out" → `process-decomposer`. The verb before "plan" disambiguates.
- Return only concrete, invokable skill names. Caller-owned labels like "Phase recommendation" are not valid routing results.
- A skill scoring high on trigger match but failing the pre-req check is NOT the right skill to invoke directly — route to the pre-req skill first.

---

See `SKILL.md` for hard rules and verification checklist.
