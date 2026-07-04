# Experiment Backlog — Full Worked Examples

Skill: `experiment-backlog` | Enriched from SKILL.md (improve-skills pass, SKIP_RESEARCH).

## Example 1 — Step-by-step execution

**Input:** "Run `experiment-backlog` on [concrete task]"

**Agent actions:**
1. Gather Candidates
2. Tag Each Candidate
3. Score with ICE + Feasibility
4. Apply the Funnel-ROI Map
5. Sort and Write the Backlog File
6. Hand Off

**Impact Report shape:**
```
Backlog updated: docs/experiments/backlog.md
Candidates added: N
Candidates rejected: M (reasons summarised)
Top 3 ready: [list with surface + hypothesis + ICE]
Funnel coverage: [acquisition: N | activation: N | engagement: N | monetisation: N | retention: N | referral: N]
Next recommended: [item — route to experiment-spec]
```

## Example 2 — Gotcha application

**Input:** Task hits a non-obvious edge case

**Apply:**
- **Feasibility is a binary gate, not an ICE multiplier.** A high-ICE item with insufficient traffic at planned MDE is REJECTED — not "deprioritised". Letting it sit on the backlog wastes attention and creates phantom queues.
- **ICE inflation.** Self-proposed ideas score themselves 8/9/8. Anchor scoring against past wins where you already know the lift size — recalibrate every quarter.
- **Retention A/Bs without a holdout are fake.** Retention metrics need a long-running holdout cohort. Reject any retention test that lacks one and surface "fix the holdout first" as a blocking dependency.
- **Don't replace the backlog file — append.** `docs/experiments/backlog.md` is a living portfolio with status. Replacing it loses the lifecycle history that downstream skills (especially `experiment-readout` learnings) depend on.

---

See `SKILL.md` for hard rules and verification checklist.
