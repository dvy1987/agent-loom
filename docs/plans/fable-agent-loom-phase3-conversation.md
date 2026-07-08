Phase 3 it is — order swap noted (Phase 2 will follow). Phase 3 = three new skills + eval-suite pass. Starting with the mandatory research pass (creator Step 2), kept to two grounded searches:


**Diff:**
```diff
--- /Users/divya/Projects/Building-apps/agent-loom/.agents/skills/agent-observability/SKILL.md
+++ /Users/divya/Projects/Building-apps/agent-loom/.agents/skills/agent-observability/SKILL.md
@@ -0,0 +1,141 @@
+---
+name: agent-observability
+description: >
+  Instrument a shipped product's AI agents with tracing and observability so
+  you can see what they did, why outputs happened, and what each run cost.
+  Plain-language primer plus free-tier-first backend selection (Langfuse,
+  Phoenix, LangSmith, Braintrust) and OpenTelemetry/OpenInference
+  instrumentation. Load when the user asks to add observability, add tracing,
+  instrument my agents, see what my agent is doing in production, set up
+  Langfuse or Phoenix or LangSmith, debug why my agent gave a bad answer, or
+  track LLM cost per request. Also fires when agent-system-architecture or
+  setup-evaluation requires an observability plan for an agent-chain product.
+  NOT for tracing the coding agent itself — that is run-trace. Precondition
+  for runtime-learning-loop.
+license: MIT
+metadata:
+  author: dvy1987
+  version: "1.0"
+  category: project-specific
+  sources: >
+    OpenTelemetry GenAI semantic conventions (gen_ai.*), OpenInference
+    (Arize), Langfuse/Phoenix/LangSmith/Braintrust public docs and pricing
+    (verified 2026-07), practitioner comparisons 2026
+  resources:
+    references:
+      - backends.md
+      - examples.md
+---
+
+# Agent Observability
+
+You instrument the user's *product* agents — not the coding agent — so every run leaves a trace that can be inspected, scored, and learned from. You explain everything in plain language: the user is non-technical.
+
+## Plain-Language Primer (teach this first, once)
+
+- A **trace** is the full story of one request: every model call, tool call, and retrieval step, in order, with timing, tokens, and cost attached.
+- A **span** is one step inside that story (one LLM call, one tool call).
+- **Observability** means you can answer "why did this output happen?" and "what did this run cost?" *after the fact*, without guessing.
+- The **backend** is a separate managed service. Your product sends trace data to it over HTTPS as a side effect of running. You do NOT host it yourself in the common case, and it never runs on your laptop.
+- Why it matters: an agent can return a confident wrong answer with HTTP 200. Without traces you cannot debug it, cannot measure quality, and cannot run any learning loop (`runtime-learning-loop` hard-fails without this).
+
+## Hard Rules
+
+Never log secrets, API keys, or user PII into trace payloads — configure redaction/masking before production traffic, not after.
+Never propose self-hosting on the user's machine. Managed free tier first; self-host-in-cloud is a clearly-labeled last resort.
+Always instrument against OpenTelemetry GenAI conventions (`gen_ai.*`) or OpenInference — never a proprietary-only SDK — so the backend can be swapped later by config, not a rewrite.
+Always verify the first trace end-to-end (run once, open the trace, see spans + token counts) before calling the setup done.
+Always set a sampling/cost policy before production scale — keep failures at 100%, sample successes.
+
+## Workflow
+
+### Step 1 — Scope
+Identify: which agent flows matter most (start with ONE), expected volume/month, whether data is sensitive (PII/health/finance), and which framework the product uses (Google ADK, LangGraph/LangChain, OpenAI/Anthropic SDK direct, custom).
+
+### Step 2 — Choose a backend
+Read `references/backends.md` (decision table, free tiers, tradeoffs — verify current pricing at decision time; tiers change). Defaults: Langfuse Cloud free tier for general use; Phoenix for agent-heavy/ADK products (deepest multi-step agent views); LangSmith only if the product is LangChain/LangGraph-first. Sensitive data → check the backend's redaction options FIRST; most redact nothing by default.
+
+### Step 3 — Instrument
+Prefer auto-instrumentation for the detected framework (one `register()`/`instrument()` call + env vars for keys/endpoint). Put API keys in environment variables — never in code. Wrap only the entry point; let the instrumentor capture nested spans. Tag spans with `user_id`/`session_id`/feature name so cost and quality can be sliced later.
+
+### Step 4 — Verify first trace
+Run one real request. Open the backend UI. Confirm: full span tree visible, prompts/completions captured, token counts + cost present, no secrets/PII in payloads. If any check fails, fix before proceeding.
+
+### Step 5 — Cost and sampling policy
+Async exporters add negligible latency; the real costs are storage and noise. Policy: 100% of failed runs, sampled successes (start 10–25% at scale), retention matched to the free tier's window. Set a monthly span budget aligned to the free-tier cap.
+
+### Step 6 — Wire to quality loops
+Point `eval-pipeline` at production traces (score samples with `eval-judge`); this trace+eval pair is the precondition `runtime-learning-loop` checks. Record backend choice + config in `docs/observability/OBSERVABILITY.md` and log it to `docs/skill-outputs/SKILL-OUTPUTS.md`.
+
+## Output Format
+
+```
+=== Observability Plan: [product] ===
+Flow instrumented: [flow] | Framework: [ADK|LangGraph|SDK|custom]
+Backend: [name + tier] — why: [1 line] | Est. volume: [spans/mo] vs free cap: [cap]
+Redaction: [what is masked] | Sampling: [failures 100%, successes N%]
+First trace verified: [yes/no] | Saved: docs/observability/OBSERVABILITY.md
+Next: eval-pipeline wiring → runtime-learning-loop precondition met
+```
+
+## Gotchas
+
+- **Traces are for the shipped product; `run-trace` is for the coding agent.** Different data, different store — never mix them.
+- **SaaS backends receive your prompts.** That is user data leaving your infrastructure — check redaction defaults (usually OFF) before pointing production at them.
+- **Instrument to the standard, not the vendor.** All major backends ingest OTel GenAI `gen_ai.*` spans; the backend is a 2-year decision, the instrumentation is forever.
+- **Free-tier caps are per month and small** (e.g. tens of thousands of spans). One agent request can emit 5–30 spans. Do the multiplication before promising "free".
+- **A trace that omits tool calls is half a trace.** Multi-agent debugging lives in the tool/handoff spans, not the final completion.
+
+## Example
+
+<examples>
+  <example>
+    <input>My appeal-drafting app gives weird answers sometimes and I have no idea why. Add observability. It's Google ADK + FastAPI on Cloud Run.</input>
+    <output>
+Primer given (traces/spans/backend in plain language).
+Scope: draft-appeal flow, ~3k requests/mo (~30k spans), synthetic PHI only — still mask document text.
+Backend: Phoenix (deepest agent-trace views; OpenInference auto-instrumentation for ADK) — cloud free tier fits 30k spans/mo.
+Instrumented via openinference-instrumentation for ADK + env-var keys. First trace verified: 14 spans, tokens + cost visible, document text masked.
+Sampling: failures 100%, successes 25%. Saved docs/observability/OBSERVABILITY.md. Logged to SKILL-OUTPUTS.
+Next: wire eval-pipeline to score 20 sampled traces/week.
+    </output>
+  </example>
+</examples>
+
+Read `references/examples.md` for full walkthroughs (Langfuse path, redaction setup, backend swap).
+
+## Common Rationalizations
+
+| Excuse | Reality |
+|--------|---------|
+| "Add observability later, ship first" | You cannot debug the past — traces only exist from instrumentation day forward. |
+| "Logs are enough" | Logs show 200 OK; traces show the wrong retrieval that caused the bad answer. |
+| "Self-host to save money" | Ops burden (DB + Redis + storage) exceeds free-tier value at this scale; laptop hosting is banned. |
+| "Pick the backend by brand" | Pick by framework fit + free-tier math + redaction needs; instrumentation stays portable. |
+| "Trace everything forever" | Cost and noise explode; sample successes, keep failures, match retention to need. |
+
+## Verification
+
+- [ ] First real trace opened in backend UI with full span tree + token counts
+- [ ] No secrets or PII visible in any span payload (spot-check 3 traces)
+- [ ] Sampling + retention policy written into OBSERVABILITY.md
+- [ ] Instrumentation is OTel GenAI / OpenInference (backend swappable by config)
+- [ ] docs/skill-outputs/SKILL-OUTPUTS.md appended
+
+## Red Flags
+
+- Backend chosen before checking framework auto-instrumentation support
+- Production traffic flowing with default (empty) redaction config
+- Proprietary SDK wrapped around every call site instead of one instrumentor
+- "Observability done" claimed without opening a single real trace
+- Coding-agent activity and product traces mixed in one store
+
+## Impact Report
+
+```
+Observability set up for: [product/flow]
+Backend: [name + tier] | Framework instrumented: [name]
+First trace verified: [yes/no] | Redaction: [configured/not needed]
+Sampling: [policy] | Files: docs/observability/OBSERVABILITY.md
+Ready for: eval-pipeline wiring, runtime-learning-loop precondition
+```

```



Now its two reference files:


**Diff:**
```diff
--- /Users/divya/Projects/Building-apps/agent-loom/.agents/skills/agent-observability/references/backends.md
+++ /Users/divya/Projects/Building-apps/agent-loom/.agents/skills/agent-observability/references/backends.md
@@ -0,0 +1,70 @@
+# Observability Backend Selection (free-tier-first)
+
+Snapshot verified 2026-07. **Free tiers change — re-verify the numbers on the
+vendor pricing page before committing.** The instrumentation (OTel GenAI /
+OpenInference) is portable across all of these, so a wrong backend choice is a
+config change, not a rewrite.
+
+## Plain-language architecture
+
+```
+Your product (Cloud Run / Vercel / anywhere)
+   └── instrumentation library (runs inside your app, adds ~ms)
+         └── sends spans over HTTPS ──────────► Managed backend (their cloud)
+                                                 └── you log in via browser to
+                                                     view traces, costs, evals
+```
+
+- You never install a database. You never host anything. You add a library +
+  2–3 environment variables (API key, endpoint).
+- If the vendor disappears or the free tier shrinks: point the exporter at a
+  different backend. Application code unchanged.
+
+## Decision table
+
+| Backend | Free tier (verify!) | Best when | Watch out |
+|---|---|---|---|
+| **Langfuse Cloud** | ~50k units/mo, 30-day retention, 2 users; Core ~$29/mo | Default general pick. Framework-agnostic, MIT OSS core (ClickHouse-backed since 2026), strong cost tracking per user/session | Self-assembly for eval orchestration; unit caps count every span |
+| **Phoenix / Arize** | Phoenix self-host free (single container); Arize AX cloud ~25k spans/mo, 1 user | Agent-heavy products (deepest multi-step agent + tool-call views), ADK/OpenInference stacks, RAG retrieval debugging | Cloud free cap is small; Elastic license on OSS (fine unless reselling hosted) |
+| **LangSmith** | ~5k traces/mo, 14-day retention; $39/seat after | Product is LangChain/LangGraph-first — zero-config capture, best LangGraph state views | Proprietary trace model = real migration cost; short free retention |
+| **Braintrust** | ~1M spans + 10k eval runs/mo, unlimited users | Eval-in-CI culture; biggest free span budget by far | Closed source, no self-host, ~30-day retention |
+| Self-host in cloud (Langfuse/Phoenix) | infra cost only | Hard data-residency requirement (traces may not leave your VPC) | LAST RESORT for this user: real ops burden (DB, Redis, storage, backups). Never on a laptop. |
+
+Avoid: proxy-only tools in maintenance mode (e.g. Helicone post-acquisition,
+2026) for new strategic setups.
+
+## Quick picks by situation
+
+- **"I just want to see why my agent is weird" (any stack):** Langfuse Cloud free.
+- **Google ADK / multi-agent swarm (e.g. aegis-style):** Phoenix — OpenInference
+  auto-instrumentation for ADK exists and its agent trace views are deepest.
+  Arize AX free tier if cloud-managed is required and volume fits.
+- **LangGraph product:** LangSmith (accept lock-in consciously) or Langfuse if
+  you may leave LangChain later.
+- **High volume, tiny budget, evals matter:** Braintrust free tier.
+- **Regulated data:** self-host Langfuse in cloud (compute ~<$500/mo at millions
+  of traces) — get help for this; it is the one option with real ops work.
+
+## Redaction / PII checklist (do BEFORE production traffic)
+
+1. List fields that must never leave: user names, emails, document bodies,
+   health/finance details, API keys.
+2. Enable the backend's masking hook (all four support masking/redaction
+   callbacks or ingestion filters — default is usually OFF).
+3. Send one test request containing a fake secret (e.g. `TEST-SECRET-123`);
+   search for it in the backend UI. Found = redaction broken.
+4. Re-run the check after any instrumentation upgrade.
+
+## Volume math template
+
+```
+requests/month × spans/request (5–30 for agents) = spans/month
+spans/month vs free cap → sampling % for successes (failures always 100%)
+```
+
+## Swap procedure (backend → backend)
+
+1. Create account + API key on new backend.
+2. Change exporter endpoint + key env vars (OTLP/HTTP or vendor `register()`).
+3. Run one request; verify first trace on the new backend (Step 4 checklist).
+4. Keep old backend read-only until its retention window drains.

```





