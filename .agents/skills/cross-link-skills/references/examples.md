# Cross-Link Skills — Full Worked Examples

Skill: `cross-link-skills` | Enriched from SKILL.md (improve-skills pass, SKIP_RESEARCH).

## Example 1 — Documented workflow

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

## Example 2 — Documented workflow

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

## Example 3 — Step-by-step execution

**Input:** "Run `cross-link-skills` on [concrete task]"

**Agent actions:**
1. Build Skill Registry
2. Detect Stale References
3. Apply Fixes
4. Validate Edits
5. Report
6. Reconcile knowledge graph

**Impact Report shape:**
```
Cross-link repair complete: YYYY-MM-DD
Trigger: [created | renamed | removed | rewired] — [skill name(s)]
Skills scanned: N
Stale references found: N
References fixed: N
References flagged for manual review: N
SKILL.md files edited: [list]
Validation: all edited skills ≥10/14 [✓ | list failures]
```

## Example 4 — Gotcha application

**Input:** Task hits a non-obvious edge case

**Apply:**
- **Description text contains skill names as triggers** — e.g., "when agent-builder checks skill availability". These ARE cross-references and must be updated on rename.
- **Examples may contain skill names** — these are illustrative, not functional. Update them to avoid confusion, but don't flag them as broken references.
- **Frontmatter `sources` field** — skill names in sources are metadata, not cross-references. Leave them alone.
- **Don't create circular references** — if skill A calls B and B calls A, flag it instead of silently wiring it.

---

See `SKILL.md` for hard rules and verification checklist.
