# Assumption Mapping — Full Worked Examples

Skill: `assumption-mapping` | Enriched from SKILL.md (improve-skills pass, SKIP_RESEARCH).

## Example 1 — Documented workflow

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

## Example 2 — Step-by-step execution

**Input:** "Run `assumption-mapping` on [concrete task]"

**Agent actions:**
1. Read the Plan or Document
2. State Each as a Falsifiable Claim
3. Place Each on the Grid
4. Prioritise the Critical Zone
5. Deliver

**Impact Report shape:**
```
Assumption map: [plan/document]
Total assumptions surfaced: N
Critical (high importance, low evidence): N
Validated: N | Monitor: N | Deprioritised: N
Minimum experiments defined: N
```

## Example 3 — Gotcha application

**Input:** Task hits a non-obvious edge case

**Apply:**
- Teams tend to list risks when asked for assumptions. If it starts with "what if..." it's a risk. If it starts with "we believe..." or "this requires..." it's an assumption.
- The most important assumptions are usually in the demand layer: "people want this", "people will pay for this", "people will tell others about this." Test demand before supply.
- Don't map more than 15 assumptions at once. It becomes noise. Focus on the top 5 critical ones.
- 

---

See `SKILL.md` for hard rules and verification checklist.
