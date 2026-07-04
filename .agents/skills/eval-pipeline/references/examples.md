# Eval Pipeline — Full Worked Examples

Skill: `eval-pipeline` | Load when producing output for this workflow.

## Example 1 — From skill workflow

**Input:** Set up an eval pipeline for our customer support chatbot

**Output:**
```
# Eval Pipeline: Support Chatbot

## Evaluator Stack
### Layer 1 — Deterministic
- Response under 300 words: PASS/FAIL
- No PII in response: regex scan
- Greeting present: string match
- JSON tool-call schema valid: schema check

### Layer 2 — Statistical
- Embedding similarity to gold responses: baseline 0.72, alert < 0.65
- Average response latency: baseline 1.2s, alert > 3s

### Layer 3 — LLM-as-Judge
- Rubric: docs/evals/2026-04-19-support-chatbot-rubric.md
- Dimensions: task resolution, accuracy, tone (from eval-rubric-design)
- Sampling: 30% on PRs, 100% nightly
- Judge model: GPT-4.1 (different from production model)

## CI/CD
Pre-merge: deterministic + statistical (full) + LLM judge (30%)
Gate: all deterministic pass, no dimension drops > 10% from baseline
Nightly: full suite + known-bad validation

Pipeline design saved to docs/evals/2026-04-19-support-chatbot-pipeline.md
```

## Example 2 — Typical invocation

**Input:** "Run `eval-pipeline` for [concrete task]"

**Output:**
```
Invoked `eval-pipeline`.
Step 1: Understand the System
Step 2: Design the Three-Layer Evaluator Stack
Step 3: Design the Eval Dataset
Pipeline designed: [system name]
```

---

See `SKILL.md` for hard rules, gotchas, and verification checklist.
