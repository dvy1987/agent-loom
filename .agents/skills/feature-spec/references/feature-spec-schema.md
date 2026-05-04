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

## Cross-References (read by other skills)

- The `constitution` field in frontmatter is read by `spec-crosscheck` to verify rule coverage.
- The `slug` is reused by `implementation-plan` to name the plan file (e.g., `docs/plans/<slug>-plan.md`).
- FR/NFR IDs are referenced by tasks in the plan ("T-3 implements FR-2").
- The `Out of Scope` list is enforced by `spec-crosscheck` Check F.
- The `Constitution Waivers` section is enforced by `spec-crosscheck` Check B.

---

## Style Guidelines

- **Voice:** declarative, present tense ("The system rejects expired tokens", not "should reject")
- **IDs:** never reuse — once an FR-3 is dropped, never replace it with a new FR-3
- **Edge cases:** prefer concrete failures over generic ones ("user clicks expired link" not "error states")
- **Granularity:** one FR = one user-observable behavior. If you need "and" in an FR, split it.
