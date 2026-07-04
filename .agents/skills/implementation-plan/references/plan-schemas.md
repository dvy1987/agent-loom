# Implementation Plan Schemas

Read when drafting `docs/plans/`. Task format adapted from addyosmani/agent-skills planning patterns + agent-loom SDD traceability.

---

## Vertical slicing (required)

Build **one complete user-visible path** per task slice — not "all DB, then all API, then all UI."

```
Good: Task 1 — user can register (schema + API + UI for registration)
Bad:  Task 1 — entire database schema
Bad:  Task 1 — all API endpoints
Bad:  Task 2 — all React pages
```

### Anti horizontal-slicing example

**Feature:** Team invitations

| Wrong (horizontal) | Right (vertical) |
|--------------------|------------------|
| T1: invitations table | T1: invite one email → pending row + send mail + settings UI shows pending |
| T2: all API routes | T2: accept invite link → user joins team + redirect |
| T3: all UI screens | T3: revoke pending invite (admin) |

Each vertical task is **demoable** after its checkpoint.

---

## Task template (copy per task)

```markdown
## Task [N]: [Verb + object — no "and"]

**Description:** One paragraph — user-visible outcome when this task completes.

**Traces:** FR-2, NFR-1, C-3 *(required when feature-spec exists)*

**Acceptance criteria:**
- [ ] AC-1: [Given / When / Then — testable]
- [ ] AC-2: [Edge case or error path]

**Verification:**
- [ ] Tests: `[project test command]` — specific file or `-k` filter
- [ ] Build: `[project build command]`
- [ ] Manual: [exact click path or curl to demo]

**Dependencies:** Task [N-1] | None

**Files likely touched:**
- `path/to/file.ts`
- `tests/path/to/file.test.ts`

**Estimated scope:** XS | S | M | L | XL → split if XL

**Risks / notes:** *(optional — integration, migration, perf)*
```

### Title rules

- **No "and"** in title — split into two tasks
- Start with verb: `Add`, `Wire`, `Guard`, `Expose`
- Bad: `Database and API for users`
- Good: `Expose POST /users registration endpoint with validation`

---

## Filled example — Task (M scope)

```markdown
## Task 3: Expose team invite accept flow end-to-end

**Description:** A user with a valid invite token can accept, join the team, and land on the team dashboard. Covers token validation API, membership write, and accept page UI.

**Traces:** FR-4, FR-5, C-2.1 (auth required)

**Acceptance criteria:**
- [ ] AC-1: Given valid token, GET /invite/accept creates membership and returns 302 to /teams/:id
- [ ] AC-2: Given expired token, returns 410 with user-safe message (no stack trace)
- [ ] AC-3: Accept page shows loading, error, and success states

**Verification:**
- [ ] Tests: `npm test -- invite.accept.test.ts`
- [ ] Build: `npm run build`
- [ ] Manual: Open invite link from email fixture → lands on dashboard as member

**Dependencies:** Task 2 (invite token generation)

**Files likely touched:**
- `src/api/invites/accept.ts`
- `src/pages/invite/AcceptPage.tsx`
- `tests/api/invite.accept.test.ts`

**Estimated scope:** M

**Risks / notes:** Race if double-click accept — use idempotent membership insert
```

---

## Filled example — Task (XS scope)

```markdown
## Task 0.2: Add ElevenLabs API key to env and verify quota

**Description:** Local and CI can call ElevenLabs with a valid key; quota limits documented for planning.

**Traces:** NFR-3 (external dependency)

**Acceptance criteria:**
- [ ] AC-1: `.env.example` documents `ELEVENLABS_API_KEY`
- [ ] AC-2: `scripts/verify-elevenlabs.sh` returns 200 on voices list endpoint

**Verification:**
- [ ] Tests: N/A (smoke script)
- [ ] Build: N/A
- [ ] Manual: `bash scripts/verify-elevenlabs.sh`

**Dependencies:** None

**Files likely touched:**
- `.env.example`
- `scripts/verify-elevenlabs.sh`

**Estimated scope:** XS
```

---

## Task sizing

| Size | Files | Duration hint | Rule |
|------|-------|---------------|------|
| XS | 1 | <2h | Config, env, single function |
| S | 1–2 | 2–4h | One endpoint or component |
| M | 3–5 | 0.5–1d | One vertical slice |
| L | 5–8 | 1–2d | Split if title has "and" |
| XL | 8+ | — | **Must decompose** before plan approved |

### Integration task decomposition

"Connect to API X" is never one task. Minimum split:

1. Auth/credentials + client factory
2. Happy-path call + response mapping
3. Error handling, retries, timeouts
4. Tests with fake/stub boundary

---

## Checkpoint block (every 2–3 tasks)

```markdown
## Checkpoint: After Tasks [N–M]

**Demo:** [What a human can click/run to prove progress]

- [ ] All tests pass: `[project test command]`
- [ ] Build clean: `[project build command]`
- [ ] Core flow demoable end-to-end (see Demo above)
- [ ] No XL tasks remaining in this phase without split
- [ ] Human review before next phase *(if auth, payments, migration)*
```

### Checkpoint example

```markdown
## Checkpoint: After Tasks 1–3

**Demo:** Register new user → see empty dashboard → log out → log in

- [ ] `npm test` — all green
- [ ] `npm run build` — no errors
- [ ] Manual: registration flow on localhost:3000
- [ ] Traceability: FR-1, FR-2 covered by Tasks 1–3
```

---

## Dependency graph snippet

```markdown
## Dependency graph

Task 1 (schema + register API + form) → Task 2 (login) → Task 3 (dashboard shell)
                                      ↘ Task 4 (password reset) — parallel after Task 1
```

---

## Plan document header

```markdown
# Implementation Plan: [Feature]
Date: YYYY-MM-DD
Spec: docs/specs/YYYY-MM-DD-<slug>-feature-spec.md
Status: Draft | Approved

## Executive summary
[2–3 sentences — what ships and first demo moment]

## Technical stack
[Languages, frameworks, key dependencies]

## Architecture overview
[Components diagram or bullet architecture]

## Requirement traceability
| Requirement | Tasks | Verification |
|-------------|-------|--------------|
| FR-1 | T1, T2 | AC on T2 |
| NFR-1 | T4 | load test script |

## Phase 0: Prerequisites
## Phase 1: MVP (demoable)
## Phase 2: Refinement
## Phase 3: Testing & deployment

## Risks and mitigations
| Risk | Mitigation |
|------|------------|

## Open questions
- [ ] ...
```

---

## TODO.md derivation (tasks-only mode)

When orchestrator passes `mode=tasks`, flatten to agent-pickable list:

```markdown
- [ ] T1 [FR-1] Register user E2E — verify: `npm test -- register`
- [ ] T2 [FR-2] Login + session — verify: `npm test -- auth`
```

Each line must include **trace ids** and **verify command**.

---

## Rationalization defense (planning)

| Excuse | Reality |
|--------|---------|
| "We'll slice vertically during implementation" | Horizontal plans hide integration risk — slice in the plan |
| "Task 7 is just everything else" | XL junk drawer — decompose or cut scope |
| "DoD: it works" | DoD must be observable: test name, curl, screenshot |
| "Verification: manual testing" | Name the exact manual path |

---

## Cross-skill links

- **Spec gate:** `feature-spec` must be Approved before plan
- **Crosscheck:** `spec-crosscheck` reads traceability table
- **Execution:** `incremental-implementation` picks one vertical task at a time
- **TDD:** each task verification should name test command — `test-driven-development`
