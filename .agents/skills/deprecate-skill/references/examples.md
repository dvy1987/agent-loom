# Deprecate Skill — Full Worked Examples

Skill: `deprecate-skill` | Enriched from SKILL.md (improve-skills pass, SKIP_RESEARCH).

## Example 1 — Documented workflow

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

## Example 2 — Step-by-step execution

**Input:** "Run `deprecate-skill` on [concrete task]"

**Agent actions:**
1. Build the Deprecation Case
2. Present and Confirm
3. Update All Callers
4. Archive the Skill
5. Update AGENTS.md
6. Update README
7. Validate and Commit

**Impact Report shape:**
```
Deprecation complete: [skill-name]
Reason: [trigger condition]
Evidence: [source]
Archive path: .agents/skills/.deprecated/[skill-name]-deprecated-YYYY-MM-DD/
DEPRECATION.md written: yes
Callers updated: [list or "none"]
AGENTS.md updated: yes
README updated: yes
Deprecation log updated: yes
Recovery command: mv .agents/skills/.deprecated/[skill-name]-deprecated-YYYY-MM-DD/ .agents/skills/[skill-name]/
```

## Example 3 — Gotcha application

**Input:** Task hits a non-obvious edge case

**Apply:**
- Check `.agents/skills/*/SKILL.md` for references to the deprecated skill — grep is faster than reading each one manually
- The `.deprecated/` directory is not scanned by platforms — archived skills do not load into agent context
- If a skill's triggers are being merged into another skill, update the surviving skill's description to include the deprecated skill's trigger phrases before archiving
- 

---

See `SKILL.md` for hard rules and verification checklist.
