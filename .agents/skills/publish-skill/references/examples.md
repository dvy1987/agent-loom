# Publish Skill — Full Worked Examples

Skill: `publish-skill` | Enriched from SKILL.md (improve-skills pass, SKIP_RESEARCH).

## Example 1 — Documented workflow

**Input:** Publish the brainstorming skill to skills.sh

**Output:**
```
Running validate-skills on brainstorming...
agentskills validate: ✓
Score: 13/14 — passes 10/14 threshold

Checking for proprietary content... none found.

Package format: single SKILL.md (Atomic tier)

README.md present: yes

Packaging: brainstorming.md

Publishing to skills.sh...
npx skills publish ./brainstorming.md

Published: brainstorming
Registry URL: https://skills.sh/brainstorming
Install: npx skills brainstorming

Test install dry-run: ✓
```

## Example 2 — Step-by-step execution

**Input:** "Run `publish-skill` on [concrete task]"

**Agent actions:**
1. Pre-publish Validation
2. Determine Package Format
3. Write or Verify README
4. Package
5. Publish to skills.sh
6. Optionally Push to GitHub
7. Report

**Impact Report shape:**
```
Published: [skill-name]
Registry URL: https://skills.sh/[skill-name]
Install command: npx skills [skill-name]
Package format: [.md / .zip]
validate-skills score at publish: [N]/14
Proprietary content scan: clean
GitHub push: [yes — commit hash / no]
```

## Example 3 — Gotcha application

**Input:** Task hits a non-obvious edge case

**Apply:**
- `npx skills publish` requires the directory name to match the `name` field in frontmatter exactly — mismatch causes a silent failure
- Check for hardcoded paths (e.g., `/home/user/workspace/`) in scripts before publishing — they won't work on other machines
- If the skill uses `scripts/`, verify the script has no hardcoded credentials, internal URLs, or machine-specific paths
- 

---

See `SKILL.md` for hard rules and verification checklist.
