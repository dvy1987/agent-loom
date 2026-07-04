# Publish Skill — Full Worked Examples

Skill: `publish-skill` | Load when producing output for this workflow.

## Example 1 — From skill workflow

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

## Example 2 — Typical invocation

**Input:** "Run `publish-skill` for [concrete task]"

**Output:**
```
Invoked `publish-skill`.
Step 1: Pre-publish Validation
Step 2: Determine Package Format
Step 3: Write or Verify README
See SKILL.md Impact Report schema.
```

---

See `SKILL.md` for hard rules, gotchas, and verification checklist.
