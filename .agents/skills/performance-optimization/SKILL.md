---
name: performance-optimization
description: >
  Measure, profile, and fix performance bottlenecks — Core Web Vitals, backend
  latency, bundle size, and database queries. Load when performance requirements
  exist, users report slowness, profiling reveals bottlenecks, or the user asks
  to optimize load time, LCP, INP, CLS, or response time. Not for premature
  optimization without evidence. Pairs with browser-testing-with-devtools and
  ci-cd-and-automation for regression guards.
license: MIT
metadata:
  author: dvy1987
  version: "1.0"
  category: project-specific
  sources: addyosmani/agent-skills performance-optimization (11/12, 2026-05-29)
  resources:
    references:
      - examples.md
---

# Performance Optimization

Measure before optimizing. Profile first, fix the proven bottleneck, measure again, then guard against regression.

## Hard Rules

- Never optimize without a **baseline measurement** (synthetic + real-user when possible).
- Fix the **actual bottleneck** — not the most interesting code.
- One change at a time when validating; otherwise you cannot attribute wins.
- Set **budgets** (LCP, bundle KB, p95 latency) and fail CI when exceeded.
- Document what you measured, what you changed, and the delta.

---

## Core Web Vitals Targets

| Metric | Good | Needs work | Poor |
|--------|------|------------|------|
| LCP | ≤ 2.5s | ≤ 4.0s | > 4.0s |
| INP | ≤ 200ms | ≤ 500ms | > 500ms |
| CLS | ≤ 0.1 | ≤ 0.25 | > 0.25 |

---

## Workflow

### Step 1 — Measure baseline

- **Frontend:** Lighthouse (synthetic), DevTools Performance, `web-vitals` RUM.
- **Backend:** APM, query logs with timing, p50/p95/p99 on critical endpoints.
- Record environment, device, and data volume.

### Step 2 — Identify bottleneck

Use symptom → probe map:

```
Slow first load → bundle size, render-blocking, LCP element
Slow interaction → INP, main-thread long tasks, layout thrash
Slow API → N+1 queries, missing indexes, cold starts
Memory growth → leaks, unbounded caches, retained DOM
```

### Step 3 — Fix narrowly

Prefer highest-impact, lowest-risk fixes: indexes, caching, code-split, image sizing, defer non-critical JS.

### Step 4 — Verify

Re-run the **same measurement** as Step 1. Report before/after numbers.

### Step 5 — Guard

Add Lighthouse CI budget, bundle-size check, or perf test on the hot path.

---

## When NOT to use

- No evidence of a problem and no stated budget
- Micro-optimizing cold paths while hot paths are unmeasured
- Replacing architecture before profiling

---

## Gotchas

- Synthetic scores ≠ real-user experience — use both.
- Optimizing the wrong layer (CSS when the DB is the bottleneck).
- Caching without invalidation creates subtle bugs.
- Bundle "tree-shaking" claims without measuring shipped bytes.

---

## Common Rationalizations

| Excuse | Reality |
|--------|---------|
| "It feels fast on my machine" | Your machine is not production traffic or network. |
| "We'll add monitoring later" | Without baselines you cannot prove improvement. |
| "Let's rewrite in Rust" | Profile first — often the query or algorithm is the issue. |
| "Lighthouse is enough" | Lab scores miss real devices and cache states. |
| "Ship now, optimize later" | Regressions are cheaper to block in CI than fix in prod. |

---

## Output Format

```markdown
## Performance report — [area]

Baseline: [metrics + how measured]
Bottleneck: [evidence]
Change: [what]
After: [metrics]
Guard: [CI/monitoring added]
```

---

## Examples

<examples>
  <example>
    <input>"Homepage LCP is 5s in CrUX."</input>
    <output>Measure LCP element (hero image). Compress, preload, fix CLS from font swap. Re-run Lighthouse + verify CrUX trend.</output>
  </example>
</examples>

---

## Verification

- [ ] Baseline captured with method and environment noted
- [ ] Bottleneck identified with evidence (not assumption)
- [ ] After metrics show improvement on the same probe
- [ ] Regression guard added or explicitly deferred with reason
- [ ] No premature micro-opts on unmeasured paths

---

## Red Flags

- Optimization started without baseline measurement
- CSS or frontend tuned while DB is actual bottleneck
- Multiple changes shipped — win cannot be attributed
- Synthetic score improved but real-user metrics flat
## Impact Report

```
Area: [frontend/backend] | Baseline: [key metric]
Bottleneck: [one line] | Delta: [before → after]
Guard: [added/deferred]
```
