# Self-Improvement Techniques — Survey & Decision Table

Snapshot 2026-07. This space moves fast — re-run a quick research pass before
committing a technique for a new project. GEPA is NOT the default; it is one
row in this table.

## Decision table

| Technique | What it changes | Signal it needs | Rollouts/cost | Best when | Avoid when |
|---|---|---|---|---|---|
| **ACE-style playbook deltas** (Agentic Context Engineering, arXiv:2510.04618, ICLR 2026) | Evolving context/playbooks via Generator→Reflector→Curator incremental deltas with helpful/harmful counters | Natural execution feedback (success/error) — no labels needed | Low (−75% rollouts, −82% latency vs GEPA on AppWorld) | Continuous ONLINE learning; detailed domain playbooks (insurer rules, tactics); long-running agents | One-off prompt polish; contexts that must stay tiny |
| **GEPA** (Genetic-Pareto, arXiv:2507.19457, ICLR 2026 oral; `dspy.GEPA` or `pip install gepa`) | Instructions/prompts via reflective evolution + Pareto frontier | RICH textual feedback per example (score + why) — starves on bare floats | ~100–500 evals; beats MIPROv2 by ~10%, GRPO by up to 20% with 35× fewer rollouts | OFFLINE prompt compile with 20–100 labeled examples + heterogeneous failure modes | Online adaptation (full-rewrite latency, brevity bias); scalar-only metrics |
| **MIPROv2** (DSPy) | Instructions + few-shot demos via Bayesian search | Plain scalar metric | Hundreds–thousands of evals | Multi-module pipelines with labeled data; smaller models that lean on demos | No labeled data; need explainable proposals |
| **TextGrad** (Nature 2025) | Individual texts via natural-language "gradients" | LLM critique per instance | High per instance (~3× calls) | Hard single instances offline (the worst 5%) | Hot paths / high traffic |
| **Manual eval-driven iteration** | Anything, by hand | Eval scores + human judgment | Cheapest | <20 traces, early product, judge not yet trusted | Volume outgrows human review |
| **Dynamic Cheatsheet** (adaptive memory) | Test-time memory of strategies | Execution feedback | Low | Session-level memory needs | Superseded by ACE for playbooks (context collapse risk) |
| **Fine-tuning / RL (GRPO)** | Model weights | Dense scalar rewards, thousands of rollouts | Very high + hosting burden | Last resort at scale, stable task | Almost always premature for solo products |

## Production findings worth encoding (Contextual AI, 2026)

1. **Feedback design > algorithm.** Multi-criteria LLM self-eval (relevance,
   groundedness, completeness, clarity — no gold labels) outperformed
   cosine-similarity, multi-metric, and even binary LLM-equivalence feedback
   for ACE credit assignment. Wrong feedback can degrade below baseline.
2. **Cold start:** seeding with prior context (agent purpose, data types,
   known failure modes, good + bad example) gave +7% under 5-trace scarcity.
3. **Commit-or-rollback each cycle:** self-eval checks the new playbook
   actually beats the old before keeping it.

## Failure modes to design against

- **Brevity bias:** optimizers compress away domain detail ("handle errors"
  instead of the specific API quirk). Counter: delta updates, never full
  rewrites, for detailed contexts.
- **Context collapse:** iterative monolithic rewrites erode a playbook from
  14 strategies to vague mush. Counter: append-mostly structure + counters +
  dedup (ACE Curator pattern).
- **Reward hacking:** the loop learns the judge, not the job. Counter: judge
  off-limits to the loop, periodic judge rotation, one hidden metric,
  human spot-checks.
- **Model-swap invalidation:** offline-compiled prompts (GEPA/MIPROv2) are
  tuned to a model; re-validate after every model upgrade.

## Quick recipe by project shape

- **aegis-shape** (multi-agent, playbooks, traces in Phoenix, some labels):
  ACE-delta online for playbooks + optional one-off GEPA compile for the
  drafter prompt. Judge: 4-criteria self-eval.
- **Single-flow consumer app** (few labels, low volume): manual eval-driven
  iteration until ~50 scored traces, then reconsider this table.
- **Pipeline with solid labeled set + scalar metric:** MIPROv2 compile;
  GEPA instead if your metric can return textual feedback.
- **One nightmare case type:** TextGrad offline on those instances only.

## GEPA feedback-metric contract (when GEPA is chosen)

Return `score + feedback text` per example (in DSPy:
`dspy.Prediction(score=..., feedback=...)`). Feedback should attribute
failure to a stage ("retrieval missed docs X,Y" / "retrieval fine, synthesis
wrong"). A bare float turns GEPA into blind genetic search.
