# Feature Spec Schema

Use this template for every feature spec. Save to `docs/specs/YYYY-MM-DD-<slug>-feature-spec.md`.

---

## Frontmatter

```yaml
---
artifact: feature-spec
status: Draft | Clarifying | Approved
constitution: docs/constitution.md@<version>
title: <Feature Title>
slug: <kebab-case-slug>
sources:
  - docs/prd/...      # optional
  - docs/specs/...    # optional design doc from brainstorming
---
```

---

## Body Template

```md
# Feature Spec: <Title>

## Summary
<1–2 sentences: what changes for the user, why now>

## Problem
<Who has this pain, what current friction, what's at stake>

## User Scenarios

### US-1 <name>
<Persona>: <plain-language scenario>

### US-2 <name>
...

## Functional Requirements

- **FR-1** <noun-verb statement of capability>
- **FR-2** ...

## Non-Functional Requirements

- **NFR-1** <category>: <measurable target>
- **NFR-2** ...

## Acceptance Criteria

### AC-FR-1.1
**Given** <preconditions>
**When** <action>
**Then** <observable outcome with measurable threshold>

### AC-FR-1.2
...

(One AC minimum per FR. NFRs that map to specific FRs reference them; global NFRs get their own AC-NFR-N section.)

## Edge Cases

- **EC-1** <abnormal/boundary condition> → expected handling
- **EC-2** ...

(Minimum 3.)

## Out of Scope

- <specific thing this spec explicitly does not cover>
- ...

## Constitution Waivers

(Only present if any constitution rule is intentionally not satisfied. Each waiver must cite the rule ID and a rationale.)

- **C-X.Y waived** — Rationale: <why this rule cannot apply here>

## Needs Clarification

- **CL-1** <question> — relates to: FR-2
- **CL-2** ...

(If empty, status can be set to Approved.)

## Review Checklist

- [ ] No architecture or library mentioned
- [ ] Every FR has ≥1 AC
- [ ] Constitution rules referenced where relevant (e.g., "satisfies C-2.1")
- [ ] No vague adjectives
- [ ] Out of Scope non-empty and specific
- [ ] All CLs resolved before Approval
- [ ] Any waivers explicit with rationale
```

---

## Status Lifecycle

```
Draft         → CL list may be non-empty, no plan yet
Clarifying    → user is actively resolving CLs
Approved      → CL list empty, user confirmed; implementation-plan can consume
```

---

## Test Skeletons from Acceptance Criteria

Every AC is written so it converts mechanically to a failing test — this is the SDD×TDD seam. Emit skeletons when the spec reaches `Approved` (on request, or when `spec-driven-development /implement` starts).

**Mapping rules:**

| AC part | Test part |
|---------|-----------|
| **Given** <preconditions> | Arrange — fixtures, seeded state, mocks at boundaries only |
| **When** <action> | Act — one call/interaction, mirroring the user-visible action |
| **Then** <outcome + threshold> | Assert — observable outcome; thresholds become explicit assertions |

**Conventions:**

- One skeleton per AC. Test name carries the AC ID so `spec-crosscheck` can trace it: `test_AC_FR_1_1_expired_token_rejected` / `it('AC-FR-1.1: rejects expired token')`.
- The skeleton body arranges and acts, then asserts against the contract — it MUST fail on current code (Red). No implementation, no `skip`, no empty assertion that vacuously passes.
- Skeletons are handed to `test-driven-development` as the Red phase starting point; `incremental-implementation` picks which AC's skeleton each slice turns green.
- Global NFR ACs (latency, error-rate) become threshold assertions or a named perf/integration test — still carrying the AC ID.

**Example** (from AC-FR-1.1 "Given a magic link older than 15 minutes, When the user clicks it, Then the API returns 410 and no session is created"):

```python
def test_AC_FR_1_1_expired_link_returns_410_and_no_session():
    link = seed_magic_link(age_minutes=16)          # Given
    response = client.get(link.url)                 # When
    assert response.status_code == 410              # Then
    assert session_store.count() == 0
```

---

## Cross-References (read by other skills)

- The `constitution` field in frontmatter is read by `spec-crosscheck` to verify rule coverage.
- The `slug` is reused by `implementation-plan` to name the plan file (e.g., `docs/plans/<slug>-plan.md`).
- FR/NFR IDs are referenced by tasks in the plan ("T-3 implements FR-2").
- AC IDs are carried into test names by the Test Skeletons above; `spec-crosscheck` Check C reads them for AC↔test traceability.
- The `Out of Scope` list is enforced by `spec-crosscheck` Check F.
- The `Constitution Waivers` section is enforced by `spec-crosscheck` Check B.

---

## Style Guidelines

- **Voice:** declarative, present tense ("The system rejects expired tokens", not "should reject")
- **IDs:** never reuse — once an FR-3 is dropped, never replace it with a new FR-3
- **Edge cases:** prefer concrete failures over generic ones ("user clicks expired link" not "error states")
- **Granularity:** one FR = one user-observable behavior. If you need "and" in an FR, split it.
