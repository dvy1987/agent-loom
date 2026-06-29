# Update Mode Reference

Load when `project-orchestrator` invokes `project-setup` with `UPDATE_ONLY=true`, or when updating an existing AGENTS.md without a full re-interview.

## Retroactive Bootstrap

For existing coded projects with no AGENTS.md, route to `retroactive-project-setup`. When invoked by that skill, run `RETROACTIVE=true`: skip interview, accept inferred matrix + gap answers, emit AGENTS.md only.

## UPDATE_ONLY Mode

Skip full interview. Update only sections actually affected.

**Update when changed:**
- **Key Commands** — manifest scripts differ
- **Non-Obvious Patterns** — new spec/ADR convention
- **Orchestration Map parallel hints** — plan revealed parallel tracks
- **Boundaries** — new protected dirs or permission gates

**Preserve:** User Context, Code Style, Project Overview, Boundaries (unless affected), Session Lifecycle.

**Process:** Read existing AGENTS.md → update affected sections → show diff → commit.

**Full re-run triggers:** new team member, user says "redo setup", major product pivot.
