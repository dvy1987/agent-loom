# Performance Optimization — Full Worked Examples

Skill: `performance-optimization` | addyosmani patterns, security-scanned SAFE.

---

## Example 1 — LCP regression on marketing page

**Input:** "CrUX shows LCP 4.8s on /pricing"

**Measure:** Lighthouse + trace — LCP element is a 2.1MB PNG hero; font blocks render 400ms.

**Fix:** WebP/AVIF hero with `fetchpriority="high"`, `font-display: swap`, preload critical font.

**Verify:** Lab LCP 2.1s; deploy `web-vitals` beacon; watch CrUX 28-day window.

**Guard:** Lighthouse CI budget `largest-contentful-paint <= 2500` on PR.

---

## Example 2 — API p95 spike

**Input:** "Checkout endpoint p95 went from 200ms to 1.2s"

**Measure:** APM shows N+1 on `order.items`; EXPLAIN on hot query — seq scan.

**Fix:** Add composite index `(user_id, created_at)`; eager-load items in one query.

**Verify:** p95 back to 220ms under load test.

**Guard:** Integration test asserts query count ≤ 3 per checkout.

---

## Example 3 — Anti-skip (rationalization defense)

**Input:** "Just memoize everything in React"

| Excuse | Reality |
|--------|---------|
| "Memo fixes slowness" | Profile first — INP may be a 300ms handler, not re-renders. |
| "We don't need RUM" | Lab-only fixes often miss real devices and cache states. |

---

See `SKILL.md` for hard rules and verification checklist.

---

## Example 4 — Extended pass (L3 enrichment)

## Example 5 — Anti-skip (rationalization defense)

**Input:** Agent tries to skip a gate

| Excuse | Reality |
|---|---|
| "It feels fast on my machine" | Your machine is not production traffic or network. |
| "We'll add monitoring later" | Without baselines you cannot prove improvement. |
| "Let's rewrite in Rust" | Profile first — often the query or algorithm is the issue. |
| "Lighthouse is enough" | Lab scores miss real devices and cache states. |
| "Ship now, optimize later" | Regressions are cheaper to block in CI than fix in prod. |

## Example 6 — Step-by-step execution

**Input:** "Run `performance-optimization` on [concrete task]"

**Agent actions:**
1. Measure baseline
2. Identify bottleneck
3. Fix narrowly
4. Verify
5. Guard

## Example 7 — Gotcha application

**Apply:**
- Synthetic scores ≠ real-user experience — use both.
- Optimizing the wrong layer (CSS when the DB is the bottleneck).
- Caching without invalidation creates subtle bugs.
- Bundle "tree-shaking" claims without measuring shipped bytes.
- 

## Verification checklist (L3)

- [ ] Examples align with SKILL.md hard rules
- [ ] Anti-skip or rationalization pattern shown
- [ ] Output shape matches Impact Report
- [ ] User can trace from input → durable artifact or chat outcome