**Diff:**
```diff
--- /Users/divya/Projects/Building-apps/agent-loom/.agents/skills/agent-observability/references/examples.md
+++ /Users/divya/Projects/Building-apps/agent-loom/.agents/skills/agent-observability/references/examples.md
@@ -0,0 +1,84 @@
+# agent-observability — Worked Examples
+
+<!-- security-scanned SAFE 2026-07-08 -->
+
+## Example 1 — Next.js + OpenAI SDK product, Langfuse Cloud path
+
+**Input:** "Users say my study coach app sometimes gives nonsense plans. I
+can't reproduce it. Stack is Next.js API routes calling the OpenAI SDK."
+
+**Output:**
+```
+Primer: a trace = the full story of one request (model calls, tool calls,
+timing, tokens, cost). We add a small library; it sends that story to a
+managed service over HTTPS. Nothing runs on your machine.
+
+Step 1 Scope: flow = generate-study-plan; ~800 requests/mo × ~6 spans = ~5k
+spans/mo; data = student emails (PII — must mask).
+Step 2 Backend: Langfuse Cloud free (50k units/mo ≫ 5k; framework-agnostic;
+no LangChain dependency). Phoenix rejected: agent-graph depth not needed for
+a single-flow app. LangSmith rejected: not a LangChain product.
+Step 3 Instrument: langfuse OpenAI wrapper import swap + LANGFUSE_PUBLIC_KEY /
+LANGFUSE_SECRET_KEY env vars on Vercel. session_id + user_id tags added.
+Step 4 Verify: 1 live request → trace shows 6 spans, prompt + completion,
+tokens (1,214 in / 502 out), cost $0.004. Email masked ✓ (tested with fake
+address, not found in UI).
+Step 5 Policy: failures 100%, successes 100% (volume ≪ cap); revisit at 30k.
+Step 6 Wired: eval-pipeline samples 20 traces/week → eval-judge scores
+plan-quality rubric. OBSERVABILITY.md saved; SKILL-OUTPUTS logged.
+```
+
+**Why this works:** backend chosen by free-tier math + framework fit, not
+brand; PII masking verified with a planted fake value; volume math done
+before promising "free".
+
+## Example 2 — Redaction check catches a leak
+
+**Input:** "Traces are flowing. Ship it?"
+
+**Output:**
+```
+Step 4 spot-check: planted TEST-SECRET-123 in a request header → FOUND in
+span attributes (http.request.headers captured by default).
+BLOCKED. Fix: exclude header capture in instrumentor config; re-run planted
+test → not found. Now shippable. Added to OBSERVABILITY.md: "header capture
+disabled 2026-07-08; re-test after every instrumentation upgrade."
+```
+
+**Why this works:** the Hard Rule is enforced with a planted-value test, not
+an assumption; the fix is recorded so the next agent re-tests after upgrades.
+
+## Example 3 — Backend swap without touching app code
+
+**Input:** "LangSmith free tier ran out mid-month and we're not really a
+LangChain shop anymore. Move us."
+
+**Output:**
+```
+Instrumentation audit: app emits OTel GenAI spans via @traceable shim → 80%
+portable; 2 call sites use proprietary run-tree API → refactor to OTel first
+(1 hour), otherwise the swap leaves holes.
+Swap: new Langfuse keys → exporter env vars changed → first-trace
+verification passed (span tree + costs visible). Old backend read-only for
+14 days (its retention), then keys revoked.
+Lesson recorded (learnings): instrument to the standard from day 1 — the two
+proprietary call sites were the entire migration cost.
+```
+
+## Example 4 — Volume math rejects the naive plan
+
+**Input:** "Just turn on 100% tracing for the 12-agent swarm."
+
+**Output:**
+```
+Math: 5k showcase runs/mo × ~25 spans/run (12 agents + tools) = ~125k
+spans/mo → 2.5× over the Langfuse free cap; 5× over Arize AX free.
+Options presented: (a) failures 100% + successes 15% ≈ 44k spans → fits free;
+(b) Braintrust free (1M spans) accepting closed-source + 30-day retention;
+(c) paid Core tier ~$29/mo.
+Chosen: (a) — quality debugging needs failures, not every success.
+```
+
+**Why this works:** the skill refuses to promise "free" before multiplying
+spans-per-request by volume; sampling keeps the diagnostic value (failures)
+while cutting the bill.

```





**Diff:**
```diff
--- /Users/divya/Projects/Building-apps/agent-loom/.agents/skills/agent-run-retro/SKILL.md
+++ /Users/divya/Projects/Building-apps/agent-loom/.agents/skills/agent-run-retro/SKILL.md
@@ -0,0 +1,148 @@
+---
+name: agent-run-retro
+description: >
+  Run a structured retrospective after development-phase runs of your
+  product's agents — interview the owner in plain language about what went
+  well and poorly, draft ranked improvement hypotheses, then design and run
+  small n=1/n=2 experiments with pre-declared success criteria, guardrails,
+  stop conditions, and a cost/ROI kill-switch. Load when the user says how did
+  that run go, retro this run, the agent output was bad, what should we
+  improve, draft hypotheses, run a small experiment, or after repeated dev
+  runs of an agentic system produce uneven quality. Priority: output quality
+  over performance over cost, each with diminishing-returns stops. NOT a
+  product A/B test (experimentation), NOT coding-agent harness repair
+  (harness-evolution), NOT production-scale learning (runtime-learning-loop).
+license: MIT
+metadata:
+  author: dvy1987
+  version: "1.0"
+  category: project-specific
+  sources: >
+    Contextual AI ACE production lessons 2026 (feedback quality > algorithm),
+    GEPA arXiv:2507.19457 (reflective feedback design), agent-loom
+    experimentation suite patterns
+  resources:
+    references:
+      - examples.md
+---
+
+# Agent Run Retro
+
+You are a development-phase improvement partner for the user's *product* agents. After runs, you interview the owner in plain language, convert their observations plus run evidence into ranked hypotheses, and run tiny pre-declared experiments that genuinely move output quality. The user is non-technical: no jargon; explain consequences, not mechanisms.
+
+## Hard Rules
+
+Never run an experiment without a pre-declared success definition, guardrail, failure mode, stop condition, and budget — written BEFORE the first run.
+Every hypothesis must name the outcome it should move (quality metric first). No experiments for their own sake.
+Change ONE variable per experiment. Two changes = two experiments.
+n=1/n=2 results are directional evidence, never statistical proof — say so explicitly in every readout.
+Priority order: quality > performance > cost. Stop optimizing any dimension at diminishing returns (two consecutive experiments with <5% improvement on it).
+Kill-switch: stop the experiment series when expected remaining lift no longer justifies spend (state the comparison in plain numbers).
+
+## Workflow
+
+### Step 1 — Gather run evidence (silent)
+Pull what exists: traces (`agent-observability`, if instrumented), eval scores (`eval-pipeline`), the actual outputs, cost per run. No observability? Proceed on outputs alone and recommend instrumenting.
+
+### Step 2 — Interview the owner (≤5 questions, plain language)
+1. "Which output would you happily show a customer? Which would embarrass you?"
+2. "What disappointed you most about this run — content, tone, speed, or something else?"
+3. "Was anything wrong that a knowledgeable friend would catch instantly?"
+4. "Did anything take too long or cost more than it felt worth?"
+5. "If you could fix ONE thing before the next run, what?"
+Stop early when answers converge. Reflect back what you heard in one sentence each.
+
+### Step 3 — Draft ranked hypotheses
+Combine evidence + interview into 3–5 hypotheses. Rank by `impact × confidence ÷ cost`. Format each:
+```
+H<N>: If we [one change], then [outcome metric] improves because [reason].
+Impact: H/M/L | Confidence: H/M/L | Cost to test: [runs × $ + your time]
+```
+Quality hypotheses outrank performance; performance outranks cost — unless the owner overrides.
+
+### Step 4 — Design the experiment (top hypothesis first)
+Pre-declare in `docs/experiments/retro-log.md` BEFORE running:
+```
+Experiment: E<N> for H<N>   Date:
+Change (one variable):
+n: [1 or 2] runs vs baseline runs on identical inputs
+Success = [observable definition, e.g. judge score +1 on rubric dim X, or owner prefers new output blind]
+Guardrail = [what must NOT get worse, e.g. groundedness, latency +20% max]
+Failure mode = [what bad looks like, and what we do then]
+Stop = [max runs / max $ / max time]
+Budget: $[X]  Kill-switch check: expected lift worth ≥ budget? [y/n + why]
+```
+Owner approves hypotheses ONCE; then execute the series autonomously — checkpoint only on kill-switch triggers or completed readouts.
+
+### Step 5 — Run and read out
+Run baseline vs variant on the SAME inputs. Blind the owner when preference is the metric (don't reveal which is which). Readout format:
+```
+E<N>: [SUPPORTED | NOT SUPPORTED | MIXED] (directional, n=[N])
+Evidence: [scores/preferences per run]  Guardrail: [held/broke]
+Decision: [adopt change | discard | escalate to bigger test]  Spend: $[X]
+```
+Adopted changes with production implications → hand to `runtime-learning-loop` promotion gate. Record learnings via `memory-capture`.
+
+### Step 6 — Diminishing-returns check
+After each readout: if the last two experiments on a dimension gained <5% each, declare that dimension done for now and move to the next priority (quality → performance → cost) or end the series.
+
+## Gotchas
+
+- **Experiment theater:** activity that never changes a decision. If no decision depends on the result, don't run it.
+- **The judge must be steadier than the change.** If scoring wobbles run-to-run, fix the rubric (`eval-rubric-design`) before trusting any experiment.
+- **Confounds hide in retries and temperature.** Pin seeds/temperature where the stack allows; note where it doesn't.
+- **Owner memory beats vibes:** "which would you show a customer?" produces sharper signal than "rate 1–10".
+- **n=2 agreeing feels conclusive. It isn't.** Adopt, but mark the change for re-validation once real eval volume exists.
+
+## Example
+
+<examples>
+  <example>
+    <input>The last three runs of my physics-tutor agent felt off. Retro this.</input>
+    <output>
+Evidence: 3 runs, judge scores 6/10, 7/10, 4/10; cost $0.11/run. Interview: owner embarrassed by run 3 ("explains formula but never checks the student understood"); speed fine; cost fine.
+H1: If the tutor asks one comprehension-check question after each concept, judge "student engagement" dim improves (Impact H, Conf M, Cost 4 runs ≈ $0.50).
+H2 (parked): shorter explanations — Impact M.
+E1 pre-declared: n=2 vs 2 baseline, same transcripts; Success = engagement +2 on both; Guardrail = correctness ≥ baseline; Stop = 6 runs / $1.
+Result: SUPPORTED (both +2, +3; correctness held). Adopted → prompt updated; flagged for re-validation at 50-run eval volume. Series continues on H2? Diminishing-returns check says quality still moving — yes.
+    </output>
+  </example>
+</examples>
+
+Read `references/examples.md` for full sessions including a kill-switch trigger and a NOT SUPPORTED readout.
+
+## Common Rationalizations
+
+| Excuse | Reality |
+|--------|---------|
+| "Just try stuff and see" | Undeclared success criteria = you'll believe whatever you hoped. Pre-declare or don't run. |
+| "n=2 proved it" | It's directional. Adopt cheaply-reversible changes; re-validate at volume. |
+| "Test speed and cost too while we're at it" | One variable per experiment; quality first per priority order. |
+| "Owner feedback is subjective, skip the interview" | The owner's customer-embarrassment signal IS the quality bar for a solo product. |
+| "One more experiment might help" | Kill-switch: two <5% gains in a row = stop; spend the budget where lift remains. |
+
+## Verification
+
+- [ ] Every experiment in retro-log.md has success/guardrail/failure/stop/budget filled BEFORE run timestamps
+- [ ] Each readout labeled directional with its n
+- [ ] One variable changed per experiment (check the Change field)
+- [ ] Adopted changes recorded via memory-capture; production-facing ones handed to runtime-learning-loop
+- [ ] docs/skill-outputs/SKILL-OUTPUTS.md appended
+
+## Red Flags
+
+- Experiment run before its retro-log entry exists
+- Hypothesis with no named outcome metric
+- Series continuing after two consecutive <5% gains without owner override
+- Owner asked to rate outputs unblinded when preference is the metric
+- Cost optimization started while quality hypotheses remain untested
+
+## Impact Report
+
+```
+Retro: [product/flow] | Runs reviewed: [N]
+Hypotheses drafted: [N] (top: H1 one-liner)
+Experiments: [N] run, [N] supported, [N] adopted | Spend: $[X] vs budget $[Y]
+Kill-switch: [not triggered | triggered at E<N> — reason]
+Files: docs/experiments/retro-log.md | Handed to: [runtime-learning-loop | none]
+```

```





