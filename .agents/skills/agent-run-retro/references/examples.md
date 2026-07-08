# agent-run-retro — Worked Examples

<!-- security-scanned SAFE 2026-07-08 -->

## Example 1 — Full session: appeal-drafter quality retro

**Input:** "Ran the appeal drafter on 5 showcase cases today. Two letters felt
great, three felt generic. Retro."

**Output:**
```
Evidence: 5 runs; judge scores 8,8,5,6,5; cost $0.34/run; traces show the
three weak letters skipped the insurer-playbook retrieval step (0 playbook
spans).
Interview (3 of 5 questions used — answers converged):
  Q1 → owner would show letters 1–2 to a customer; 3–5 "read like templates".
  Q3 → "a caseworker friend would say letters 3–5 don't cite the denial
       reason." Q5 → fix specificity first.
Hypotheses:
  H1: If playbook retrieval is made mandatory (fail loudly when empty), judge
      "specificity" improves — evidence: weak letters all skipped it.
      Impact H | Conf H | Cost 6 runs ≈ $2
  H2: If drafter prompt requires quoting the denial reason verbatim,
      specificity improves. Impact M | Conf M | Cost 4 runs ≈ $1.40
  H3 (cost, parked per priority order): cache playbook lookups.
E1 pre-declared → run → SUPPORTED (specificity +3,+2 on both variant runs;
groundedness guardrail held). Adopted. E2 queued.
```

**Why this works:** trace evidence (missing spans) turned a vibe ("generic")
into a mechanism hypothesis with High confidence; the cost idea was parked
because quality hypotheses remained.

## Example 2 — Kill-switch triggers mid-series

**Input:** "Keep going — try the tone rewrite next." (after E1–E3)

**Output:**
```
Kill-switch check before E4:
  E2 gain: +4% specificity. E3 gain: +2% specificity. Two consecutive <5%
  gains → quality dimension at diminishing returns.
  Remaining hypotheses (tone rewrite) : Impact L, expected lift ~2–3%,
  cost $3 + your review time.
  Plain numbers: we'd spend ~$3 to maybe move a metric 2% that customers
  haven't complained about.
STOPPING the series. Recommendation: bank the E1 win, revisit after 50 real
users produce new evidence. Logged to retro-log.md; memory-capture updated.
```

**Why this works:** the stop rule fired on the declared threshold, the
trade-off was stated in plain numbers, and stopping was framed as banking
wins — not giving up.

## Example 3 — NOT SUPPORTED, guardrail broke

**Input:** "I think a longer system prompt with more examples will fix the
shallow answers."

**Output:**
```
E2 for H2: add 3 worked examples to system prompt (one variable).
Pre-declared: Success = depth +2 on both runs; Guardrail = latency ≤ +20%,
cost ≤ +30%; Stop = 4 runs / $2.
Result: NOT SUPPORTED (directional, n=2). Depth +1, +0. Guardrail BROKE:
cost +85% per run (examples ballooned input tokens).
Decision: discard change. Learning captured: this agent's depth problem is
not example-starvation; queue hypothesis about retrieval quality instead.
Spend: $1.10 of $2.
```

**Why this works:** a broken guardrail forces discard even with a small
positive drift; the failed experiment still produced a sharper next
hypothesis — that's the point of the series.

## Example 4 — No observability yet

**Input:** "Retro my scheduling agent. I don't have any tracing set up."

**Output:**
```
Proceeding on outputs alone (5 saved transcripts). Interview run.
Hypotheses drafted but confidence capped at M — without traces we can't see
WHERE runs diverge (tool calls? retrieval? prompt?).
Recommendation logged: run agent-observability first (~30 min, free tier);
re-run this retro with trace evidence to unlock High-confidence hypotheses.
E1 (prompt-level, testable without traces) pre-declared and run anyway.
```

**Why this works:** the skill degrades gracefully — it still delivers value
without instrumentation, but is honest that hypothesis confidence is capped
and routes the user to the precondition skill.
