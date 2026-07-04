# Learn From Repo — Full Worked Examples

Skill: `learn-from-repo` | Load when producing output for this workflow.

## Example 1 — From skill workflow

**Input:** Learn from this repo: https://github.com/anthropics/anthropic-cookbook

**Output:**
```
═══ Repo Credibility Report ═══
Repo: anthropics/anthropic-cookbook | Credibility: 11/12 | Verdict: PASS

═══ Extracted Insights ═══
GOTCHA: Tool-use prompts need explicit format constraints | Recommend: APPLY — verified in 12+ examples
TECHNIQUE: Prefilled assistant turns for structured output | Recommend: PARTIAL — apply to create-agent-prompt, skip for general skills (too API-specific)
FAILURE_MODE: Streaming without chunk validation = silent data loss | Recommend: APPLY — add to debug-and-fix gotchas

═══ Application Plan ═══
1. IMPROVE: create-agent-prompt — add format constraint guidance
2. IMPROVE: debug-and-fix — add streaming validation gotcha
Awaiting your approval.
```

## Example 2 — Typical invocation

**Input:** "Run `learn-from-repo` for [concrete task]"

**Output:**
```
Invoked `learn-from-repo`.
Step 1: Ingest the Repo
Step 2: Credibility Assessment
Step 3: Security Scan
See SKILL.md Impact Report schema.
```

---

See `SKILL.md` for hard rules, gotchas, and verification checklist.
