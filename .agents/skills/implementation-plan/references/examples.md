# Implementation Plan — Full Session Examples

Read when you need a complete walkthrough beyond the inline teaser in SKILL.md.

Vertical slices, AO task templates, and checkpoint blocks. Deep reference: `references/plan-schemas.md`.

---

## Example 1 — Vertical slice plan (registration)

**Input:** "Plan user registration with email verification"

```markdown
# Implementation Plan: User Registration
Date: 2026-07-04 | Spec: docs/specs/2026-07-04-registration-feature-spec.md

## Executive summary
Users register with email/password; verify via link; MVP demoable after Task 2.

## Requirement traceability
| Requirement | Tasks | Verification |
|-------------|-------|--------------|
| FR-1 | T1, T2 | AC on T2 |
| FR-2 | T3 | verify email e2e |
| C-2.1 | T1 | password policy unit test |

## Phase 1: MVP

### Task 1: Register user happy path E2E [FR-1, C-2.1]
**Description:** User submits valid email/password → account row + session/JWT.
**Acceptance criteria:**
- [ ] AC-1: POST /register 201 with valid body
- [ ] AC-2: Duplicate email → 409
**Verification:** `npm test -- auth.register`
**Dependencies:** None
**Scope:** M

### Task 2: Registration form UI with validation states [FR-1]
**Description:** Form shows inline errors; success redirects to dashboard.
**Verification:** `npm test -- RegisterForm.test.tsx`; manual localhost register
**Dependencies:** Task 1
**Scope:** M

### Checkpoint: After Tasks 1–2
**Demo:** Register on localhost → land on dashboard
- [ ] `npm test` green
- [ ] Manual demo recorded

### Task 3: Email verification flow [FR-2]
...
```

---

## Example 2 — Reject horizontal plan

**Input:** Agent drafts:
- T1: All database tables
- T2: All API routes
- T3: All pages

**Output:** Rewrite per `plan-schemas.md` vertical slicing — each task ships one user path (schema+API+UI for that path).

---

## Example 3 — XL decomposition

**Input:** Task "Build entire admin dashboard" (XL)

**Split:**
| New task | Scope | Verify |
|----------|-------|--------|
| T5: Admin auth gate + shell layout | S | manual /admin redirect |
| T6: User list with pagination | M | `npm test -- admin.users` |
| T7: User detail edit | M | manual edit save |
| T8: Audit log read-only view | S | snapshot test |

---

## Example 4 — Integration task split

**Input:** "Connect to Stripe"

**Wrong:** one task  
**Right:** T1 credentials + client factory (XS) → T2 checkout session API (M) → T3 webhook handler + idempotency (M) → T4 failure/retry tests (S)

---

## Example 5 — TODO.md derivation

**Input:** `mode=tasks` from orchestrator

```markdown
# Registration tasks
- [ ] T1 [FR-1,C-2.1] Register API E2E — verify: `npm test -- auth.register`
- [ ] T2 [FR-1] Registration form UI — verify: `npm test -- RegisterForm`
- [ ] T3 [FR-2] Email verification — verify: `npm test -- auth.verify`
```

---

## Example 6 — Open question stop

**Input:** Spec silent on duplicate slug policy

**Output:** Stop — present options A) reject duplicate B) auto-suffix C) merge; do not invent in plan.

---

## Example 7 — Checkpoint failure

**Input:** Checkpoint after T1–T3 fails — tests red

**Output:** Do not start Phase 2. Fix or cut scope until checkpoint passes.

---

See `references/plan-schemas.md` for task template, sizing table, and filled M/XS examples.
---

## Verification checklist (full session)

- [ ] Examples demonstrate SKILL.md hard rules, not generic chat
- [ ] Deep reference file cited and used (patterns / triage / conventions / schemas / prompts / ui-patterns)
- [ ] Reader can trace input → concrete agent actions → durable outcome
- [ ] Cross-skill links honored (TDD↔debug↔review, design suite chain)