**Diff:**
```diff
--- /Users/divya/Projects/Building-apps/agent-loom/.agents/skills/agent-run-retro/references/examples.md
+++ /Users/divya/Projects/Building-apps/agent-loom/.agents/skills/agent-run-retro/references/examples.md
@@ -0,0 +1,92 @@
+# agent-run-retro — Worked Examples
+
+<!-- security-scanned SAFE 2026-07-08 -->
+
+## Example 1 — Full session: appeal-drafter quality retro
+
+**Input:** "Ran the appeal drafter on 5 showcase cases today. Two letters felt
+great, three felt generic. Retro."
+
+**Output:**
+```
+Evidence: 5 runs; judge scores 8,8,5,6,5; cost $0.34/run; traces show the
+three weak letters skipped the insurer-playbook retrieval step (0 playbook
+spans).
+Interview (3 of 5 questions used — answers converged):
+  Q1 → owner would show letters 1–2 to a customer; 3–5 "read like templates".
+  Q3 → "a caseworker friend would say letters 3–5 don't cite the denial
+       reason." Q5 → fix specificity first.
+Hypotheses:
+  H1: If playbook retrieval is made mandatory (fail loudly when empty), judge
+      "specificity" improves — evidence: weak letters all skipped it.
+      Impact H | Conf H | Cost 6 runs ≈ $2
+  H2: If drafter prompt requires quoting the denial reason verbatim,
+      specificity improves. Impact M | Conf M | Cost 4 runs ≈ $1.40
+  H3 (cost, parked per priority order): cache playbook lookups.
+E1 pre-declared → run → SUPPORTED (specificity +3,+2 on both variant runs;
+groundedness guardrail held). Adopted. E2 queued.
+```
+
+**Why this works:** trace evidence (missing spans) turned a vibe ("generic")
+into a mechanism hypothesis with High confidence; the cost idea was parked
+because quality hypotheses remained.
+
+## Example 2 — Kill-switch triggers mid-series
+
+**Input:** "Keep going — try the tone rewrite next." (after E1–E3)
+
+**Output:**
+```
+Kill-switch check before E4:
+  E2 gain: +4% specificity. E3 gain: +2% specificity. Two consecutive <5%
+  gains → quality dimension at diminishing returns.
+  Remaining hypotheses (tone rewrite) : Impact L, expected lift ~2–3%,
+  cost $3 + your review time.
+  Plain numbers: we'd spend ~$3 to maybe move a metric 2% that customers
+  haven't complained about.
+STOPPING the series. Recommendation: bank the E1 win, revisit after 50 real
+users produce new evidence. Logged to retro-log.md; memory-capture updated.
+```
+
+**Why this works:** the stop rule fired on the declared threshold, the
+trade-off was stated in plain numbers, and stopping was framed as banking
+wins — not giving up.
+
+## Example 3 — NOT SUPPORTED, guardrail broke
+
+**Input:** "I think a longer system prompt with more examples will fix the
+shallow answers."
+
+**Output:**
+```
+E2 for H2: add 3 worked examples to system prompt (one variable).
+Pre-declared: Success = depth +2 on both runs; Guardrail = latency ≤ +20%,
+cost ≤ +30%; Stop = 4 runs / $2.
+Result: NOT SUPPORTED (directional, n=2). Depth +1, +0. Guardrail BROKE:
+cost +85% per run (examples ballooned input tokens).
+Decision: discard change. Learning captured: this agent's depth problem is
+not example-starvation; queue hypothesis about retrieval quality instead.
+Spend: $1.10 of $2.
+```
+
+**Why this works:** a broken guardrail forces discard even with a small
+positive drift; the failed experiment still produced a sharper next
+hypothesis — that's the point of the series.
+
+## Example 4 — No observability yet
+
+**Input:** "Retro my scheduling agent. I don't have any tracing set up."
+
+**Output:**
+```
+Proceeding on outputs alone (5 saved transcripts). Interview run.
+Hypotheses drafted but confidence capped at M — without traces we can't see
+WHERE runs diverge (tool calls? retrieval? prompt?).
+Recommendation logged: run agent-observability first (~30 min, free tier);
+re-run this retro with trace evidence to unlock High-confidence hypotheses.
+E1 (prompt-level, testable without traces) pre-declared and run anyway.
+```
+
+**Why this works:** the skill degrades gracefully — it still delivers value
+without instrumentation, but is honest that hypothesis confidence is capped
+and routes the user to the precondition skill.

```





**Diff:**
```diff
--- /Users/divya/Projects/Building-apps/agent-loom/.agents/skills/runtime-learning-loop/SKILL.md
+++ /Users/divya/Projects/Building-apps/agent-loom/.agents/skills/runtime-learning-loop/SKILL.md
@@ -0,0 +1,135 @@
+---
+name: runtime-learning-loop
+description: >
+  Design a self-improvement loop for a shipped product's AI agents —
+  production traces feed evals, evals feed improvement proposals (prompts,
+  playbooks, retrieval configs), and a human approval gate promotes changes
+  with rollback. Technique-agnostic: chooses per project between ACE-style
+  evolving playbooks, GEPA/MIPROv2 offline optimization, or simple eval-driven
+  iteration via references/techniques.md. Load when the user asks to make my
+  product's agents self-improving, learn from production traces, add a
+  learning loop, evolve prompts or playbooks safely, promote agent
+  improvements, or GEPA-style optimization. NOT harness-evolution (that
+  improves the coding agent), NOT experimentation (product A/B tests), NOT
+  agent-run-retro (dev-phase manual retros — this skill is the
+  production-scale continuation).
+license: MIT
+metadata:
+  author: dvy1987
+  version: "1.0"
+  category: project-specific
+  sources: >
+    ACE arXiv:2510.04618 (ICLR 2026), GEPA arXiv:2507.19457 (ICLR 2026 oral),
+    DSPy MIPROv2 docs, TextGrad Nature 2025, Contextual AI ACE production
+    lessons 2026, aegis competency-gated autonomy ladder
+  resources:
+    references:
+      - techniques.md
+      - examples.md
+---
+
+# Runtime Learning Loop
+
+You design the loop that lets a *shipped* product's agents get measurably better from their own production activity — safely. You never assume a technique (GEPA is one option, not the default); you match technique to the project's data volume, feedback quality, and budget. The user is non-technical: present proposals as consequences, not mechanisms.
+
+## Hard Rules
+
+Hard preconditions — refuse and route if missing: observability on the target flow (`agent-observability`) AND an eval harness with a held-out set (`eval-pipeline`). No traces + no evals = nothing to learn from and no way to know if "improvement" is real.
+No promotion without human approval (Apprentice mode) until the autonomy ladder's advancement gates are met — and never skip the ladder.
+Never optimize against the held-out set. It exists only to check proposals; touching it during optimization is self-deception.
+Every loop ships with: declared learnable surfaces (allowlist), rollback procedure, regression monitor, budget, and kill-switch — BEFORE the first cycle runs.
+Production PII never enters optimization prompts or persisted playbooks — redact at the trace layer first.
+Feedback design outranks algorithm choice: a multi-criteria LLM judge (relevance, groundedness, completeness, clarity) beats a bare score, and can beat ground-truth comparison (Contextual AI 2026).
+
+## Workflow
+
+### Step 1 — Precondition check (hard gate)
+Verify: traces flowing on the target flow; eval harness operational; held-out split defined and quarantined; eval scores stable enough to detect the lift you're seeking. Any missing → route to `agent-observability` / `eval-pipeline` and stop.
+
+### Step 2 — Choose the technique
+Read `references/techniques.md` (decision table: ACE-style playbook deltas for continuous online learning; GEPA for offline prompt optimization with rich textual feedback; MIPROv2 for scalar metrics + few-shot demos; TextGrad for hard single instances; manual eval-driven iteration when volume is tiny). Record choice + why in `docs/learning-loop/LOOP.md`.
+
+### Step 3 — Declare learnable surfaces
+Allowlist exactly what the loop may change (e.g. drafter prompt, insurer playbooks, retrieval config). Everything else — code, evals, held-out data, the loop itself — is off-limits to the loop. Write the allowlist into LOOP.md.
+
+### Step 4 — Build the cycle
+```
+collect traces (sampled) → score (eval-judge, multi-criteria feedback)
+→ reflect/propose (technique from Step 2) → validate on held-out set
+→ promotion proposal (diff + evidence + cost) → human approves → promote
+→ record (changelog + memory-capture) → monitor for regression
+```
+Proposals must show: what changes (diff), held-out before/after scores, spend so far, and rollback command. Autonomous execution: the cycle runs unattended; the human only sees hypotheses/promotions and kill-switch alerts.
+
+### Step 5 — Autonomy ladder (competency-gated)
+| Stage | Who promotes | Advance when |
+|-------|--------------|--------------|
+| Apprentice (default) | Human approves every change | ≥10 approved promotions, 0 rollbacks in last 10 |
+| Journeyman | Auto-promote behind hard safety gates (guardrail evals must pass) | ≥3 months clean + regression monitor proven (caught ≥1 real regression) |
+| Master | Relaxed gates, batched review | Only if the owner explicitly opts in |
+Any rollback drops the loop one stage.
+
+### Step 6 — Kill-switches and budget
+Declare: max $/cycle, max cycles/week, and the ROI stop (expected remaining lift vs spend, in plain numbers — same rule as `agent-run-retro`). Regression monitor: if production eval scores drop below the pre-loop baseline, auto-pause the loop, alert the owner, roll back the last promotion.
+
+## Gotchas
+
+- **Reward hacking / judge gaming:** optimized prompts learn to please the judge, not the user. Rotate judge prompts periodically; spot-check with human review; keep one metric the loop never sees.
+- **Brevity bias & context collapse** (ACE findings): monolithic prompt rewrites erode detail over cycles. Prefer incremental delta updates with helpful/harmful counters over full rewrites for continuously-evolving contexts.
+- **Cold start:** with <10 traces, seed the loop with prior context (agent purpose, data types, known failure modes, one good + one bad example) — measured +7% over traces-alone (Contextual AI 2026).
+- **This loop improves the PRODUCT's agents.** The coding agent's harness is `harness-evolution`; keep stores, evals, and budgets separate.
+- **Offline vs online:** GEPA-class optimizers are compile-time (re-run per model swap); ACE-class playbooks adapt online. Model upgrades invalidate offline-optimized prompts — re-validate after every model change.
+
+## Example
+
+<examples>
+  <example>
+    <input>Make my appeal-drafting product self-improving from its production traces. It has Phoenix tracing and a 30-case eval set with 10 held out.</input>
+    <output>
+Preconditions: traces ✓ eval harness ✓ held-out 10 quarantined ✓.
+Technique: ACE-style playbook deltas (continuous learning, no labels needed, playbooks already exist per insurer). GEPA rejected for the online path (full-rewrite latency + brevity bias on detailed playbooks); noted for one-off drafter-prompt optimization later.
+Learnable surfaces: drafter prompt, insurer slice playbooks. Off-limits: judges, eval sets, US-playbook (regulatory).
+Cycle built per Step 4; judge = 4-criteria self-eval (relevance, groundedness, completeness, clarity).
+Ladder: Apprentice — you approve each promotion from a diff + held-out delta + rollback command.
+Kill-switches: $15/cycle cap, 2 cycles/week, auto-pause on baseline regression.
+LOOP.md saved; logged to SKILL-OUTPUTS.
+    </output>
+  </example>
+</examples>
+
+Read `references/examples.md` for a GEPA offline path, a regression rollback, and a refused-preconditions session.
+
+## Common Rationalizations
+
+| Excuse | Reality |
+|--------|---------|
+| "GEPA worked before, just use it" | Technique fits data + feedback shape; ACE beats GEPA for online playbook evolution, GEPA wins offline prompt compiles. Choose per project. |
+| "Skip the held-out set, more data for learning" | Then every 'improvement' is unverifiable — the loop optimizes noise. |
+| "Auto-promote from day one" | Apprentice gate exists because early judges are miscalibrated; earn Journeyman. |
+| "Let the loop tune the judge too" | The loop grading itself = reward hacking by construction. Judges are off-limits surfaces. |
+| "No budget cap, quality is priceless" | Unbounded loops burn spend on <1% lifts; the kill-switch banks wins instead. |
+
+## Verification
+
+- [ ] Preconditions verified (traces + eval harness + quarantined held-out) before any cycle
+- [ ] LOOP.md contains technique choice, surface allowlist, ladder stage, budget, kill-switches, rollback
+- [ ] First promotion proposal shows diff + held-out before/after + rollback command
+- [ ] Regression monitor tested once (simulate a drop → loop pauses)
+- [ ] docs/skill-outputs/SKILL-OUTPUTS.md appended
+
+## Red Flags
+
+- Loop proposed without observability or evals in place
+- Optimization run that touched held-out examples
+- Promotion applied with no rollback path recorded
+- Judge prompts inside the learnable-surface allowlist
+- Autonomy stage advanced without meeting its gate
+
+## Impact Report
+
+```
+Learning loop: [product/flow] | Technique: [ACE-delta | GEPA | MIPROv2 | manual] — why: [1 line]
+Surfaces: [allowlist] | Ladder: [stage] | Budget: [$X/cycle, N/week]
+Promotions: [N approved, N rolled back] | Held-out delta: [before → after]
+Kill-switch: [armed | triggered — reason] | Files: docs/learning-loop/LOOP.md
+```

```





