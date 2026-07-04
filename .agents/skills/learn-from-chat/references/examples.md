# Learn From Chat — Full Worked Examples

Skill: `learn-from-chat` | Load when producing output for this workflow.

## Example 1 — From skill workflow

**Input:** During debugging, the agent discovers that compress-skill's workflow doesn't check whether moved references are actually loaded by the skill at runtime.

**Output:**
```
═══ Chat Learning ═══
Discovered: compress-skill can move content to references/ without verifying load triggers exist
Evidence: During compression, background was moved to references/background.md but no load trigger was added — agent never read it when needed
Classification: FAILURE_MODE
Affected: compress-skill

═══ Proposed Changes ═══
compress-skill:
  Section: ## Gotchas
  Change:
  + - Every file moved to `references/` must have a specific load trigger in the workflow — "see references/" is not sufficient.

Awaiting your approval to apply.
```

## Example 2 — Typical invocation

**Input:** "Run `learn-from-chat` for [concrete task]"

**Output:**
```
Invoked `learn-from-chat`.
Step 1: Capture
Step 2: Classify
Step 3: Match
See SKILL.md Impact Report schema.
```

---

See `SKILL.md` for hard rules, gotchas, and verification checklist.
