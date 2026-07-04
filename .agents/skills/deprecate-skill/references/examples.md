# Deprecate Skill — Full Worked Examples

Skill: `deprecate-skill` | Load when producing output for this workflow.

## Example 1 — From skill workflow

**Input:** The write-commit-messages skill scores 4/14 and GPT-5 now writes perfect conventional commits with no instruction — should we deprecate it?

**Output:**
```
Deprecation case for: write-commit-messages
Trigger: Score 4/14 AND domain now model-native
Evidence: validate-skills report (4/14); GPT-5 release notes confirm native conventional commits support; arXiv:2411.02093 confirms frontier models handle SE tasks without prompting
Callers: none found in AGENTS.md or other SKILL.md files
Capability lost: none — GPT-5 handles this natively
Migration: no skill needed; users can describe commits naturally

This will archive write-commit-messages to .agents/skills/.deprecated/.
The skill can be recovered at any time.
No callers to update.

Proceed? (yes/no)
```

## Example 2 — Typical invocation

**Input:** "Run `deprecate-skill` for [concrete task]"

**Output:**
```
Invoked `deprecate-skill`.
Step 1: Build the Deprecation Case
Step 2: Present and Confirm
Step 3: Update All Callers
See SKILL.md Impact Report schema.
```

---

See `SKILL.md` for hard rules, gotchas, and verification checklist.
