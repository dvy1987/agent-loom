# Eval Output — Full Worked Examples

Skill: `eval-output` | Enriched from SKILL.md (improve-skills pass, SKIP_RESEARCH).

## Example 1 — Documented workflow

**Input:** Evaluate this response my agent gave about database indexing

**Output:**
```
=== Eval Output Report ===
Target: Agent response on database indexing
Eval type: Needs rubric first

No rubric found for this task. Routing to eval-rubric-design to create one.

[Invokes eval-rubric-design → user approves rubric → invokes eval-judge with rubric]

=== Evaluation ===
[Structured scores per dimension with justifications]

=== Summary ===
Overall: 3 of 5 dimensions scored 4+/5. Accuracy strong, completeness weak.
Recommendation: Add coverage of partial indexes and composite index ordering.
```

## Example 2 — Step-by-step execution

**Input:** "Run `eval-output` on [concrete task]"

**Agent actions:**
1. Accept Input
2. Classify Evaluation Need
3. Route to Sub-Skill
4. Unified Report

**Impact Report shape:**
```
=== Eval Output Report ===
Target: [what was evaluated — output type, task, model]
Eval type: [rubric-design / direct-scoring / pairwise / pipeline-design]

=== Evaluation ===
[Sub-skill specific output]

=== Summary ===
[Key findings, recommendations, next steps]
```

## Example 3 — Gotcha application

**Input:** Task hits a non-obvious edge case

**Apply:**
- An output that "sounds good" can still fail on accuracy, safety, or completeness — never skip structured evaluation because the output reads well.
- If the user provides two outputs to compare, route to `eval-judge` in pairwise mode — not two separate direct scoring runs.
- Rubrics drift over time as tasks and models evolve. Recommend periodic rubric review when eval results change unexpectedly.
- Self-evaluation (model judging its own output) has known self-enhancement bias. Recommend a different model for judging when possible.

---

See `SKILL.md` for hard rules and verification checklist.
