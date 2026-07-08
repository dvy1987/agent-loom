# agent-observability — Worked Examples

<!-- security-scanned SAFE 2026-07-08 -->

## Example 1 — Next.js + OpenAI SDK product, Langfuse Cloud path

**Input:** "Users say my study coach app sometimes gives nonsense plans. I
can't reproduce it. Stack is Next.js API routes calling the OpenAI SDK."

**Output:**
```
Primer: a trace = the full story of one request (model calls, tool calls,
timing, tokens, cost). We add a small library; it sends that story to a
managed service over HTTPS. Nothing runs on your machine.

Step 1 Scope: flow = generate-study-plan; ~800 requests/mo × ~6 spans = ~5k
spans/mo; data = student emails (PII — must mask).
Step 2 Backend: Langfuse Cloud free (50k units/mo ≫ 5k; framework-agnostic;
no LangChain dependency). Phoenix rejected: agent-graph depth not needed for
a single-flow app. LangSmith rejected: not a LangChain product.
Step 3 Instrument: langfuse OpenAI wrapper import swap + LANGFUSE_PUBLIC_KEY /
LANGFUSE_SECRET_KEY env vars on Vercel. session_id + user_id tags added.
Step 4 Verify: 1 live request → trace shows 6 spans, prompt + completion,
tokens (1,214 in / 502 out), cost $0.004. Email masked ✓ (tested with fake
address, not found in UI).
Step 5 Policy: failures 100%, successes 100% (volume ≪ cap); revisit at 30k.
Step 6 Wired: eval-pipeline samples 20 traces/week → eval-judge scores
plan-quality rubric. OBSERVABILITY.md saved; SKILL-OUTPUTS logged.
```

**Why this works:** backend chosen by free-tier math + framework fit, not
brand; PII masking verified with a planted fake value; volume math done
before promising "free".

## Example 2 — Redaction check catches a leak

**Input:** "Traces are flowing. Ship it?"

**Output:**
```
Step 4 spot-check: planted TEST-SECRET-123 in a request header → FOUND in
span attributes (http.request.headers captured by default).
BLOCKED. Fix: exclude header capture in instrumentor config; re-run planted
test → not found. Now shippable. Added to OBSERVABILITY.md: "header capture
disabled 2026-07-08; re-test after every instrumentation upgrade."
```

**Why this works:** the Hard Rule is enforced with a planted-value test, not
an assumption; the fix is recorded so the next agent re-tests after upgrades.

## Example 3 — Backend swap without touching app code

**Input:** "LangSmith free tier ran out mid-month and we're not really a
LangChain shop anymore. Move us."

**Output:**
```
Instrumentation audit: app emits OTel GenAI spans via @traceable shim → 80%
portable; 2 call sites use proprietary run-tree API → refactor to OTel first
(1 hour), otherwise the swap leaves holes.
Swap: new Langfuse keys → exporter env vars changed → first-trace
verification passed (span tree + costs visible). Old backend read-only for
14 days (its retention), then keys revoked.
Lesson recorded (learnings): instrument to the standard from day 1 — the two
proprietary call sites were the entire migration cost.
```

## Example 4 — Volume math rejects the naive plan

**Input:** "Just turn on 100% tracing for the 12-agent swarm."

**Output:**
```
Math: 5k showcase runs/mo × ~25 spans/run (12 agents + tools) = ~125k
spans/mo → 2.5× over the Langfuse free cap; 5× over Arize AX free.
Options presented: (a) failures 100% + successes 15% ≈ 44k spans → fits free;
(b) Braintrust free (1M spans) accepting closed-source + 30-day retention;
(c) paid Core tier ~$29/mo.
Chosen: (a) — quality debugging needs failures, not every success.
```

**Why this works:** the skill refuses to promise "free" before multiplying
spans-per-request by volume; sampling keeps the diagnostic value (failures)
while cutting the bill.
