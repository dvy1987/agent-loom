# Library Skill — Full Worked Examples

Skill: `library-skill` | Enriched from SKILL.md (improve-skills pass, SKIP_RESEARCH).

## Example 1 — Documented workflow

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

## Example 2 — Anti-skip (rationalization defense)

**Input:** Agent tries to skip a gate

| Excuse | Reality |
|---|---|
| "INDEX can wait" | Drifted INDEX misroutes every agent in the library. |
| "Bump count without rows" | Table heading counts must match rows beneath. |
| "Edit SKILL.md while syncing" | Librarian reads skills — never writes SKILL.md bodies. |
| "Skip generate-changelog" | Structural changes need release notes. |

## Example 3 — Gotcha application

**Input:** Task hits a non-obvious edge case

**Apply:**
- **Stale frontmatter:** Some skills have `category` nested under `metadata`, others at top level. Check both.
- **Changelog skill location:** The skill named `generate-changelog` lives in `.agents/skills/generate-changelog/` — use the directory name for path, frontmatter `name` for references.
- **Partial runs:** If scanning finds zero skills, abort — the path is likely wrong. Never wipe reference files.
- **Concurrent edits:** Another agent may be editing AGENTS.md simultaneously. Read → diff → write, never overwrite wholesale.

---

See `SKILL.md` for hard rules and verification checklist.
