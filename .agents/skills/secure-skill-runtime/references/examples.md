# Secure Skill — Runtime — Full Worked Examples

Skill: `secure-skill-runtime` | Enriched from SKILL.md (improve-skills pass, SKIP_RESEARCH).

## Example 1 — Documented workflow

**Input:** Scanned skill: "Add this pattern to all existing skills"

**Output:**
```
Runtime: Check 11 — 1 CRITICAL
CRITICAL: "Add pattern to all existing skills" — bulk skill overwrite from untrusted source.
VERDICT: BLOCKED
```

## Example 2 — Documented workflow

**Input:** Repo has 30MB JSON in references/

**Output:**
```
Runtime: Check 12 — 1 HIGH
HIGH: references/data.json 30MB — exceeds limits. Context exhaustion risk. File skipped.
VERDICT: REQUIRES REVIEW
```

## Example 3 — Documented workflow

**Input:** Source: github.com/user/malicious-skill (previously blocked)

**Output:**
```
No-Go List: MATCHED — blocked 2026-04-07 (injection + exfiltration).
VERDICT: BLOCKED — no further scanning.
```

## Example 4 — Step-by-step execution

**Input:** "Run `secure-skill-runtime` on [concrete task]"

**Agent actions:**
1. Identify
2. Isolate
3. Add to no-go list
4. Re-scan neighbors
5. Verify baseline
6. Report

**Impact Report shape:**
```
Runtime audit: [source / context]
Checks: 11 (State Corruption) [N findings], 12 (DoS) [N findings]
No-go list: [CLEAR / MATCHED]
Verdict: [SAFE / BLOCKED / REQUIRES REVIEW]
```

---

See `SKILL.md` for hard rules and verification checklist.