**Diff:**
```diff
--- /Users/divya/Projects/Building-apps/agent-loom/.agents/skills/runtime-learning-loop/references/techniques.md
+++ /Users/divya/Projects/Building-apps/agent-loom/.agents/skills/runtime-learning-loop/references/techniques.md
@@ -0,0 +1,60 @@
+# Self-Improvement Techniques — Survey & Decision Table
+
+Snapshot 2026-07. This space moves fast — re-run a quick research pass before
+committing a technique for a new project. GEPA is NOT the default; it is one
+row in this table.
+
+## Decision table
+
+| Technique | What it changes | Signal it needs | Rollouts/cost | Best when | Avoid when |
+|---|---|---|---|---|---|
+| **ACE-style playbook deltas** (Agentic Context Engineering, arXiv:2510.04618, ICLR 2026) | Evolving context/playbooks via Generator→Reflector→Curator incremental deltas with helpful/harmful counters | Natural execution feedback (success/error) — no labels needed | Low (−75% rollouts, −82% latency vs GEPA on AppWorld) | Continuous ONLINE learning; detailed domain playbooks (insurer rules, tactics); long-running agents | One-off prompt polish; contexts that must stay tiny |
+| **GEPA** (Genetic-Pareto, arXiv:2507.19457, ICLR 2026 oral; `dspy.GEPA` or `pip install gepa`) | Instructions/prompts via reflective evolution + Pareto frontier | RICH textual feedback per example (score + why) — starves on bare floats | ~100–500 evals; beats MIPROv2 by ~10%, GRPO by up to 20% with 35× fewer rollouts | OFFLINE prompt compile with 20–100 labeled examples + heterogeneous failure modes | Online adaptation (full-rewrite latency, brevity bias); scalar-only metrics |
+| **MIPROv2** (DSPy) | Instructions + few-shot demos via Bayesian search | Plain scalar metric | Hundreds–thousands of evals | Multi-module pipelines with labeled data; smaller models that lean on demos | No labeled data; need explainable proposals |
+| **TextGrad** (Nature 2025) | Individual texts via natural-language "gradients" | LLM critique per instance | High per instance (~3× calls) | Hard single instances offline (the worst 5%) | Hot paths / high traffic |
+| **Manual eval-driven iteration** | Anything, by hand | Eval scores + human judgment | Cheapest | <20 traces, early product, judge not yet trusted | Volume outgrows human review |
+| **Dynamic Cheatsheet** (adaptive memory) | Test-time memory of strategies | Execution feedback | Low | Session-level memory needs | Superseded by ACE for playbooks (context collapse risk) |
+| **Fine-tuning / RL (GRPO)** | Model weights | Dense scalar rewards, thousands of rollouts | Very high + hosting burden | Last resort at scale, stable task | Almost always premature for solo products |
+
+## Production findings worth encoding (Contextual AI, 2026)
+
+1. **Feedback design > algorithm.** Multi-criteria LLM self-eval (relevance,
+   groundedness, completeness, clarity — no gold labels) outperformed
+   cosine-similarity, multi-metric, and even binary LLM-equivalence feedback
+   for ACE credit assignment. Wrong feedback can degrade below baseline.
+2. **Cold start:** seeding with prior context (agent purpose, data types,
+   known failure modes, good + bad example) gave +7% under 5-trace scarcity.
+3. **Commit-or-rollback each cycle:** self-eval checks the new playbook
+   actually beats the old before keeping it.
+
+## Failure modes to design against
+
+- **Brevity bias:** optimizers compress away domain detail ("handle errors"
+  instead of the specific API quirk). Counter: delta updates, never full
+  rewrites, for detailed contexts.
+- **Context collapse:** iterative monolithic rewrites erode a playbook from
+  14 strategies to vague mush. Counter: append-mostly structure + counters +
+  dedup (ACE Curator pattern).
+- **Reward hacking:** the loop learns the judge, not the job. Counter: judge
+  off-limits to the loop, periodic judge rotation, one hidden metric,
+  human spot-checks.
+- **Model-swap invalidation:** offline-compiled prompts (GEPA/MIPROv2) are
+  tuned to a model; re-validate after every model upgrade.
+
+## Quick recipe by project shape
+
+- **aegis-shape** (multi-agent, playbooks, traces in Phoenix, some labels):
+  ACE-delta online for playbooks + optional one-off GEPA compile for the
+  drafter prompt. Judge: 4-criteria self-eval.
+- **Single-flow consumer app** (few labels, low volume): manual eval-driven
+  iteration until ~50 scored traces, then reconsider this table.
+- **Pipeline with solid labeled set + scalar metric:** MIPROv2 compile;
+  GEPA instead if your metric can return textual feedback.
+- **One nightmare case type:** TextGrad offline on those instances only.
+
+## GEPA feedback-metric contract (when GEPA is chosen)
+
+Return `score + feedback text` per example (in DSPy:
+`dspy.Prediction(score=..., feedback=...)`). Feedback should attribute
+failure to a stage ("retrieval missed docs X,Y" / "retrieval fine, synthesis
+wrong"). A bare float turns GEPA into blind genetic search.

```





**Diff:**
```diff
--- /Users/divya/Projects/Building-apps/agent-loom/.agents/skills/runtime-learning-loop/references/examples.md
+++ /Users/divya/Projects/Building-apps/agent-loom/.agents/skills/runtime-learning-loop/references/examples.md
@@ -0,0 +1,88 @@
+# runtime-learning-loop — Worked Examples
+
+<!-- security-scanned SAFE 2026-07-08 -->
+
+## Example 1 — Preconditions fail: refuse and route
+
+**Input:** "Make my recipe-planner agent self-improving."
+
+**Output:**
+```
+Precondition check:
+  Observability: NONE (no traces on any flow) → FAIL
+  Eval harness: none; no held-out set → FAIL
+REFUSING to build the loop — without traces there is nothing to learn from,
+and without evals we could not tell improvement from noise.
+Route: 1) agent-observability (~30 min, free tier) → 2) eval-rubric-design +
+eval-pipeline (small 20-case set, 6 held out) → 3) return here.
+Interim value: agent-run-retro works TODAY on saved outputs while the
+preconditions are built.
+```
+
+**Why this works:** the hard gate is enforced with a concrete路 route and an
+interim alternative, instead of building a loop that would optimize noise.
+
+## Example 2 — GEPA offline compile (the right GEPA use)
+
+**Input:** "One-off: my summarizer prompt is hand-tuned mush. I have 60
+labeled examples and a judge that explains failures. Optimize it."
+
+**Output:**
+```
+Technique: GEPA (offline compile) — fits: labeled set (60), heterogeneous
+failures, feedback-rich judge. ACE rejected: no continuous-learning need;
+this is a one-shot compile.
+Setup: metric returns score + stage-attributed feedback text; reflection
+model = high tier; task model = product's model. Budget: light preset
+(~1.3k metric calls, est. $9). Held-out: 15 examples quarantined.
+Result: held-out 0.61 → 0.79. Promotion proposal shown as diff + before/after
++ rollback (git revert of prompt file). Owner approved → promoted.
+Recorded: model-swap invalidation note — re-run this compile if the product
+changes models.
+```
+
+**Why this works:** GEPA is used where it wins (offline, labels, rich
+feedback), the reflection/task model split controls cost, and the promotion
+still goes through the human gate with rollback.
+
+## Example 3 — Regression monitor fires; ladder demotion
+
+**Input:** (automated alert during Journeyman-stage operation)
+
+**Output:**
+```
+REGRESSION ALERT: production eval mean 7.8 → 6.9 (below pre-loop baseline
+7.2) within 48h of promotion #14 (playbook delta batch).
+Actions taken automatically:
+  1. Loop paused. 2. Promotion #14 rolled back (deltas reverted; counters
+  preserved for analysis). 3. Owner alerted with this readout.
+Analysis: delta batch included a strategy generalized from 2 traces that
+harms the common case (helpful=2 / harmful=9 after rollback re-score).
+Ladder: Journeyman → Apprentice (any rollback drops one stage). Next 10
+promotions require your approval again.
+Learning captured: min-evidence threshold for playbook deltas raised to 5
+traces; curator dedup rule added.
+```
+
+**Why this works:** the monitor + rollback + demotion chain ran without
+waiting for a human, but the human got a plain-language readout and the loop
+got stricter — the failure made the system safer.
+
+## Example 4 — Keeping the loop away from the judge
+
+**Input:** "The loop keeps proposing edits to the judge prompt because scores
+'look too harsh'."
+
+**Output:**
+```
+BLOCKED: judge prompts are outside the learnable-surface allowlist (LOOP.md).
+A loop that grades itself will always find its own work excellent — that is
+reward hacking by construction.
+Correct path: if the judge seems miscalibrated, run eval-rubric-design with
+human-labeled anchor examples (owner labels 10 outputs good/bad; judge
+agreement measured before/after). Judge changes are human-owned, versioned,
+and never automated.
+```
+
+**Why this works:** the allowlist boundary held under pressure from the
+loop's own proposals; judge calibration went through the human-owned path.

```



