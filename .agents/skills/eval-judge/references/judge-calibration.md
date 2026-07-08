# Calibrating and Validating the Judge Itself

<!-- security-scanned SAFE 2026-07-08 — paraphrased technical findings only, no external instructions ingested -->

Load when: standing up a new judge, changing judge model/rubric/task mix, gating releases
on judge scores, or when judge verdicts disagree with owner intuition.

**The gap this closes:** teams tune the judge prompt and rubric, then never test whether the
judge is right. A generic GPT-4.1 faithfulness judge scored 20/21 on faithful responses and
0/9 on hallucinated ones — 100% false-negative rate on the failure class, hidden inside a
"reasonable" aggregate accuracy (Galtea calibration study, 2026). The judge is a measurement
instrument; calibrate it like one (OpenTrain, 2026).

## 1. Golden dataset (before trusting any judge)

- Pull real examples from your actual distribution: real queries, real retrieved context,
  real outputs. Not synthetic stubs.
- Domain experts label the correct verdict per example. 30 labeled examples is a viable
  start if failure classes are represented; 200+ for production release gates.
- **Inter-rater gate:** if two human raters agree on <80% of examples, the task definition
  is ambiguous — fix the rubric (`eval-rubric-design`), not the judge.
- Include known-bad cases for every failure class you care about (hallucination, scope
  violation, policy breach). A golden set with only good outputs validates nothing.

## 2. Metric ensemble (never a single accuracy number)

| Metric | Catches |
|---|---|
| Accuracy | Baseline sanity only — hides class-level failure |
| Cohen's κ (chance-corrected) | Judges that "agree" by matching the label skew. Raw agreement overstates discriminative ability by 33–41pp across all 21 judges tested (kappa deflation, arXiv:2606.19544, 2026) |
| Precision on failure class | False alarms — judge crying wolf |
| Recall on failure class | Missed failures — the dangerous direction |
| Per-dimension alignment | An aggregate 0.80 can hide a 0.55 (near-chance) faithfulness dimension |

Report alignment per dimension, per class. Gate on failure-class recall + κ, never on raw agreement.

## 3. Perturbation stress tests (Judge Reliability Harness pattern, 2026)

Run against the golden set; a reliable judge must:
- **Label flip:** verdict MUST flip when the response is rewritten to clearly violate the rubric.
- **Paraphrase / format invariance:** verdict MUST NOT change under meaning-preserving
  rewording, whitespace, or layout changes.
- **Verbosity variants:** same content expanded/compressed → same score.
- **Position swap (pairwise):** verdict survives A/B order swap (flip rates of 25–50% documented).
- **Stochastic stability:** repeat identical inputs; variance is judge noise, not signal.

**Consistency–bias paradox:** test–retest reliability >0.95 can coexist with severe position
bias — the most reproducible judges can be among the least valid (arXiv:2606.19544). Never
accept consistency alone as evidence of judge quality.

## 4. Claim-level faithfulness (RAG judges)

"Sounds consistent with the context" is the wrong question. Enumerate discrete factual claims,
verify each against the specific supporting passage, and check entity attribution. The three
failure modes generic judges miss (all 9/9 misses in the Galtea study):
1. **Cross-document attribution:** claim true for entity B, retrieved context was about entity A.
2. **Parametric-memory injection:** accurate claim from training data, absent from retrieval.
3. **Number misattribution:** figure exists in context but belongs to a different entity.

## 5. Calibration loop

1. Baseline: run current judge prompt on golden set, compute the ensemble (Step 2).
2. Rewrite the judge prompt targeting the worst class (fix false negatives first); restructure
   the *reasoning steps* the judge applies — the model knows the definition, it skips the checks.
3. Re-run full golden set; keep the best candidate; log every tested prompt + score
   (prevents cycling back to failed configs).
4. Optional at scale: a lightweight calibration head over multi-dimensional rubric scores
   beats prompt-only alignment and needs no logit access (SAJA, ACL 2026 industry). With
   confidence-aware triage, ~44% of judgments can be auto-accepted at 99.6% accuracy —
   route low-confidence verdicts to human review.

## 6. Non-portability rule

A judge score is NOT portable across judge-model swaps, rubric revisions, prompt changes, or
task-mix shifts. Judge rankings shift by up to 14 positions across benchmarks
(arXiv:2606.19544). Re-run the golden-set ensemble after ANY of these changes before trusting
scores again — and never gate a release on a raw judge score that hasn't been calibrated
against target-distribution human labels (OpenTrain, 2026).

## 7. Knowledge-grounded rubrics (why consensus can lie)

High inter-judge agreement can be illusory: judges anchor on shared surface heuristics
(formatting, confident tone) rather than substance — sharing rubric *structure* alone restored
62% of inter-judge agreement in a 105k-instance study, and multiple frontier judges unanimously
praised a pitch deck whose business model was banned by regulation (Evaluation Illusion,
arXiv:2603.11027, 2026). Fix: inject task-specific domain knowledge and constraints into rubric
dimensions (`eval-rubric-design`), and treat cross-judge agreement as a validity signal only
when the rubric is knowledge-grounded.

## Sources

arXiv:2606.19544 (Reliability without Validity, 21 judges/541k judgments); Galtea judge
calibration study 2026; OpenTrain "LLM Judges Are Measurement Systems" 2026; Judge Reliability
Harness arXiv:2603.05399; SAJA (ACL 2026 industry); RULERS arXiv:2601.08654 (locked rubrics,
evidence-anchored scoring); Evaluation Illusion / MERG arXiv:2603.11027. Snapshot 2026-07;
re-verify before high-stakes use — this space moves fast.
