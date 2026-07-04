# OODA — Full Worked Examples

Skill: `ooda` | Load when producing output for this workflow.

## Example 1 — From skill workflow

**Input:** A competitor just launched a nearly identical feature to what we've been building for 3 months. We ship in 6 weeks. What do we do?

**Output:**
```
OBSERVE
Facts: Competitor launched Feature X. Our version ships in 6 weeks. We have 3 months of build invested. Their implementation is public and reviewable.
Assumptions: We're assuming their implementation is complete (may not be). We're assuming our users know about it (may not be true yet).

ORIENT
Situation: We are not first, but we are not necessarily late. "First to market" matters less than "best for our specific users" in most B2B contexts. Our orientation advantage: we know our users' specific workflow in a way the competitor doesn't. Their launch gives us a forcing function and a benchmark, not necessarily a defeat.
Key insight: The competitor's launch is a validation signal — someone else thinks this is worth building. The question is not whether to ship, but how to ship differently.
Blind spot risk: We might be overestimating how much our users care about being "first." Check with 3 users before changing course.

DECIDE
Options:
1. Ship as planned, add a direct comparison to the competitor in messaging — lean into the existing build.
2. Delay 2 weeks to differentiate on one specific dimension the competitor clearly missed.
3. Pivot completely to something adjacent — too costly given 3 months of investment.

Chosen: Option 1 — ship as planned, accelerate messaging that positions around the specific workflow advantage we have.
Reason: Delay costs momentum and credibility with users who are waiting. The differentiation story is more important than the differentiation itself at this stage.

ACT
Owner: Product + Marketing
Timeline: Ship in 6 weeks as planned. Messaging ready in 2 weeks.
Reversibility: Reversible — we can iterate the feature post-launch.

NEXT LOOP TRIGGER
Observe user response to the competitor's feature in the next 2 weeks. If 3+ users mention the competitor unprompted, loop immediately on messaging strategy.
```

## Example 2 — Typical invocation

**Input:** "Run `ooda` for [concrete task]"

**Output:**
```
Invoked `ooda`.
Step 1: Observe: What Do We Actually Know?
Step 2: Orient: What Does This Mean?
Step 3: Decide: What's the Move?
OODA loop: [situation]
```

---

See `SKILL.md` for hard rules, gotchas, and verification checklist.
