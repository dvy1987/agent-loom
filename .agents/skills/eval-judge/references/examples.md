# Eval Judge — Full Worked Examples

Skill: `eval-judge` | Enriched from SKILL.md (improve-skills pass, SKIP_RESEARCH).

## Example 1 — Documented workflow

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

## Example 2 — Step-by-step execution

**Input:** "Run `eval-judge` on [concrete task]"

**Agent actions:**
1. Gather Inputs
2. Choose Evaluation Mode
3. Direct Scoring
4. Pairwise Comparison (if two outputs)
5. Confidence Scoring
6. Internal Consistency Check (long-form outputs only)
7. Produce Evaluation Report

**Impact Report shape:**
```
Evaluation complete: [target]
Mode: [direct scoring / pairwise comparison]
Rubric used: [name/path]
Hard gates: [N] pass, [N] fail
Dimensions scored: [N]
Average confidence: [0-1]
Verdict: [PASS / FAIL / Winner A/B/TIE]
Key finding: [one-line summary]
```

## Example 3 — Gotcha application

**Input:** Task hits a non-obvious edge case

**Apply:**
- **Length ≠ quality.** Longer responses are systematically rated higher by LLM judges. Actively check: "Would a shorter version with the same content score equally?"
- **Confident tone ≠ accuracy.** Authoritative-sounding responses get higher scores even when wrong. Always verify factual claims against rubric criteria, not delivery style.
- **Chain-of-thought improves reliability 15-25%** but also increases token cost. Worth it for quality-critical evals; consider sampling for high-volume pipelines.
- In pairwise mode, if one output is much longer, the position swap is especially critical — length bias and position bias can compound.

---

See `SKILL.md` for hard rules and verification checklist.