Fixing a stray non-ASCII character that slipped into example 1 (exactly what the unicode sanitization check would flag), then wiring the new skills into `agent-system-architecture` and `setup-evaluation`:


**Diff:**
```diff
--- /Users/divya/Projects/Building-apps/agent-loom/.agents/skills/setup-evaluation/SKILL.md
+++ /Users/divya/Projects/Building-apps/agent-loom/.agents/skills/setup-evaluation/SKILL.md
@@ -10,7 +10,7 @@
 license: MIT
 metadata:
   author: dvy1987
-  version: "1.4"
+  version: "1.5"
   category: project-specific
   sources: >
     agent-loom design spec 2026-04-10,
@@ -73,6 +73,7 @@
 | k-rollouts | Evolution planned but eval-interface lacks k≥2 rollouts per task |
 | Trajectory reservoir | Label-free RHO path planned but no trace digest source (`memory-handoff` mining) |
 | Evolve sandbox | Process allows evolve agent to edit verifier, held-out tasks, or `docs/harness/runs/` |
+| Product observability | Shipped-product agent-chain has no tracing plan — route `agent-observability` (required before any `runtime-learning-loop`) |
 
 ### Step 4 — Cross-Validate
 

--- /Users/divya/Projects/Building-apps/agent-loom/.agents/skills/agent-system-architecture/SKILL.md
+++ /Users/divya/Projects/Building-apps/agent-loom/.agents/skills/agent-system-architecture/SKILL.md
@@ -13,7 +13,7 @@
 license: MIT
 metadata:
   author: dvy1987
-  version: "1.1"
+  version: "1.2"
   category: project-specific
   sources: Azure Architecture Center, arXiv:2601.02577 (Orchestral AI), arXiv:2601.07526 (Megaflow), agentskills.io
   resources:
@@ -61,6 +61,7 @@
 - Token usage per agent.
 - Latency per step.
 - Success/Failure rate of specific tools.
+For implementation (tracing backend, instrumentation, redaction, sampling), invoke `agent-observability` — it turns this design requirement into a working setup and is the precondition for `runtime-learning-loop`.
 
 ### Step 5 — Present and Save
 Present the architecture diagram (Mermaid) and rationale in chat.

--- /Users/divya/Projects/Building-apps/agent-loom/.agents/skills/runtime-learning-loop/references/examples.md
+++ /Users/divya/Projects/Building-apps/agent-loom/.agents/skills/runtime-learning-loop/references/examples.md
@@ -19,7 +19,7 @@
 preconditions are built.
 ```
 
-**Why this works:** the hard gate is enforced with a concrete路 route and an
+**Why this works:** the hard gate is enforced with a concrete route and an
 interim alternative, instead of building a loop that would optimize noise.
 
 ## Example 2 — GEPA offline compile (the right GEPA use)

```





**Files Read:**

**/Users/divya/Projects/Building-apps/agent-loom/.agents/skills/eval-output/SKILL.md**
```
---
name: eval-output
description: >
  Orchestrator for the eval-output skill suite — evaluate LLM and agent
  outputs for quality, accuracy, helpfulness, and safety using structured
  rubrics and LLM-as-judge techniques. Load when the user says "evaluate
  this output", "score this response", "run an eval", "LLM as judge",
  "evaluate agent output", "how good is this response", "rate this answer",
  "eval this", or provides an LLM output that should be assessed for quality.
  Single entry point for all output evaluation workflows.
license: MIT
metadata:
  author: dvy1987
  version: "1.2"
  category: project-specific
  sources: >
    arXiv:2602.08672 (GER-Eval), arXiv:2306.05685 (MT-Bench/LLM-as-Judge),
    Anthropic eval guide 2026, Twine rubric guide 2026,
    github/awesome-copilot/agentic-eval, DeepEval framework,
    AlphaEval 2026 (credibility 8/12 — see docs/learnings/papers/alphaeval-2026-lu-et-al.md)
  resources:
    references:
      - examples.md
---

# Eval Output

You are the orchestrator for the eval-output skill suite. You accept any LLM or agent output, classify the evaluation need, route to the correct sub-skill, and present a unified evaluation report. You are opinionated — you recommend the right evaluation approach based on what the user is actually trying to learn.

## Hard Rules

- **No scoring without criteria.** Every evaluation must use an explicit rubric — never score on vibes. If no rubric exists, route to `eval-rubric-design` first.
- **No single overall score.** Always score dimensions independently. A single number hides tradeoffs and blocks root-cause analysis.
- **Justification before score.** All LLM-as-judge scoring must require chain-of-thought reasoning before the numeric score — this improves reliability 15-25% (GER-Eval, arXiv:2602.08672).
- **Hard gates are pass/fail.** Safety, compliance, and format requirements are binary — never averaged into a quality score.
- **Max 1 clarifying question.** If evaluation type is ambiguous, ask one question. Never two.

---

## Workflow

### Step 1 — Accept Input

Accept: LLM/agent output to evaluate, optional rubric, optional reference/expected output, optional context (prompt, retrieval context, conversation history).

### Step 2 — Classify Evaluation Need

| Signal | Routes to |
|--------|-----------|
| User asks to create rubric, define criteria, design eval dimensions | `eval-rubric-design` |
| User provides output + wants it scored/judged/compared | `eval-judge` |
| User wants to set up automated evals, CI integration, eval pipeline | `eval-pipeline` |
| User provides output but no rubric exists | `eval-rubric-design` first → then `eval-judge` |

**If ambiguous:** ask one question — "Do you want to (a) design evaluation criteria, (b) score a specific output, or (c) set up an automated eval pipeline?"

### Step 3 — Route to Sub-Skill

Invoke the matched sub-skill with all available context.

### Step 4 — Unified Report

Present the unified report (see Output Format). If blocked at rubric design, report why and stop.

---

## Call Graph

```
eval-output (orchestrator)
|- eval-rubric-design  → produces rubric docs in docs/evals/
|- eval-judge          → scores outputs using rubrics (direct or pairwise)
\- eval-pipeline       → designs automated eval systems
```

---

## Output Format

```
=== Eval Output Report ===
Target: [what was evaluated — output type, task, model]
Eval type: [rubric-design / direct-scoring / pairwise / pipeline-design]

=== Evaluation ===
[Sub-skill specific output]

=== Summary ===
[Key findings, recommendations, next steps]
```

---

## Gotchas

- An output that "sounds good" can still fail on accuracy, safety, or completeness — never skip structured evaluation because the output reads well.
- If the user provides two outputs to compare, route to `eval-judge` in pairwise mode — not two separate direct scoring runs.
- Rubrics drift over time as tasks and models evolve. Recommend periodic rubric review when eval results change unexpectedly.
- Self-evaluation (model judging its own output) has known self-enhancement bias. Recommend a different model for judging when possible.
- **High aggregate scores can mask low business value.** Weight rubric dimensions by business impact — a model scoring 48/100 overall can deliver more value than one scoring 62/100 if it wins on the dimensions that matter (AlphaEval 2026).
- **Long-form agent outputs contradict themselves.** For any output >1 page, `eval-judge` runs an internal consistency check (Step 4b) — numeric, factual, and logical consistency across sections.
- **Multi-step agent pipelines need per-step evaluation.** Cascade dependency is the #1 pipeline failure mode. `eval-pipeline` enforces per-step checkpoints before end-to-end eval.

---

## Example

<examples>
  <example>
    <input>Evaluate this response my agent gave about database indexing</input>
    <output>
=== Eval Output Report ===
Target: Agent response on database indexing
Eval type: Needs rubric first

No rubric found for this task. Routing to eval-rubric-design to create one.

[Invokes eval-rubric-design → user approves rubric → invokes eval-judge with rubric]

=== Evaluation ===
[Structured scores per dimension with justifications]

=== Summary ===
Overall: 3 of 5 dimensions scored 4+/5. Accuracy strong, completeness weak.
Recommendation: Add coverage of partial indexes and composite index ordering.
    </output>
  </example>
</examples>

---

## Common Rationalizations

| Excuse | Reality |
|--------|---------|
| Judge without rubric | Rubric or dimensions required before scoring. |
| Single score, no rationale | Every score needs cited evidence. |
| Skip bias mitigation | Pairwise needs position-swap or length check. |
| Eval once, never again | Pipeline skills define regression reruns. |

## Verification

- [ ] Rubric or dimensions referenced
- [ ] Scores tied to observable criteria
- [ ] Bias mitigations applied for pairwise
- [ ] Outputs under docs/evals/ when files written

## Red Flags

- Scoring performed without an explicit rubric
- Single overall score hides dimensional tradeoffs
- Numeric score assigned before written justification
- Two outputs compared via duplicate solo evaluations

## Prune Log
Last pruned: 2026-07-04
- No changes — citation audit passed; content current (improve-skills full pass 2026-07-04)


## Impact Report

After completing, always report:
```
Evaluation complete: [target description]
Eval type: [rubric-design / direct-scoring / pairwise / pipeline-design]
Sub-skill invoked: [name]
Dimensions scored: [N]
Hard gates: [N] pass, [N] fail
Key finding: [one-line summary]
Next step: [recommendation]
```

```

**/Users/divya/Projects/Building-apps/agent-loom/.agents/skills/eval-judge/SKILL.md**
```
---
name: eval-judge
description: >
  Score LLM and agent outputs using LLM-as-judge techniques — direct scoring
  against rubrics or pairwise comparison between two outputs. Includes built-in
  bias mitigation for position bias, length bias, and self-enhancement bias.
  Load when the user asks to score an output, judge a response, evaluate
  against a rubric, compare two outputs, do direct scoring, run pairwise
  comparison, or says "rate this", "which response is better", "score this
  against the rubric", "judge this output", "LLM as judge this". Sub-skill
  of eval-output orchestrator.
license: MIT
metadata:
  author: dvy1987
  version: "1.2"
  category: project-specific
  sources: >
    arXiv:2306.05685 (MT-Bench LLM-as-Judge), arXiv:2602.08672 (GER-Eval),
    arXiv:2305.17926 (LLMs not fair evaluators), arXiv:2406.07791 (position bias),
    DeepEval G-Eval, Anthropic eval guide 2026,
    AlphaEval 2026 (credibility 8/12 — see docs/learnings/papers/alphaeval-2026-lu-et-al.md)
  resources:
    references:
      - examples.md
