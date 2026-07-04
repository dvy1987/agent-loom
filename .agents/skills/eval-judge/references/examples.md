# Eval Judge — Full Worked Examples

Skill: `eval-judge` | Load when producing output for this workflow.

## Example 1 — From skill workflow

**Input:** Score this API documentation response against our rubric

**Output:**
```
=== Evaluation Report ===
Target: API documentation response for /users endpoint
Rubric: docs/evals/2026-04-19-api-docs-rubric.md
Mode: Direct scoring

=== Hard Gates ===
| Gate | Verdict | Evidence |
|------|---------|----------|
| Format | PASS | Includes endpoint, method, params, response example |
| Safety | PASS | No internal URLs or credentials exposed |

=== Dimension Scores ===
### Accuracy — Score: 4/5 (confidence: 0.85)
Evidence: All parameter types correct. Response schema matches actual API.
Reasoning: One minor issue — rate limit header documented as X-Rate-Limit but actual is X-RateLimit-Remaining.
Improvement: Update rate limit header name to X-RateLimit-Remaining.

### Completeness — Score: 3/5 (confidence: 0.9)
Evidence: Missing error response examples for 401 and 429 status codes.
Reasoning: Core happy path documented but error handling incomplete — rubric requires all documented status codes.
Improvement: Add error response examples for 401 (unauthorized) and 429 (rate limited).

=== Summary ===
Hard gates: 2 pass, 0 fail
Dimensions: Accuracy 4/5, Completeness 3/5
Lowest-scoring: Completeness — missing error response examples
Overall verdict: PASS (all gates pass, quality improvements recommended)
```

## Example 2 — Typical invocation

**Input:** "Run `eval-judge` for [concrete task]"

**Output:**
```
Invoked `eval-judge`.
Step 1: Gather Inputs
Step 2: Choose Evaluation Mode
Step 3: Direct Scoring
Evaluation complete: [target]
```

---

See `SKILL.md` for hard rules, gotchas, and verification checklist.
