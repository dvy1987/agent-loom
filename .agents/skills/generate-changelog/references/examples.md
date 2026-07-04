# Generate Changelog — Full Worked Examples

Skill: `generate-changelog` | Enriched from SKILL.md (improve-skills pass, SKIP_RESEARCH).

## Example 1 — Documented workflow

**Input:** Generate a changelog for the agent-loom skill library. Recent changes: renamed agent-architect to agent-builder across 8 files, created cross-link-skills skill, created living PRD at docs/prd/PRD.md, updated library-skill to maintain PRD and architecture docs, improved 6 skills to 14/14 scores.

**Output:**
```
## [0.4.0] - 2026-04-12

**Summary:** Major structural improvements — the skill library now self-maintains its own documentation, skills are cross-linked automatically, and the first living PRD establishes a single source of truth for the project.

### Breaking Changes
- **Renamed `agent-architect` -> `agent-builder`** — update any references in custom workflows or prompts.

### Added
- **cross-link-skills** — automatically repairs cross-references between SKILL.md files after creation, rename, or removal.
- **Living PRD** (`docs/prd/PRD.md`) — single source of truth for both agents and humans. Point-in-time PRDs are now historical snapshots only.
- **library-skill** now maintains `docs/prd/PRD.md` and `docs/architecture.md` automatically when structural changes occur.

### Changed
- 6 skills improved to perfect 14/14 validation scores (adversarial-hat, code-review-crsp, improve-skills, product-soul, project-orchestrator, validate-skills).

### Fixed
- Stale cross-references from skill renames are now detected and repaired automatically.

Changelog generated: v0.4.0
Changes categorized: 8
Breaking changes found: 1
User-facing value statements: 4
Ready for: release
```

## Example 2 — Step-by-step execution

**Input:** "Run `generate-changelog` on [concrete task]"

**Agent actions:**
1. Gather Recent Changes
2. Significance Triage (MANDATORY GATE)
3. Categorize the Changes
4. Synthesize the Value (Four-Dimension Test)
5. Draft the Changelog
6. Conditional README Update (MAJOR or MINOR only)
7. Conditional Release Push (MAJOR or MINOR only)
8. Present and Save

## Example 3 — Gotcha application

**Input:** Task hits a non-obvious edge case

**Apply:**
- Agents default to listing every commit verbatim — this produces noise, not a changelog. Group 5-15 related commits into one user-facing change with a value statement.
- Breaking changes buried under "Changed" get missed by users. They must be the FIRST section with a clear prefix, even if there is only one.
- Internal refactors, dependency bumps, and CI fixes are not user-facing changes. Omit them from user-facing changelogs entirely — they belong in internal release notes only.
- Agents tend to default every release to MAJOR. Be honest in Step 2 — most releases are PATCH. Only escalate when the criteria genuinely match.

---

See `SKILL.md` for hard rules and verification checklist.