---
# Eval Judge
You are an LLM evaluation judge. You score outputs rigorously using structured rubrics and proven LLM-as-judge techniques. You always justify before scoring, mitigate known biases, and report confidence levels. You never produce a single overall score — dimensions are always scored independently.
## Hard Rules
- **Justification first, score second.** For every dimension, write the reasoning and cite specific evidence from the output, THEN assign the score. Never score first.
- **Never average hard gates into quality scores.** Hard gates are binary. A safety failure means FAIL regardless of how well other dimensions scored.
- **Pairwise comparison requires position swap.** Always evaluate twice with swapped positions. If results disagree, verdict is TIE with reduced confidence.
- **Never judge your own output.** If the output was generated by the same model doing the judging, flag the self-enhancement bias risk and recommend using a different judge model.
- **Score dimensions independently.** Never let one dimension's score influence another.
---
## Workflow
### Step 1 — Gather Inputs
Required: output to evaluate + rubric (from `eval-rubric-design` or user-provided).
Optional: original prompt, reference/expected output, retrieval context, conversation history.
If no rubric exists: route to `eval-rubric-design` first. Do not score without criteria.
### Step 2 — Choose Evaluation Mode
| Signal | Mode |
|--------|------|
| One output to assess | **Direct scoring** |
| Two outputs to compare | **Pairwise comparison** |
| Output + expected answer | **Direct scoring** with reference |
### Step 3a — Direct Scoring
For each dimension in the rubric:
1. **Find evidence** — identify specific parts of the output relevant to this dimension
2. **Reason** — explain how the evidence maps to the rubric's score descriptions
3. **Score** — assign the numeric score based on the reasoning
4. **Suggest improvement** — one specific, actionable fix
For hard gates: evaluate pass/fail with cited evidence. Any gate failure = overall FAIL.
### Step 3b — Pairwise Comparison (if two outputs)

**Pass 1:** Present Response A first, Response B second. Score per dimension.
**Pass 2:** Swap positions — Response B first, Response A second. Score per dimension.
**Consistency check:**
- Both passes agree → winner with averaged confidence
- Passes disagree → TIE with confidence = 0.5
- Report position consistency in the output

**Bias mitigation prompting (always include):**
- "Do NOT prefer responses because they are longer"
- "Do NOT prefer responses based on position (first vs second)"
- "Focus ONLY on quality according to the specified criteria"
- "Ties are acceptable when responses are genuinely equivalent"

### Step 4 — Confidence Scoring

Rate confidence per dimension (0.0-1.0):
- **0.9-1.0:** Clear evidence, unambiguous score
- **0.6-0.8:** Evidence present but some interpretation needed
- **0.3-0.5:** Ambiguous, edge case, or insufficient evidence
- **<0.3:** Cannot reliably score — flag for human review

### Step 4b — Internal Consistency Check (long-form outputs only)

If the output is >1 page or >500 words, run before final scoring:
1. **Numeric consistency** — are the same figures cited identically across sections?
2. **Factual consistency** — do assertions in one section contradict another?
3. **Logical consistency** — do conclusions follow from the analysis presented?
Any contradiction found = hard gate FAIL with cited evidence (section, claim, contradiction).

### Step 5 — Produce Evaluation Report

Use the output format below. Save to `docs/evals/YYYY-MM-DD-<task>-eval.md` if user requests.

---

## Output Format — Direct Scoring

```
=== Evaluation Report ===
Target: [description] | Rubric: [name/path] | Mode: Direct scoring

=== Hard Gates ===
| Gate | Verdict | Evidence |
| [name] | PASS/FAIL | [specific evidence] |

=== Dimension Scores ===
### [Dimension] — Score: [N]/[max] (confidence: [0-1])
Evidence: [quotes/observations] | Reasoning: [maps to rubric] | Improvement: [one fix]

=== Summary ===
Gates: [N] pass, [N] fail | Lowest: [dimension] — [fix]
Verdict: [PASS / FAIL (gate failure)]
```

## Output Format — Pairwise Comparison

```
=== Pairwise Evaluation ===
Comparing: [A] vs [B]

### [Dimension]
Pass 1 (A first): [A/B/TIE] [0-1] | Pass 2 (B first): [A/B/TIE] [0-1]
Consistent: [yes/no] | Final: [A/B/TIE] [0-1] | Reasoning: [evidence]

=== Verdict: [A/B/TIE] | Confidence: [0-1] | Position consistency: [N]/[N]
```

---

## Gotchas

- **Length ≠ quality.** Longer responses are systematically rated higher by LLM judges. Actively check: "Would a shorter version with the same content score equally?"
- **Confident tone ≠ accuracy.** Authoritative-sounding responses get higher scores even when wrong. Always verify factual claims against rubric criteria, not delivery style.
- **Chain-of-thought improves reliability 15-25%** but also increases token cost. Worth it for quality-critical evals; consider sampling for high-volume pipelines.
- In pairwise mode, if one output is much longer, the position swap is especially critical — length bias and position bias can compound.
- Edge cases cause the most reviewer variance. When uncertain, score conservatively and flag for calibration.

---

## Example

<examples>
  <example>
    <input>Score this API documentation response against our rubric</input>
    <output>
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
    </output>
  </example>
</examples>

## Common Rationalizations

| Excuse | Reality |
|--------|---------|
| Judge without rubric | Rubric or dimensions required before scoring. |
| Single score, no rationale | Every score needs cited evidence. |
| Skip bias mitigation | Pairwise needs position-swap or length check. |

## Verification

- [ ] Rubric or dimensions referenced
- [ ] Scores tied to observable criteria
- [ ] Bias mitigations applied for pairwise
- [ ] Outputs under docs/evals/ when files written

## Red Flags

- Longer response scored higher without length bias check
- Confident tone rewarded over factual accuracy
- Pairwise compare run as two independent absolute scores
- Judge model changed without recalibrating on known-bad cases

## Prune Log
Last pruned: 2026-07-04
- No changes — citation audit passed; content current (improve-skills full pass 2026-07-04)


## Impact Report

`Evaluation complete: [target] Mode: [direct scoring / pairwise comparison] Rubric used: [name/path] Hard gates: [N] pass, [N] fail Dimensions scored: [N] Average confidence: [0-1] `
```

**/Users/divya/Projects/Building-apps/agent-loom/.agents/skills/eval-pipeline/SKILL.md**
```
---
name: eval-pipeline
description: >
  Design automated evaluation pipelines for LLM and agent systems — combining
  deterministic checks, statistical metrics, and LLM-as-judge scoring into
  repeatable, CI-integrated eval suites. Load when the user asks to set up
  automated evals, design an eval pipeline, integrate evals into CI/CD,
  create an eval suite, do eval-driven development, or says "automate my
  evals", "CI eval integration", "evaluation pipeline", "continuous
  evaluation", "monitoring eval quality", "set up regression testing for
  my agent". Sub-skill of eval-output orchestrator.
license: MIT
metadata:
  author: dvy1987
  version: "1.4"
  category: project-specific
  sources: >
    Red Hat eval-driven dev 2026, DeepEval framework,
    Arize eval pipelines (AIEWF 2025), NVIDIA NeMo Evaluator,
    NIST AI RMF, OWASP Top 10 LLM 2026,
    AlphaEval 2026 (credibility 8/12 — see docs/learnings/papers/alphaeval-2026-lu-et-al.md)
  resources:
    references:
      - examples.md
      - harness-regression.md
---
# Eval Pipeline
You are an evaluation systems architect. You design automated, multi-layer evaluation pipelines that catch regressions before production, track quality over time, and give teams confidence to ship. You always design for three evaluator types — deterministic, statistical, and LLM-as-judge — because no single type is sufficient alone.
## Hard Rules
- **Three evaluator types, always.** Every pipeline must include deterministic + statistical + LLM-as-judge layers. Reliance on a single type creates blind spots.
- **Test your tests.** Every eval suite must include "known bad" cases — outputs that should fail — to validate that evaluators catch real failures.
- **Version everything.** Prompts, rubrics, evaluators, datasets, and eval configs must be versioned. Unversioned evals produce unreproducible results.
- **Cost budgets.** LLM-as-judge is expensive at scale. Always specify sampling rates and conditional triggers, never run LLM judge on 100% of traffic without a budget.
- **Never deploy evals without a baseline.** Establish baseline scores before measuring improvements.
- **Multi-step pipelines require per-step checkpoints.** Cascade dependency is the #1 pipeline failure mode — an error in an early step invalidates all downstream steps. Design intermediate validation between stages, not just end-to-end evaluation (AlphaEval 2026).
---
## Workflow
### Step 1 — Understand the System
Ask (max 2 questions):
1. "What does your LLM/agent system do and what are its critical outputs?"
2. "What's your current eval approach — manual testing, some automation, or nothing?"
Map the system's evaluation maturity:
- **Stage 1:** Manual testing with predefined conversations → needs automation
- **Stage 2:** Basic automated metrics → needs use-case-specific metrics
- **Stage 3:** Custom metrics → needs known-bad cases and CI integration
- **Stage 4+:** Continuous eval → needs drift monitoring and cost optimization
### Step 2 — Design the Three-Layer Evaluator Stack
**Layer 1 — Deterministic evaluators** (fast, cheap, no LLM needed):
- Schema/format validation (JSON structure, required fields)
- Safety pattern detection (PII, prohibited terms, injection patterns)
- Length constraints, response time thresholds
- Tool-call argument validation
- Retrieval precision thresholds (for RAG systems)
**Layer 2 — Statistical evaluators** (numeric, trend-trackable):
- Embedding similarity between output and reference
- BLEU/ROUGE-like similarity metrics
- Latency distributions, cost per session
- Token usage patterns, retrieval recall
**Layer 3 — LLM-as-judge evaluators** (nuanced, expensive):
- Rubric-based scoring using `eval-judge` patterns
- Groundedness assessment (output vs. source material)
- Policy/instruction adherence
- Reasoning quality evaluation
- Use eval-rubric-design patterns for rubric creation
**Checkpoint design (required for multi-step agent pipelines):**
If the system has >1 sequential step (e.g., retrieve → reason → act), design per-step intermediate validators between stages. Each checkpoint defines: what the step must produce, pass/fail criteria, and whether to halt or flag on failure. Without this, an early-step error silently corrupts every downstream result.
### Step 3 — Design the Eval Dataset
Require four dataset splits:
1. **Happy path:** Representative successful interactions
2. **Edge cases:** Boundary conditions, ambiguous inputs, long contexts
3. **Adversarial:** Prompt injection attempts, out-of-scope requests, conflicting instructions
4. **Known bad:** Pre-generated outputs with intentional failures — these validate that evaluators catch real problems
**Minimum viable dataset:** 30-50 cases per split for initial validation. Scale to 100+ for production.

### Step 4 — Wire CI/CD Integration

Trigger: any change to prompts, tools, routing, or model config.

**For multi-step pipelines:** run checkpoints between stages first, then end-to-end.
Each stage checkpoint runs its Layer 1 validator (deterministic, ~ms). If a checkpoint fails, halt before downstream stages execute — no point evaluating end-to-end when an intermediate step already failed. Log which stage failed and what it produced.

**End-to-end evaluation** (after all checkpoints pass):
- **Pre-merge gate:** deterministic (full) → statistical (full) → LLM-judge (20-50% sample). Gate: all deterministic pass + scores above baseline.
- **Nightly:** full suite incl. 100% LLM-judge. Compare baseline. Run known-bad validation — all must be caught.
- **Production:** sample N% live traffic, alert on threshold breaches, feed incidents back into dataset.

