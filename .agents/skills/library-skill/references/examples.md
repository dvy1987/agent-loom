# Library Skill — Full Worked Examples

Skill: `library-skill` | Load when producing output for this workflow.

## Example 1 — From skill workflow

**Input:** universal-skill-creator just created a new skill called `library-skill`. Run library-skill to sync the library.

**Output:**
```
Librarian sync triggered by: new skill added (library-skill)
Skills scanned: 35
New entries added: library-skill (meta)
Removed entries: none

Files updated:
  docs/SKILL-INDEX.md — added library-skill entry, updated call graph
  AGENTS.md — added library-skill to user entry points
  README.md — added library-skill row to meta skills table
  docs/skill-graph.md — rebuilt with 35 nodes, 48 edges
  docs/prd/PRD.md — added library-skill to meta skills table, count 35→36
  docs/architecture.md — no structural flow change, skipped

Cross-reference check:
  Broken references: 0
  Orphaned entries: 0

Logged to docs/skill-outputs/SKILL-OUTPUTS.md.
Invoking generate-changelog...
```

## Example 2 — Success criteria

**Input:** "Use `library-skill` on this project"

**Output:**
```
See SKILL.md Impact Report schema.
```

---

See `SKILL.md` for hard rules, gotchas, and verification checklist.
