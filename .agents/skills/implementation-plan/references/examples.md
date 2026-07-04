# Implementation Plan — Full Worked Examples

Source: addyosmani/agent-skills `planning-and-task-breakdown` (2026-05-29 snapshot). Security-scanned SAFE. Adapted to agent-loom `docs/plans/` output.

---

## Example 1 — Vertical slice task list

**Input:** "Plan user registration"

```markdown
# Implementation Plan: User Registration

## Overview
Email/password registration with verification email; vertical slices leave app deployable after each phase.

## Tasks

### Slice 1 — Happy path API (S)
- [ ] POST /register accepts email+password; returns 201
- **Verify:** `npm test -- auth.register`
- **Files:** `src/routes/auth.ts`, `tests/auth.register.test.ts`

### Checkpoint 1
- [ ] Suite green; manual POST succeeds

### Slice 2 — Validation errors (S)
- [ ] Duplicate email → 409; weak password → 422
- **Verify:** extend auth tests

### Slice 3 — Email verification (M)
- [ ] Token table + verify endpoint
- **Verify:** e2e test with mock mailer
```

No task >5 files. No "implement registration" without acceptance criteria.

---

## Example 2 — Dependency ordering

**Input:** "Plan search with filters"

Order: (1) read-only search API, (2) filter query params, (3) UI — foundation before UI. Mark parallel only when API contract is frozen.

---

## Example 3 — XL task rejection

**Input:** Task "Build entire admin dashboard"

**Output:** Split into S/M tasks — auth gate, user list, user edit, audit log — each with verify step. XL → decompose before implementation.

---

## Example 4 — Open question stop

**Input:** Spec silent on duplicate task titles

**Output:** Stop planning — present options A/B/C to user; do not invent requirement in plan.
