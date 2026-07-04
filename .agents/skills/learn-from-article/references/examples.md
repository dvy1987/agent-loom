# Learn From Article — Full Worked Examples

Skill: `learn-from-article` | Enriched from SKILL.md (improve-skills pass, SKIP_RESEARCH).

## Example 1 — Documented workflow

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

## Example 2 — Step-by-step execution

**Input:** "Run `learn-from-article` on [concrete task]"

**Agent actions:**
1. Accept via: URL (blog, Medium, Substack, dev.to, HN, engineering blog), pasted content, or local file.
2. Score across 6 dimensions (max 12/12). **Gate: >=6/12 to proceed.**
3. Run security pipeline per `learn-from` protocol. BLOCKED = stop.
4. Classify production-backed findings using taxonomy from `learn-from`.
5. Match insights to existing skills and apply per `learn-from` shared application protocol, including the mandatory **Post-Application Hardening Cycle** on every modified/created skill: modified-skill security sweep via ALL `secure-*` skills, 200-line gate via `compress-skill` / `split-skill`, then `validate-skills` (≥10/14).
6. Citation format:

**Impact Report shape:**
```
=== Article Credibility Report ===
Title: [title] | Author: [name] | Venue: [publication] | Date: [date]
Credibility: [N]/12 | Verdict: [PASS/BORDERLINE/REJECT]

=== Security ===
[secure-* verdicts]

=== Extracted Insights ===
[Tag]: [insight] [confidence] | Agent recommendation: [APPLY/PARTIAL/SKIP/KEEP CURRENT] - [reasoning]
Discarded: [N] opinion, [N] background

=== Application Plan ===
[Per learn-from shared protocol]
```

## Example 3 — Gotcha application

**Input:** Task hits a non-obvious edge case

**Apply:**
- Eng blogs from top companies are high-signal but may describe solutions for scale the user doesn't have - flag scale mismatch explicitly.
- Medium/dev.to articles vary wildly - credibility check is critical.
- "Best practices" articles often present opinions as facts - look for production evidence.
- Articles may be outdated - check publish date and whether the tech has changed.

---

See `SKILL.md` for hard rules and verification checklist.
