# Learn From Article — Full Worked Examples

Skill: `learn-from-article` | Load when producing output for this workflow.

## Example 1 — From skill workflow

**Input:** Learn from this article: https://stripe.com/blog/rate-limiters

**Output:**
```
=== Article Credibility Report ===
Title: Scaling rate limiters at Stripe | Credibility: 10/12 | Verdict: PASS

=== Extracted Insights ===
GOTCHA: Token bucket alone fails under bursty microservice traffic [HIGH] | Recommend: SKIP - no current skill covers rate limiting, but valuable learning
TECHNIQUE: Layered rate limiting - per-user + per-service + global [HIGH] | Recommend: SKIP - scale mismatch for most projects
FAILURE_MODE: Single shared counter = hot-key bottleneck at scale [HIGH] | Recommend: SKIP - same reason

=== Application Plan ===
Learnings only - no current skill covers rate limiting. Save to `docs/learnings/research-learnings.md`
```

## Example 2 — Typical invocation

**Input:** "Run `learn-from-article` for [concrete task]"

**Output:**
```
Invoked `learn-from-article`.
Step 1: Accept via: URL (blog, Medium, Substack, dev.to, HN, engineering blog), pasted content, or local file.
Step 2: Score across 6 dimensions (max 12/12). **Gate: >=6/12 to proceed.**
Step 3: Run security pipeline per `learn-from` protocol. BLOCKED = stop.
See SKILL.md Impact Report schema.
```

---

See `SKILL.md` for hard rules, gotchas, and verification checklist.