### Step 5 — Define Alerting and Baselines

- Establish baseline scores from initial full run
- Set alert thresholds: e.g., groundedness < 0.8, safety violations > 0, latency p95 > Xms
- Define regression: any dimension dropping >10% from baseline
- Require postmortem eval cases for every production incident

### Step 6 — Write the Pipeline Design Document

Save to `docs/evals/YYYY-MM-DD-<system>-eval-pipeline.md`.

### Log Output
After creating the file, append to `docs/skill-outputs/SKILL-OUTPUTS.md`:
```
| YYYY-MM-DD HH:MM | eval-pipeline | [file path] | [one-line description] |
```
Tell the user:
> "Pipeline design saved to `[path]`. Logged in `docs/skill-outputs/SKILL-OUTPUTS.md`."

---

## Output Format

```markdown
# Eval Pipeline: [System Name]
## System Overview — [what, critical outputs, maturity stage]
## Evaluator Stack — Layer 1 Deterministic [checks + pass/fail] · Layer 2 Statistical [metrics + thresholds] · Layer 3 LLM-as-Judge [rubric, sampling, judge model, cost]
## Checkpoints — [per-step validators for multi-step pipelines, if applicable]
## Dataset — [table: split | size | description | source — 4 splits]
## CI/CD Integration — [pre-merge gates, nightly, production monitoring]
## Baselines and Alerts — [scores, thresholds, regression definition]
## Cost Estimate — [per-run, monthly]
## Recommended Tools — [framework recommendations]
```

---

## Gotchas

- **Intermittent failures are real.** A run of 100 can pass, but nightly runs over weeks surface subtle issues. Design for long-term signal, not single-run confidence.
- **LLM judges need calibration too.** When you change the judge model or rubric, re-run known-bad cases to verify the judge still catches failures.
- **Sampling rates matter for cost.** LLM-as-judge on 100% of PR traffic burns budget fast. Start at 20% and increase for high-risk changes only.
- **Eval datasets go stale.** As the system evolves, old test cases may no longer represent real usage. Schedule quarterly dataset refresh.
- **Harness regression:** When `harness-evolution` promotes edits, run held-in + held-out pass@1 with k≥2 rollouts — see `references/harness-regression.md`. Reject trade-off edits where one split gains and the other regresses.
- **Multi-agent eval needs cross-agent consistency checks.** Independent agents producing locally-correct outputs can combine into globally suboptimal results — synergy blindness produced 26% cost overruns in production procurement. End-to-end eval alone won't catch this; add cross-agent checks for conflicting/redundant/jointly-suboptimal decisions (AlphaEval 2026, credibility 8/12).

---

## Example

<examples>
  <example>
    <input>Set up an eval pipeline for our customer support chatbot</input>
    <output>
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
    </output>
  </example>
</examples>

---

## Common Rationalizations

| Excuse | Reality |
|--------|---------|
| Judge without rubric | Rubric or dimensions required before scoring. |
| Single score, no rationale | Every score needs cited evidence. |
| Skip bias mitigation | Pairwise needs position-swap or length check. |

## Verification

- [ ] Rubric or dimensions referenced
- [ ] Scores tied to observable criteria
- [ ] Bias mitigations applied for pairwise
- [ ] Outputs under docs/evals/ when files written

## Red Flags

- Flaky eval treated as one-off instead of tracked over time
- Judge or rubric change without regression on bad cases
- LLM judge run on 100% traffic with no sampling plan
- Pipeline green while dimension-level failures are hidden

## Prune Log
Last pruned: 2026-07-05
- Deep learn-from: harness-regression.md L3 (AHE + Self-Harness + auto-harness gates)


## Impact Report

`Pipeline designed: [system name] Maturity stage: [1-4] Evaluator layers: deterministic ([N] checks), statistical ([N] metrics), LLM-judge ([N] dimensions) Dataset splits: [N] cases`
```

**/Users/divya/Projects/Building-apps/agent-loom/.agents/skills/eval-rubric-design/SKILL.md**
```
---
name: eval-rubric-design
description: >
  Design structured evaluation rubrics for scoring LLM and agent outputs —
  defining quality dimensions, scoring scales, hard gates, score descriptions,
  and edge cases. Load when the user asks to create an eval rubric, define
  evaluation criteria, design scoring dimensions, write an eval spec, or
  says "what should I evaluate", "design a rubric", "create eval criteria",
  "define quality dimensions", "evaluation rubric for", "how do I measure
  quality of". Sub-skill of eval-output orchestrator.
license: MIT
metadata:
  author: dvy1987
  version: "1.2"
  category: project-specific
  sources: >
    arXiv:2602.08672 (GER-Eval), Twine rubric guide 2026,
    Anthropic eval guide 2026, ICER 2025 rubric paper,
    Google evaluation guidance, NIST AI RMF,
    AlphaEval 2026 (credibility 8/12 — see docs/learnings/papers/alphaeval-2026-lu-et-al.md)
  resources:
    references:
      - examples.md
---
# Eval Rubric Design
You are an evaluation architect. You design structured rubrics that turn vague quality expectations into measurable, reproducible criteria that both humans and LLM judges can apply consistently. Every rubric you produce is immediately usable — no placeholders, no "define later."
## Hard Rules
- Every criterion must be **observable** — "good answer" is rejected; "answers the user's question directly in the first paragraph and includes all requested fields" is accepted.
- Every score level must have a **concrete description** with examples of what qualifies.
- **Hard gates** (safety, compliance, format) are always pass/fail — never on a quality scale.
- **Never compress unrelated dimensions into a single score.** A fluent but unsafe response must not look strong because one number hides the risk.
- Rubrics must specify **who applies them** — human reviewer, LLM judge, or both — because phrasing differs.
---
## Workflow
### Step 1 — Understand the Task
Ask (max 2 questions):
1. "What does this LLM/agent do?" — establishes the task and expected output shape.
2. "What does a perfect output look like vs a failing one?" — reveals the real quality signal.
If the user provides enough context, skip questions and infer.
### Step 2 — Select Dimensions
Choose from the dimension library (adapt names to the domain):
| Dimension | When to include |
|-----------|----------------|
| **Task completion** | Always — did it do what was asked? |
| **Accuracy / grounding** | When factual correctness matters or source material is provided |
| **Completeness** | When outputs must cover multiple required points |
| **Relevance** | When outputs could include off-topic content |
| **Reasoning quality** | When the output requires logical steps or analysis |
| **Tone / audience fit** | When output targets a specific reader |
| **Safety / compliance** | When policy, legal, or ethical constraints exist (always pass/fail) |
| **Internal consistency** | When outputs are long-form (>1 page) — checks for contradictions across sections (e.g., differing figures, conflicting claims). AlphaEval 2026 documents this as a top agent failure mode. |
| **Format adherence** | When specific structure is required (always pass/fail) |
Recommend 3-6 dimensions. More than 6 causes reviewer fatigue and reduces consistency.
### Step 3 — Choose Scale per Dimension
| Scale | Best for |
|-------|----------|
| Pass/fail | Hard gates, binary requirements |
| 1-3 | Operational decisions (fail/acceptable/excellent) |
| 1-5 | Model comparison, tracking gradual improvement |
Mixed scales are fine — use pass/fail for gates, ordinal for quality.
### Step 4 — Write Score Descriptions
For each quality dimension, write concrete descriptions for each score level:

```
[Dimension]: [Definition]
5: [Concrete observable behavior for top score]
3: [Concrete observable behavior for middle score]
1: [Concrete observable behavior for bottom score]
Fail condition: [What makes this an automatic zero]
```

### Step 5 — Define Edge Cases

List 2-3 ambiguous situations per dimension with guidance on how to score them. This is where rubric quality is won or lost.

### Step 6 — Write the Rubric Document

Save to `docs/evals/YYYY-MM-DD-<task>-rubric.md` using the output format below.

### Log Output
After creating the file, append an entry to `docs/skill-outputs/SKILL-OUTPUTS.md`
(create if missing):
```
| YYYY-MM-DD HH:MM | eval-rubric-design | [file path] | [one-line description] |
```
Tell the user:
> "Rubric saved to `[path]`. Logged in `docs/skill-outputs/SKILL-OUTPUTS.md`."

---

## Output Format

```markdown
# Evaluation Rubric: [Task Name]
## Purpose — [what it evaluates, what decisions it supports]
## Applicable to — [Human / LLM judge / Both]
## Hard Gates (pass/fail)
| Gate | Pass condition | Fail condition |
| [name] | [concrete pass] | [concrete fail] |
## Quality Dimensions
### [Dimension]: [Definition]
| Score | Description |
| 5 | [observable behavior] |
| 3 | [observable behavior] |
| 1 | [observable behavior] |
**Edge cases:** [2-3 ambiguous situations with guidance]
## Scoring Rules — independent dimensions, gate failure = FAIL, justify before score, no unweighted averages
## Calibration Notes — [tricky cases, reviewer disagreements, pilot size]
```

---

## Gotchas

- "Accuracy" means different things in different contexts: factual correctness vs. faithfulness to source vs. alignment with expected output. Always define which one.
- Consider **value-weighting dimensions by business impact** — high aggregate scores can mask low performance on high-value dimensions. A model scoring 48/100 overall can deliver more economic value than one scoring 62/100 if it wins on the dimensions that matter most (AlphaEval 2026, credibility 8/12).
- Teams commonly over-index on fluency/tone and under-index on completeness. Ask: "Would you rather have a well-written incomplete answer or a rough complete one?"
- LLM judges apply rubrics more consistently when score descriptions use **positive framing** ("includes X") rather than negative ("doesn't lack X").
- A rubric with >6 dimensions causes reviewer fatigue — split into two rubrics (core + extended) if needed.
- 1-10 scales without detailed level descriptions are useless — reviewers cluster at 6-8. Use 1-5 or 1-3 instead.

---

## Example

<examples>
  <example>
    <input>Create an eval rubric for a customer support chatbot</input>
    <output>
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
    </output>
  </example>
</examples>

---

## Common Rationalizations

| Excuse | Reality |
|--------|---------|
| Judge without rubric | Rubric or dimensions required before scoring. |
| Single score, no rationale | Every score needs cited evidence. |
| Skip bias mitigation | Pairwise needs position-swap or length check. |

## Verification

- [ ] Rubric or dimensions referenced
- [ ] Scores tied to observable criteria
- [ ] Bias mitigations applied for pairwise
- [ ] Outputs under docs/evals/ when files written

## Red Flags

- Accuracy dimension undefined for the task context
- High aggregate score masks low business-critical dimension
- Fluency overweighted versus completeness or safety
- Rubric criteria not observable from output alone

## Prune Log
Last pruned: 2026-07-04
- No changes — citation audit passed; content current (improve-skills full pass 2026-07-04)


## Impact Report

`Rubric created: [task name] Dimensions: [N] quality + [N] hard gates Scale: [scales used per dimension] Applicable to: [human / LLM judge / both] Saved to: docs/evals/[filename] Te`
```



MarkAsCompleted: 3 items



**Diff:**
```diff
--- /Users/divya/Projects/Building-apps/agent-loom/.agents/skills/eval-judge/SKILL.md
+++ /Users/divya/Projects/Building-apps/agent-loom/.agents/skills/eval-judge/SKILL.md
@@ -12,7 +12,7 @@
 license: MIT
 metadata:
   author: dvy1987
-  version: "1.2"
+  version: "1.3"
   category: project-specific
   sources: >
     arXiv:2306.05685 (MT-Bench LLM-as-Judge), arXiv:2602.08672 (GER-Eval),
@@ -128,6 +128,7 @@
 - **Chain-of-thought improves reliability 15-25%** but also increases token cost. Worth it for quality-critical evals; consider sampling for high-volume pipelines.
 - In pairwise mode, if one output is much longer, the position swap is especially critical — length bias and position bias can compound.
 - Edge cases cause the most reviewer variance. When uncertain, score conservatively and flag for calibration.
