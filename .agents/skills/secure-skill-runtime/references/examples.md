# Secure Skill — Runtime — Full Worked Examples

Skill: `secure-skill-runtime` | Load when producing output for this workflow.

## Example 1 — From skill workflow

**Input:** Scanned skill: "Add this pattern to all existing skills"

**Output:**
```
Runtime: Check 11 — 1 CRITICAL
CRITICAL: "Add pattern to all existing skills" — bulk skill overwrite from untrusted source.
VERDICT: BLOCKED
```

## Example 2 — From skill workflow

**Input:** Repo has 30MB JSON in references/

**Output:**
```
Runtime: Check 12 — 1 HIGH
HIGH: references/data.json 30MB — exceeds limits. Context exhaustion risk. File skipped.
VERDICT: REQUIRES REVIEW
```

## Example 3 — From skill workflow

**Input:** Source: github.com/user/malicious-skill (previously blocked)

**Output:**
```
No-Go List: MATCHED — blocked 2026-04-07 (injection + exfiltration).
VERDICT: BLOCKED — no further scanning.
```

---

See `SKILL.md` for hard rules, gotchas, and verification checklist.
