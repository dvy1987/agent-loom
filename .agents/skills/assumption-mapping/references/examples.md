# Assumption Mapping — Full Worked Examples

Skill: `assumption-mapping` | Load when producing output for this workflow.

## Example 1 — From skill workflow

**Input:** Map the assumptions in our community feature plan

**Output:**
```
Assumption Map: Community Feature Plan

CRITICAL — test first
┌─────────────────────────────────────────────
│ "Users want to connect with each other, not just the product"
│ Evidence: 0 — no user research conducted on peer connection desire
│ Minimum test: Interview 10 active users. Ask: "When was the last time you wanted to talk to another user of this product?" If fewer than 5 have a real story, assumption is likely false.
│ False condition: <30% of users can name a specific thing they'd ask another user
└─────────────────────────────────────────────
┌─────────────────────────────────────────────
│ "Founding members will sustain posting for 90+ days without incentive"
│ Evidence: None — no precedent in this user base
│ Minimum test: Ask 5 prospective founding members to commit to 2 posts/week for 4 weeks before launch. See who follows through.
│ False condition: Fewer than 3 of 5 complete the 4-week pilot
└─────────────────────────────────────────────

VALIDATED
- "Users are active in the product at least monthly": confirmed by usage data (68% MAU)

MONITOR
- "Community content will appear in search results": plausible, not yet tested

TOTAL: 8 assumptions found | Critical: 2 | Validated: 1 | Monitor: 5
```

## Example 2 — Typical invocation

**Input:** "Run `assumption-mapping` for [concrete task]"

**Output:**
```
Invoked `assumption-mapping`.
Step 1: Read the Plan or Document
Step 2: State Each as a Falsifiable Claim
Step 3: Place Each on the Grid
Assumption map: [plan/document]
```

---

See `SKILL.md` for hard rules, gotchas, and verification checklist.
