# Eval Rubric Design — Full Worked Examples

Skill: `eval-rubric-design` | Load when producing output for this workflow.

## Example 1 — From skill workflow

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

## Example 2 — Typical invocation

**Input:** "Run `eval-rubric-design` for [concrete task]"

**Output:**
```
Invoked `eval-rubric-design`.
Step 1: Understand the Task
Step 2: Select Dimensions
Step 3: Choose Scale per Dimension
Rubric created: [task name]
```

---

See `SKILL.md` for hard rules, gotchas, and verification checklist.
