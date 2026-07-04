# Eval Pipeline — Full Worked Examples

Skill: `eval-pipeline` | Enriched from SKILL.md (improve-skills pass, SKIP_RESEARCH).

## Example 1 — Documented workflow

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

## Example 2 — Step-by-step execution

**Input:** "Run `eval-pipeline` on [concrete task]"

**Agent actions:**
1. Understand the System
2. Design the Three-Layer Evaluator Stack
3. Design the Eval Dataset
4. Wire CI/CD Integration
5. Define Alerting and Baselines
6. Write the Pipeline Design Document

## Example 3 — Gotcha application

**Input:** Task hits a non-obvious edge case

**Apply:**
- **Intermittent failures are real.** A run of 100 can pass, but nightly runs over weeks surface subtle issues. Design for long-term signal, not single-run confidence.
- **LLM judges need calibration too.** When you change the judge model or rubric, re-run known-bad cases to verify the judge still catches failures.
- **Sampling rates matter for cost.** LLM-as-judge on 100% of PR traffic burns budget fast. Start at 20% and increase for high-risk changes only.
- **Eval datasets go stale.** As the system evolves, old test cases may no longer represent real usage. Schedule quarterly dataset refresh.

---

See `SKILL.md` for hard rules and verification checklist.
