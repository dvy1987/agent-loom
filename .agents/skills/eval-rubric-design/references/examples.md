# Eval Rubric Design — Full Worked Examples

Skill: `eval-rubric-design` | Enriched from SKILL.md (improve-skills pass, SKIP_RESEARCH).

## Example 1 — Documented workflow

**Input:** Create an eval rubric for a customer support chatbot

**Output:**
```
# Evaluation Rubric: Customer Support Chatbot

## Purpose
Evaluate chatbot responses for customer support quality. Supports model comparison and prompt iteration.

## Hard Gates (pass/fail)
| Gate | Pass | Fail |
|------|------|------|
| Safety | No PII exposure, no prohibited guidance | Any privacy breach or policy violation |
| Format | Response under 300 words, uses greeting | Missing greeting or exceeds length |

## Quality Dimensions
### Task Resolution: Did the response address the customer's issue?
| Score | Description |
|-------|-------------|
| 5 | Directly resolves the issue with clear next steps |
| 3 | Addresses the issue but missing specific next steps |
| 1 | Does not address the stated issue |
**Edge cases:** Customer asks multiple questions — score based on primary issue coverage.

### Accuracy: Are policy details and product info correct?
| Score | Description |
|-------|-------------|
| 5 | All claims match current policy documentation |
| 3 | Core answer correct, one minor policy detail imprecise |
| 1 | Contains incorrect policy information |

### Tone: Appropriate for frustrated customer?
| Score | Description |
|-------|-------------|
| 3 | Empathetic, professional, acknowledges frustration |
| 2 | Professional but lacks empathy signals |
| 1 | Dismissive, overly casual, or robotic |

Rubric saved to docs/evals/2026-04-19-support-chatbot-rubric.md
```

## Example 2 — Step-by-step execution

**Input:** "Run `eval-rubric-design` on [concrete task]"

**Agent actions:**
1. Understand the Task
2. Select Dimensions
3. Choose Scale per Dimension
4. Write Score Descriptions
5. Define Edge Cases
6. Write the Rubric Document

## Example 3 — Gotcha application

**Input:** Task hits a non-obvious edge case

**Apply:**
- "Accuracy" means different things in different contexts: factual correctness vs. faithfulness to source vs. alignment with expected output. Always define which one.
- Consider **value-weighting dimensions by business impact** — high aggregate scores can mask low performance on high-value dimensions. A model scoring 48/100 overall can deliver more economic value than one scoring 62/100 if it wins on the dimensions that matter most (AlphaEval 2026, credibility 8/12).
- Teams commonly over-index on fluency/tone and under-index on completeness. Ask: "Would you rather have a well-written incomplete answer or a rough complete one?"
- LLM judges apply rubrics more consistently when score descriptions use **positive framing** ("includes X") rather than negative ("doesn't lack X").

---

See `SKILL.md` for hard rules and verification checklist.
