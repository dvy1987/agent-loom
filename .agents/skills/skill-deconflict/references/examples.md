# Skill Deconflict — Full Worked Examples

Skill: `skill-deconflict` | Enriched from SKILL.md (improve-skills pass, SKIP_RESEARCH).

## Example 1 — Documented workflow

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

## Example 2 — Step-by-step execution

**Input:** "Run `skill-deconflict` on [concrete task]"

**Agent actions:**
1. Build the Name + Intent Registry
2. Name Collision Check
3. Trigger Overlap Check
4. Intent Diversity Check
5. Produce Report

**Impact Report shape:**
```
Deconflict complete: YYYY-MM-DD
Mode: single-skill | library-wide
Skills scanned: N
Name collisions found: N
Trigger overlaps found: N pairs
Over-used triggers: N phrases
Diversity failures: N | warnings: N | passes: N
Verdict (single-skill mode): PASS | RENAME | REVISE
```

## Example 3 — Gotcha application

**Input:** Task hits a non-obvious edge case

**Apply:**
- `learn-from` + `learn-from-paper` + `learn-from-repo` + `learn-from-article` + `learn-from-chat` are an intentional orchestrator + sub-skill family. Same for `secure-skill` + siblings. Do not flag these as name collisions.
- `inversion` and `adversarial-hat` sound similar but serve different purposes (inversion = flip the problem, adversarial = critique what exists). Flag only if triggers overlap — not because they are both "critical thinking".
- A trigger phrase like "improve" is too generic to flag alone. Only flag when the FULL phrase overlaps (e.g., "improve all skills" in two descriptions).
- `debug-and-fix` and `fixing-bugs` — one is in this library, one is a builtin. Only flag conflicts within this library.

---

See `SKILL.md` for hard rules and verification checklist.
