# Implementation Plan Schemas

Read when drafting `docs/plans/`. Task format adapted from addyosmani/agent-skills planning patterns.

## Vertical slicing (required)

Build **one complete user-visible path** per task slice — not "all DB, then all API, then all UI."

```
Good: Task 1 — user can register (schema + API + UI for registration)
Bad:  Task 1 — entire database schema
```

## Task template (copy per task)

```markdown
## Task [N]: [Short title]

**Description:** One paragraph — what this accomplishes.

**Traces:** FR-2, NFR-1, C-3 (required when feature-spec exists)

**Acceptance criteria:**
- [ ] [Specific, testable condition]

**Verification:**
- [ ] Tests: `[project test command]`
- [ ] Build: `[project build command]`
- [ ] Manual: [what to spot-check]

**Dependencies:** Task [N-1] or None

**Files likely touched:**
- `path/to/file`

**Estimated scope:** XS (1 file) | S (1–2) | M (3–5) | L (5–8) | XL → split further
```

## Task sizing

| Size | Files | Rule |
|------|-------|------|
| XS–S | 1–2 | Single function, endpoint, or config |
| M | 3–5 | One feature slice |
| L | 5–8 | Split if title contains "and" |
| XL | 8+ | Must decompose |

## Checkpoint block (every 2–3 tasks)

```markdown
## Checkpoint: After Tasks [N–M]
- [ ] All tests pass
- [ ] Build clean
- [ ] Core flow demoable end-to-end
- [ ] Human review before next phase (if high risk)
```

## Plan document header

```markdown
# Implementation Plan: [Feature]
Date: YYYY-MM-DD | Spec: docs/specs/YYYY-MM-DD-<slug>-feature-spec.md

## Overview
## Architecture Decisions
## Requirement Traceability
| Requirement | Tasks | Verification |
## Phase 1: …
## Risks and Mitigations
## Open Questions
```
