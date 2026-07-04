# Eval Output — Full Worked Examples

Skill: `eval-output` | Load when producing output for this workflow.

## Example 1 — From skill workflow

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

## Example 2 — Typical invocation

**Input:** "Run `eval-output` for [concrete task]"

**Output:**
```
Invoked `eval-output`.
Step 1: Accept Input
Step 2: Classify Evaluation Need
Step 3: Route to Sub-Skill
See SKILL.md Impact Report schema.
```

---

See `SKILL.md` for hard rules, gotchas, and verification checklist.