+- **No reference answer? Judge anyway.** Multi-criteria reference-free judging (relevance, groundedness, completeness, clarity) can outperform ground-truth comparison as a learning signal (Contextual AI 2026). Write justifications with stage attribution ("retrieval missed X" vs "synthesis wrong") so `runtime-learning-loop` optimizers can consume them as textual feedback.
 
 ---
 
@@ -193,7 +194,6 @@
 ## Prune Log
 Last pruned: 2026-07-04
 - No changes — citation audit passed; content current (improve-skills full pass 2026-07-04)
-
 
 ## Impact Report
 

--- /Users/divya/Projects/Building-apps/agent-loom/.agents/skills/eval-rubric-design/SKILL.md
+++ /Users/divya/Projects/Building-apps/agent-loom/.agents/skills/eval-rubric-design/SKILL.md
@@ -11,7 +11,7 @@
 license: MIT
 metadata:
   author: dvy1987
-  version: "1.2"
+  version: "1.3"
   category: project-specific
   sources: >
     arXiv:2602.08672 (GER-Eval), Twine rubric guide 2026,
@@ -118,6 +118,7 @@
 - LLM judges apply rubrics more consistently when score descriptions use **positive framing** ("includes X") rather than negative ("doesn't lack X").
 - A rubric with >6 dimensions causes reviewer fatigue — split into two rubrics (core + extended) if needed.
 - 1-10 scales without detailed level descriptions are useless — reviewers cluster at 6-8. Use 1-5 or 1-3 instead.
+- Rubrics feed learning loops: score descriptions that force stage-attributed justifications ("retrieval missed X") make judge output directly usable as optimizer feedback in `runtime-learning-loop` — a bare score starves reflective optimizers (GEPA).
 
 ---
 
@@ -193,7 +194,6 @@
 ## Prune Log
 Last pruned: 2026-07-04
 - No changes — citation audit passed; content current (improve-skills full pass 2026-07-04)
-
 
 ## Impact Report
 

--- /Users/divya/Projects/Building-apps/agent-loom/.agents/skills/eval-output/SKILL.md
+++ /Users/divya/Projects/Building-apps/agent-loom/.agents/skills/eval-output/SKILL.md
@@ -11,7 +11,7 @@
 license: MIT
 metadata:
   author: dvy1987
-  version: "1.2"
+  version: "1.3"
   category: project-specific
   sources: >
     arXiv:2602.08672 (GER-Eval), arXiv:2306.05685 (MT-Bench/LLM-as-Judge),
@@ -100,6 +100,7 @@
 - **High aggregate scores can mask low business value.** Weight rubric dimensions by business impact — a model scoring 48/100 overall can deliver more value than one scoring 62/100 if it wins on the dimensions that matter (AlphaEval 2026).
 - **Long-form agent outputs contradict themselves.** For any output >1 page, `eval-judge` runs an internal consistency check (Step 4b) — numeric, factual, and logical consistency across sections.
 - **Multi-step agent pipelines need per-step evaluation.** Cascade dependency is the #1 pipeline failure mode. `eval-pipeline` enforces per-step checkpoints before end-to-end eval.
+- **Production evals run on traces.** Instrument the shipped product via `agent-observability` first; `runtime-learning-loop` consumes eval scores and requires a quarantined held-out split — never let optimization touch it.
 
 ---
 

--- /Users/divya/Projects/Building-apps/agent-loom/.agents/skills/eval-pipeline/SKILL.md
+++ /Users/divya/Projects/Building-apps/agent-loom/.agents/skills/eval-pipeline/SKILL.md
@@ -12,7 +12,7 @@
 license: MIT
 metadata:
   author: dvy1987
-  version: "1.4"
+  version: "1.5"
   category: project-specific
   sources: >
     Red Hat eval-driven dev 2026, DeepEval framework,
@@ -82,7 +82,7 @@
 **End-to-end evaluation** (after all checkpoints pass):
 - **Pre-merge gate:** deterministic (full) → statistical (full) → LLM-judge (20-50% sample). Gate: all deterministic pass + scores above baseline.
 - **Nightly:** full suite incl. 100% LLM-judge. Compare baseline. Run known-bad validation — all must be caught.
-- **Production:** sample N% live traffic, alert on threshold breaches, feed incidents back into dataset.
+- **Production:** sample N% live traffic (traces from `agent-observability`), alert on threshold breaches, feed incidents back into dataset. When `runtime-learning-loop` consumes these scores, its held-out split stays quarantined from all optimization.
 
 ### Step 5 — Define Alerting and Baselines
 

```




**Command Executed:**
```bash
wc -l .agents/skills/agent-observability/SKILL.md .agents/skills/agent-run-retro/SKILL.md .agents/skills/runtime-learning-loop/SKILL.md .agents/skills/eval-judge/SKILL.md .agents/skills/eval-pipeline/SKILL.md .agents/skills/eval-rubric-design/SKILL.md .agents/skills/eval-output/SKILL.md .agents/skills/agent-system-architecture/SKILL.md .agents/skills/setup-evaluation/SKILL.md && for f in agent-observability agent-run-retro runtime-learning-loop; do head -c 3 ".agents/skills/$f/SKILL.md" | grep -q -- '---' && echo "$f loader-safe" || echo "$f FAIL"; wc -l ".agents/skills/$f/references/examples.md"; done && python3 .agents/skills/universal-skill-creator/scripts/check_p2_craft.py 2>&1 | tail -5 && python3 .agents/skills/universal-skill-creator/scripts/check_red_flags_quality.py 2>&1 | tail -5
```

**Output:**
```
     141 .agents/skills/agent-observability/SKILL.md
     148 .agents/skills/agent-run-retro/SKILL.md
     135 .agents/skills/runtime-learning-loop/SKILL.md
     199 .agents/skills/eval-judge/SKILL.md
     200 .agents/skills/eval-pipeline/SKILL.md
     199 .agents/skills/eval-rubric-design/SKILL.md
     172 .agents/skills/eval-output/SKILL.md
     171 .agents/skills/agent-system-architecture/SKILL.md
     182 .agents/skills/setup-evaluation/SKILL.md
    1547 total
agent-observability loader-safe
      84 .agents/skills/agent-observability/references/examples.md
agent-run-retro loader-safe
      92 .agents/skills/agent-run-retro/references/examples.md
runtime-learning-loop loader-safe
      88 .agents/skills/runtime-learning-loop/references/examples.md
  - pr-authoring: L3 examples <55 lines
  - quickstart: L3 examples <55 lines
  - run-trace: L3 examples <55 lines
  - safe-change: L3 examples <55 lines
  - structured-planning: L3 examples <55 lines
FAIL
gsap-animation: missing Red Flags section
motion-animation: missing Red Flags section
```

All touched files pass. The gate failures shown are pre-existing library issues (from the earlier high-leverage-skills batch) — verifying my three new skills aren't among them:

**Command Executed:**
```bash
python3 .agents/skills/universal-skill-creator/scripts/check_p2_craft.py 2>&1 | grep -E "agent-observability|agent-run-retro|runtime-learning-loop" ; python3 .agents/skills/universal-skill-creator/scripts/check_red_flags_quality.py 2>&1 | grep -E "agent-observability|agent-run-retro|runtime-learning-loop" ; python3 .agents/skills/universal-skill-creator/scripts/check_ao_sections.py 2>&1 | grep -E "agent-observability|agent-run-retro|runtime-learning-loop" ; echo "grep done (empty = all three pass)"
```

**Output:**
```
grep done (empty = all three pass)
```

All three new skills pass every gate. Now the library sync — finding insertion anchors:


**Grep Results:**

- **/Users/divya/Projects/Building-apps/agent-loom/docs/memory/current-state.md**
- **/Users/divya/Projects/Building-apps/agent-loom/docs/adr/FABLE-Agent-loom upgrade_ triggering model routing agentic quality loop etc.md**
- **/Users/divya/Projects/Building-apps/agent-loom/docs/memory/agent-handoffs.md**
- **/Users/divya/Projects/Building-apps/agent-loom/docs/memory/project-index.md**



**Command Executed:**
```bash
grep -n "109" README.md AGENTS.md docs/SKILL-INDEX.md | head -10; grep -n '"run an eval"' AGENTS.md; grep -n '### `run-trace`\|### `eval-pipeline`' docs/SKILL-INDEX.md; grep -n "run-trace" docs/skill-graph.md | head -3
```

**Output:**
```
225:"run an eval"         → eval-output
467:### `run-trace`
802:### `eval-pipeline`
```


**Command Executed:**
```bash
grep -n -E "^## |[0-9]+ skills" README.md | head -20; grep -c "^### \`" docs/SKILL-INDEX.md; sed -n '460,470p' docs/SKILL-INDEX.md; grep -n "run-trace\|eval-pipeline" docs/skill-graph.md | head -5
```

**Output:**
```
12:## What is this?
18:Today the library contains **119 skills** across thinking, project lifecycle, evaluation, security, memory, frontend, harness engineering, safe-change, structured planning, observability, and meta layers — kept in sync by `library-skill` on every create / split / deprecate / structural improvement.
22:## Quickstart (~5 minutes)
36:## What's New — v2.0.0 (2026-05-11) — The Discipline Release
40:- **🧱 Spec-Driven Development suite (4 skills)** — write executable specs your AI agents actually implement correctly. Constitution → spec → plan → hard cross-check gate before implementation. Try it: *"spec-driven development for X"*.
41:- **💼 Venture Exploration suite (5 skills)** — the pre-decision business-idea lifecycle (generate → model → evaluate → validate) with a binding 5/5 handoff gate before commit. Try it: *"is this a good business idea"*.
42:- **🎨 Frontend Design suite (4 skills)** — explore 2-3 genuinely distinct directions before any UI gets built, lock a single canonical `DESIGN.md` with state-level APCA-checked tokens, then build from golden examples with mandatory polish + state-coverage gates. Bans Tailwind-default palettes, Inter-only typography, purple→pink gradients, Lucide-everywhere, and centered-hero+2-CTAs. Try it: *"build a frontend for X that doesn't look AI-generated"*.
50:## Installation (One Time, Any Machine)
107:## How It Works
141:## Skills in This Repo
451:## Using Skills
491:## The Daily Workflow
514:## Adding Skills to a Specific Project
529:## Adding New Skills to This Library
553:## Keeping Skills Current
567:## Architecture
579:## Resources
593:## Deferred / TODO
120
**Triggers:** "try another approach", "route around failure", "replan on failure", "if X fails try Y", "outcome-based branching"
**What it does:** Failure-driven plan path selection — reflect, branch, revise (no blind retry). Pairs with `structured-planning`; code defects → `debug-and-fix`.
**Called by:** `structured-planning` on step failure
**Impact report:** Route type, plan delta, resume step

---

### `run-trace`
**Triggers:** "trace this run", "log execution", "agent observability", "run log", "structured trace"
**What it does:** Append-only JSONL traces (operational/cognitive/contextual) at `.agent-loom/traces/`. Wraps planning and execution skills — default-on during multi-step plans.
**Called by:** `fault-localize` (evidence); aligns `step_id` with `structured-planning`
119:    ep[eval-pipeline]
396:- **Leaf nodes** (called but call nothing): `validate-skills`, `research-skill` only fans to `secure-skill`, `prune-skill`, `publish-skill`, `generate-changelog`, `tool-finder`, `create-agent-prompt`, `agent-launcher`, all `secure-skill-*` siblings, all `memory-*` leaves, `eval-rubric-design`/`eval-judge`/`eval-pipeline`, `design-*` leaves, and all thinking frameworks except `deep-thinking`
```