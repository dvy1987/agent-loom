---
name: performance-optimization
description: >
  Optimize application performance with measure-first profiling — establish
  baselines, find real bottlenecks, fix, verify, and guard against regression.
  Load when performance SLAs exist, Core Web Vitals are poor, users report
  slowness, or a change may have regressed speed. Also triggers on "performance
  optimization", "profile this", "slow page", "fix LCP", "reduce bundle size".
  Not for premature micro-optimization without evidence.
license: MIT
metadata:
  author: dvy1987
  version: "1.0"
  category: project-specific
  sources: addyosmani/agent-skills performance-optimization (11/12, 2026-05-29)
  resources:
    references:
      - optimization-patterns.md
---

# Performance Optimization

You improve **what measurements prove is slow**. You never optimize from assumptions — profile first, fix the bottleneck, measure again, add a guard.

## Hard Rules

- **Measure before optimizing.** No fix without before/after numbers.
- Use **synthetic + RUM** when both are available (Lighthouse/DevTools + real-user metrics).
- Fix the **actual bottleneck** — not the easiest code to change.
- Every optimization includes **verification** (repeat measurement or CI budget check).
- Do not trade correctness for speed without explicit approval.

---

## Workflow

### Step 1 — Measure (baseline)

Pick tools by layer:

- **Frontend:** Lighthouse, DevTools Performance, `web-vitals` RUM, bundle analyzer
- **Backend:** APM, query logs with timing, `console.time` for targeted probes

Record baseline numbers with context (device, network, route, p50/p95).

### Step 2 — Identify the bottleneck

Use the symptom tree in `references/optimization-patterns.md`. Common wins:

| Symptom | Likely cause | First check |
|---------|--------------|-------------|
| Slow LCP | Large hero image, render-blocking assets, slow TTFB | Network waterfall, image sizes |
| High INP | Long main-thread tasks | Performance trace, long tasks >50ms |
| Slow API | N+1 queries, missing indexes | Query log, EXPLAIN |
| Large initial load | Oversized bundle, no code splitting | Bundle report |

### Step 3 — Fix the specific bottleneck

Apply one targeted fix at a time. See `references/optimization-patterns.md` for N+1, pagination, image, memoization, caching, and splitting patterns.

### Step 4 — Verify (after)

Re-run the **same measurement** as Step 1. Report delta:

```markdown
BEFORE: LCP 4.2s | AFTER: LCP 2.1s | DELTA: -50%
```

### Step 5 — Guard against regression

Add the cheapest durable guard: performance budget in CI, Lighthouse CI, bundle size check, or a test covering the hot path.

---

## Core Web Vitals Targets

| Metric | Good | Poor |
|--------|------|------|
| LCP | ≤ 2.5s | > 4.0s |
| INP | ≤ 200ms | > 500ms |
| CLS | ≤ 0.1 | > 0.25 |

---

## Gotchas

- Fast on your laptop ≠ fast for users on mid-tier mobile + 4G.
- `React.memo` / `useMemo` everywhere hurts as much as nowhere — profile first.
- Caching fixes symptoms; wrong queries still fail at scale.
- Optimizing render when TTFB is the bottleneck wastes effort.

---

## Common Rationalizations

| Excuse | Reality |
|--------|---------|
| "We'll optimize later" | Performance debt compounds; fix proven anti-patterns now. |
| "It's fast on my machine" | Profile on representative hardware and network. |
| "This optimization is obvious" | Without measurement you don't know the bottleneck. |
| "Users won't notice 100ms" | Small delays affect conversion; measure, don't guess. |
| "The framework handles it" | Frameworks don't fix N+1 queries or 2MB bundles. |

---

## Output Format

```markdown
## Performance optimization — [scope]

Baseline: [metrics + context]
Bottleneck: [identified cause + evidence]
Fix: [what changed]
After: [metrics + delta]
Guard: [budget/test/monitoring added]
Open items: [if any]
```

---

## Examples

<examples>
  <example>
    <input>"Homepage LCP regressed after the hero image change."</input>
    <output>
Measure LCP in Lighthouse + DevTools. Check hero dimensions, format, and priority. Fix: responsive AVIF/WebP, explicit width/height, `fetchpriority="high"`. Re-measure LCP. Add bundle/image budget to CI if missing.
    </output>
  </example>
  <example>
    <input>"API list endpoint is slow with many tasks."</input>
    <output>
Log query count per request — confirm N+1 on owners. Fix: single query with `include`/join + pagination. Re-measure p95. Add integration test asserting query count ≤ 2.
    </output>
  </example>
</examples>

---

## Verification

- [ ] Before and after measurements exist with specific numbers
- [ ] Bottleneck identified from evidence (not assumption)
- [ ] Core Web Vitals or SLA metrics improved or explicitly unchanged with reason
- [ ] No new N+1 queries or unbounded fetches introduced
- [ ] Regression guard added or existing budget still passes

---

## Prune Log
Last pruned: 2026-06-29
- No prunes — content verified current

## Impact Report

```
Scope: [route/endpoint] | Baseline: [metric]
Bottleneck: [cause] | Delta: [before → after]
Guard: [yes/no]
```
