# runtime-learning-loop — Worked Examples

<!-- security-scanned SAFE 2026-07-08 -->

## Example 1 — Preconditions fail: refuse and route

**Input:** "Make my recipe-planner agent self-improving."

**Output:**
```
Precondition check:
  Observability: NONE (no traces on any flow) → FAIL
  Eval harness: none; no held-out set → FAIL
REFUSING to build the loop — without traces there is nothing to learn from,
and without evals we could not tell improvement from noise.
Route: 1) agent-observability (~30 min, free tier) → 2) eval-rubric-design +
eval-pipeline (small 20-case set, 6 held out) → 3) return here.
Interim value: agent-run-retro works TODAY on saved outputs while the
preconditions are built.
```

**Why this works:** the hard gate is enforced with a concrete route and an
interim alternative, instead of building a loop that would optimize noise.

## Example 2 — GEPA offline compile (the right GEPA use)

**Input:** "One-off: my summarizer prompt is hand-tuned mush. I have 60
labeled examples and a judge that explains failures. Optimize it."

**Output:**
```
Technique: GEPA (offline compile) — fits: labeled set (60), heterogeneous
failures, feedback-rich judge. ACE rejected: no continuous-learning need;
this is a one-shot compile.
Setup: metric returns score + stage-attributed feedback text; reflection
model = high tier; task model = product's model. Budget: light preset
(~1.3k metric calls, est. $9). Held-out: 15 examples quarantined.
Result: held-out 0.61 → 0.79. Promotion proposal shown as diff + before/after
+ rollback (git revert of prompt file). Owner approved → promoted.
Recorded: model-swap invalidation note — re-run this compile if the product
changes models.
```

**Why this works:** GEPA is used where it wins (offline, labels, rich
feedback), the reflection/task model split controls cost, and the promotion
still goes through the human gate with rollback.

## Example 3 — Regression monitor fires; ladder demotion

**Input:** (automated alert during Journeyman-stage operation)

**Output:**
```
REGRESSION ALERT: production eval mean 7.8 → 6.9 (below pre-loop baseline
7.2) within 48h of promotion #14 (playbook delta batch).
Actions taken automatically:
  1. Loop paused. 2. Promotion #14 rolled back (deltas reverted; counters
  preserved for analysis). 3. Owner alerted with this readout.
Analysis: delta batch included a strategy generalized from 2 traces that
harms the common case (helpful=2 / harmful=9 after rollback re-score).
Ladder: Journeyman → Apprentice (any rollback drops one stage). Next 10
promotions require your approval again.
Learning captured: min-evidence threshold for playbook deltas raised to 5
traces; curator dedup rule added.
```

**Why this works:** the monitor + rollback + demotion chain ran without
waiting for a human, but the human got a plain-language readout and the loop
got stricter — the failure made the system safer.

## Example 4 — Keeping the loop away from the judge

**Input:** "The loop keeps proposing edits to the judge prompt because scores
'look too harsh'."

**Output:**
```
BLOCKED: judge prompts are outside the learnable-surface allowlist (LOOP.md).
A loop that grades itself will always find its own work excellent — that is
reward hacking by construction.
Correct path: if the judge seems miscalibrated, run eval-rubric-design with
human-labeled anchor examples (owner labels 10 outputs good/bad; judge
agreement measured before/after). Judge changes are human-owned, versioned,
and never automated.
```

**Why this works:** the allowlist boundary held under pressure from the
loop's own proposals; judge calibration went through the human-owned path.
