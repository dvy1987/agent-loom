# Skill Routing — Full Worked Examples

Skill: `skill-routing` | Load when producing output for this workflow.

## Example 1 — From skill workflow

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

## Example 2 — Typical invocation

**Input:** "Run `skill-routing` for [concrete task]"

**Output:**
```
Invoked `skill-routing`.
Step 1: Discover Candidate Skills
Step 2: Score Ambiguity (1–10)
Step 3: Resolve Ambiguity
Routing complete: [request summary]
```

---

See `SKILL.md` for hard rules, gotchas, and verification checklist.
