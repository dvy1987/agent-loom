# Skill Deconflict — Full Worked Examples

Skill: `skill-deconflict` | Load when producing output for this workflow.

## Example 1 — From skill workflow

**Input:** Deconflict new skill: code-audit

**Output:**
```
SKILL DECONFLICT — code-audit
═══════════════════════════════
Verdict: RENAME

NAME CHECK
  Collision: code-audit ↔ code-review-crsp (semantic: "audit" ≈ "review" in code context)
  Action: rename to `security-audit` or `compliance-audit` if purpose differs from code-review-crsp

TRIGGER OVERLAP
  Overlapping with code-review-crsp: "review this code", "audit this diff" (2 shared)
  Action: remove "review this code" from code-audit; reword "audit this diff" to "audit this for compliance"

INTENT DIVERSITY
  Trigger count: 3
  Semantic clusters: 1
  Score: FAIL
  Missing triggers: "check for vulnerabilities", "scan this code", "security review", "compliance check"
```

## Example 2 — Typical invocation

**Input:** "Run `skill-deconflict` for [concrete task]"

**Output:**
```
Invoked `skill-deconflict`.
Step 1: Build the Name + Intent Registry
Step 2: Name Collision Check
Step 3: Trigger Overlap Check
Deconflict complete: YYYY-MM-DD
```

---

See `SKILL.md` for hard rules, gotchas, and verification checklist.
