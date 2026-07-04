# Split Skill — Full Worked Examples

Skill: `split-skill` | Load when producing output for this workflow.

## Example 1 — From skill workflow

**Input:** improve-skills is 220 lines — the link check section is CORE but takes 15 lines

**Output:**
```
Sub-capability: scan library for delegation opportunities
Existing skill match: validate-skills checks call graph but does NOT recommend new links — different job, cannot cover this without scope creep.
Duplication: not found in other skills.
Action: Type A extract → new child "link-check"

improve-skills: 220 → 198 lines ✓ | link-check: 140 lines (new) ✓
```

## Example 2 — Typical invocation

**Input:** "Run `split-skill` for [concrete task]"

**Output:**
```
Invoked `split-skill`.
Step 1: Identify the Excess Sub-Capability
Step 2: Check Existing Skills First (before creating anything)
Step 3: Execute the Chosen Action
See SKILL.md Impact Report schema.
```

---

See `SKILL.md` for hard rules, gotchas, and verification checklist.
