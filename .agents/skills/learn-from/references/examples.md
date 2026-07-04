# Learn From — Full Worked Examples

Skill: `learn-from` | Enriched from SKILL.md (improve-skills pass, SKIP_RESEARCH).

## Example 1 — Documented workflow

**Input:** Learn from this: https://arxiv.org/abs/2603.29919

**Output:**
```
=== Learn-From Report ===
Source: https://arxiv.org/abs/2603.29919 | Type: paper
Routed to: learn-from-paper

[Sub-skill extracts insights, orchestrator applies shared protocol with recommendations]
```

## Example 2 — Step-by-step execution

**Input:** "Run `learn-from` on [concrete task]"

**Agent actions:**
1. Accept: URL, file path, pasted content, or in-conversation trigger.
2. | Signal | Routes to |
3. Invoke the matched sub-skill. It handles: ingestion, credibility assessment, security scan, insight extraction, and skill matching.
4. After sub-skill extracts and matches insights, present recommendations and get user approval. Once changes are applied, run the mandatory **Post-Application Hardening Cycle** on every modified or created skill before marking the workflow complete.
5. Present the unified report (see Output Format). Include post-apply check results per skill. If blocked at credibility, security, or post-apply security, report why and stop.

**Impact Report shape:**
```
=== Learn-From Report ===
Source: [URL / file path / "conversation"] | Type: [paper/repo/article/chat]

=== Credibility ===
Score: [N]/[max] | Verdict: [PASS/BORDERLINE/REJECT]

=== Security ===
[secure-* verdicts]

=== Extracted Insights ===
[Tag]: [insight] | Agent recommendation: [APPLY/PARTIAL/SKIP] - [reasoning]

=== Contradictions (if any) ===
[skill]: Current [X] vs New [Y] | Agent recommends: [verdict + reasoning]

=== Application Plan ===
[Changes to make, user approval needed]
```

## Example 3 — Anti-skip (rationalization defense)

**Input:** Agent tries to skip a gate

| Excuse | Reality |
|---|---|
| "Source is obviously credible — skip the credibility check" | Credibility scoring catches the non-obvious gaps (sample size, replication, vendor bias). Skipping is how marketing copy gets adopted as method |
| "I'll apply this directly — skip the contradiction check" | Present CONTRADICTION choices — never silent overwrite |
| "Insight is small, skip the hardening cycle" | Post-apply hardening is the audit trail that the skill still validates and fits 200 lines |

## Example 4 — Gotcha application

**Input:** Task hits a non-obvious edge case

**Apply:**
- A `.pdf` URL is not always a paper - check for academic signals. Corporate whitepapers route to `learn-from-article`.
- GitHub repos can contain papers in `/docs` - route to `learn-from-repo` for the repo itself.
- Multiple sources in one message: process each independently, combined report.
- When recommending KEEP CURRENT, explain specifically why the current approach is stronger - don't just say "it's fine."

---

See `SKILL.md` for hard rules and verification checklist.
