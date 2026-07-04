# Cross-Link Skills — Full Worked Examples

Skill: `cross-link-skills` | Load when producing output for this workflow.

## Example 1 — From skill workflow

**Input:** Skill `agent-architect` was renamed to `agent-builder`. Run cross-link repair.

**Output:**
```
Cross-link repair triggered by: rename (agent-architect → agent-builder)
Skills scanned: 35

Stale references found: 13
  process-decomposer/SKILL.md: 2 references → fixed
  setup-evaluation/SKILL.md: 4 references → fixed
  project-orchestrator/SKILL.md: 2 references → fixed
  create-agent-prompt/SKILL.md: 2 references → fixed
  skill-finder/SKILL.md: 1 reference → fixed
  tool-finder/SKILL.md: 1 reference → fixed
  ROUTING.md: 1 reference → fixed (not a SKILL.md, flagged for library-skill)

Validation: all 6 edited skills still ≥10/14 ✓
```

## Example 2 — From skill workflow

**Input:** New skill `cross-link-skills` was just created. Run cross-link repair.

**Output:**
```
Cross-link repair triggered by: new skill (cross-link-skills)
Skills scanned: 36

New skill calls: validate-skills
New skill called by: universal-skill-creator, improve-skills
  universal-skill-creator/SKILL.md: reference present ✓
  improve-skills/SKILL.md: reference present ✓

Stale references: 0
Missing references: 0
No edits needed.
```

---

See `SKILL.md` for hard rules, gotchas, and verification checklist.
