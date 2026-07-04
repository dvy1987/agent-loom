# Generate Changelog — Full Worked Examples

Skill: `generate-changelog` | Load when producing output for this workflow.

## Example 1 — From skill workflow

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

## Example 2 — Typical invocation

**Input:** "Run `generate-changelog` for [concrete task]"

**Output:**
```
Invoked `generate-changelog`.
Step 1: Gather Recent Changes
Step 2: Significance Triage (MANDATORY GATE)
Step 3: Categorize the Changes
See SKILL.md Impact Report schema.
```

---

See `SKILL.md` for hard rules, gotchas, and verification checklist.
